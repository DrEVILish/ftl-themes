# Authoring a new theme

A theme is one file, `themes/<slug>/theme.css`, plus an optional
`themes/<slug>/chrome.css` if it needs a decorative layout primitive
(LCARS is the existing example — see `docs/lcars-chrome.md`). Nothing else
in the repo needs to change to add a theme.

## 1. Scaffold it

```sh
scripts/new-theme.sh <slug>
```

This creates `themes/<slug>/theme.css` from a template pre-filled with
every `--ftl-*` token and the components most themes end up overriding
(`.ftl-btn`, `.ftl-panel`/`.ftl-modal`/`.ftl-dropdown`, `.ftl-input`/
`.ftl-select`, `.ftl-table th`, `.ftl-nav`), each left blank for you to
fill in. Read `CONTRACT.md` first for what each token/class controls — or
just open an existing theme close to what you're building
(`themes/windows95/theme.css` for a beveled-hardware look,
`themes/tron/theme.css` for a glow-and-angles look, `themes/aqua/theme.css`
for a glossy/gradient look) and use it as a worked reference.

## 2. Fill in the tokens

Pick real colors/fonts for all fourteen `--ftl-*` tokens under
`html[data-theme="<slug>"]`. Do this before touching any component
override — a theme that only sets tokens and changes nothing else already
looks coherent, because `core/ftl-core.css`'s structural rules read every
token. Component overrides are for when the token-only result doesn't
capture the reference look (Windows 95's bevel, LCARS's pill shape,
Aqua's gloss highlight) — not a required step.

## 3. Add component overrides only where the theme's identity needs them

Common overrides, roughly in the order themes tend to need them:
1. Page background (gradient, grid lines, texture) — set on
   `html[data-theme="<slug>"]` directly.
2. Heading voice (case, letter-spacing, glow).
3. `.ftl-btn` shape (border-radius override, bevel, clip-path corners) if
   the token-recolored default button doesn't read as the reference.
4. `.ftl-panel`/`.ftl-modal`/`.ftl-dropdown` surface texture.
5. `.ftl-table th` header treatment.
6. `.ftl-nav` bar treatment.

Don't touch `core/ftl-core.css` or another theme's file — every step above
is additive to your own `themes/<slug>/theme.css` only.

## 4. Build and check it

```sh
scripts/build.sh
```

Regenerates every `dist/<theme>.css`, including yours. Open
`demo.html?theme=<slug>` (or use its in-page switcher) and check every
component renders distinctly and nothing looks like unstyled browser
default — that's the sign a selector in `core.css` isn't being picked up
by your theme (usually a typo in the `data-theme` value, or a token left
at its `:root` fallback that clashes with your palette).

## 5. Register it

- Add a row to `CONTRACT.md`'s theme index table.
- Add an `<option>` for it in `demo.html`'s theme switcher.

## Respecting motion preferences

Any animation (glow pulse, flicker, scanline) must be wrapped in
`@media (prefers-reduced-motion: no-preference)` (opt the animation in)
or have a paired `@media (prefers-reduced-motion: reduce)` rule that turns
it off (opt it out) — see `themes/matrix/theme.css`'s heading flicker for
the opt-in pattern. Never make an animation the only way a piece of state
is communicated (e.g. don't rely on a pulse alone to mean "connected" —
pair it with `.ftl-status-ok`'s color, per `core/ftl-core.css`).

## A minimal runtime theme switcher

`ftl-themes` ships no JavaScript — theme switching is just swapping a
stylesheet `<link>` and a `data-theme` attribute together. A consuming app
typically does this server-side (render the chosen theme's `<link>` and
`data-theme` directly, from a cookie/session value, to avoid a flash of
the wrong theme) with a small client-side fallback for first-visit/no-
cookie cases:

```html
<script>
  (function () {
    var t = localStorage.getItem("ftl-theme") || "blue-future";
    document.documentElement.dataset.theme = t;
    document.getElementById("ftl-theme-link").href = "/themes/" + t + ".css";
  })();
</script>
```
