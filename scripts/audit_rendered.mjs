#!/usr/bin/env node
// Rendered-contrast audit for examples/*.html.
//
// scripts/check.py reasons about token VALUES; this measures what actually
// renders. It records every element that owns visible text, then hides all
// text and screenshots the page, so each element's background is the real
// pixel colour behind it — gradients, translucent glass, tinted badges and
// gloss included, none of which a token lookup can resolve.
//
// Usage (needs Playwright; serve the repo root first):
//   python3 -m http.server 8000 &
//   node scripts/audit_rendered.mjs [--base http://localhost:8000] [--floor 4.5] [theme ...]
//
// Exits non-zero if any text falls below --fail-below (default 3.0), so it
// can gate CI on "unreadable" while still reporting the AA band above it.
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const opt = (name, dflt) => { const i = args.indexOf(name); return i >= 0 ? args.splice(i, 2)[1] : dflt; };
const base = opt('--base', 'http://localhost:8000');
const floor = parseFloat(opt('--floor', '4.5'));
const failBelow = parseFloat(opt('--fail-below', '3.0'));
const names = args.length ? args : fs.readdirSync(path.join(root, 'themes')).filter(t => fs.existsSync(path.join(root, 'themes', t, 'theme.css'))).sort();

const browser = await chromium.launch(process.env.PLAYWRIGHT_CHROMIUM ? { executablePath: process.env.PLAYWRIGHT_CHROMIUM } : {});
const page = await browser.newPage({ viewport: { width: 1100, height: 900 } });
let below = 0, broken = 0;

for (const theme of names) {
  await page.goto(`${base}/examples/${theme}.html`, { waitUntil: 'networkidle' });
  await page.addStyleTag({ content: '*{transition:none!important;animation:none!important} .ftl-toast-region{position:static!important}' });
  const els = await page.evaluate(() => {
    const out = [];
    for (const e of document.querySelectorAll('body *')) {
      if (![...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) continue;
      const cs = getComputedStyle(e);
      if (cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) continue;
      if (cs.webkitTextFillColor === 'rgba(0, 0, 0, 0)') continue; // gradient-clipped text
      const r = e.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      const size = parseFloat(cs.fontSize);
      out.push({
        label: `<${e.tagName.toLowerCase()}${[...e.classList].map(c => '.' + c).join('')}> "${e.textContent.trim().slice(0, 32)}"`,
        color: cs.color, x: r.x + scrollX, y: r.y + scrollY, w: r.width, h: r.height,
        large: size >= 24 || (parseInt(cs.fontWeight) >= 700 && size >= 18.66),
        disabled: !!e.closest(':disabled,.is-disabled,[aria-disabled=true]'),
      });
    }
    return out;
  });
  await page.addStyleTag({ content: '*{color:transparent!important;-webkit-text-fill-color:transparent!important;text-shadow:none!important}' });
  const png = (await page.screenshot({ fullPage: true })).toString('base64');
  const results = await page.evaluate(async ({ png, els }) => {
    const img = new Image(); img.src = 'data:image/png;base64,' + png; await img.decode();
    const c = document.createElement('canvas'); c.width = img.width; c.height = img.height;
    const ctx = c.getContext('2d'); ctx.drawImage(img, 0, 0);
    const L = ([r, g, b]) => { const f = v => { v /= 255; return v <= .03928 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4; }; return .2126 * f(r) + .7152 * f(g) + .0722 * f(b); };
    // Computed colors aren't always rgb(): oklch(), lab(), color(display-p3 …)
    // and color-mix() results serialize as-is, and pulling numbers out of
    // those with a regex measured nonsense. Let the browser convert: paint
    // the color onto a 1px canvas and read the sRGB pixel back.
    const px1 = document.createElement('canvas').getContext('2d', { willReadFrequently: true });
    const toRGBA = css => {
      px1.clearRect(0, 0, 1, 1); px1.fillStyle = '#000'; px1.fillStyle = css; px1.fillRect(0, 0, 1, 1);
      const [r, g, b, a] = px1.getImageData(0, 0, 1, 1).data;
      return [r, g, b, a / 255];
    };
    return els.filter(e => !e.disabled).map(e => {
      const m = toRGBA(e.color), a = m[3];
      const d = ctx.getImageData(Math.round(e.x + 2), Math.round(e.y + e.h / 2), Math.max(1, Math.round(e.w - 4)), 1).data;
      const px = []; for (let i = 0; i < d.length; i += 4) px.push([d[i], d[i + 1], d[i + 2]]);
      px.sort((p, q) => L(p) - L(q));
      const bg = px[Math.floor(px.length / 2)]; // median pixel on the text's midline
      const fg = [0, 1, 2].map(i => m[i] * a + bg[i] * (1 - a));
      return { label: e.label, large: e.large, ratio: (Math.max(L(fg), L(bg)) + .05) / (Math.min(L(fg), L(bg)) + .05) };
    });
  }, { png, els });
  const bad = results.filter(r => r.ratio < (r.large ? Math.min(3, floor) : floor));
  below += bad.length;
  broken += bad.filter(r => r.ratio < failBelow).length;
  if (bad.length) console.log(`${theme}:\n` + bad.map(r => `  ${r.ratio.toFixed(1)}:1 ${r.label}`).join('\n'));
}
console.log(`\n${below} text element(s) below ${floor}:1, ${broken} below ${failBelow}:1, across ${names.length} page(s)`);
await browser.close();
process.exit(broken ? 1 : 0);
