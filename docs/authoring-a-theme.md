# Authoring a new theme

A theme is one file, `themes/<slug>/theme.css`, plus an optional
`themes/<slug>/chrome.css` if it needs a decorative layout primitive
(LCARS is the existing example — see `docs/lcars-chrome.md`). Nothing else
in the repo needs to change.

## 0. Read the one rule first

`CONTRACT.md` § "How a theme overrides a component". Set component look via
`--ftl-<component>-*` properties **at root scope**; never declare
`background`/`color` on a base component selector like
`html[data-theme="x"] .ftl-btn`, because that outranks core's
`.ftl-btn-danger`/`-success` rules and silently erases them — a delete
button ends up looking identical to a normal one. `scripts/check.sh`
enforces this, but knowing why saves a confusing detour.

## 1. Scaffold it

```sh
scripts/new-theme.sh <slug>
```

Creates `themes/<slug>/theme.css` pre-filled with every required token and
a commented-out list of the common component override points. Fill in the
header's `Theme-Name:` and `Description:` too — the build reads them into
`dist/themes.json`, which is what theme pickers and `demo.html` display.

## 2. Fill in the tokens

Set all the required `--ftl-*` tokens. A theme that sets *only* tokens and
overrides nothing else already looks coherent, because core's structural
rules read every token — component overrides are for when that isn't enough
to capture the reference look.

Pay attention to `--ftl-on-accent` / `-on-danger` / `-on-success`: these are
the text colors on top of those fills, and they must hit 4.5:1 against
them. If your accent is mid-tone you'll usually need white or near-black,
not the page background. The lint computes this for you.

Pick a worked reference close to what you're building:
- `themes/windows95/theme.css` — beveled hardware, sharp corners, light palette
- `themes/aqua/theme.css` — gradients, gloss, light palette
- `themes/tron/theme.css` — glow, cut corners, dark palette
- `themes/matrix/theme.css` — outline-only buttons, monospace, dark palette
- `themes/lcars/theme.css` — heavy shape overrides (pills, elbows)

## 3. Add component overrides where the theme's identity needs them

Roughly in the order themes tend to need them:
1. Page background (gradient, grid, texture) — on `html[data-theme="…"]`.
2. Heading voice (case, tracking, glow).
3. Button look — via `--ftl-btn-*` at root; shape properties
   (`border-radius`, `clip-path`, bevel `border-color`) are fine directly
   on `.ftl-btn`.
4. Surfaces — `--ftl-panel-bg`, `--ftl-panel-shadow`, `--ftl-modal-*`.
5. Table header/rows — `--ftl-table-head-*`, `--ftl-row-*`.
6. Nav/tabs — `--ftl-nav-*`, `--ftl-tab-*`.
7. The htmx indicator — `--ftl-indicator-fg` / `-track`, so pending states
   look like they belong to the theme.

Never edit `core/ftl-core.css` or another theme's file; authoring is
strictly additive.

## 4. Build and check

```sh
scripts/build.sh    # dist/<slug>.css + dist/themes.json
scripts/check.sh    # the contract lint
```

The lint fails on: a missing token, a base-component `background`/`color`
override, `outline: none` on a focus state, `!important` on a universal
selector, a contrast floor violation, a stale `dist/`, and a manifest that
doesn't match `themes/`. Each of those rules exists because that exact bug
shipped once — see `CHANGELOG.md`.

Then open `demo.html` (serve the folder over HTTP so `dist/themes.json`
loads) and pick your theme. Check every component renders distinctly, Tab
through the controls to confirm the focus ring is visible everywhere, and
verify the semantic buttons still read as primary/danger/success.

## 5. Give it a layout

A theme is a layout as much as a palette. Set the `--ftl-app-*` properties
so that switching to your theme visibly re-arranges the shell — bar height
and radius, whether a decorative rail appears and how it is painted, how
the content is inset, what the status strip looks like. Compare
`themes/lcars/theme.css` (a 6rem candy rail and an elbowed sweep bar)
against `themes/blue-future/theme.css` (no rail, edge-to-edge content) for
the two extremes. The lint warns if a theme sets none of these.

## 6. Write its README.md

Every theme has a `README.md` beside its `theme.css` saying what it is
trying to achieve — the lint fails without one. It should cover: the
reference being reproduced, the theme's core values as numbered rules, why
the significant token values are what they are, what a contributor must not
change, and the tell-tales of an inauthentic result. The point is that the
next person extends the theme instead of gradually turning it into a
different one.

## 7. Register it

Add a row to `CONTRACT.md`'s theme index. `demo.html` and `dist/themes.json`
pick the theme up automatically — no list to edit.

## Motion

Any animation must either be opted in under
`@media (prefers-reduced-motion: no-preference)` (see the Matrix heading
flicker) or turned off in a paired `reduce` block. Never let an animation
be the only carrier of state — pair it with color and shape, the way
`.ftl-status` and the table row states do.

## Stay offline-safe: no remote URLs, and vendor fonts you actually use

`scripts/check.py` fails a theme (or a core file) containing a remote
`url(...)` or `@import` — `http://`, `https://`, or protocol-relative
`//`. Some consuming apps embed the compiled bundles specifically so their
UI works with zero network access (a field recorder, a kiosk); a single
remote reference upstream would silently break that guarantee for every
one of them.

The corollary: if a theme's authentic look depends on a font, either
vendor it into `assets/fonts/` with a local `@font-face` (see
`themes/lcars/theme.css` for the pattern — note that `scripts/build.sh`
rewrites the relative `url()` for the `dist/` bundle, so write paths as
`url("assets/…")` in the theme source) or don't name it in the font stack
at all. Naming an unvendored face (as `tron` used to do with Eurostile)
doesn't 404 — it silently falls back to the next stack entry, so the
theme quietly never looks like its reference on a real machine. Say so in
a header comment instead (see `tron`'s or `alienware`'s "Note on fonts").

## A minimal runtime theme switcher

`ftl-themes` ships no JavaScript; switching is swapping a `<link>` and the
`data-theme` attribute. Prefer rendering both server-side from a
cookie/session value so there's no flash of the wrong theme, with a client
fallback for first visits:

```html
<script>
  (function () {
    var t = localStorage.getItem("ftl-theme") || "blue-future";
    document.documentElement.dataset.theme = t;
    document.getElementById("ftl-theme-link").href = "/static/themes/" + t + ".css";
  })();
</script>
```
