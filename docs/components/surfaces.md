# Surfaces and media (v5)

Source: `core/components/surfaces.css` and `assets/js/window.js`. Live
examples: `components-surfaces.html`. Covers PLAN.md §9 #47 (image card),
#49 (draggable window) and #50 (brand sign-in buttons). Builds on core's
`.card`, `.modal`, the window pattern (`.window-max`, `.is-maximized`,
`.btn-close`/`-min`/`-max`), `.skeleton` and `.stretched-link`.

Tokens are listed as `token: default`. Set them on `html[data-theme="x"]` like
every other component token. The brand buttons have no tokens, on purpose.

---

## Image card `.card.has-media`

```html
<article class="card has-media">
  <img src="ridge.jpg" alt="Mountain ridge at dusk" loading="lazy" width="1600" height="900">
  <div class="card-body">
    <h4>Ridge walk</h4>
    <p class="text-muted">Six hours, 14 km.</p>
  </div>
</article>
```

- **Media** is the first child: `<img>`, `<video>`, `<picture>` or a
  `.card-media` box (for badges over the image, or an inline `<svg>`). It
  bleeds to the card edge, takes the card's corners and is locked to
  `--card-media-ratio`, whatever the `width`/`height` attributes say (keep
  them anyway: they let the browser reserve space before CSS loads).
  An `<img>`/`<video>` inside a `<picture>`/`.card-media` fills it with
  `object-fit: cover`.
- **Body**: `.card-body` takes the card's padding (`--surface-pad`) and spaces
  its children by `--space-2xs`.
- **Ratio**: `style="--card-media-ratio: 1"` (square), `4 / 3`, `3 / 2`… The
  inline style is the documented value API.
- **Whole card clickable**: put `.stretched-link` on the title link. The card
  is already `position: relative`.

### States and variants

| Markup | Result |
|---|---|
| `.card.has-media.is-overlay` | Body on top of the media's bottom edge, on a dark scrim, with white text. The scrim keeps text at ≥ 4.5:1 over any image, including pure white. `--text`, `--muted` and `--on-surface` are re-pointed inside the body, so `.text-muted` and links stay readable. |
| `.card.has-media.is-horizontal` | Media beside the body (`--card-media-size` of the width, the card's full height) when the **nearest size container** is wider than 480px; stacked when it is 480px or less. Containers are `.modal`, `.drawer` and `.cq`: put `.cq` on the grid cell, column or panel that holds the card. With no container ancestor the card follows the viewport (horizontal above 480px). Ignored with `.is-overlay`. |
| `aria-busy="true"` on the card | Lazy-load skeleton: the reserved media box runs core's shimmer and hides alt text. The box always shows `--card-media-placeholder` until the image paints over it, so a slow image never collapses the layout. The app removes `aria-busy` on `load`. Pair with `.skeleton-text` lines in the body when the text is loading too. |

```html
<!-- Horizontal in a container that decides its own width -->
<div class="cq"><article class="card has-media is-horizontal">…</article></div>

<!-- Loading -->
<article class="card has-media" aria-busy="true">
  <div class="card-media" role="img" aria-label="Image loading"></div>
  <div class="card-body"><span class="skeleton skeleton-text"></span></div>
</article>
<script>img.addEventListener("load", () => card.removeAttribute("aria-busy"));</script>
```

### Tokens

| Token | Default |
|---|---|
| `--card-media-ratio` | `16 / 9` |
| `--card-media-size` | `40%` (horizontal media width) |
| `--card-media-placeholder` | `var(--skeleton-bg, var(--surface-2))` |
| `--skeleton-shine` | `rgba(255, 255, 255, 0.08)` (shimmer highlight) |
| `--card-body-pad` | `var(--surface-pad)` (the card's `--card-pad`) |
| `--card-overlay-bg` | `linear-gradient(transparent, rgba(0,0,0,.78) var(--space-l), rgba(0,0,0,.85))` |
| `--card-overlay-fg` | `#fff` |
| `--card-overlay-muted` | `rgba(255, 255, 255, 0.82)` |

Plus the card's own `--card-bg`, `--card-border`, `--card-radius`,
`--card-shadow`, `--card-pad`.

### Tier and touch

Cards are not containers (they shrink-wrap in flex rows). On phones a
`.grid` of cards becomes one column by itself. The shimmer runs only with
`prefers-reduced-motion: no-preference` and stops with
`html[data-motion="reduced"]`.

### Accessibility

Give every image real `alt` text, or `alt=""` when the title says it all.
`aria-busy` tells assistive tech the card is still loading. A
`.card-media` placeholder needs `role="img"` and a label.

---

## Draggable window `.modal[data-drag]`

```html
<input type="checkbox" class="window-max" id="w1max">
<div class="modal" data-drag role="dialog" aria-labelledby="w1title">
  <div class="modal-header" tabindex="0" aria-describedby="drag-hint">
    <span id="w1title">Uploads</span>
    <label for="w1max" class="btn-max" aria-label="Maximize"></label>
    <button class="btn-close" aria-label="Close"></button>
  </div>
  …
</div>
<p class="visually-hidden" id="drag-hint">Draggable. Alt plus arrow keys move the window; double-click maximizes.</p>
<script src="assets/js/window.js"></script>
```

`assets/js/window.js` is a small reference snippet (no dependencies, about
90 lines). Load it once; it handles every `[data-drag]` on the page,
including windows added later.

| Behaviour | How |
|---|---|
| Drag | Press on bare title-bar surface and move, with mouse, pen or finger (Pointer Events, pointer capture). Buttons, links, inputs and the min/max labels in the header stay clickable. The window is lifted out of the page flow (`position: fixed`, inline `left`/`top`/`width`) on the first move, not on press. |
| Touch | CSS puts `touch-action: none` on the header only, so a finger on the title bar drags the window and a finger on the body still scrolls it. |
| Stays on screen | Every move is clamped so the whole window stays inside the viewport. On window resize, dragged windows are pulled back in. |
| Maximize | Double-click or double-tap the header (window.js times the taps itself, as touch browsers don't reliably send `dblclick`). It flips the `.window-max` checkbox when one immediately precedes the modal, otherwise toggles `.is-maximized`. Maximized windows can't be dragged; double-click again restores them to where they were. |
| Keyboard | With the header focused (`tabindex="0"`), Alt+Arrow keys move the window 16px, Shift+Alt+Arrow 1px. The browser's Alt+Left/Right history shortcut is suppressed only while the header has focus. |
| Focus stacking | Core's `.modal:focus-within` raises the focused window to `--z-window`; clicking the header focuses it. |

### States (CSS)

| State | Look |
|---|---|
| `[data-drag] > .modal-header` | `cursor: grab`, `touch-action: none`, no text selection. |
| `.is-dragging` (set by window.js during a drag) | `--window-drag-shadow`, `cursor: grabbing` on the header. |
| `.is-maximized` / `.window-max:checked + .modal` | Overrides the inline position a drag left behind (`!important`, as the checkbox path has no script to clear it) and fills the viewport for a dragged window, or its container for one still in flow. The header loses the grab cursor. |
| Focused header | 2px `--focus` ring drawn inside the window edge. |

### Tokens

| Token | Default |
|---|---|
| `--window-drag-shadow` | `var(--modal-shadow, var(--panel-shadow, 0 .75rem 2rem rgba(0,0,0,.35)))` |
| `--window-focus-z` (core) | `1500` |

### Notes

- **Container ancestors.** `.modal`, `.drawer` and `.cq` are size containers,
  and a container is the containing block for `position: fixed`
  descendants. A window nested inside one is positioned relative to that box,
  not the viewport (and is clipped by its `overflow`). window.js measures the
  offset and corrects for it, so dragging still tracks the pointer, but for
  free movement across the whole screen put windows outside any container, or
  make them top-layer: `<div class="modal" popover data-drag>` or
  `<dialog class="modal" data-drag>` opened with `showModal()`. The demo page's
  "Open floating window" is that case.
- **Native `<dialog>`/popover** windows drag the same way; the checkbox-hack
  maximize doesn't compose with them (CONTRACT.md "Window pattern"), so use
  `.is-maximized`.
- Positions are inline styles, correctly unthemeable.

---

## Brand sign-in and connect buttons `.btn-brand`

```html
<button class="btn-brand is-google">
  <img class="btn-brand-logo" src="assets/logos/google/google-g.svg" alt="">
  Sign in with Google
</button>
```

These follow each company's **published** button or logo guidelines and are
deliberately **not re-themed**. Colours, height, radius, font, padding, gap
and logo size are literal values held in private `--_bb-*` properties on the
button itself, so no theme token reaches them, and the button doesn't carry
`.btn`, so no theme's `.btn` rules apply. They render identically in all 42
themes (checked: computed colours, font, sizes and logo placement match in
every theme). Only the focus ring (`--focus`) and the hit area (`--tap-min`)
follow the library. Hover, focus and press add a light tint of the text
colour over the brand fill (a Material-style state layer); disabled is 38%
opacity.

The logo is always an `<img class="btn-brand-logo" alt="">` the app puts in
the markup (the button text names the action, so the logo is decorative).
Logos are never part of a theme bundle (`assets/logos/README.md`).

| Class | Variants | Logo | Wording (guideline) | Spec applied |
|---|---|---|---|---|
| `.is-google` | default light, `.is-dark`, `.is-neutral`, `.is-pill`, `.is-icon` | **Shipped:** `assets/logos/google/google-g.svg` | "Sign in with Google", "Sign up with Google", "Continue with Google" (localise freely). Never "Google" alone. | 40px tall; padding 12px / logo / 10px / text / 12px; 20px G (fixed, never resized); Google Sans Medium 14/20 (falls back to Roboto, Arial); light `#FFFFFF` fill, `#747775` 1px stroke, `#1F1F1F` text; dark `#131314` / `#8E918F` / `#E3E3E3`; neutral `#F2F2F2`, no stroke, `#1F1F1F`; 4px or pill (20px) corners. Source: developers.google.com/identity/branding-guidelines |
| `.is-microsoft` | default light, `.is-dark`, `.is-icon` | **Shipped:** `assets/logos/microsoft/microsoft-logo.svg` | "Sign in with Microsoft", or "Sign in" when short of space. Pair with "work or school account" where relevant. | 41px; 12px padding and logo gap; 21px logo; Segoe UI 15px weight 600; square corners; light `#FFFFFF`, text `#5E5E5E`, 1px `#8C8C8C` border; dark `#2F2F2F`, text `#FFFFFF`. Source: learn.microsoft.com/en-us/entra/identity-platform/howto-add-branding-in-apps |
| `.is-apple` | default black, `.is-white` (on dark backgrounds), `.is-outline` (white with black outline, on light backgrounds), `.is-icon` | **App supplies** (see below) | "Sign in with Apple", "Sign up with Apple", "Continue with Apple". Keep the capitalisation. | 44px (Apple's recommended height); title 43% of the height in the system font; logo file as tall as the button with no added padding (the file carries its own); ≥ 2em after the title (Apple: ≥ 8% of the width); min 140 × 30px; logo and title both black or both white; 6px corners (any radius allowed). Leave ≥ 1/10 of the height clear around the button. Source: developer.apple.com/design/human-interface-guidelines/sign-in-with-apple |
| `.is-github` | default black, `.is-light` | **App supplies** | GitHub publishes no sign-in wording; "Sign in with GitHub" (one word, capital G and H). Don't imply endorsement. | The Invertocat only in black or white, high contrast, no effects. No GitHub button spec exists, so the box uses the Google/Microsoft proportions (40px, 12/10/12px, 20px mark). Source: brand.github.com/foundations/logo |
| `.is-spotify` | default `#121212`, `.is-light` | **App supplies** | Links to Spotify: OPEN SPOTIFY, PLAY ON SPOTIFY, LISTEN ON SPOTIFY, or GET SPOTIFY FREE when the app isn't installed (rendered uppercase by CSS; write it in sentence case for screen readers). No connect-button wording is published. | Green icon only on black or white; icon ≥ 21px (24px used); clear space half the icon height (12px gap and padding); platform sans-serif (Helvetica Neue, Helvetica, Arial). Spotify's terms forbid pairing its brand with other brands, so don't put it in a `.btn-brand-stack` with other providers. Source: developer.spotify.com/documentation/design |

Layout helpers:

- `.btn-brand.is-block`: full width, content centred.
- `.btn-brand.is-icon` (with `aria-label`): logo-only square button. Google,
  Apple and Microsoft allow logo-only buttons.
- `.btn-brand-stack`: a column of equal-width providers (up to 22rem). Google
  and Apple both require their button to be at least as prominent as other
  sign-in options.

### Supplying a logo this library doesn't ship

GitHub, Apple and Spotify don't give this shared library a right to
redistribute their marks (see `assets/logos/manifest.json`, the `pending`
entries), so the app fetches the official file itself and keeps it with its
own static assets (`assets/logos/README.md`, "Self-hosting a third-party
mark"):

1. **Apple:** download the Sign in with Apple "logo and text" artwork
   (SVG) from https://developer.apple.com/design/resources/: the white logo
   for the black button, the black logo for `.is-white`/`.is-outline`. For
   `.is-icon`, use the logo-only artwork. Don't crop the file or add padding:
   CSS makes it exactly as tall as the button.
2. **GitHub:** download https://brand.github.com/GitHub_Logos.zip and use
   the Invertocat mark SVG, white for the default button and black for
   `.is-light`.
3. **Spotify:** download the icon from
   https://developer.spotify.com/documentation/design ("Download Icon"), green
   on either button (green is allowed on black and on white).
4. Save it beside your app's own assets, e.g. `static/service-logos/apple-white.svg`,
   and reference it:
   ```html
   <button class="btn-brand is-apple">
     <img class="btn-brand-logo" src="/static/service-logos/apple-white.svg" alt="">
     Sign in with Apple
   </button>
   ```
   CSS sizes the image to the brand's logo size (`block-size`, width from the
   file's own ratio). Use an `<img>`, not inline SVG with `currentColor`:
   the marks must not be recoloured.

### Tier and touch

The visual height is the brand's own on every tier. On touch tiers an
`::after` grows the hit area to `--tap-min` (44px) vertically, and for
`.is-icon` horizontally too, without changing the look. In a row on a touch
tier keep at least 8px between buttons (core's `.cluster` gap does).

### Accessibility

The text label is the accessible name; the logo is `alt=""`. An `.is-icon`
button needs `aria-label="Sign in with Google"` (etc.). Every variant's text
clears 4.5:1 on its own fill (the lowest is Microsoft light, `#5E5E5E` on
white, 6.4:1). Use `<a class="btn-brand">` for a link (Spotify's "Open
Spotify"), `<button>` for an action. In forced-colors mode the button gets a
`ButtonText` border.
