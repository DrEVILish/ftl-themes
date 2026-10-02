#!/usr/bin/env node
// Accessibility audit (PLAN.md §24): axe-core's WCAG 2.0/2.1/2.2 A and AA
// rules on every example page (each root *.html that loads a theme), per
// theme, at the Mobile (393x852, touch) and Desktop (1280x800) tiers.
// Palette variants only repaint, so they run on the dashboard only.
//
// Needs axe-core next to Playwright in scripts/node_modules (see
// test/README.md for the one-line install).
//
// Usage:
//   node scripts/a11y_audit.mjs [--theme slug[~variant]]... [--page name]...
//                               [--tier mobile|desktop]... [--engine chromium|firefox|webkit]...
//                               [--strict | --blame slug]
// Prints violations by impact per theme/page/tier and the rules, worst
// first, each attributed to core/page markup or to the themes that cause
// it, and writes test/a11y/report.json. Exit 0 unless --strict and a
// serious or critical violation was found, or --blame <slug> and a serious
// or critical rule is attributed to that theme (or one of its variants);
// --blame needs a second theme in the run to compare against. A violation
// listed for its engine in test/engine-known-issues.json (script "a11y",
// key "<theme> <tier> <page> <rule-id>") is reported but never fails.
import fs from 'fs';
import path from 'path';
import { createRequire } from 'module';
import { ROOT as root, takeEngines, launch, contextOptions, knownIssues, serveRoot, openThemed, themeEntries, examplePages, FREEZE_CSS } from './_harness.mjs';

let axePath;
try { axePath = createRequire(import.meta.url).resolve('axe-core/axe.min.js'); } catch {
  console.error('axe-core is not installed. Run:\n  npm i --no-save --no-package-lock --prefix scripts playwright@1.63.0 axe-core');
  process.exit(2);
}

const TIERS = {
  mobile: { viewport: { width: 393, height: 852 }, hasTouch: true, isMobile: true },
  desktop: { viewport: { width: 1280, height: 800 } },
};
const IMPACTS = ['critical', 'serious', 'moderate', 'minor'];
const TAGS = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'];

// ---- args
const argv = process.argv.slice(2), want = { theme: [], page: [], tier: [] };
const engines = takeEngines(argv);
let strict = false, blame = null;
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (a === '--strict') strict = true;
  else if (a === '--blame' && argv[i + 1]) blame = argv[++i];
  else if (a.startsWith('--') && a.slice(2) in want && argv[i + 1]) want[a.slice(2)].push(argv[++i]);
  else { console.error(`unknown or incomplete argument: ${a}`); process.exit(2); }
}
const all = themeEntries(), PAGES = examplePages();
const themes = want.theme.length ? want.theme : all;
const pages = want.page.length ? want.page : PAGES;
const tiers = want.tier.length ? want.tier : Object.keys(TIERS);
for (const [list, known, what] of [[themes, all, 'theme'], [pages, PAGES, 'page'], [tiers, Object.keys(TIERS), 'tier']])
  for (const x of list) if (!known.includes(x)) { console.error(`unknown ${what}: ${x} (known: ${known.join(', ')})`); process.exit(2); }

// ---- run
const { base, close } = await serveRoot();
const results = [];
for (const engine of engines) {
  const browser = await launch(engine);
  if (!browser) { results.push({ engine, skipped: true }); continue; }
  const known = knownIssues(engine, 'a11y');
  console.log(`\n[${engine}]  rules (nodes) by impact`);
  console.log(['theme'.padEnd(22), 'tier'.padEnd(8), 'page'.padEnd(22), ...IMPACTS.map(h => h.padStart(9))].join(' '));
  for (const tier of tiers) {
    const ctx = await browser.newContext(contextOptions(engine, TIERS[tier]));
    const pw = await ctx.newPage();
    for (const entry of themes) {
      const [slug, variant] = entry.split('~');
      for (const pg of variant ? pages.filter(p => p === 'dashboard') : pages) {
        const url = `${base}/${pg}.html?theme=${slug}` + (variant ? `&variant=${variant}` : '') + (pg === 'components' ? '&embed=1' : '');
        const row = { engine, theme: entry, tier, page: pg, counts: {}, violations: [] };
        try {
          if (!await openThemed(pw, url, slug)) row.warning = 'theme CSS/fonts never fully applied';
          await pw.addStyleTag({ content: FREEZE_CSS });
          await pw.addScriptTag({ path: axePath });
          const v = await pw.evaluate(async (tags) => (await window.axe.run(document, { runOnly: { type: 'tag', values: tags }, resultTypes: ['violations'] })).violations
            .map(x => ({ id: x.id, impact: x.impact, help: x.help, url: x.helpUrl, nodes: x.nodes.length,
              targets: x.nodes.slice(0, 5).map(n => n.target.join(' ')), summary: x.nodes[0]?.failureSummary?.split('\n').slice(0, 2).join(' ') })), TAGS);
          for (const x of v) {
            const k = known(`${entry} ${tier} ${pg} ${x.id}`);
            if (k) x.knownIssue = k.reason || k.match;
          }
          row.violations = v;
        } catch (err) {
          row.error = String(err?.message || err);
        }
        for (const i of IMPACTS) {
          const hit = row.violations.filter(x => x.impact === i);
          row.counts[i] = { rules: hit.length, nodes: hit.reduce((n, x) => n + x.nodes, 0) };
        }
        row.fail = !!row.error || row.violations.some(x => !x.knownIssue && (x.impact === 'critical' || x.impact === 'serious'));
        results.push(row);
        const cells = row.error ? ['ERROR', row.error.split('\n')[0]] : IMPACTS.map(i => row.counts[i].rules ? `${row.counts[i].rules} (${row.counts[i].nodes})` : '-');
        console.log([entry.padEnd(22), tier.padEnd(8), pg.padEnd(22), ...cells.map(c => c.padStart(9))].join(' '));
      }
    }
    await ctx.close();
  }
  await browser.close();
}
close();

// ---- rules, worst first. Where a rule fails the same way (same node
// count) for every theme run on a page and tier, the page markup or core is
// at fault; where only some themes fail it, or fail more nodes, the theme is.
const ran = results.filter(r => !r.skipped && !r.error);
const runsAt = new Map();   // "engine tier page" -> themes run there
for (const r of ran) { const k = `${r.engine} ${r.tier} ${r.page}`; runsAt.set(k, (runsAt.get(k) || new Set()).add(r.theme)); }
const byRule = new Map();
for (const r of ran) for (const v of r.violations.filter(v => !v.knownIssue)) {
  const s = byRule.get(v.id) || { id: v.id, impact: v.impact, help: v.help, runs: 0, nodes: 0, pages: new Set(), sample: v.targets[0], at: new Map() };
  s.runs++; s.nodes += v.nodes; s.pages.add(r.page);
  const k = `${r.engine} ${r.tier} ${r.page}`;
  s.at.set(k, (s.at.get(k) || new Map()).set(r.theme, v.nodes));
  byRule.set(v.id, s);
}
for (const s of byRule.values()) {
  s.core = new Set(); s.themes = new Set();
  for (const [k, hits] of s.at) {
    const run = runsAt.get(k), min = Math.min(...[...run].map(t => hits.get(t) || 0));
    if (min > 0 && run.size > 1) s.core.add(k.split(' ')[2]);
    for (const [t, n] of hits) if (n > min) s.themes.add(t);
  }
  delete s.at;
}
const themesRun = new Set(ran.map(r => r.theme)).size;
const top = [...byRule.values()].sort((a, b) => IMPACTS.indexOf(a.impact) - IMPACTS.indexOf(b.impact) || b.runs - a.runs);
if (top.length) {
  console.log(`\nRules, worst first (${ran.length} runs, ${themesRun} theme(s)). "core/page": fails alike in every theme; "theme": only in, or worse in, the themes named.`);
  for (const s of top) {
    const where = themesRun < 2 ? '' : [s.core.size && `core/page on ${[...s.core].join(', ')}`, s.themes.size && `theme: ${[...s.themes].join(', ')}`].filter(Boolean).join('; ');
    console.log(`  ${s.impact.padEnd(9)} ${s.id.padEnd(28)} ${String(s.runs).padStart(4)} runs ${String(s.nodes).padStart(5)} nodes  ${where}`);
    console.log(`  ${''.padEnd(9)} ${s.help}  e.g. ${s.sample}`);
  }
}

const out = path.join(root, 'test/a11y/report.json');
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.writeFileSync(out, JSON.stringify({ generated: new Date().toISOString(), tags: TAGS, tiers: TIERS, results,
  rules: top.map(s => ({ ...s, themes: [...s.themes], core: [...s.core], pages: [...s.pages] })) }, null, 1));
const failed = results.filter(r => r.fail).length;
console.log(`\n${ran.length} runs, ${failed} with serious/critical violations${strict ? '' : ' (report mode)'}. Report: ${path.relative(root, out)}`);
if (blame) {
  const mine = top.filter(s => (s.impact === 'critical' || s.impact === 'serious') && [...s.themes].some(t => t === blame || t.startsWith(blame + '~')));
  console.log(`${blame}: ${mine.length} serious/critical rule(s) caused by the theme${mine.length ? ': ' + mine.map(s => s.id).join(', ') : ''}`);
  process.exit(mine.length ? 1 : 0);
}
process.exit(strict && failed ? 1 : 0);
