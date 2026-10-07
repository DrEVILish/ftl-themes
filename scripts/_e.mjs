import { chromium } from 'playwright';
const [,, url, sel, out, theme] = process.argv;
const b = await chromium.launch({ executablePath: '/root/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome' });
const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
await p.goto(url);
if (theme) await p.evaluate(t => { document.documentElement.dataset.theme = t; const l=[...document.querySelectorAll('link[rel=stylesheet]')].find(l=>/dist\//.test(l.href)); if (l) l.href = l.href.replace(/dist\/[^/]+\.css/, `dist/${t}.css`); }, theme);
await p.waitForTimeout(700);
await p.locator(sel).first().screenshot({ path: out });
await b.close();
