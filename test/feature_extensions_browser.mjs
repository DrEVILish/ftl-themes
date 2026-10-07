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
  // ProSeries console: pages switch by radio, the compressor curve bends at
  // its threshold, the PEQ curve moves with a band's gain, linked knobs follow.
  await page.goto(`${server.base}/proseries.html`, { waitUntil: 'networkidle' });
  assert.equal(await page.evaluate(() => document.documentElement.dataset.theme), 'proseries');
  await page.evaluate(() => { document.getElementById('pg-channel').checked = true; });
  assert(await page.locator('.ps-page[data-page="channel"]').isVisible());
  const comp = page.locator('.ps-dyn-panel[data-dyn="comp"]');
  const curve = () => comp.locator('.dyn-graph-line').getAttribute('d');
  await comp.locator('[data-param="threshold"]').evaluate(el => { el.value = -30; el.dispatchEvent(new Event('input', { bubbles: true })); });
  await comp.locator('[data-param="ratio"]').evaluate(el => { el.value = 4; el.dispatchEvent(new Event('input', { bubbles: true })); });
  // At 0 dB in, a 4:1 compressor at -30 dB outputs -22.5 dB: y = 100 - 62.5.
  assert.match(await curve(), /L100\.00 37\.50$/);
  const peq = page.locator('.ps-peq .eq-graph-curve path');
  const before = await peq.getAttribute('d');
  await page.locator('.ps-peq [data-band="3"][data-param="g"]').evaluate(el => { el.value = -12; el.dispatchEvent(new Event('input', { bubbles: true })); });
  assert.notEqual(await peq.getAttribute('d'), before);
  assert.equal(await page.locator('.ps-peq .eq-node[data-band="3"]').evaluate(el => el.style.getPropertyValue('--g')), '-0.8000');
  await page.evaluate(() => { document.getElementById('pg-effects').checked = true; document.querySelector('[name=fx-unit][value=chamber]').checked = true; });
  const twins = page.locator('[data-link="chamber-decay"]');
  await twins.first().evaluate(el => { el.value = 90; el.dispatchEvent(new Event('input', { bubbles: true })); });
  assert.equal(await twins.nth(1).inputValue(), '90');
  // Bank keys swap channel names; scene next/previous move the scene shown
  // in the home bar; patch points undo.
  await page.evaluate(() => { document.getElementById('pg-inputs').checked = true; });
  await page.click('.ps-bank >> nth=1');
  assert.equal(await page.locator('.ps-strip .ps-tag').first().innerText(), 'Kick');
  await page.click('.ps-bank >> nth=0');
  await page.evaluate(() => { document.getElementById('pg-scenes').checked = true; });
  await page.click('[data-scene-step="1"]');
  assert.equal(await page.locator('.ps-scene').innerText(), 'Walk-in');
  await page.evaluate(() => { document.getElementById('pg-patching').checked = true; });
  const point = page.locator('#patch-from .patch-point').first();
  const wasPatched = await point.locator('input').isChecked();
  await point.click();
  await page.click('[data-undo]');
  assert.equal(await point.locator('input').isChecked(), wasPatched);
  // Gallery desktop: boots as XP, clears its boot screen once themes load,
  // lists every theme, and Apply restyles the whole desktop.
  await page.goto(`${server.base}/gallery.html`, { waitUntil: 'networkidle' });
  await page.waitForFunction(() => document.querySelector('[data-boot-screen]').hidden);
  assert.equal(await page.evaluate(() => document.documentElement.dataset.theme), 'winxp-luna');
  const themeCount = await page.evaluate(() => fetch('dist/themes.json').then(r => r.json()).then(t => t.length));
  assert.equal(await page.locator('.theme-card').count(), themeCount);
  await page.click('.logon-user >> nth=0');
  await page.evaluate(() => { document.getElementById('open-themes').checked = true; document.getElementById('app-themes').checked = true; });
  await page.click('button[aria-label="Apply LCARS"]');
  await page.waitForFunction(() => document.documentElement.dataset.theme === 'lcars');
  // Waveform regions: edges stay in order, --start/--end follow, the body drags, markers seek.
  await page.goto(`${server.base}/audio-components.html?theme=blue-future`, { waitUntil: 'networkidle' });
  const region = page.locator('.waveform-region').nth(1);
  const edges = region.locator('input');
  await edges.nth(0).evaluate(el => { el.value = 999; el.dispatchEvent(new Event('input', { bubbles: true })); });
  assert.deepEqual(await edges.evaluateAll(i => i.map(e => +e.value)), [94.9, 95]);
  assert.equal(await region.evaluate(r => r.style.getPropertyValue('--start')), String((94.9 / 180).toFixed(4)));
  assert.equal(await edges.nth(0).getAttribute('aria-valuetext'), '1:35');
  await edges.nth(0).evaluate(el => { el.value = 62; el.dispatchEvent(new Event('input', { bubbles: true })); });
  await region.scrollIntoViewIfNeeded();
  const wave = await page.locator('.waveform').first().boundingBox();
  const grabX = wave.x + wave.width * (78 / 180), grabY = wave.y + wave.height * 0.7;
  await page.mouse.move(grabX, grabY);
  await page.mouse.down();
  await page.mouse.move(grabX + wave.width * 0.1, grabY, { steps: 4 });
  await page.mouse.up();
  const moved = await edges.evaluateAll(i => i.map(e => +e.value));
  assert(moved[0] > 70 && Math.abs(moved[1] - moved[0] - 33) < 0.2, `region drag keeps its length: ${moved}`);
  await page.locator('button.waveform-marker[data-time="110"]').click();
  assert.equal(await page.locator('.waveform').first().locator(':scope > input').inputValue(), '110');
  // Zoom: the window moves, inputs keep their values, out-of-view edges leave the tab order;
  // a fade region's single input sets its end; the app's --gain follows.
  const trim = page.locator('#wf-trim');
  const trimValues = await trim.locator('input').evaluateAll(i => i.map(e => e.value));
  await page.click('[data-for=wf-trim] [data-zoom=in]');
  await page.click('[data-for=wf-trim] [data-zoom=in]');
  assert.equal(await trim.evaluate(w => w.style.getPropertyValue('--zoom-from')), '0.37500');
  assert.deepEqual(await trim.locator('input').evaluateAll(i => i.map(e => e.value)), trimValues);
  assert.equal(await trim.locator('.is-trim > input').first().getAttribute('tabindex'), '-1');
  assert.match(await trim.locator('.is-trim > input').first().getAttribute('aria-description'), /before/);
  assert.equal(await page.locator('.waveform-window').evaluate(r => r.style.getPropertyValue('--start')), '0.3750');
  await page.click('[data-for=wf-trim] [data-zoom=reset]');
  assert.equal(await trim.locator('.is-trim > input').first().getAttribute('tabindex'), null);
  await trim.locator('.is-fade-in > input').evaluate(el => { el.value = 24; el.dispatchEvent(new Event('input', { bubbles: true })); });
  assert.equal(await trim.locator('.is-fade-in').evaluate(r => r.style.getPropertyValue('--end')), '0.1333');
  assert.equal(await trim.locator('.waveform-bars > i').nth(15).evaluate(i => i.style.getPropertyValue('--gain')), '0.542');
  // Parameter slider mirrors its number and resets; a bipolar slider snaps to centre.
  await page.locator('#p-delay').evaluate(el => { el.value = 50; el.dispatchEvent(new Event('input', { bubbles: true })); });
  assert.equal(await page.inputValue('[aria-label="Delay, milliseconds"]'), '50');
  await page.click('[aria-label="Reset delay"]');
  assert.equal(await page.inputValue('#p-delay'), '120');
  const balance = page.locator('input.slider.is-bipolar');
  await balance.evaluate(el => { el.value = 3; el.dispatchEvent(new Event('input', { bubbles: true })); });
  assert.equal(await balance.inputValue(), '0');
  assert.equal(await balance.evaluate(el => el.style.getPropertyValue('--value')), '0.5000');
  // Themed exit: the outgoing theme's --motion-leave plays on the old snapshot.
  assert(await openThemed(page, `${server.base}/components-experience.html?theme=msdos`, 'msdos'), 'msdos failed to load');
  await page.selectOption('#theme-picker', 'lcars');
  await page.waitForFunction(() => document.getAnimations().some(a => String(a.effect?.pseudoElement).includes('view-transition-old')));
  assert.equal(await page.evaluate(() => document.documentElement.dataset.leaving), 'power-off');
  assert(await page.evaluate(() => document.getAnimations().some(a => a.animationName === 'leave-power-off')));
  await page.waitForFunction(() => !document.documentElement.dataset.leaving);
  // Alert level: the Konami easter egg sets red alert, which frames the page.
  for (const key of ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a']) await page.keyboard.press(key);
  assert.equal(await page.evaluate(() => document.documentElement.dataset.alert), 'red');
  assert.notEqual(await page.evaluate(() => getComputedStyle(document.documentElement, '::after').boxShadow), 'none');
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
