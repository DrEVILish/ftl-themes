# LCARS decorative chrome

`themes/lcars/chrome.css` adds a generic layout primitive,
`.ftl-lcars-chrome`, that wraps an app's existing content in the
sweep-header + elbowed-rail frame seen on screen in Star Trek TNG/DS9/
Voyager — without requiring any change to the content's own markup or
behavior. This is optional: the `lcars` theme's component styling
(`themes/lcars/theme.css`) works standalone if you don't want the frame.

Reference source: the uploaded `LCARS-26` theme pack's `voyager.css` (the
closest match to the on-screen TNG/DS9/Voyager look; `classic.css` in the
same pack is the more garish original-series look, not used here). Only
the visual sweep/elbow shapes were adapted — not that pack's `lcars.js`
(click sounds, color-cycling animation), which is out of scope; any
motion/audio here is opt-in and respects `prefers-reduced-motion`.

## Markup contract

```html
<div class="ftl-lcars-chrome">
  <header class="ftl-lcars-chrome-header">
    <span class="ftl-lcars-chrome-brand">Ship Name</span>
  </header>

  <div class="ftl-lcars-chrome-rail">
    <div class="ftl-lcars-chrome-rail-bar"></div>
    <div class="ftl-lcars-chrome-rail-bar"></div>
    <div class="ftl-lcars-chrome-rail-bar"></div>
    <div class="ftl-lcars-chrome-rail-bar"></div>
    <nav class="ftl-lcars-chrome-nav">
      <a class="ftl-nav-item is-active" href="#">Ops</a>
      <a class="ftl-nav-item" href="#">Science</a>
    </nav>
  </div>

  <main class="ftl-lcars-chrome-content">
    <!-- your app's real content, unmodified -->
  </main>
</div>
```

## Slots

| Class | Real or decorative | Notes |
|---|---|---|
| `.ftl-lcars-chrome` | Structural | The grid container. Wrap your whole page body in this. |
| `.ftl-lcars-chrome-header` | Structural + real content | The sweep bar; `.ftl-lcars-chrome-brand` inside it is real text. |
| `.ftl-lcars-chrome-rail` | Decorative | The candy-bar stack. `pointer-events: none` — never put real controls directly in it. |
| `.ftl-lcars-chrome-rail-bar` | Decorative | Individual bars; the template ships four, add/remove for taste. |
| `.ftl-lcars-chrome-nav` | Real content | Your actual nav, placed inside the rail visually via `pointer-events: auto`; use ordinary `.ftl-nav-item` links inside it. |
| `.ftl-lcars-chrome-content` | Real content | Your app's existing content region, unmodified. |
| `.ftl-lcars-chrome-corner` | Decorative | Optional filler block; position it yourself per layout (`position: absolute` with your own top/left). |

## Design rules for this primitive

- **Never intercept clicks on decorative pieces.** Every purely decorative
  element here is `pointer-events: none`; only `.ftl-lcars-chrome-nav` and
  `.ftl-lcars-chrome-content` (both real content) receive pointer events.
- **Frame, don't cover.** The chrome is sized via CSS grid so it takes up
  real layout space around the content, never `position: absolute` on top
  of it.
- **Namespace everything** `ftl-lcars-*` so it can't collide with any
  consuming app's own class names — this primitive is meant to wrap
  arbitrary existing markup.
- **Antonio for chrome text only.** The chrome's own labels
  (`.ftl-lcars-chrome-brand`) use the Antonio display font
  (`assets/fonts/Antonio-{Regular,Bold}.woff2`); real app content inside
  `.ftl-lcars-chrome-content` keeps using `--ftl-font` so it stays legible
  and consistent with the rest of the `lcars` theme's component styling.
- **Responsive collapse, not disappearance.** Below 720px the rail
  collapses to a horizontal strip rather than vanishing — see the
  `@media (max-width: 720px)` block in `chrome.css`.

## Using it

Link `dist/lcars.css` (which already includes `chrome.css` — see
`scripts/build.sh`), set `data-theme="lcars"`, and wrap your page body in
the markup above. No separate stylesheet or script is required.
