#!/usr/bin/env node
// Render cost (PLAN.md §20): scrolls dashboard.html on the Mobile tier
// (393x852, touch) with the CPU throttled 4x (CDP
// Emulation.setCPUThrottlingRate, a mid-range phone) and reports the frame
// time per theme. Heavy effects (backdrop blur, glow, large shadows,
// animated gutters) show up as frames over the 16.7ms budget. Chromium only:
// the throttling is a DevTools-protocol feature.
//
// Usage:
//   node scripts/render_cost.mjs [--theme slug[~variant]]... [--page name]
//                                [--frames n] [--threshold ms] [--strict]
// A theme whose average frame time is over --threshold is flagged; --strict
// exits 1 when any is. `prefers-reduced-transparency` and
// data-transparency="reduced" stay the user's escape hatch for a flagged
// theme; the fix is still the theme's.
import { launch, serveRoot, openThemed, themeEntries, examplePages } from './_harness.mjs';

// 60Hz is 16.7ms a frame. 20ms average means about one frame in five was
// dropped while scrolling; flat themes measure 16.7-16.8 here, so anything
// above 20 is the theme's effects, not noise.
const THRESHOLD_MS = 20;

const argv = process.argv.slice(2), themes = [];
let page = 'dashboard', frames = 240, threshold = THRESHOLD_MS, strict = false;
for (let i = 0; i < argv.length; i++) {
  const a = argv[i], v = argv[i + 1];
  if (a === '--strict') strict = true;
  else if (a === '--theme' && v) themes.push(argv[++i]);
  else if (a === '--page' && v) page = argv[++i];
  else if (a === '--frames' && v) frames = +argv[++i];
  else if (a === '--threshold' && v) threshold = +argv[++i];
  else { console.error(`unknown or incomplete argument: ${a}`); process.exit(2); }
}
const all = themeEntries();
for (const t of themes) if (!all.includes(t)) { console.error(`unknown theme: ${t}`); process.exit(2); }
if (!examplePages().includes(page)) { console.error(`unknown page: ${page}`); process.exit(2); }
const list = themes.length ? themes : all.filter(t => !t.includes('~'));

const { base, close } = await serveRoot();
const browser = await launch('chromium');
if (!browser) process.exit(2);
console.log(`${page}.html, 393x852 touch, CPU 4x slower, ${frames} frames scrolled; flag at avg > ${threshold}ms`);
console.log(['theme'.padEnd(22), 'avg ms'.padStart(7), 'p95 ms'.padStart(7), 'max ms'.padStart(7), 'dropped'.padStart(8)].join(' '));
const rows = [];
for (const entry of list) {
  const [slug, variant] = entry.split('~');
  const ctx = await browser.newContext({ viewport: { width: 393, height: 852 }, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  await openThemed(p, `${base}/${page}.html?theme=${slug}` + (variant ? `&variant=${variant}` : ''), slug);
  const cdp = await ctx.newCDPSession(p);
  await cdp.send('Emulation.setCPUThrottlingRate', { rate: 4 });
  // Scroll the page down and back, one step per frame, timing each frame.
  const deltas = await p.evaluate(async (frames) => {
    const se = document.scrollingElement, max = se.scrollHeight - innerHeight;
    const step = Math.max(8, (2 * max) / frames), raf = () => new Promise(requestAnimationFrame);
    let dir = 1, last = await raf();
    const out = [];
    for (let i = 0; i < frames; i++) {
      se.scrollTop += dir * step;
      if (se.scrollTop >= max - 1) dir = -1; else if (se.scrollTop <= 0) dir = 1;
      const t = await raf(); out.push(t - last); last = t;
    }
    return out;
  }, frames);
  await ctx.close();
  const v = deltas.slice(5).sort((a, b) => a - b);   // the first frames include settling
  const avg = v.reduce((a, b) => a + b, 0) / v.length;
  const row = { theme: entry, avg, p95: v[Math.floor(v.length * 0.95)], max: v.at(-1), dropped: v.filter(d => d > 25).length / v.length, flag: avg > threshold };
  rows.push(row);
  console.log([entry.padEnd(22), row.avg.toFixed(1).padStart(7), row.p95.toFixed(1).padStart(7), row.max.toFixed(1).padStart(7),
    `${Math.round(row.dropped * 100)}%`.padStart(8), row.flag ? ' OVER' : ''].join(' '));
}
await browser.close();
close();
const over = rows.filter(r => r.flag);
console.log(`\n${rows.length} theme(s), ${over.length} over ${threshold}ms${over.length ? ': ' + over.map(r => r.theme).join(', ') : ''}`);
process.exit(strict && over.length ? 1 : 0);
