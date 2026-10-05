// Dependency-free edge checks for the tiny browser-to-app JS bridges.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

function runBridge(file, { standalone = true, mode = '', posture = null, appPresent = true, screenPresent = true } = {}) {
  const listeners = new Map();
  const html = { dataset: {} };
  const attrs = new Set();
  const app = appPresent ? {
    setAttribute: (key) => attrs.add(key),
    removeAttribute: (key) => attrs.delete(key),
  } : null;
  const screen = screenPresent ? { hidden: false } : null;
  const devicePosture = posture === null ? null : {
    type: posture,
    addEventListener: (name, fn) => listeners.set(`posture:${name}`, fn),
  };
  const documentListeners = new Map();
  const context = {
    document: {
      documentElement: html,
      querySelector: (selector) => selector.startsWith('.splash') ? screen : app,
      addEventListener: (name, fn, options) => documentListeners.set(name, { fn, options }),
      dispatchEvent: (event) => documentListeners.get(event.type)?.fn(event),
    },
    navigator: { devicePosture },
    matchMedia: () => ({ matches: standalone }),
    getComputedStyle: () => ({ getPropertyValue: () => mode }),
    addEventListener: (name, fn) => listeners.set(name, fn),
    Event: class { constructor(type) { this.type = type; } },
    window: {},
  };
  vm.runInNewContext(fs.readFileSync(new URL(`../assets/js/${file}.js`, import.meta.url), 'utf8'), context);
  return { context, html, attrs, app, screen, listeners, documentListeners };
}

// Fold bridge: installed PWA only; unknown CSS mode clears stale state; posture
// updates are forwarded, while browser resize re-reads CSS-owned layout state.
const windowed = runBridge('foldable', { standalone: false, mode: 'book' });
assert.equal(windowed.html.dataset.foldMode, undefined);
const fold = runBridge('foldable', { mode: 'book', posture: 'continuous' });
assert.equal(fold.html.dataset.foldMode, 'book');
assert.equal(fold.html.dataset.foldPosture, 'continuous');
fold.context.getComputedStyle = () => ({ getPropertyValue: () => 'tabletop' });
fold.listeners.get('resize')();
assert.equal(fold.html.dataset.foldMode, 'tabletop');
fold.context.navigator.devicePosture.type = 'folded';
fold.listeners.get('posture:change')();
assert.equal(fold.html.dataset.foldPosture, 'folded');
fold.context.getComputedStyle = () => ({ getPropertyValue: () => 'unknown' });
fold.listeners.get('resize')();
assert.equal(fold.html.dataset.foldMode, undefined);

// Boot bridge: absent markup is harmless; app readiness is one-shot and also
// works when no app shell exists.
const noScreen = runBridge('boot', { screenPresent: false });
assert.equal(noScreen.context.window.ftlAppReady, undefined);
const boot = runBridge('boot');
assert.equal(boot.attrs.has('aria-busy'), true);
boot.context.window.ftlAppReady();
boot.context.window.ftlAppReady();
assert.equal(boot.attrs.has('aria-busy'), false);
assert.equal(boot.screen.hidden, true);
assert.equal(boot.html.dataset.appReady, '');
assert.equal(boot.documentListeners.get('ftl:app-ready').options.once, true);
const noApp = runBridge('boot', { appPresent: false });
noApp.context.window.ftlAppReady();
assert.equal(noApp.screen.hidden, true);
console.log('browser bridge edge checks passed (foldable and boot readiness)');

// CSS remains responsible for PWA-only segment layout and keeping the status
// region inside a segment; this guards the CSS half without device hardware.
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const layout = fs.readFileSync(path.join(root, 'core/layout.css'), 'utf8');
assert.match(layout, /display-mode:\s*standalone\).*horizontal-viewport-segments:\s*2/);
assert.match(layout, /display-mode:\s*standalone\).*vertical-viewport-segments:\s*2/);
assert.match(layout, /env\(viewport-segment-right 0 0\)/);
assert.match(layout, /env\(viewport-segment-bottom 0 0\)/);
assert.match(layout, /\.app-rail\s*\{\s*display:\s*none !important/);
console.log('foldable CSS guard checks passed (PWA segment layouts and hinge clearance)');
