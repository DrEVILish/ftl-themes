#!/usr/bin/env node
// Screenshot helper for scripts/screenshot_themes.py — do not run directly
// unless you know what you're doing. Launches one Chromium instance and
// walks every theme x example page combination, writing
// <outdir>/<slug>/<page-name>.png at a fixed 1280x900 viewport.
//
// Needs the `playwright` package resolvable from this file (see the
// scripts/node_modules/playwright symlink that screenshot_themes.py sets
// up before invoking this).
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const opt = (name, dflt) => { const i = args.indexOf(name); return i >= 0 ? args.splice(i, 2)[1] : dflt; };
const base = opt('--base', 'http://localhost:8000');
const outdir = opt('--outdir');
if (!outdir) { console.error('--outdir is required'); process.exit(2); }

const EXAMPLE_PAGES = ['example.html', 'example-2.html', 'example-3.html', 'example-4.html'];
const VIEWPORT = { width: 1280, height: 900 };

const themes = JSON.parse(fs.readFileSync(path.join(root, 'dist', 'themes.json'), 'utf8'))
  .map(t => t.slug)
  .sort();

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: VIEWPORT });

// Freeze anything time-based (CSS animations/transitions, blinking carets)
// so repeated runs of the same markup produce byte-identical screenshots.
const FREEZE_CSS = '*{animation:none!important;transition:none!important;caret-color:transparent!important;scroll-behavior:auto!important}';

// theme-loader.js sets html[data-theme] and the #ftl-theme-link href
// synchronously, but the stylesheet itself loads async — and under the
// dev-only ThreadingHTTPServer, occasional connection hiccups can leave a
// page rendered with no theme CSS at all (or a still-loading custom font,
// e.g. the LEGO wordmark) even after networkidle. Verify the stylesheet
// actually applied and fonts are done, retrying the navigation a few times
// before giving up, so a screenshot never silently captures an unstyled page.
// Polls (rather than a single snapshot check) so a page that's still
// loading its webfont -- normal right after a cold navigation, especially
// the very first one of a run -- gets real time to finish instead of
// being retried (and reloaded) for no reason.
async function waitForThemeReady(pw, slug, timeout = 5000) {
  try {
    await pw.waitForFunction((slug) => {
      if (document.documentElement.dataset.theme !== slug) return false;
      const link = document.getElementById('ftl-theme-link');
      if (!link || !link.sheet) return false;
      try { if (link.sheet.cssRules.length < 3) return false; } catch (e) { return false; }
      return document.fonts.status === 'loaded';
    }, slug, { timeout, polling: 100 });
    return true;
  } catch (e) {
    return false;
  }
}

let shots = 0;
const failures = [];
for (const slug of themes) {
  const dir = path.join(outdir, slug);
  fs.mkdirSync(dir, { recursive: true });
  for (const pageName of EXAMPLE_PAGES) {
    const url = `${base}/${pageName}?theme=${slug}`;
    try {
      let ready = false;
      for (let attempt = 0; attempt < 3 && !ready; attempt++) {
        await page.goto(url, { waitUntil: 'networkidle' });
        ready = await waitForThemeReady(page, slug);
        if (!ready && process.env.FTL_SHOT_DEBUG) console.error(`retrying ${slug} ${pageName} (attempt ${attempt + 1})`);
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
