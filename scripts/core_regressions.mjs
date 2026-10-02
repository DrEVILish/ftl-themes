#!/usr/bin/env node
// Rendered regression check for core layout bugs reported by adopting apps
// (Playlist Lab, 2026-10): [hidden] on display-setting components,
// .nav-collapse under Chromium's ::details-content, shrink-to-fit .modal,
// .modal-header layout, transparent buttons/muted text in .app-bar, and
// sticky table headers trapping an open dropdown. Runs every theme.
//
// Usage (Playwright in scripts/node_modules or on NODE_PATH):
//   node scripts/core_regressions.mjs [--engine chromium|firefox|webkit]... [theme ...]
// Exits non-zero on any failure. A failure listed for its engine in
// test/engine-known-issues.json (script "core_regressions", key
// "<theme>: <message>") is printed as a warning instead.
import fs from 'fs';
import path from 'path';
import { ROOT as root, takeEngines, launch, knownIssues } from './_harness.mjs';

const args = process.argv.slice(2), engines = takeEngines(args);
const themes = args.length ? args
  : JSON.parse(fs.readFileSync(path.join(root, 'dist/themes.json'))).map(t => t.slug);

const page = (slug) => `<!doctype html><html data-theme="${slug}"><head>
<link rel="stylesheet" href="file://${root}/dist/${slug}.css"></head><body>
<div class="app"><header class="app-bar"><span class="nav-brand">App</span><a class="nav-item" id="barnav" href="#">Home</a>
  <button class="btn btn-secondary" id="barbtn">Log out</button>
  <span class="text-muted" id="barmuted">jo@example.com</span></header>
<main class="app-main">
  <div class="alert alert-warning" id="h1" hidden>x</div><span class="badge" id="h2" hidden>1</span>
  <details class="nav-collapse" id="nc"><summary class="nav-toggle"></summary>
    <nav class="nav" id="ncnav"><a class="nav-item" href="#">One</a><a class="nav-item" href="#">Two</a></nav></details>
  <table class="table is-sticky"><thead><tr><th id="th1"><details open><summary>f</summary>
    <div class="dropdown">opts</div></details></th><th id="th2">b</th></tr></thead><tbody><tr><td>1</td><td>2</td></tr></tbody></table>
</main></div>
<div class="modal-overlay" id="ov"><div class="modal modal-lg" id="m">
  <div class="modal-header" id="mh"><h2>Edit</h2><button class="btn-close" id="mc" aria-label="Close"></button></div>
  <input class="input"></div></div>
</body></html>`;


let failures = 0, warnings = 0;
const ran = [];
for (const engine of engines) {
  const browser = await launch(engine);
  if (!browser) continue;
  ran.push(engine);
  const known = knownIssues(engine, 'core_regressions');
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const p = await ctx.newPage();
  const fail = (t, msg) => {
    const k = known(`${t}: ${msg}`);
    if (k) { warnings++; console.log(`warn  [${engine}] ${t}: ${msg} (known issue: ${k.reason || k.match})`); }
    else { failures++; console.log(`FAIL  [${engine}] ${t}: ${msg}`); }
  };

  for (const t of themes) {
    const file = path.join(root, `test/.core-regressions.html`);
    fs.writeFileSync(file, page(t));
    await p.setViewportSize({ width: 1280, height: 900 });
    await p.goto('file://' + file);
    const r = await p.evaluate(() => {
      const $ = (id) => document.getElementById(id), cs = (id) => getComputedStyle($(id));
      const m = $('m').getBoundingClientRect(), mh = $('mh').getBoundingClientRect(), mc = $('mc').getBoundingClientRect();
      return {
        hidden: [cs('h1').display, cs('h2').display],
        navVisible: $('ncnav').checkVisibility(), navDir: cs('ncnav').flexDirection,
        modalW: m.width, closeEnd: m.right - mc.right < 48 || (getComputedStyle($('mc')).order === '-1' && mc.left - m.left < 64) /* a theme may put it first (Mac OS 9, Aqua) */, closeRow: mc.bottom <= document.querySelector('#m .input').getBoundingClientRect().top,
        dbg: [m.right, mc.right, mc.bottom, document.querySelector('#m .input').getBoundingClientRect().top, mh.width],
        titleFg: getComputedStyle(document.querySelector('#mh h2')).color, headFg: cs('mh').color,
      
        thZ: cs('th1').zIndex, th2Z: cs('th2').zIndex,
      };
    });
    if (r.hidden.some(d => d !== 'none')) fail(t, `[hidden] ignored (display ${r.hidden})`);
    if (!r.navVisible || r.navDir !== 'row') fail(t, `.nav-collapse nav not laid out on desktop (visible=${r.navVisible}, ${r.navDir})`);
    if (r.modalW < 600) fail(t, `.modal-lg shrank to ${r.modalW}px`);
    if (process.env.DEBUG && (!r.closeEnd || !r.closeRow)) console.log(t, r.dbg);
    if (!r.closeEnd || !r.closeRow) fail(t, `.btn-close not in the modal's top-right`);
    if (r.titleFg !== r.headFg) fail(t, `<h2> in .modal-header is ${r.titleFg}, header text is ${r.headFg}`);
    if (+r.thZ <= +r.th2Z) fail(t, `sticky th with an open dropdown not lifted (z ${r.thZ} vs ${r.th2Z})`);
    // Bar text contrast, measured on pixels: hide the text, screenshot what
    // is behind it (gradients, gloss and glass included), take the median.
    // The modal's overlay would dim the bar, so it goes first.
    await p.evaluate(() => document.getElementById('ov').style.display = 'none');
    for (const [id, label] of [['barbtn', '.btn-secondary'], ['barmuted', '.text-muted']]) {
      const loc = p.locator('#' + id), fg = await loc.evaluate(e => getComputedStyle(e).color);
      await loc.evaluate(e => e.style.setProperty('color', 'transparent', 'important'));
      const png = (await loc.screenshot()).toString('base64');
      await loc.evaluate(e => e.style.removeProperty('color'));
      const c = await p.evaluate(async ([png, fg]) => {
        const img = new Image(); img.src = 'data:image/png;base64,' + png; await img.decode();
        const cv = document.createElement('canvas'); cv.width = img.width; cv.height = img.height;
        const g = cv.getContext('2d'); g.drawImage(img, 0, 0);
        const d = g.getImageData(0, 0, cv.width, cv.height).data, px = [];
        for (let k = 0; k < d.length; k += 4) px.push([d[k], d[k + 1], d[k + 2]]);
        const med = [0, 1, 2].map(ch => px.map(q => q[ch]).sort((a, b) => a - b)[px.length >> 1]);
        const [r, gg, b, a = 1] = fg.match(/[\d.]+/g).map(Number);
        const f = [r, gg, b].map((v, ch) => v * a + med[ch] * (1 - a));
        const L = (c) => { const [x, y, z] = c.map(v => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }); return 0.2126 * x + 0.7152 * y + 0.0722 * z; };
        const [hi, lo] = [L(f), L(med)].sort((m, n) => n - m); return (hi + 0.05) / (lo + 0.05);
      }, [png, fg]);
      if (c < 4.5) fail(t, `${label} in .app-bar is ${c.toFixed(1)}:1 on the bar (floor 4.5)`);
    }
    const forcedOpen = await p.evaluate(() => { const d = document.getElementById('nc'); d.open = true;
      const dir = getComputedStyle(document.getElementById('ncnav')).flexDirection; d.open = false; return dir; });
    if (forcedOpen !== 'row') fail(t, `.nav-collapse forced open on desktop stacks (${forcedOpen})`);
    await p.setViewportSize({ width: 390, height: 900 });
    const small = await p.evaluate(() => { const n = document.getElementById('ncnav'), d = document.getElementById('nc');
      const closed = n.checkVisibility(); d.open = true; return { closed, dir: getComputedStyle(n).flexDirection }; });
    if (small.closed || small.dir !== 'column') fail(t, `.nav-collapse at 390px: closed nav visible=${small.closed}, open direction ${small.dir}`);
  }
  await browser.close();
}
fs.rmSync(path.join(root, 'test/.core-regressions.html'), { force: true });
console.log(`${themes.length} themes x ${ran.join(', ') || 'no engine'}: ${failures} failure(s), ${warnings} known-issue warning(s)`);
process.exit(failures ? 1 : 0);
