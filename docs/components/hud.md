# Game HUD kit (v5)

Source: `core/components/hud.css`. Live examples: `hud.html`. Covers PLAN.md
§19 "Game HUD": the overlay layer, resource bars, minimap, quest tracker,
hotbar and inventory slots, floating numbers, achievement toast and key
prompts. Builds on core's `.toast`/`.toast-region`, `<kbd>`, `.progress`,
`.drawer` and the radio selection mechanism, and on instruments.css's
`.map`, `.map-pin`, `.map-north`, `.map-attribution` and `.compass-strip`.

Tokens are listed as `token: default`. A theme sets them on
`html[data-theme="x"]` like every other component token. Inline styles are
only for the value APIs named in each section (`--value`, `--trail`,
`--segments`, `--cooldown`, `--x`/`--y`, `--heading`, `--hud-float-*`,
`--hud-min-height`).

Every motion below runs only with `prefers-reduced-motion: no-preference`
and stops under `<html data-motion="reduced">` or `"none"`. Each state that
moves also has a still signal (a glyph, a border, text), so nothing depends
on motion or colour alone.

---

## HUD overlay `.hud`

```html
<div class="hud" role="region" aria-label="Game HUD">
  <svg class="hud-scene" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">…</svg>
  <div class="hud-top"><ol class="compass-strip" style="--heading:300">…</ol></div>
  <div class="hud-top-start"><div class="hud-bars">…</div></div>
  <div class="hud-top-end"><figure class="map hud-minimap is-round">…</figure><section class="hud-quests">…</section></div>
  <div class="hud-bottom"><div class="hud-hotbar">…</div></div>
  <div class="hud-bottom-start"><p class="hud-prompt"><kbd>E</kbd> Open</p></div>
  <div class="hud-bottom-end"><div class="toast hud-achievement" role="status">…</div></div>
  <span class="hud-float" style="--x:48%; --y:52%" aria-hidden="true">−48</span>
</div>
```

- **Scene:** `.hud-scene` is any `<img>`, `<svg>`, `<video>` or `<canvas>`. It
  fills the layer behind everything (`object-fit: cover`). Without one the
  layer shows `--hud-scene-bg`.
- **Regions:** each is a flex column that holds any HUD component. Use the
  ones you need. DOM order is free, so write them in reading order.
- **The centre stays clear.** The middle row (at least `--hud-center-min`)
  never holds a region. Only `.hud-float` crosses it.
- **Full screen:** `.hud.is-fullscreen` is fixed to the viewport, drops the
  frame, and pads by `env(safe-area-inset-*)` so it clears notches and the
  home indicator.

### Tiers (container queries on the `.hud` box)

| HUD width | Layout |
|---|---|
| > 900px | Four corners plus top centre and bottom centre. Corner regions grow towards the middle row. |
| 481–900px | Stacked edges. Top: the compass row, then top-start and top-end side by side. Bottom: the hotbar row, then bottom-start and bottom-end side by side. |
| ≤ 480px | As above, but bottom-start and bottom-end stack. The minimap shrinks to 7.5rem. |

The HUD is a container (`container: hud / inline-size`), so a HUD in a side
panel lays out for its own width. It is also a stacking context
(`isolation: isolate`). Popovers opened from it (map pins, the inventory
drawer) use the top layer and are not clipped.

### Tokens

| Token | Default |
|---|---|
| `--hud-min-height` | `34rem` (also an inline value API) |
| `--hud-center-min` | `8rem` |
| `--hud-pad` | `var(--space-m)` |
| `--hud-gap` | `var(--space-s)` |
| `--hud-scene-bg` | `linear-gradient(var(--surface-2), var(--bg))` |
| `--hud-scene-filter` | `none` (e.g. `saturate(.6)` for a muted world) |
| `--hud-fg` | `var(--text)` |
| `--hud-border`, `--hud-border-width`, `--hud-radius` | `var(--border)`, `1px`, `var(--radius)` |
| `--hud-font`, `--hud-font-size` | `inherit`, `0.875rem` |
| `--hud-compass-width` | `22rem` (a `.compass-strip` in `.hud-top`) |
| `--hud-panel-bg` | `color-mix(in srgb, var(--surface) 82%, transparent)`: the backing of bars, quests and prompts |
| `--hud-panel-border`, `--hud-panel-border-width` | `color-mix(in srgb, var(--border) 60%, transparent)`, `1px` |
| `--hud-panel-radius`, `--hud-panel-pad` | `var(--radius)`, `var(--space-xs) var(--space-s)` |
| `--hud-panel-shadow`, `--hud-panel-blur` | `none`, `none` (`blur(12px)` for glass themes) |

### Accessibility

Give the layer `role="region"` and a name. Text sits on `--hud-panel-bg`,
not on the scene, so its contrast is the theme's own text-on-surface
contrast. A theme whose `--surface` is translucent should set an opaque
enough `--hud-panel-bg`. The regions are not focus traps: everything
interactive stays in the tab order.

---

## Resource bars `.hud-bar`

```html
<div class="hud-bar hud-bar-health" role="meter" aria-label="Health"
     aria-valuemin="0" aria-valuemax="250" aria-valuenow="168" aria-valuetext="168 of 250"
     style="--value:.672">
  <span class="hud-bar-label">Health</span>
  <span class="hud-bar-value">168 / 250</span>
</div>

<!-- a stack of bars on the HUD backing -->
<div class="hud-bars">…bars…</div>
```

- **Value:** `--value` (0–1) is the fill. Keep `aria-valuenow` in step, and
  set `aria-valuetext` too: `role="meter"` makes the children presentational,
  so the printed "168 / 250" is not read out.
- **Kinds:** `.hud-bar-health`, `.hud-bar-mana`, `.hud-bar-stamina`. Without a
  kind the bar uses `--hud-bar-fill` (the accent): experience, shields, breath.
- **Children are optional.** A bare `<div class="hud-bar" role="meter" …>`
  is just the track (Skyrim style). An `<svg class="icon">` as the first
  child sits beside the label and track, in the fill colour.
- **Damage trail:** `--trail` (0–1) is the value before the hit; the part
  between `--value` and `--trail` shows in `--hud-bar-trail`. With motion on
  you don't need `--trail`: the trail follows `--value` by itself, after
  `--hud-bar-trail-delay`, so the app only ever sets `--value`.

### States and variants

| Markup | Result |
|---|---|
| `style="--trail:.8"` | A trailing segment from `--value` up to `--trail`. |
| `.is-low` | The app adds it under its own threshold. Rule and text turn `--hud-bar-low`, and the value gets a `!`. With motion the bar pulses. |
| `.is-regen` | A `▲` after the value. With motion a light runs along the fill. |
| `.is-segmented` + `style="--segments:10"` | The bar is cut into pips (`--hud-bar-gap` apart). Use a whole-pip `--value` (7 of 10 = `.7`). |
| `.is-centered` | Fills and drains from the centre (Skyrim's attribute bars). |
| `.is-reversed` | Fills from the end (a right-hand bar in a mirrored HUD). |

### Tokens

| Token | Default |
|---|---|
| `--hud-health` | `var(--danger)` |
| `--hud-mana` | `var(--accent-2)` |
| `--hud-stamina` | `var(--success)` |
| `--hud-bar-fill` | `var(--accent)` (kind-less bars) |
| `--hud-bar-trail` | `color-mix(in oklab, <fill> 35%, var(--text))` |
| `--hud-bar-track` | `var(--meter-track, var(--surface-2))` (a colour or an image) |
| `--hud-bar-border`, `--hud-bar-border-width` | `var(--meter-border, var(--border))`, `1px` |
| `--hud-bar-radius` | `var(--radius)` |
| `--hud-bar-height`, `--hud-bar-width` | `0.625rem`, `16rem` |
| `--hud-bar-sheen` | `linear-gradient(rgba(255,255,255,.22), transparent 70%)` over the fill (`none` for flat) |
| `--hud-bar-shadow` | `none` |
| `--hud-bar-clip` | `none` (a `clip-path`, e.g. diamond end caps) |
| `--hud-bar-anchor` | `0` (start), `.5` centre, `1` end |
| `--hud-bar-gap` | `3px` (segment gap) |
| `--hud-bar-low`, `--hud-bar-low-fg` | `var(--danger)`, `var(--danger-text, var(--danger))` |
| `--hud-bar-regen-fg`, `--hud-bar-regen-glow` | `var(--success-text, var(--success))`, `rgba(255,255,255,.55)` |
| `--hud-bar-speed` | `0.15s` (fill) |
| `--hud-bar-trail-speed`, `--hud-bar-trail-delay` | `0.6s`, `0.5s` |
| `--hud-bar-fg`, `--hud-bar-font-size` | `var(--text)`, `0.75rem` |
| `--hud-bar-label-transform`, `--hud-bar-label-spacing` | `none`, `normal` |

The automatic trail uses two registered properties (`--hud-bar-v`,
`--hud-bar-t`). Don't set them; set `--value`/`--trail`.

---

## Minimap `.map.hud-minimap`

```html
<figure class="map hud-minimap is-round" aria-label="Minimap: Whiterun Hold, heading north-west">
  <svg viewBox="0 0 200 200" preserveAspectRatio="xMidYMid slice" aria-hidden="true">…</svg>
  <span class="hud-minimap-player" style="--heading:300"></span>
  <button class="map-pin" style="--x:68%; --y:32%" data-series="2" popovertarget="pin-quest" aria-label="Quest: Bleak Falls Barrow"></button>
  <span class="map-north" role="img" aria-label="North">N</span>
  <figcaption class="map-attribution">Whiterun Hold</figcaption>
</figure>
<div class="popover" popover id="pin-quest">…</div>
```

Core's `.map` frame (see [instruments.md](instruments.md)) made square:
pins, north arrow, legend, controls and attribution all work as there.

- `.is-round` makes it a circle, with the north arrow and the caption centred
  (the corners are cut off).
- `.hud-minimap-player` is the player arrow, at the centre or at `--x`/`--y`,
  turned by `--heading` (degrees, clockwise from north). It is decoration:
  name the place and heading on the figure.
- The heading strip is core's `.compass-strip` with `--heading`; in
  `.hud-top` it is `--hud-compass-width` wide, full width on narrow HUDs.
- Pins keep core's `--tap-min` hit area, so a small minimap stays tappable.

| Token | Default |
|---|---|
| `--hud-minimap-size` | `11rem` (`7.5rem` in a HUD ≤ 480px) |
| `--hud-minimap-border-width` | `2px` |
| `--hud-minimap-shadow` | `inset 0 0 1.5rem rgba(0,0,0,.45)` (vignette) |
| `--hud-minimap-player`, `--hud-minimap-player-size` | `var(--accent)`, `1.1rem` |

Plus every `.map-*` token (`--map-bg`, `--map-border`, `--map-pin-bg`, …).

---

## Quest tracker `.hud-quests`

```html
<section class="hud-quests" aria-label="Quest tracker">
  <h3>The Golden Claw</h3>
  <ol class="hud-objectives">
    <li class="is-done">Speak to Lucan Valerius</li>
    <li aria-current="step">Retrieve the golden claw <span class="hud-count">0/1</span></li>
    <li class="is-failed">Keep Camilla out of danger</li>
    <li>Collect wolf pelts <span class="hud-count">3/5</span></li>
  </ol>
</section>
```

Several quests: repeat the heading and list in one `.hud-quests`.

| State | Markup | Mark | Look |
|---|---|---|---|
| Pending | `<li>` | ○ | Normal text |
| Current | `<li aria-current="step">` | ◆ in the accent | Bold |
| Done | `<li class="is-done">` | ✓, read as "Done:" | Muted, struck through |
| Failed | `<li class="is-failed">` | ✗, read as "Failed:" | Danger colour, struck through |

`.hud-count` ("3/5") sits at the end of the line. Write each objective as
plain text (or one `<span>`) plus the count: the item is a three-column
grid, so several inline elements would each take a cell.

| Token | Default |
|---|---|
| `--hud-quests-width` | `17rem` |
| `--hud-quests-title-fg`, `--hud-quests-title-transform`, `--hud-quests-title-spacing` | `var(--text)`, `none`, `normal` |
| `--hud-objective-fg` | `var(--text)` |
| `--hud-objective-glyph`, `--hud-objective-current-glyph` | `"\25CB"` ○, `"\25C6"` ◆ |
| `--hud-objective-done-glyph`, `--hud-objective-failed-glyph` | `"\2713"` ✓, `"\2717"` ✗ |
| `--hud-objective-done-label`, `--hud-objective-failed-label` | `"Done:"`, `"Failed:"` (screen-reader text; localise here) |
| `--hud-objective-current` | `var(--accent)` |
| `--hud-objective-done`, `--hud-objective-done-fg` | `var(--success-text, var(--success))`, `var(--muted)` |
| `--hud-objective-failed-fg` | `var(--danger-text, var(--danger))` |
| `--hud-count-fg` | `var(--muted)` |

---

## Hotbar and inventory slots `.hud-slot`

```html
<div class="hud-hotbar" role="radiogroup" aria-label="Hotbar">
  <label class="hud-slot" data-rarity="rare" style="--cooldown:.4">
    <input type="radio" name="hotbar" aria-label="2: Frost bolt, rare, ready in 4 seconds" checked>
    <svg class="icon" aria-hidden="true"><use href="assets/icons/icons.svg#icon-snowflake"/></svg>
    <kbd class="hud-slot-key">2</kbd>
    <span class="hud-slot-timer">4s</span>
  </label>
  <label class="hud-slot" data-rarity="uncommon">
    <input type="radio" name="hotbar" aria-label="3: Healing potion, uncommon, 12 left">
    <svg class="icon" aria-hidden="true">…</svg>
    <kbd class="hud-slot-key">3</kbd><span class="hud-slot-count">12</span>
  </label>
  <label class="hud-slot is-empty"><input type="radio" name="hotbar" aria-label="7: empty"><kbd class="hud-slot-key">7</kbd></label>
</div>

<div class="hud-inventory" role="radiogroup" aria-label="Inventory">…slots…</div>
```

- **Selection** is a hidden radio in the slot (no JS). `.is-active` and
  `aria-selected="true"` style the same way, for apps that keep state.
  Use checkboxes for multi-select. Arrow keys move through a radio group.
- **Name** each slot on its input with `aria-label` (slot, item, rarity,
  count, cooldown); the visible parts are short codes.
- **`.hud-hotbar`** is a centred row that wraps. **`.hud-inventory`** is a
  grid of as many slot columns as fit.

### States

| Markup | Result |
|---|---|
| `data-rarity="common…legendary"` | Border and inner glow in the rarity colour, plus 1–5 pips in the top corner (the non-colour signal). `[data-rarity]` works on any element: it sets `--rarity` and `--rarity-rank`. |
| `style="--cooldown:.4"` | The part still to wait (0–1) is shaded, sweeping clockwise from 12 o'clock. Add `.hud-slot-timer` text ("4s") so the wait isn't only a picture. |
| checked radio / `.is-active` | Accent border plus an outer ring; the key cap fills with the accent. |
| `.is-empty` | Dashed border, fainter background. |
| disabled input / `aria-disabled="true"` | Dimmed. |
| `:focus-visible` on the radio | Core focus colour, ringed outside the slot. |

### Tokens

| Token | Default |
|---|---|
| `--rarity-common` | `var(--muted)` |
| `--rarity-uncommon` | `#3fae2a` |
| `--rarity-rare` | `#2f80e8` |
| `--rarity-epic` | `#a64ff0` |
| `--rarity-legendary` | `#f08a12` |
| `--hud-slot-size` | `3rem` (never below `--tap-min`) |
| `--hud-slot-gap` | `var(--space-2xs)` |
| `--hud-slot-bg`, `--hud-slot-bg-hover`, `--hud-slot-empty-bg` | `color-mix(var(--surface) 85%, transparent)`, `color-mix(var(--surface-2) 92%, transparent)`, `color-mix(var(--surface) 50%, transparent)` |
| `--hud-slot-fg` | `var(--text)` |
| `--hud-slot-border`, `--hud-slot-border-width` | `var(--border)` (no rarity), `2px` |
| `--hud-slot-radius` | `var(--radius)` |
| `--hud-slot-glow` | `0.9rem` (inner rarity glow) |
| `--hud-slot-cooldown` | `rgba(0,0,0,.62)` |
| `--hud-slot-selected`, `--hud-slot-selected-fg`, `--hud-slot-selected-width` | `var(--accent)`, `var(--on-accent)`, `2px` |

The rarity defaults are the genre's grey, green, blue, purple and orange,
because players read them that way. Themes with a narrow palette remap them.

### Tier and touch

Slots are at least `--tap-min` square (44px on touch tiers). The hotbar
wraps instead of overflowing on a phone. Hover only lightens the background
on devices that can hover.

---

## Floating numbers `.hud-float`

```html
<span class="hud-float" style="--x:48%; --y:40%" aria-hidden="true">−48</span>
<span class="hud-float is-crit" style="--x:55%; --y:36%" aria-hidden="true">−212!</span>
<span class="hud-float is-heal" style="--x:20%; --y:46%" aria-hidden="true">+30</span>
```

```js
const f = Object.assign(document.createElement('span'), { className: 'hud-float', textContent: '−48' });
f.setAttribute('aria-hidden', 'true');
f.style.cssText = `--x:${x}%; --y:${y}%`;
f.addEventListener('animationend', () => f.remove());
setTimeout(() => f.remove(), 1500); // motion off: nothing animates
hud.append(f);
```

- Placed at `--x`/`--y` (centred on the point) in the nearest positioned
  box: `.hud` is one.
- With motion it pops, rises `--hud-float-rise` and fades once over
  `--hud-float-duration`. With motion off it stays still, so the app
  removes it on a timer.
- Variants: `.is-heal`, `.is-crit` (bigger, warning colour), `.is-mana`,
  `.is-miss` (small, muted, italic). Write the sign in the text ("+30",
  "−48", "!"): colour is not the only signal.
- They are a visual echo: keep `aria-hidden="true"` and report damage that
  matters through a live region (or the bar's `aria-valuetext`).

| Token / inline API | Default |
|---|---|
| `--hud-float-damage`, `--hud-float-heal`, `--hud-float-crit`, `--hud-float-mana`, `--hud-float-miss` | `var(--danger)`, `var(--success)`, `var(--warning)`, `var(--hud-mana)`, `var(--muted)` |
| `--hud-float-size`, `--hud-float-crit-size` | `1.5rem`, `2.25rem` |
| `--hud-float-stroke`, `--hud-float-stroke-width` | `rgba(0,0,0,.8)`, `3px` (outline, so numbers read over any scene) |
| `--hud-float-shadow` | `0 2px 6px rgba(0,0,0,.5)` |
| `--hud-float-rise` | `3rem` |
| `--hud-float-duration`, `--hud-float-delay`, `--hud-float-repeat` | `1.2s`, `0s`, `1` (inline APIs; `infinite` is for demos) |

---

## Achievement toast `.toast.hud-achievement`

```html
<div class="toast-region" popover="manual" id="ach">
  <div class="toast hud-achievement" role="status">
    <svg class="icon hud-achievement-icon" aria-hidden="true"><use href="assets/icons/icons.svg#icon-star"/></svg>
    <div class="hud-achievement-body">
      <span class="hud-achievement-kicker">Achievement unlocked</span>
      <strong class="hud-achievement-title">Dragonslayer</strong>
      <span class="hud-achievement-text">Defeat Alduin at the Throat of the World</span>
      <progress class="progress" value="72" max="100">72 of 100</progress>  <!-- optional -->
    </div>
    <span class="hud-achievement-score">50G</span>                         <!-- optional -->
    <button class="btn-close" popovertarget="ach" popovertargetaction="hide" aria-label="Dismiss"></button>
  </div>
</div>
```

A core `.toast`, so the theme's toast look applies. In a
`.toast-region popover="manual"` it shows in the top layer, over the game
and over an open modal (`ach.showPopover()`; hide it after a few seconds).
It can also sit in a HUD region. With motion it slides in each time it is
shown. Extra trailing children (score, close) take their own columns.

| Token | Default |
|---|---|
| `--hud-achievement-width` | `22rem` |
| `--hud-achievement-border` | `var(--toast-border, var(--border))` |
| `--hud-achievement-icon-size` | `2.75rem` |
| `--hud-achievement-icon-bg`, `--hud-achievement-icon-fg` | `var(--accent)`, `var(--on-accent)` |
| `--hud-achievement-icon-radius` | `50%` |
| `--hud-achievement-kicker-transform` | `uppercase` |

Plus the toast's `--toast-bg`, `--toast-fg`, `--toast-border`,
`--toast-radius`, `--toast-shadow`, `--toast-pad`, and the progress bar's
`--progress-*`.

---

## Key prompts `.hud-prompt`

```html
<p class="hud-prompt"><kbd>E</kbd> Open</p>
<p class="hud-prompt"><kbd>Shift</kbd> + <kbd>E</kbd> Steal</p>
<p class="hud-prompt"><kbd class="hud-pad" data-button="south">A</kbd> Open</p>
<p class="hud-prompt"><kbd class="hud-pad">LB</kbd><kbd class="hud-pad">RB</kbd> Switch tab</p>
<button class="hud-prompt" popovertarget="inventory"><kbd>I</kbd> Inventory</button>
```

- Keys are core `<kbd>` (the theme's `--kbd-*` look).
- `kbd.hud-pad` is a gamepad button: round for one character, a pill for
  "LB"/"RT". `data-button="south|east|west|north"` rings it in that face
  button's colour (layout-neutral names: south is Xbox A / PlayStation ✕).
  The letter or symbol inside is the real signal.
- A prompt the player can tap is a `<button class="hud-prompt">`: it grows to
  `--tap-min` on touch and gets core's focus ring. The bare `<p>` form is a
  hint only.

| Token | Default |
|---|---|
| `--hud-prompt-bg`, `--hud-prompt-bg-hover` | `var(--hud-panel-bg)`, `var(--surface-2)` |
| `--hud-prompt-fg`, `--hud-prompt-font-size`, `--hud-prompt-pad` | `var(--text)`, `0.85rem`, `var(--space-2xs) var(--space-xs)` |
| `--hud-pad-bg`, `--hud-pad-fg`, `--hud-pad-font` | `var(--kbd-bg)`, `var(--kbd-fg)`, `var(--font)` |
| `--hud-pad-south` | `var(--success)` |
| `--hud-pad-east` | `var(--danger)` |
| `--hud-pad-west` | `var(--accent-2)` |
| `--hud-pad-north` | `var(--warning)` |

---

## Per-theme suggestions

| Theme | Tokens |
|---|---|
| `skyrim` | `--hud-bar-anchor: .5` (bars drain to the centre), `--hud-bar-clip: polygon(0.45rem 0, calc(100% - 0.45rem) 0, 100% 50%, calc(100% - 0.45rem) 100%, 0.45rem 100%, 0 50%)` (diamond caps, as its `.progress`), `--hud-bar-height: .7rem`, `--hud-bar-sheen: linear-gradient(rgba(255,255,255,.28), transparent 45%, rgba(0,0,0,.35))`, `--hud-panel-bg: var(--sky-smoke), transparent`, `--hud-panel-border: var(--sky-line)`, `--hud-slot-radius: 0`, `--hud-objective-current-glyph: "\25C6"`, `--hud-quests-title-transform: uppercase`. |
| `pipboy` | One green on purpose: `--rarity-common..legendary` as five greens of rising brightness (the pips carry the rank), `--hud-slot-cooldown: rgba(4,20,10,.7)`, `--hud-pad-south..north: var(--accent)`, `--hud-float-stroke: #04140a`, `--hud-bar-sheen: none`, `--hud-bar-track: repeating-linear-gradient(90deg, #0a2e15 0 6px, #04140a 6px 8px)` (ticked track). |
| `xmb` | `--hud-panel-bg: rgba(8,18,40,.7)`, `--hud-panel-blur: blur(12px)`, `--hud-slot-radius: 50%` (round XMB icons), `--hud-pad-south: #7cb2e8` (✕), `--hud-pad-east: #ff6b6b` (○), `--hud-pad-west: #f29ad8` (□), `--hud-pad-north: #6bffb0` (△), `--hud-bar-radius: 999px`. |
| `cassette-futurism` | `.is-segmented` reads as LED ladders: `--hud-bar-gap: 2px`, `--hud-bar-track: #2a241c` (recessed window), `--hud-bar-sheen: none`; keycap-coloured gamepad rings `--hud-pad-south: var(--cf-orange)` etc.; `--hud-scene-filter: sepia(.3)`; `--hud-font: var(--font-mono)` for the VFD look. |
| `lcars` | Its `--meter-track` tick graphics already flow into the bars; `--hud-bar-radius: 999px`, `--hud-slot-radius: 999px 0 0 999px` for elbow-ish slots. |
| `blue-future`, `cyberpunk-2077` | `--hud-bar-shadow: 0 0 .5rem var(--accent)`, `--hud-slot-glow: 1.2rem`. |
