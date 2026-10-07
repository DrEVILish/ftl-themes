#!/usr/bin/env node
// Rendered checks for the dashboard states and boot readiness across families.
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
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
    await page.check('[name="scenario"][value="offline"]', { force: true });
    assert.equal(await page.locator('.connection:visible').getAttribute('data-state'), 'offline', theme);
    assert.equal(await page.locator('.demo-metric').evaluateAll(cs => cs.filter(c => getComputedStyle(c).outlineStyle === 'dashed').length), 4, theme);
    await page.check('[name="scenario"][value="alert"]', { force: true });
    const look = await page.locator('.demo-metric').evaluateAll(cs => cs.map(c => getComputedStyle(c).boxShadow + getComputedStyle(c).borderTopColor));
    assert(look[3] !== look[2] && look[2] === look[1], `${theme}: only the error-rate card is in alert`);
    assert.equal(await page.locator('[data-scenario]:visible').count(), 2, theme);
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
  assert.equal(await page.locator('[data-boot-screen] > .splash-art').evaluate(el => getComputedStyle(el).animationName), 'none');
  await page.evaluate(() => window.ftlAppReady());
  assert.equal(await page.locator('.app-main').getAttribute('aria-busy'), null);
  assert.equal(await page.locator('[data-boot-screen]').evaluate(el => el.hidden), true);
  await page.goto(`${server.base}/theme-feedback.html`, { waitUntil: 'networkidle' });
  // Corrupt saved JSON is ignored instead of preventing the feedback tool from opening.
  await page.evaluate(() => localStorage.setItem('theme-feedback-v1', '{broken'));
  await page.reload({ waitUntil: 'networkidle' });
  assert.equal(await page.locator('#reports').innerText(), 'No reports saved yet.');
  await page.evaluate(() => localStorage.removeItem('theme-feedback-v1'));
  await page.locator('#theme').selectOption('winxp-luna');
  await page.locator('#page').selectOption('components-instruments.html');
  await page.frameLocator('#preview').locator('body').waitFor();
  const dialogs = [];
  page.on('dialog', async dialog => { dialogs.push(dialog.message()); await dialog.accept(); });
  // Saving without a drawn region or description must not create a report.
  await page.locator('#save').click();
  assert.match(dialogs.at(-1), /Draw a box/);
  assert.equal(await page.evaluate(() => JSON.parse(localStorage.getItem('theme-feedback-v1') || '[]').length), 0);
  await page.locator('#draw').click();
  let stage = await page.locator('#stage').boundingBox();
  await page.mouse.move(stage.x + 50, stage.y + 50);
  await page.mouse.down();
  await page.mouse.up();
  await page.locator('#save').click();
  assert.match(dialogs.at(-1), /Draw a box/);
  assert.equal(await page.evaluate(() => JSON.parse(localStorage.getItem('theme-feedback-v1') || '[]').length), 0);
  await page.locator('#draw').click();
  // Drag bottom-right to top-left: coordinates must normalize to positive bounds.
  await page.evaluate(() => scrollTo(0, 0)); // #save scrolled the page
  stage = await page.locator('#stage').boundingBox();
  await page.mouse.move(stage.x + 190, stage.y + 140);
  await page.mouse.down();
  await page.mouse.move(stage.x + 30, stage.y + 30, { steps: 4 });
  await page.mouse.up();
  await page.locator('#save').click();
  assert.match(dialogs.at(-1), /description/);
  assert.equal(await page.evaluate(() => JSON.parse(localStorage.getItem('theme-feedback-v1') || '[]').length), 0);
  await page.locator('#comment').fill('The chart labels overlap on a narrow screen.');
  await page.locator('#save').click();
  const feedback = await page.evaluate(() => JSON.parse(localStorage.getItem('theme-feedback-v1') || '[]'));
  assert.equal(feedback.length, 1);
  assert.equal(feedback[0].theme, 'winxp-luna');
  assert.equal(feedback[0].page, 'components-instruments.html');
  assert(feedback[0].selection.width > 0 && feedback[0].selection.height > 0);
  assert(feedback[0].selection.x > 0 && feedback[0].selection.y > 0);
  // Storage quota/privacy failures leave the existing report intact and tell
  // the user the save failed instead of silently discarding it.
  await page.evaluate(() => {
    const original = Storage.prototype.setItem;
    Storage.prototype.setItem = function (key, value) {
      if (key === 'theme-feedback-v1') throw new DOMException('blocked', 'QuotaExceededError');
      return original.call(this, key, value);
    };
  });
  await page.locator('#draw').click();
  await page.evaluate(() => scrollTo(0, 0));
  const updatedStage = await page.locator('#stage').boundingBox();
  await page.mouse.move(updatedStage.x + 220, updatedStage.y + 170);
  await page.mouse.down();
  await page.mouse.move(updatedStage.x + 80, updatedStage.y + 60, { steps: 3 });
  await page.mouse.up();
  await page.locator('#comment').fill('A second issue that cannot be persisted.');
  await page.locator('#save').click();
  assert.match(dialogs.at(-1), /could not be saved/);
  assert.equal(await page.evaluate(() => JSON.parse(localStorage.getItem('theme-feedback-v1') || '[]').length), 1);
  const download = page.waitForEvent('download');
  await page.locator('#download').click();
  const reportFile = await download;
  assert.equal(reportFile.suggestedFilename(), 'theme-feedback.json');
  const reportText = await readFile(await reportFile.path(), 'utf8');
  const exported = JSON.parse(reportText);
  assert.equal(exported.format, 'theme-feedback');
  assert.equal(exported.version, 1);
  assert.equal(exported.reports.length, 1);
  console.log('browser feature checks passed (Windows and iOS theme families; reduced motion)');
} finally {
  await browser.close();
  server.close();
}
