#!/usr/bin/env node
// Exercise readiness through the browser, including pages that look loaded but are wrong.
import assert from 'node:assert/strict';
import { test, after } from 'node:test';
let harness;
try { harness = await import('../scripts/_harness.mjs'); }
catch (error) {
  if (error.code !== 'ERR_MODULE_NOT_FOUND') throw error;
  console.log('SKIP  Harness browser checks: Playwright is not installed');
  process.exit(0);
}
const { launch, serveRoot, themeReady, openThemed } = harness;

const browser = await launch('chromium');
if (!browser) process.exit(0);
const server = await serveRoot();
after(async () => { await browser.close(); server.close(); });
const page = await browser.newPage();
await page.route('**/dist/*.css', route => route.fulfill({
  contentType: 'text/css', body: 'html {color: red} body {margin: 0} p {padding: 0}',
}));
await page.route('**/test/harness-fixture.html*', route => {
  const params = new URL(route.request().url()).searchParams;
  return route.fulfill({ contentType: 'text/html', body: `<!doctype html>
    <html data-theme="wanted" data-variant="day"><head>
    <link id="theme-link" rel="stylesheet" href="/dist/${params.get('sheet') || 'wanted'}.css">
    </head><body><p>Ready fixture</p></body></html>` });
});
const fixture = `${server.base}/test/harness-fixture.html`;

test('readiness accepts the requested stylesheet and variant', async () => {
  await page.goto(fixture);
  assert.equal(await themeReady(page, 'wanted', 200, 'day'), true);
});
test('readiness rejects a different palette variant', async () => {
  await page.goto(fixture);
  assert.equal(await themeReady(page, 'wanted', 200, 'night'), false);
});
test('readiness rejects a different loaded stylesheet', async () => {
  await page.goto(`${fixture}?sheet=other`);
  assert.equal(await themeReady(page, 'wanted', 200, 'day'), false);
});
test('navigation fails instead of returning an unprepared page', async () => {
  await assert.rejects(openThemed(page, `${fixture}?variant=night`, 'wanted'), /theme.*never fully applied/i);
});
