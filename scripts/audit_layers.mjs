#!/usr/bin/env node
// Checks that dist/<slug>.layered.css renders exactly like dist/<slug>.css.
//
// For each example page it records every computed property of every element
// and its ::before/::after, once with the plain bundle and once with the
// layered one, and fails on any difference. Properties that change on their
// own while an animation runs (a spinner's rotation, a shimmer's position)
// are ignored, since two snapshots of a running animation never agree.
//
// Usage (needs Playwright; serve the repo root first):
//   python3 -m http.server 8000 &
//   node scripts/audit_layers.mjs [--base http://localhost:8000] [theme ...]
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const i = args.indexOf('--base');
const base = i >= 0 ? args.splice(i, 2)[1] : 'http://localhost:8000';
const names = args.length ? args : fs.readdirSync(path.join(root, 'themes'))
  .filter(t => fs.existsSync(path.join(root, 'themes', t, 'theme.css'))).sort();
const ANIMATED = new Set(['transform', 'background-position', 'background-position-x', 'opacity', 'rotate']);

const browser = await chromium.launch(process.env.PLAYWRIGHT_CHROMIUM ? { executablePath: process.env.PLAYWRIGHT_CHROMIUM } : {});
const page = await browser.newPage({ viewport: { width: 1100, height: 900 } });
const failures = [];

async function snapshot(theme, bundle) {
  await page.goto(`${base}/examples/${theme}.html`, { waitUntil: 'networkidle' });
  await page.evaluate(href => { document.querySelector('link[rel=stylesheet]').href = href; }, `../dist/${bundle}`);
  await page.waitForLoadState('networkidle');
  await page.waitForTimeout(200);
  return page.evaluate(() => {
    const out = [];
    for (const el of [document.documentElement, ...document.querySelectorAll('body, body *')]) {
      const animated = getComputedStyle(el).animationName !== 'none';
      for (const pseudo of [null, '::before', '::after']) {
        const cs = getComputedStyle(el, pseudo);
        const props = {};
        for (let k = 0; k < cs.length; k++) props[cs[k]] = cs.getPropertyValue(cs[k]);
        out.push({ tag: el.tagName.toLowerCase() + (el.className ? '.' + String(el.className).split(' ').join('.') : '') + (pseudo || ''), animated, props });
      }
    }
    return out;
  });
}

for (const theme of names) {
  const a = await snapshot(theme, `${theme}.css`);
  const b = await snapshot(theme, `${theme}.layered.css`);
  for (let k = 0; k < a.length; k++) {
    for (const [prop, val] of Object.entries(a[k].props)) {
      if (b[k].props[prop] === val) continue;
      if (a[k].animated && ANIMATED.has(prop)) continue;
      failures.push(`${theme}: <${a[k].tag}> ${prop}: ${val} -> ${b[k].props[prop]}`);
      break;
    }
  }
}
await browser.close();
if (failures.length) {
  console.log(failures.slice(0, 40).join('\n'));
  console.log(`\n${failures.length} element(s) render differently when layered`);
  process.exit(1);
}
console.log(`layered bundles match the plain ones across ${names.length} themes`);
