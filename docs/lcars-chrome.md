# LCARS decorative chrome (optional)

**Most apps do not need this file.** Adopting the shared app shell
(`core/layout.css` — `.app` + `.app-bar` + `.app-rail` +
`.app-main`, see CONTRACT.md) already gives the LCARS theme its sweep
bar and candy rail automatically, and switches the layout back when another
theme is selected. That path costs no LCARS-specific markup.

`themes/lcars/chrome.css` is the richer, opt-in alternative for an app that
wants the fuller on-screen treatment with explicit markup: individually
rounded rail bars and a real nav living inside the rail. It wraps an app's
existing content in the sweep-header + elbowed-rail frame seen in TNG/DS9/
Voyager without changing that content's own markup or behaviour — but the
wrapper itself is LCARS-specific, so it stays in place under every other
theme too.

Reference source: the uploaded `LCARS-26` theme pack's `voyager.css` (the
closest match to the on-screen TNG/DS9/Voyager look; `classic.css` in the
same pack is the more garish original-series look, not used here). Only
the visual sweep/elbow shapes were adapted — not that pack's `lcars.js`
(click sounds, color-cycling animation), which is out of scope; any
motion/audio here is opt-in and respects `prefers-reduced-motion`.

## Markup contract

```html
<div class="lcars-chrome">
  <header class="lcars-chrome-header">
    <span class="lcars-chrome-brand">Ship Name</span>
  </header>

  <div class="lcars-chrome-rail">
    <div class="lcars-chrome-rail-bar"></div>
    <div class="lcars-chrome-rail-bar"></div>
    <div class="lcars-chrome-rail-bar"></div>
    <div class="lcars-chrome-rail-bar"></div>
    <nav class="lcars-chrome-nav">
      <a class="nav-item is-active" href="#">Ops</a>
      <a class="nav-item" href="#">Science</a>
    </nav>
  </div>

  <main class="lcars-chrome-content">
    <!-- your app's real content, unmodified -->
  </main>
</div>
```

## Slots

| Class | Real or decorative | Notes |
|---|---|---|
| `.lcars-chrome` | Structural | The grid container. Wrap your whole page body in this. |
| `.lcars-chrome-header` | Structural + real content | The sweep bar; `.lcars-chrome-brand` inside it is real text. |
| `.lcars-chrome-rail` | Decorative | The candy-bar stack. `pointer-events: none` — never put real controls directly in it. |
| `.lcars-chrome-rail-bar` | Decorative | Individual bars; the template ships four, add/remove for taste. |
| `.lcars-chrome-nav` | Real content | Your actual nav, placed inside the rail visually via `pointer-events: auto`; use ordinary `.nav-item` links inside it. |
| `.lcars-chrome-content` | Real content | Your app's existing content region, unmodified. |
| `.lcars-chrome-corner` | Decorative | Optional filler block; position it yourself per layout (`position: absolute` with your own top/left). |

## Design rules for this primitive

- **Never intercept clicks on decorative pieces.** Every purely decorative
  element here is `pointer-events: none`; only `.lcars-chrome-nav` and
  `.lcars-chrome-content` (both real content) receive pointer events.
- **Frame, don't cover.** The chrome is sized via CSS grid so it takes up
  real layout space around the content, never `position: absolute` on top
  of it.
- **Namespace everything** `lcars-*` so it can't collide with any
  consuming app's own class names — this primitive is meant to wrap
  arbitrary existing markup.
- **Antonio for chrome text only.** The chrome's own labels
  (`.lcars-chrome-brand`) use the Antonio display font
  (`assets/fonts/Antonio-{Regular,Bold}.woff2`); real app content inside
  `.lcars-chrome-content` keeps using `--font` so it stays legible
  and consistent with the rest of the `lcars` theme's component styling.
- **Responsive collapse, not disappearance.** Below 720px the rail
  collapses to a horizontal strip rather than vanishing — see the
  `@media (max-width: 720px)` block in `chrome.css`.

## Using it

Link `dist/lcars.css` (which already includes `chrome.css` — see
`scripts/build.sh`), set `data-theme="lcars"`, and wrap your page body in
the markup above. No separate stylesheet or script is required.
