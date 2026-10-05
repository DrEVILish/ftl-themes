# Experience layer (v5)

User display settings, forced colours, motion, accent swatches and seasons,
splash screens and themed empty/error states (PLAN.md §10–§14).

- CSS: `core/components/experience.css` (in every `dist/<slug>.css` bundle)
- Reference script: `assets/js/prefs.js` (optional; load it in `<head>` after the theme stylesheet)
- Theme switch transition: `assets/js/theme-loader.js`
- Examples: `components-experience.html`, `404.html`

---

## Display settings on `<html>`

All are optional. When one is unset, the OS preference applies, so an app
only stores the overrides.

| Attribute | Values | Effect | OS default |
|---|---|---|---|
| `data-text-size` | `s`, `l`, `xl` (unset = `m`) | Root font size ×0.875 / ×1.125 / ×1.25. Everything in rem follows. | Browser font size |
| `data-density` | `compact`, `comfortable` (unset = default) | Multiplies the theme's `--density` by 0.8 / 1.25. | – |
| `data-contrast` | `standard`, `high`, `more` | `high`: hairlines take the border colour, muted text takes the text colour, thicker focus ring. `more`: also every border in the text colour, links underlined, no text glow, no blur. `standard` opts out of the OS setting. | `prefers-contrast: more` → `high` |
| `data-motion` | `full`, `reduced`, `none` | `reduced` pauses animations (pseudo-elements and gutter art too) and zeroes transitions. `none` removes every animation and transition, including ambient theme motion and view transitions. `full` is the same as unset in CSS, but lets `theme-loader.js` play the theme-switch transition. | `prefers-reduced-motion: reduce` |
| `data-transparency` | `reduced`, `default` | `reduced` removes every `backdrop-filter` and `--overlay-blur`; translucent themes also make their fills opaque (see below). `default` opts out of the OS setting. | `prefers-reduced-transparency: reduce` |
| `data-pointer` | `touch` | 44px targets on any screen (core.css). | `any-pointer: coarse` |
| `data-underline-links` | present | Underlines running-text links. Links that are controls (`.btn`, `.nav-item`, `.tab`, menu items…) keep their shape. | – |
| `data-accent` | `1`–`6` | Picks the theme's swatch `n` (see Accent swatches). | – |
| `data-season` | any name | Theme-defined seasonal tint (see Seasons). | – |

These rules use `!important` on custom properties: a user's setting must
beat a theme's root block (`html[data-theme]`) and palette variants, which
load after core.

### For theme authors

- **Root font size.** If your theme sets a root size other than the browser
  default (`ios-flat`: 17px), declare it as `--root-font-size: 17px` so the
  text-size steps scale from it. Sizes in px don't scale; use rem.
- **Translucency.** Core removes the blur. Your translucent fills are your
  own tokens, so make them opaque in your theme, for both the attribute and
  the OS setting:
  ```css
  html[data-theme="x"][data-transparency="reduced"] { --x-glass: var(--surface); }
  @media (prefers-reduced-transparency: reduce) {
    html[data-theme="x"]:not([data-transparency="default"]) { --x-glass: var(--surface); }
  }
  ```
- **Ambient motion** (gutter art, glows, scanlines) stops under
  `data-motion="none"` automatically. Keep it inside
  `prefers-reduced-motion: no-preference` and off under `data-motion="reduced"`.

## Forced colours (Windows High Contrast)

Nothing to set: under `@media (forced-colors: active)` core

- keeps the focus ring (`Highlight`, 2px);
- outlines surfaces and controls that themes draw with shadows or fills
  (`.panel`, `.card`, `.modal`, `.drawer`, menus, `.toast`, `.segmented`,
  `.tabs`, `.btn`, `.tab`, `.nav-item`…), since the OS drops box-shadows
  and background images;
- paints selected items (`.is-active`, `aria-selected`, `aria-pressed`,
  `aria-current`, checked segmented radios) in `Highlight`/`HighlightText`;
- keeps value fills visible (`.meter-fill`, `.progress-bar`, `<progress>`,
  `<meter>`, switch thumbs, sliders) in system colours;
- uses `GrayText` for disabled buttons.

A theme that draws a component's only boundary with `box-shadow` gets an
outline in this mode; it doesn't need its own rules.

---

## `.prefs` — the settings panel

A plain form. Drop it in a page, a `.modal` or a `.drawer`. Each change
applies as it happens (the page itself is the preview).

```html
<form class="prefs">
  <fieldset class="prefs-item">
    <legend class="prefs-label">Text size</legend>
    <div class="segmented">
      <label class="segmented-item"><input type="radio" name="text-size" value="s"><span class="prefs-sample is-s" aria-hidden="true">A</span><span class="visually-hidden">Small</span></label>
      <label class="segmented-item"><input type="radio" name="text-size" value="" checked><span class="prefs-sample" aria-hidden="true">A</span><span class="visually-hidden">Default</span></label>
      <label class="segmented-item"><input type="radio" name="text-size" value="l"><span class="prefs-sample is-l" aria-hidden="true">A</span><span class="visually-hidden">Large</span></label>
      <label class="segmented-item"><input type="radio" name="text-size" value="xl"><span class="prefs-sample is-xl" aria-hidden="true">A</span><span class="visually-hidden">Extra large</span></label>
    </div>
  </fieldset>
  <fieldset class="prefs-item">
    <legend class="prefs-label">Motion<span class="prefs-hint">Off also stops background art.</span></legend>
    <div class="segmented">
      <label class="segmented-item"><input type="radio" name="motion" value="full" checked>Full</label>
      <label class="segmented-item"><input type="radio" name="motion" value="reduced" data-media="(prefers-reduced-motion: reduce)">Reduced</label>
      <label class="segmented-item"><input type="radio" name="motion" value="none">Off</label>
    </div>
  </fieldset>
  <label class="prefs-item">
    <span class="prefs-label">Reduce transparency<span class="prefs-hint">Glass and blur become solid.</span></span>
    <span class="switch"><input type="checkbox" name="transparency" value="reduced"
      data-media="(prefers-reduced-transparency: reduce)" data-off="default"><span class="switch-track"><span class="switch-thumb"></span></span></span>
  </label>
  <fieldset class="prefs-item">
    <legend class="prefs-label">Accent</legend>
    <div class="prefs-accents" data-prefs-accents>
      <label class="prefs-swatch is-default"><input type="radio" name="accent" value="" checked><span>Theme</span></label>
    </div>
  </fieldset>
  <div class="prefs-actions"><button class="btn" type="reset">Reset to system</button></div>
</form>
```

The full set (density, contrast, touch targets, underline links) is in
`components-experience.html`.

| Part | Role |
|---|---|
| `.prefs-item` | One setting: a `<fieldset>` (legend + segmented radios) or a `<label>` (text + switch). Label and control share a line when there is room and wrap otherwise. The whole label row is the switch's hit area. |
| `.prefs-label` / `.prefs-hint` | The setting's name and an optional one-line explanation. |
| `.prefs .segmented-item` | Radio-based segments: the label is the segment, the radio sits invisibly inside it (arrow keys move between options). |
| `.prefs-sample.is-s/.is-l/.is-xl` | The scaled "A" in the text-size options. |
| `.prefs-accents` / `.prefs-swatch` | The accent picker (see below). |
| `.prefs-actions` | Footer row; a `type="reset"` button clears every override. |

**prefs.js wiring.** The `name` of each control is the attribute name
without `data-`; the `value` is written on `<html>`, an empty value removes
it. `data-media="(query)"` checks that option when nothing is stored and the
OS already asks for it. `data-off="value"` on a switch writes that value
when the user unchecks it against the OS setting (transparency `default`).
Choices are stored as JSON in `localStorage["display-prefs"]`. An app that
stores settings server-side renders the same attributes on `<html>` and
skips the script.

**Tokens:** `--prefs-fg`, `--prefs-item-pad` (`var(--space-s) 0`),
`--prefs-divider` (`--hairline`), `--prefs-label-fg` (`--text`),
`--prefs-label-weight` (500), `--prefs-hint-fg` (`--muted`),
`--prefs-checked-weight` (600), `--prefs-swatch-size` (1.6rem),
`--prefs-swatch-radius` (50%), `--prefs-swatch-ring` (`--text`). Segments
read core's `--segmented-*` tokens.

**Touch and tiers:** rows are at least `--tap-min` tall; segments at least
`--tap-min` wide and tall; swatches have a `--tap-min` square hit area
around the smaller dot. Segmented groups wrap on narrow screens.

**Accessibility:** native fieldset/legend and radios, so each group is
announced with its name; the text-size letters carry visually hidden names;
focus shows on the segment or swatch; the checked segment is bold as well
as filled and the checked swatch has a ring and a check mark.

---

## Motion tokens and theme switching

| Token | Default | Use |
|---|---|---|
| `--motion-duration-s` | 120ms | Hover, press, small state changes |
| `--motion-duration-m` | 200ms | Surfaces opening |
| `--motion-duration-l` | 320ms | Theme switch, splash exit |
| `--motion-ease` | `cubic-bezier(0.2, 0, 0, 1)` | Default easing |
| `--motion-enter` | `motion-fade-in var(--motion-duration-m) var(--motion-ease) both` | `animation` shorthand for an element arriving |
| `--motion-exit` | `motion-fade-out var(--motion-duration-s) var(--motion-ease) both` | `animation` shorthand for an element leaving |

`--motion-enter`/`--motion-exit` are whole `animation` values, so a theme
can name its own keyframes and timing:

```css
html[data-theme="matrix"] { --motion-enter: matrix-decode 300ms steps(8) both; }
html[data-theme="windows95"] { --motion-duration-m: 0ms; --motion-ease: linear; }
```

Rules: animations only inside `@media (prefers-reduced-motion: no-preference)`
and off under `data-motion="reduced"` or `"none"`; routine UI under 400ms;
nothing blocks input.

**Theme switching.** `theme-loader.js` swaps the stylesheet inside
`document.startViewTransition`, waiting for the new sheet to load, so the
change cross-fades over `--motion-duration-l`. It is instant without the
API, under the OS reduced-motion setting (unless `data-motion="full"`), or
under `data-motion="reduced"`/`"none"`. A theme supplies its own entrance:

```css
html[data-theme="silo"]::view-transition-new(root) { animation: silo-crt-on 400ms steps(6) both; }
```

After each theme loads, `theme-loader.js` fires a `themechange` event on
`document` (prefs.js uses it to rebuild the accent swatches).

---

## Accent swatches (§12)

A theme declares the accents a user may pick, as numbered pairs, each one
contrast-checked by the author. An optional name labels it for screen
readers:

```css
html[data-theme="imac-g3"] {
  --accent-swatch-1: #00b0d4; --on-accent-swatch-1: #04262c; --accent-swatch-1-name: "Bondi";
  --accent-swatch-2: #3a5fcf; --on-accent-swatch-2: #ffffff; --accent-swatch-2-name: "Blueberry";
}
```

- `data-accent="<n>"` on `<html>` sets `--accent` and `--on-accent` from the
  pair. Always declare both halves, and only set a number the theme
  declares: an undeclared swatch leaves `--accent` invalid. prefs.js only
  offers and applies declared swatches, and drops the choice for a theme
  without that swatch (keeping it for when the user switches back).
- **No choice:** a theme that declares no swatches (`teletext`, whose eight
  broadcast colours are the identity) gets no accent row.
- **Derived colours follow** when the theme writes them from `--accent`
  rather than as hex, e.g.
  `--btn-bg-hover: color-mix(in oklab, var(--accent) 85%, black)`. Core's
  own `--focus` already derives from `--accent`.

The picker markup is a `.prefs-accents` box with `data-prefs-accents`;
prefs.js adds one `<label class="prefs-swatch">` per declared swatch, each
with `style="--swatch: var(--accent-swatch-n); --on-swatch: var(--on-accent-swatch-n)"`.
Without the script, write those labels by hand.

## Seasons (§12)

`data-season="winter|spring|summer|autumn|halloween|festive"` (or any name)
on `<html>`, switched on by the app (for example by date). Off by default.
Core ships no palettes; a theme opts in per season, tinting only its
accent and gutter art, never base surfaces:

```css
html[data-theme="blue-future"][data-season="winter"]:not([data-accent]) {
  --accent: #9fe4ff; --on-accent: #001018;
}
html[data-theme="blue-future"][data-season="winter"] {
  --app-gutter-art: radial-gradient(…snow…), var(--blue-future-gutter);
}
```

The `:not([data-accent])` keeps the user's own accent choice ahead of the
season. A theme without that season simply ignores the attribute.

---

## `.splash` — boot and loading screen (§13)

```html
<!-- Render before the app content; load boot.js after this markup -->
<div class="splash" data-boot-screen role="status" aria-live="polite">
  <div class="splash-art" aria-hidden="true"></div>
  <p class="splash-title">Northwind Analytics</p>
  <progress class="progress" aria-label="Loading"></progress>
  <p class="splash-message">Starting…</p>
</div>
<main class="app-main">…app or login screen…</main>
<script src="assets/js/boot.js"></script>
<script>/* Call after the app or login screen is usable: */ window.ftlAppReady();</script>

<!-- Optional legacy theme intro; loading overlays should use data-boot-screen -->
<div class="splash" data-intro="2s" role="status" aria-live="polite">
  …
  <p class="splash-skip">Press any key to skip</p>
</div>
```

| Part / state | |
|---|---|
| `.splash` | Fixed over the whole viewport, above windows. |
| `.splash.is-contained` | Covers its nearest positioned ancestor instead (a panel loading, a demo box). |
| `.splash-art` | The theme's mark. Default: an accent ring with a gap, which turns when motion is allowed. |
| `.splash-title`, `.splash-message`, `.splash-skip` | Text lines. Update `.splash-message` as loading progresses; `aria-live` announces it. |
| `<progress>` | With `value`: determinate. Without: an indeterminate sweep (a static centred segment without motion). |
| `[hidden]` | Fades out over `--motion-duration-l` where motion is allowed. |
| `[data-boot-screen]` | Visible immediately. `boot.js` holds it until the app calls `window.ftlAppReady()`, then clears `aria-busy` and hides the cover. No timeout or skip can reveal an app that is not ready. |
| `[data-intro="2s"]` | Optional timed theme intro (`s` or `ms`). Children enter with `--motion-enter`, staggered. Skippable; remembered in `sessionStorage`; `window.playSplash(el)` replays one. Under reduced motion it is a static frame. |

The boot animation is CSS-only and stops under reduced motion. If your page
can render without the app's script, hide the splash for no-JS visitors:
`<noscript><style>.splash { display: none }</style></noscript>`.

## Foldable PWAs

In standalone display mode only, `core/layout.css` uses the viewport-segment
media features to reserve the hinge gap and keep shell regions within their
segments. `assets/js/foldable.js` is optional and exposes `data-fold-mode`
(`book` or `tabletop`) plus `data-fold-posture` for app decisions. Segment
support is progressive enhancement; unsupported browsers and windowed apps
use the ordinary responsive tiers. Load the detector only where the app
needs the metadata.

**Tokens:** `--splash-bg` (`--surface`), `--splash-fg` (`--text`),
`--splash-font`, `--splash-gap` (`--space-m`), `--splash-art` (background
layers), `--splash-art-size` (5rem), `--splash-art-radius` (50%),
`--splash-art-mask` (a ring; set `none` for full-bleed art),
`--splash-art-motion` (an `animation` value), `--splash-title-fg`,
`--splash-title-size` (1.5rem), `--splash-title-weight` (600),
`--splash-title-tracking` (0.02em), `--splash-title-transform`,
`--splash-message-fg` (`--muted`), `--splash-message-font`,
`--splash-progress-width` (16rem). The progress bar reads core's
`--progress-*` tokens.

---

## Themed states (§14)

Modifiers on core's `.empty-state`. An `<svg class="icon empty-state-icon">`
becomes the illustration: the icon on a disc tinted with the state's colour,
or the theme's own art.

```html
<div class="empty-state is-offline" role="status">
  <svg class="icon empty-state-icon" aria-hidden="true"><use href="assets/icons/icons.svg#icon-cloud-off"/></svg>
  <h2 class="empty-state-title">You’re offline</h2>
  <p class="empty-state-hint">Changes are saved here and sync when you reconnect.</p>
  <div class="cluster"><button class="btn">Retry</button></div>
</div>
```

| State | Modifier | Suggested icon | Tone | Suggested heading |
|---|---|---|---|---|
| Empty | – | `icon-folder` | `--muted` | – |
| Error | `.is-error` (use `role="alert"`) | `icon-warning` | `--danger` | Something went wrong |
| Offline | `.is-offline` | `icon-cloud-off` | `--warning` | You’re offline |
| Not found | `.is-404` | `icon-map-question` | `--accent` | Page not found |
| No permission | `.is-locked` | `icon-lock` | `--text` | You don’t have access |
| Loading | `.is-loading` (add `aria-busy="true"`) | `icon-hourglass` | `--accent` | Loading… |

- **Suggested heading:** leave `.empty-state-title` empty and the theme's
  heading shows (`content:`); the app's own text always wins. Real apps
  should write their own copy.
- **Loading** turns the icon (an hourglass flip) when motion is allowed.
- `404.html` is the full-page example and the GitHub Pages 404. It adds a
  `<base>` on `*.github.io` so its relative links work at any depth.

**Tokens:** `--empty-state-icon-size` (2.5rem), `--empty-state-art-pad`
(`--space-m`), `--empty-state-art-radius` (50%), `--empty-state-art` (the
disc behind every state's icon: any background layers), per state
`--empty-state-<state>-art`, `--empty-state-<state>-fg` (the tone) and
`--empty-state-<state>-title` (a quoted string), with `<state>` one of
`error`, `offline`, `404`, `locked`, `loading`; `--empty-state-loading-motion` (an `animation` value).

```css
/* windows95: the 95 error icon and IE4's wording */
html[data-theme="windows95"] {
  --empty-state-error-art: url("data:image/svg+xml,…red circle with X…") center / 70% no-repeat;
  --empty-state-404-title: "The page cannot be found";
}
```

A theme can also replace the icon shapes everywhere through its
`themes/<slug>/icons.svg` overrides (CONTRACT.md "Icon system").

**Accessibility:** the icon is decorative (`aria-hidden`), the title and
hint carry the meaning; state is shown by icon, tone and heading together,
never colour alone. Use `role="status"` (or `role="alert"` for errors that
appear after an action).
