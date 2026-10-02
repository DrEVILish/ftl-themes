#!/usr/bin/env node
// Screenshot helper for scripts/screenshot_themes.py — do not run directly
// unless you know what you're doing. Launches one browser (--engine,
// default chromium) and walks every theme x example page combination,
// writing <outdir>/<slug>/<page-name>.png at a fixed 1280x900 viewport.
// Prints one JSON line; {"skipped": "..."} when the engine isn't installed.
//
// Needs the `playwright` package resolvable from this file (see the
// scripts/node_modules/playwright symlink that screenshot_themes.py sets
// up before invoking this).
import fs from 'fs';
import path from 'path';
import { ROOT as root, launch, themeReady, FREEZE_CSS } from './_harness.mjs';

const args = process.argv.slice(2);
const opt = (name, dflt) => { const i = args.indexOf(name); return i >= 0 ? args.splice(i, 2)[1] : dflt; };
const base = opt('--base', 'http://localhost:8000');
const outdir = opt('--outdir');
const only = opt('--themes', '');
const engine = opt('--engine', 'chromium');
if (!outdir) { console.error('--outdir is required'); process.exit(2); }

const EXAMPLE_PAGES = ['components.html', 'dashboard.html', 'marketing.html', 'ticketsystem.html', 'powerstation.html', 'soundmixer.html', 'livechat.html'];
const VARIANT_PAGES = ['dashboard.html'];
const VIEWPORT = { width: 1280, height: 900 };

// Each palette variant is shot as its own "theme": <slug>~<variant>.
const themes = JSON.parse(fs.readFileSync(path.join(root, 'dist', 'themes.json'), 'utf8'))
  .flatMap(t => [t.slug, ...(t.variants || []).map(v => `${t.slug}~${v.id}`)])
  .filter(s => !only || only.split(',').includes(s.split('~')[0]))
  .sort();

const browser = await launch(engine);
if (!browser) { console.log(JSON.stringify({ skipped: `${engine} is not installed (npx playwright install ${engine}, or set ${engine.toUpperCase()}_PATH)` })); process.exit(0); }
const page = await browser.newPage({ viewport: VIEWPORT });

// FREEZE_CSS stops anything time-based (animations, transitions, carets)
// so repeated runs of the same markup produce byte-identical screenshots.
// themeReady (scripts/_harness.mjs) waits until the theme stylesheet has
// actually applied and fonts are done, so a screenshot never silently
// captures an unstyled page; the navigation is retried up to three times.

let shots = 0;
const failures = [];
for (const entry of themes) {
  const [slug, variant] = entry.split('~');
  const dir = path.join(outdir, entry);
  fs.mkdirSync(dir, { recursive: true });
  // A palette variant only repaints; one page is enough to catch a
  // regression, and shooting all seven per variant bloats the baseline.
  for (const pageName of variant ? VARIANT_PAGES : EXAMPLE_PAGES) {
    const url = `${base}/${pageName}?theme=${slug}` + (variant ? `&variant=${variant}` : '');
    try {
      let ready = false;
      for (let attempt = 0; attempt < 3 && !ready; attempt++) {
        await page.goto(url, { waitUntil: 'networkidle' });
        ready = await themeReady(page, slug);
        if (!ready && process.env.SHOT_DEBUG) console.error(`retrying ${slug} ${pageName} (attempt ${attempt + 1})`);
      }
      await page.addStyleTag({ content: FREEZE_CSS });
      await page.waitForTimeout(30);
      const dest = path.join(dir, pageName.replace(/\.html$/, '') + '.png');
      await page.screenshot({ path: dest });
      shots++;
      if (!ready) failures.push({ slug, pageName, error: 'theme CSS/fonts never fully applied after 3 attempts' });
    } catch (err) {
      failures.push({ slug, pageName, error: String(err && err.message || err) });
    }
  }
}

await browser.close();
console.log(JSON.stringify({ shots, themes: themes.length, pages: EXAMPLE_PAGES.length, failures }));
process.exit(failures.length ? 1 : 0);
