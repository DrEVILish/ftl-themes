#!/usr/bin/env node
// v5 harness check (PLAN.md §2 target devices, §4 touch targets, §5
// "Enforced by a check"). For every theme x example page x target device:
//
//   1. horizontal overflow: documentElement.scrollWidth past the layout
//      viewport, plus the elements that escape it (no clipping/scrolling
//      ancestor holds them)
//   2. touch targets under the tier minimum (44px mobile/tablet, 24px
//      desktop/xl); inline links in running text are exempt (WCAG 2.5.8)
//   3. mobile/tablet only: adjacent targets closer than 8px
//   4. text closer than 4px to the padding edge of a bordered/filled box
//   5. xl only: .app capped at <= 1800px and centred
//
// Usage (Playwright resolvable from scripts/node_modules, see
// screenshot_themes.py; CHROMIUM_PATH optional):
//   node scripts/v5_audit.mjs [--theme slug[~variant]]... [--page name]...
//                             [--device name]... [--strict]
// Writes test/v5-audit/report.json. Exit 0 (report mode) unless --strict
// and something failed.
import { chromium } from 'playwright';
import http from 'http';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

const DEVICES = {
  'iphone-15-pro': { width: 393, height: 852, tier: 'mobile' },
  'duo-folded': { width: 466, height: 678, tier: 'mobile' },
  'duo-unfolded': { width: 890, height: 626, tier: 'tablet' },
  'macbook-air': { width: 1280, height: 800, tier: 'desktop' },
  'desktop-1440p': { width: 2560, height: 1440, tier: 'xl' },
};
const PAGES = ['components', 'dashboard', 'marketing', 'ticketsystem', 'powerstation', 'soundmixer', 'livechat', 'nesting']
  .filter(p => fs.existsSync(path.join(root, p + '.html')));
// Palette variants only repaint, so (as in _pw_shot.mjs) they run on one page.
const VARIANT_PAGES = ['dashboard'];

// ---- args
const argv = process.argv.slice(2), want = { theme: [], page: [], device: [] };
let strict = false;
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (a === '--strict') strict = true;
  else if (a.startsWith('--') && a.slice(2) in want && argv[i + 1]) want[a.slice(2)].push(argv[++i]);
  else { console.error(`unknown or incomplete argument: ${a}`); process.exit(2); }
}
const all = JSON.parse(fs.readFileSync(path.join(root, 'dist/themes.json'), 'utf8'))
  .flatMap(t => [t.slug, ...(t.variants || []).map(v => `${t.slug}~${v.id}`)]);
const themes = want.theme.length ? want.theme : all;
const pages = want.page.length ? want.page : PAGES;
const devices = want.device.length ? want.device : Object.keys(DEVICES);
for (const [list, known, what] of [[themes, all, 'theme'], [pages, PAGES, 'page'], [devices, Object.keys(DEVICES), 'device']])
  for (const x of list) if (!known.includes(x)) { console.error(`unknown ${what}: ${x} (known: ${known.join(', ')})`); process.exit(2); }

// ---- static server on the repo root (pages fetch dist/themes.json)
const TYPES = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.mjs': 'text/javascript', '.json': 'application/json',
  '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.gif': 'image/gif',
  '.woff2': 'font/woff2', '.woff': 'font/woff', '.ttf': 'font/ttf', '.otf': 'font/otf' };
const server = http.createServer((req, res) => {
  const file = path.join(root, decodeURIComponent(new URL(req.url, 'http://x').pathname));
  if (!file.startsWith(root + path.sep)) { res.writeHead(403); return res.end(); }
  fs.readFile(file, (err, buf) => {
    if (err) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'content-type': TYPES[path.extname(file)] || 'application/octet-stream' });
    res.end(buf);
  });
});
await new Promise(r => server.listen(0, '127.0.0.1', r));
const base = `http://127.0.0.1:${server.address().port}`;

// Same readiness test as _pw_shot.mjs: theme stylesheet applied, fonts done.
async function themeReady(pw, slug) {
  try {
    await pw.waitForFunction((slug) => {
      if (document.documentElement.dataset.theme !== slug) return false;
      const link = document.getElementById('theme-link');
      if (!link || !link.sheet) return false;
      const count = (rules) => Array.from(rules).reduce((n, r) => n + 1 + (r.cssRules ? count(r.cssRules) : 0), 0);
      try { if (count(link.sheet.cssRules) < 3) return false; } catch (e) { return false; }
      return document.fonts.status === 'loaded';
    }, slug, { timeout: 5000, polling: 100 });
    return true;
  } catch { return false; }
}
const FREEZE_CSS = '*{animation:none!important;transition:none!important;scroll-behavior:auto!important}';

// ---- the in-page measurement (runs in the browser)
function measure({ tier }) {
  const touch = tier === 'mobile' || tier === 'tablet';
  const MIN = touch ? 44 : 24, GAP = 8, EDGE = 4, CAP = 1800;
  const vw = document.documentElement.clientWidth;
  const cs = (el, p) => getComputedStyle(el, p);
  const desc = (el) => {
    const one = (e) => e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') +
      [...e.classList].slice(0, 2).map(c => '.' + c).join('');
    const txt = (el.innerText || el.getAttribute('aria-label') || (/^(button|submit|reset)$/.test(el.type) ? el.value : '') || '').trim().replace(/\s+/g, ' ').slice(0, 24);
    return (el.parentElement && el.parentElement !== document.body ? one(el.parentElement) + ' > ' : '') + one(el) + (txt ? ` "${txt}"` : '');
  };
  const visible = (el) => el.checkVisibility({ opacityProperty: true, visibilityProperty: true }) && !el.closest('[inert]');
  const clipsX = (el) => cs(el).overflowX !== 'visible';
  const r1 = (n) => Math.round(n * 10) / 10;

  // 1. overflow: elements whose right edge passes the viewport with no
  // clipping/scrolling ancestor to hold them. Only the outermost escapee of
  // each subtree is reported.
  const escapes = new Set();
  for (const el of document.body.querySelectorAll('*')) {
    const r = el.getBoundingClientRect();
    if (!r.width || r.right <= vw + 0.5 || !visible(el)) continue;
    let a = el.parentElement, held = false;
    for (; a && a !== document.body; a = a.parentElement) if (clipsX(a)) { held = true; break; }
    if (!held) escapes.add(el);
  }
  const outer = [...escapes].filter(el => !escapes.has(el.parentElement))
    .map(el => ({ el: desc(el), px: r1(el.getBoundingClientRect().right - vw) })).sort((a, b) => b.px - a.px);
  const overflow = { px: Math.max(0, document.documentElement.scrollWidth - vw), elements: outer.length, worst: outer.slice(0, 10) };

  // 2. touch targets. A checkbox/radio with a <label> is hit through the
  // label, so the label is measured instead. A positioned ::before/::after (the §4 hit
  // area expander) counts towards the hit size.
  const SEL = 'a[href], button, input:not([type=hidden]), select, textarea, summary, label, [role=button], [role=tab], [role=menuitem], [role=switch], [tabindex]:not([tabindex="-1"])';
  const blockOf = (el) => { let a = el.parentElement; while (a && cs(a).display.startsWith('inline')) a = a.parentElement; return a; };
  const inlineLink = (el) => el.tagName === 'A' && cs(el).display === 'inline' &&
    (blockOf(el)?.innerText || '').trim().length > (el.innerText || '').trim().length + 1;
  const hitSize = (el, r) => {
    let w = r.width, h = r.height;
    for (const p of ['::before', '::after']) {
      const s = cs(el, p);
      if (s.content === 'none' || s.display === 'none' || !/absolute|fixed/.test(s.position)) continue;
      const px = (v) => v.endsWith('px') ? parseFloat(v) : null;
      const [t, rt, b, l] = [s.top, s.right, s.bottom, s.left].map(px);
      const pw = l !== null && rt !== null ? el.clientWidth - l - rt : parseFloat(s.width) || 0;
      const ph = t !== null && b !== null ? el.clientHeight - t - b : parseFloat(s.height) || 0;
      w = Math.max(w, pw); h = Math.max(h, ph);
    }
    return [w, h];
  };
  const docW = document.documentElement.scrollWidth;
  const targets = [];
  for (const el of document.querySelectorAll(SEL)) {
    const check = (c) => c && /^(checkbox|radio)$/.test(c.type);
    if (el.tagName === 'LABEL' && !check(el.control)) continue;
    if (check(el) && el.labels && [...el.labels].some(visible)) continue;
    if (!visible(el) || inlineLink(el)) continue;
    const r = el.getBoundingClientRect();
    if (!r.width || !r.height || r.right <= 0 || r.left >= docW) continue;
    const [w, h] = hitSize(el, r);
    targets.push({ el, r, w, h });
  }
  const small = targets.filter(t => t.w < MIN - 0.5 || t.h < MIN - 0.5)
    .sort((a, b) => Math.min(a.w, a.h) - Math.min(b.w, b.h))
    .map(t => ({ el: desc(t.el), w: r1(t.w), h: r1(t.h) }));

  // 3. spacing between targets (touch tiers). ponytail: O(n²) pair scan,
  // fine for a few hundred targets per page.
  const tight = [];
  if (touch) for (let i = 0; i < targets.length; i++) for (let j = i + 1; j < targets.length; j++) {
    const a = targets[i], b = targets[j];
    if (a.el.contains(b.el) || b.el.contains(a.el)) continue;
    // WCAG 2.5.8: spacing only matters around undersized targets; full-size
    // rows stacked edge to edge (menus, lists, iOS-style groups) are fine.
    const big = (t) => t.w >= MIN - 0.5 && t.h >= MIN - 0.5;
    if (big(a) && big(b)) continue;
    const dx = Math.max(0, b.r.left - a.r.right, a.r.left - b.r.right), dy = Math.max(0, b.r.top - a.r.bottom, a.r.top - b.r.bottom);
    const gap = Math.max(dx, dy);
    if (gap < GAP - 0.5) tight.push({ a: desc(a.el), b: desc(b.el), gap: r1(gap) });
  }
  tight.sort((a, b) => a.gap - b.gap);

  // 4. text vs. the padding edge of the nearest bordered or filled box.
  const alpha = (c) => { const m = c.match(/[\d.]+/g); return !m ? 0 : m.length > 3 ? +m[3] : 1; };
  const bgOf = new Map();
  const effBg = (el) => {
    if (!el) return 'rgb(255, 255, 255)';
    if (!bgOf.has(el)) { const c = cs(el).backgroundColor; bgOf.set(el, alpha(c) > 0 ? c : effBg(el.parentElement)); }
    return bgOf.get(el);
  };
  const boxOf = new Map();
  // A filled box is checked on all four sides; a box drawn only by borders
  // (a row separator, a callout's left rule) only on its bordered sides.
  const SIDES = ['Top', 'Right', 'Bottom', 'Left'];
  const sidesOf = (el) => {
    const s = cs(el);
    if (s.backgroundImage !== 'none' || s.boxShadow !== 'none' ||
      (alpha(s.backgroundColor) > 0 && s.backgroundColor !== effBg(el.parentElement))) return SIDES;
    const b = SIDES.filter(k => parseFloat(s[`border${k}Width`]) > 0 && s[`border${k}Style`] !== 'none' && alpha(s[`border${k}Color`]) > 0);
    return b.length ? b : null;
  };
  const isBox = (el) => sidesOf(el) !== null;
  const box = (el) => {
    if (!el || el === document.body || el === document.documentElement) return null;
    if (!boxOf.has(el)) boxOf.set(el, isBox(el) ? el : box(el.parentElement));
    return boxOf.get(el);
  };
  const edge = [];
  const range = document.createRange();
  for (const el of document.body.querySelectorAll('*')) {
    const texts = [...el.childNodes].filter(n => n.nodeType === 3 && n.data.trim());
    if (!texts.length || /^(SCRIPT|STYLE|TEXTAREA|OPTION|SELECT)$/.test(el.tagName) || !visible(el)) continue;
    const b = box(el);
    if (!b) continue;
    range.setStartBefore(texts[0]); range.setEndAfter(texts[texts.length - 1]);
    const t = range.getBoundingClientRect();
    if (t.width < 2 || t.height < 2) continue;
    const br = b.getBoundingClientRect(), s = cs(b);
    const pad = { l: br.left + parseFloat(s.borderLeftWidth), r: br.right - parseFloat(s.borderRightWidth),
      t: br.top + parseFloat(s.borderTopWidth), b: br.bottom - parseFloat(s.borderBottomWidth) };
    const dist = { Left: t.left - pad.l, Right: pad.r - t.right, Top: t.top - pad.t, Bottom: pad.b - t.bottom };
    const d = Math.min(...sidesOf(b).map(k => dist[k]));
    if (d >= EDGE - 0.5) continue;
    if (d < 0) { // text past the edge: fine if something between clips or scrolls it (ellipsis, scroller)
      let a = el, clipped = false;
      for (; a && !clipped; a = a === b ? null : a.parentElement) clipped = cs(a).overflowX !== 'visible' || cs(a).overflowY !== 'visible';
      if (clipped) continue;
    }
    edge.push({ el: desc(el), box: desc(b), d: r1(d) });
  }
  edge.sort((a, b) => a.d - b.d);

  // 5. xl cap on the app shell. A page without .app (marketing's full-bleed
  // bands) is n/a: §3 caps the shell, not every layout.
  let xl = null;
  if (tier === 'xl') {
    const app = document.querySelector('.app');
    if (app) {
      const r = app.getBoundingClientRect(), left = r1(r.left), right = r1(vw - r.right);
      xl = { el: desc(app).replace(/ ".*/, ''), width: r1(r.width), left, right, ok: r.width <= CAP + 0.5 && Math.abs(left - right) <= 1 };
    }
  }

  return { viewport: vw, overflow, targets: { min: MIN, checked: targets.length, small: small.length, worst: small.slice(0, 10) },
    spacing: touch ? { min: GAP, tight: tight.length, worst: tight.slice(0, 10) } : null,
    edgeText: { min: EDGE, count: edge.length, sample: edge.slice(0, 10) }, xl };
}

// ---- run
const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || undefined });
const results = [];
console.log(['theme'.padEnd(22), 'device'.padEnd(14), 'page'.padEnd(13), ...['overflow', 'small', 'tight', 'edge', 'xl-cap'].map(h => h.padStart(8))].join(' '));
for (const dname of devices) {
  const d = DEVICES[dname], touch = d.tier !== 'desktop' && d.tier !== 'xl';
  const ctx = await browser.newContext({ viewport: { width: d.width, height: d.height }, hasTouch: touch, isMobile: touch });
  const pw = await ctx.newPage();
  for (const entry of themes) {
    const [slug, variant] = entry.split('~');
    for (const pg of variant ? pages.filter(p => VARIANT_PAGES.includes(p)) : pages) {
      const url = `${base}/${pg}.html?theme=${slug}` + (variant ? `&variant=${variant}` : '') + (pg === 'components' ? '&embed=1' : '');
      const row = { theme: entry, device: dname, tier: d.tier, page: pg };
      try {
        let ready = false;
        for (let i = 0; i < 3 && !ready; i++) { await pw.goto(url, { waitUntil: 'networkidle' }); ready = await themeReady(pw, slug); }
        if (!ready) row.warning = 'theme CSS/fonts never fully applied';
        await pw.addStyleTag({ content: FREEZE_CSS });
        Object.assign(row, await pw.evaluate(measure, { tier: d.tier }));
        row.fail = row.overflow.px > 0 || row.overflow.elements > 0 || row.targets.small > 0 ||
          (row.spacing?.tight ?? 0) > 0 || row.edgeText.count > 0 || row.xl?.ok === false;
      } catch (err) {
        row.error = String(err?.message || err); row.fail = true;
      }
      results.push(row);
      const x = row.error ? ['ERROR', '', '', '', row.error.split('\n')[0]]
        : [row.overflow.px + (row.overflow.elements ? `/${row.overflow.elements}el` : ''), row.targets.small, row.spacing ? row.spacing.tight : '-',
          row.edgeText.count, row.xl ? (row.xl.ok ? 'ok' : `NO ${row.xl.width}w ${row.xl.left}/${row.xl.right}`) : d.tier === 'xl' ? 'n/a' : '-'];
      console.log([entry.padEnd(22), dname.padEnd(14), pg.padEnd(13), ...x.map(v => String(v).padStart(8)), row.fail ? ' FAIL' : ' pass'].join(' '));
    }
  }
  await ctx.close();
}
await browser.close();
server.close();

const out = path.join(root, 'test/v5-audit/report.json');
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.writeFileSync(out, JSON.stringify({ generated: new Date().toISOString(), devices: DEVICES, results }, null, 1));
const failed = results.filter(r => r.fail).length;
console.log(`\n${results.length} runs, ${failed} failing. Columns: overflow px[/escaping elements], small targets, tight pairs, edge text, xl cap.`);
console.log(`Report: ${path.relative(root, out)}`);
process.exit(strict && failed ? 1 : 0);
