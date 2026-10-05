#!/usr/bin/env node
// Rendered checks for the dashboard states and boot readiness across families.
import assert from 'node:assert/strict';
let harness;
try { harness = await import('../scripts/_harness.mjs'); }
catch (error) {
  if (error.code === 'ERR_MODULE_NOT_FOUND') {
    console.log('SKIP  Chromium feature checks: Playwright is not installed');
    process.exit(0);
  }
  throw error;
}
const { launch, openThemed, serveRoot } = harness;

const themes = ['windows95', 'winxp-luna', 'win7-aero', 'ios-skeuomorphic', 'ios-flat', 'liquid-glass'];
const browser = await launch('chromium');
if (!browser) process.exit(0);
const server = await serveRoot();
try {
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  for (const theme of themes) {
    assert(await openThemed(page, `${server.base}/dashboard.html?theme=${theme}`, theme), `${theme} failed to load`);
    await page.locator('#dashboard-scenario').selectOption('offline');
    assert.equal(await page.locator('#dashboard-connection').getAttribute('data-state'), 'offline', theme);
    assert.equal(await page.locator('#dashboard-demo .demo-metric.is-stale').count(), 4, theme);
    await page.locator('#dashboard-scenario').selectOption('alert');
    assert.equal(await page.locator('#dashboard-demo .demo-metric.is-error').count(), 1, theme);
    assert.equal(await page.locator('#dashboard-scenario').inputValue(), 'alert', theme);
  }
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto(`${server.base}/components-experience.html?theme=ios-flat`, { waitUntil: 'networkidle' });
  await page.evaluate(() => {
    const splash = document.createElement('div');
    splash.className = 'splash';
    splash.dataset.bootScreen = '';
    splash.innerHTML = '<div class="splash-art"></div>';
    document.body.prepend(splash);
  });
  await page.addScriptTag({ url: `${server.base}/assets/js/boot.js` });
  assert.equal(await page.locator('.app-main').getAttribute('aria-busy'), 'true');
  assert.equal(await page.locator('.splash-art').evaluate(el => getComputedStyle(el).animationName), 'none');
  await page.evaluate(() => window.ftlAppReady());
  assert.equal(await page.locator('.app-main').getAttribute('aria-busy'), null);
  assert.equal(await page.locator('.splash').evaluate(el => el.hidden), true);
  await page.goto(`${server.base}/theme-feedback.html`, { waitUntil: 'networkidle' });
  await page.locator('#theme').selectOption('winxp-luna');
  await page.locator('#page').selectOption('components-instruments.html');
  await page.frameLocator('#preview').locator('body').waitFor();
  await page.locator('#draw').click();
  const stage = await page.locator('#stage').boundingBox();
  await page.mouse.move(stage.x + 30, stage.y + 30);
  await page.mouse.down();
  await page.mouse.move(stage.x + 190, stage.y + 140, { steps: 4 });
  await page.mouse.up();
  await page.locator('#comment').fill('The chart labels overlap on a narrow screen.');
  await page.locator('#save').click();
  const feedback = await page.evaluate(() => JSON.parse(localStorage.getItem('theme-feedback-v1')));
  assert.equal(feedback.length, 1);
  assert.equal(feedback[0].theme, 'winxp-luna');
  assert.equal(feedback[0].page, 'components-instruments.html');
  assert(feedback[0].selection.width > 0 && feedback[0].selection.height > 0);
  console.log('browser feature checks passed (Windows and iOS theme families; reduced motion)');
} finally {
  await browser.close();
  server.close();
}
