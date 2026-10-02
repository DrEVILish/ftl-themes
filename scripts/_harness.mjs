// Shared plumbing for the rendered checks (v5_audit, core_regressions,
// _pw_shot, a11y_audit, render_cost): engine selection and launch, the
// known-issue list, a static server on the repo root, and the
// "theme applied" wait. Not a CLI.
import * as pw from 'playwright';
import http from 'http';
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';

export const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const ENGINES = ['chromium', 'firefox', 'webkit'];

// Pulls every `--engine name` pair out of argv (mutating it) and returns the
// engines asked for, chromium when none.
export function takeEngines(argv) {
  const out = [];
  for (let i = argv.indexOf('--engine'); i >= 0; i = argv.indexOf('--engine')) {
    const [, name] = argv.splice(i, 2);
    if (!ENGINES.includes(name)) { console.error(`unknown engine: ${name} (known: ${ENGINES.join(', ')})`); process.exit(2); }
    if (!out.includes(name)) out.push(name);
  }
  return out.length ? out : ['chromium'];
}

// Chromium speaks CDP, which tolerates a browser build that doesn't match the
// installed Playwright, so any Playwright-downloaded Chromium will do.
// Firefox and WebKit are patched builds tied to their Playwright version, so
// they get no such fallback.
// ponytail: Linux folder layout only; set CHROMIUM_PATH on macOS/Windows.
function installedChromium() {
  const dirs = [process.env.PLAYWRIGHT_BROWSERS_PATH, path.join(os.homedir(), '.cache/ms-playwright')].filter(Boolean);
  const found = [];
  for (const d of dirs) {
    if (!fs.existsSync(d)) continue;
    for (const sub of fs.readdirSync(d).sort().reverse())
      for (const rel of ['chrome-headless-shell-linux64/chrome-headless-shell', 'chrome-linux64/chrome', 'chrome-linux/chrome'])
        if (/^chromium(_headless_shell)?-\d+$/.test(sub) && fs.existsSync(path.join(d, sub, rel))) found.push(path.join(d, sub, rel));
  }
  return found.find(f => f.includes('headless_shell')) || found[0];
}

// A browser, or null (with a SKIP line) when the engine isn't installed.
// <ENGINE>_PATH (CHROMIUM_PATH, FIREFOX_PATH, WEBKIT_PATH) overrides the
// executable.
export async function launch(name) {
  const exe = process.env[`${name.toUpperCase()}_PATH`];
  try {
    return await pw[name].launch({ executablePath: exe || undefined });
  } catch (err) {
    const missing = /Executable doesn't exist|missing dependencies|ENOENT/i.test(err.message);
    const alt = !exe && name === 'chromium' && missing && installedChromium();
    if (alt) return pw.chromium.launch({ executablePath: alt });
    if (!missing) throw err;
    console.log(`SKIP  ${name}: not installed for this Playwright (${err.message.split('\n')[0].replace(/^.*?: /, '')}). ` +
      `Install with \`npx playwright install ${name}\` or set ${name.toUpperCase()}_PATH.`);
    return null;
  }
}

// Firefox has no mobile emulation; isMobile throws there.
export const contextOptions = (engine, opts) => {
  const o = { ...opts };
  if (engine === 'firefox') delete o.isMobile;
  return o;
};

// test/engine-known-issues.json: { "<engine>": [{ "script", "match", "reason" }] }.
// Returns (key) => the matching entry or undefined; each script documents
// the shape of its keys (see test/README.md).
export function knownIssues(engine, script) {
  const file = path.join(ROOT, 'test/engine-known-issues.json');
  const list = fs.existsSync(file) ? (JSON.parse(fs.readFileSync(file, 'utf8'))[engine] || []) : [];
  const mine = list.filter(e => e.script === script).map(e => ({ ...e, re: new RegExp(e.match) }));
  return (key) => mine.find(e => e.re.test(key));
}

// Every theme, plus each palette variant as <slug>~<variant>. build.sh
// deletes dist/ first and writes themes.json last, so a build running in
// parallel gets up to a minute to finish.
export function themeEntries() {
  const file = path.join(ROOT, 'dist/themes.json');
  for (let i = 0; i < 60 && !fs.existsSync(file); i++) Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 1000);
  if (!fs.existsSync(file)) { console.error('dist/themes.json is missing: run scripts/build.sh'); process.exit(2); }
  return JSON.parse(fs.readFileSync(file, 'utf8')).flatMap(t => [t.slug, ...(t.variants || []).map(v => `${t.slug}~${v.id}`)]);
}

// Example pages: every root *.html that loads a theme (gallery and index don't).
export const examplePages = () => fs.readdirSync(ROOT)
  .filter(f => f.endsWith('.html') && fs.readFileSync(path.join(ROOT, f), 'utf8').includes('id="theme-link"'))
  .map(f => f.replace(/\.html$/, '')).sort();

// Static server on the repo root (pages fetch dist/themes.json). Resolves to
// { base, close }.
const TYPES = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.mjs': 'text/javascript', '.json': 'application/json',
  '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.gif': 'image/gif',
  '.woff2': 'font/woff2', '.woff': 'font/woff', '.ttf': 'font/ttf', '.otf': 'font/otf' };
export async function serveRoot() {
  const server = http.createServer((req, res) => {
    const file = path.join(ROOT, decodeURIComponent(new URL(req.url, 'http://x').pathname));
    if (!file.startsWith(ROOT + path.sep)) { res.writeHead(403); return res.end(); }
    fs.readFile(file, (err, buf) => {
      if (err) { res.writeHead(404); return res.end(); }
      res.writeHead(200, { 'content-type': TYPES[path.extname(file)] || 'application/octet-stream' });
      res.end(buf);
    });
  });
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  return { base: `http://127.0.0.1:${server.address().port}`, close: () => server.close() };
}

// True once theme-loader.js has applied the theme's stylesheet and fonts are
// done. The bundle is one `@layer ui {}` block, so nested rules are counted.
export async function themeReady(page, slug, timeout = 5000) {
  try {
    await page.waitForFunction((slug) => {
      if (document.documentElement.dataset.theme !== slug) return false;
      const link = document.getElementById('theme-link');
      if (!link || !link.sheet) return false;
      const count = (rules) => Array.from(rules).reduce((n, r) => n + 1 + (r.cssRules ? count(r.cssRules) : 0), 0);
      try { if (count(link.sheet.cssRules) < 3) return false; } catch (e) { return false; }
      return document.fonts.status === 'loaded';
    }, slug, { timeout, polling: 100 });
    return true;
  } catch { return false; }
}

// goto + themeReady, up to three tries. Returns whether the theme applied.
export async function openThemed(page, url, slug) {
  for (let i = 0; i < 3; i++) {
    await page.goto(url, { waitUntil: 'networkidle' });
    if (await themeReady(page, slug)) return true;
  }
  return false;
}

export const FREEZE_CSS = '*{animation:none!important;transition:none!important;caret-color:transparent!important;scroll-behavior:auto!important}';
