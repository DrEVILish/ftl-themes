# Instruments and data display (v5)

Source: `core/components/instruments.css`. Example page: `components-instruments.html`.
Covers PLAN.md §9 #1–16 and the library-neutral chart contract from §18.

Shared conventions:

- Values come in through native elements (`<meter>`, `<ol>`, `<dl>`) or one documented
  inline custom property (`--value`, `--heading`, `--x`/`--y`, `--seg-n`, `--v`, `--at`).
  Nothing here needs JavaScript; apps update attributes or properties.
- Every colour and size is a `--<component>-*` token with a fallback to the base tokens.
  Themes set them at root scope (`html[data-theme="x"] { --gauge-needle: … }`).
- `data-series="1".."6"` on any element sets `--series` (and `--series-dash`) from
  `--chart-series-n` / `--chart-dash-n`. Legends, chart series, map pins and compass
  markers all read it, so one legend matches all of them.
- Motion (the needle sweep, the indeterminate ring) runs only under
  `prefers-reduced-motion: no-preference` and stops under `html[data-motion="reduced"]`.
- Under `forced-colors: active` the gauges switch to system colours; the other
  colour-coded components keep their colours (`forced-color-adjust: none`), because the
  colour is the data. Each one also has a text alternative (label, table or `aria-label`).

---

## Dial gauge `.gauge-dial`

```html
<div class="gauge-dial" style="--value:.72; --gauge-redline:.8125">
  <meter min="0" max="8000" low="5500" high="6500" value="5760">5,760 rpm</meter>
  <ol class="gauge-ticks" aria-hidden="true">
    <li>0</li><li>1</li><li>2</li><li>3</li><li>4</li><li>5</li><li>6</li>
    <li class="is-redline">7</li><li class="is-redline">8</li>
  </ol>
  <div class="gauge-readout"><span class="readout">5.7</span>×1000 rpm</div>
</div>
```

- **Value.** The `<meter>` is the documented default: it gives screen readers the value,
  and where typed `attr()` is supported (Chromium today) its `value`, `min` and `max`
  drive the needle with full precision. Set `--value` (0–1) on the gauge too, so Firefox
  and Safari place the needle. Apps that prefer an ARIA meter use a span:
  `<div class="gauge-dial" role="meter" aria-label="Boost" aria-valuenow="1.72" aria-valuemin="0" aria-valuemax="2" style="--value:.86"><span class="gauge-needle"></span>…</div>`.
- **Parts.** `::before` is the arc track, `::after` the ticks (major and minor) plus the
  redline band, the `<meter>`/`.gauge-needle` is the value layer (fill arc, needle, hub,
  turned as one), `ol.gauge-ticks` prints numbers round the arc (up to 13 items, spread
  evenly from the first to the last), `.gauge-readout` sits in the lower centre and may
  hold a `.readout`.
- **States:** `.is-warn`, `.is-error` recolour the fill arc. The redline band shows the
  danger zone by position, not colour alone; `li.is-redline` colours a number.
- **Value API (inline):** `--value` (0–1), `--gauge-redline` (0–1, where the band starts;
  default 1 = none), `--gauge-ticks` (major intervals, 8), `--gauge-minor` (subdivisions
  per major, 5), `--gauge-size` (12rem), `--gauge-sweep` (270deg), `--gauge-start`.
- **Theme tokens (defaults):**

| Token | Default |
|---|---|
| `--gauge-size` | `12rem` (sizes inside are in `cqi` of the gauge, so everything scales) |
| `--gauge-face` | `var(--surface-2)` |
| `--gauge-border`, `--gauge-border-width` | `var(--border)`, `1px` |
| `--gauge-shadow` | `none` |
| `--gauge-inset` | `3cqi` (gap between rim and arc) |
| `--gauge-arc-width` | `5cqi` |
| `--gauge-track` | `var(--meter-track, var(--bg))` |
| `--gauge-fill` | `var(--accent)`; `--gauge-fill-warn` `var(--warning)`; `--gauge-fill-error` `var(--danger)` |
| `--gauge-redline-color` | `var(--danger)`; numbers `--gauge-redline-fg` `var(--danger-text, var(--danger))` |
| `--gauge-tick`, `--gauge-tick-minor`, `--gauge-tick-length` | `var(--text)`, `var(--muted)`, `5cqi` |
| `--gauge-label-fg`, `--gauge-label-size`, `--gauge-label-r` | `var(--text)`, `7cqi`, `29cqi` |
| `--gauge-needle` | `var(--danger)` (must be opaque) |
| `--gauge-needle-width`, `--gauge-needle-length`, `--gauge-needle-tail` | `2.5cqi`, `82%`, `8%` |
| `--gauge-needle-image` | a linear-gradient bar built from the above; set any image (an SVG data URI for a brass or tapered needle) — it is used as both paint and mask |
| `--gauge-hub`, `--gauge-hub-size` | `var(--text)`, `12%` of the radius |
| `--gauge-readout-fg`, `--gauge-readout-size` | `var(--muted)`, `6cqi` |
| `--gauge-speed` | `0.4s` (needle sweep) |

- **Glow:** the value layer is masked, so a `filter` on it is clipped. Put a glow on the
  gauge itself: `html[data-theme="x"] .gauge-dial { filter: drop-shadow(…) }`.
- **Tiers:** fixed size, `max-inline-size: 100%`, so a gauge never overflows a phone; in a
  `.cluster` they wrap. Not interactive, so no touch sizing.
- **Accessibility:** the `<meter>` (or `role="meter"`) carries the value; the numbers are
  `aria-hidden`. Give the meter fallback text or the gauge an `aria-label` with the unit.

## Arc gauge `.gauge-arc`

Same markup as the dial, without a needle (a fuel or level gauge). A 180° top half, the
readout in the bowl. Defaults: `--gauge-sweep: 180deg`, `--gauge-arc-width: 9cqi`,
`--gauge-ticks: 4`, `--gauge-minor: 2`. States `.is-warn`, `.is-error`; `--gauge-redline`
works.

```html
<div class="gauge-arc" style="--value:.3">
  <meter min="0" max="60" low="10" value="18">18 of 60 litres</meter>
  <ol class="gauge-ticks" aria-hidden="true"><li>E</li><li>½</li><li>F</li></ol>
  <div class="gauge-readout"><span class="readout">18</span>litres</div>
</div>
```

## Linear gauge `.gauge-linear`

Extends `.meter` (div form or native `<meter class="meter">`) with marks.

```html
<div class="gauge-linear">
  <div class="meter" style="--meter-level:62%" role="meter" aria-label="Feeder load, kW"
       aria-valuenow="62" aria-valuemin="0" aria-valuemax="100"><div class="meter-fill"></div></div>
  <span class="gauge-mark" style="--at:0%">0</span>
  <span class="gauge-mark" style="--at:100%">100</span>
  <span class="gauge-mark is-target" style="--at:50%">Target 50</span>
  <span class="gauge-mark is-warn" style="--at:80%">Warn 80</span>
  <span class="gauge-mark is-min" style="--at:14%">min 14</span>
  <span class="gauge-mark is-max" style="--at:91%">max 91</span>
</div>
```

- Plain `.gauge-mark` = scale label with a short tick below the bar. `.is-target` (line
  plus a ▼ head, bold label) and `.is-warn` (dashed line) label below; `.is-min`/`.is-max`
  (recorded extremes) label above. Each label slides so it stays inside the bar at 0% and
  100%. Every kind differs by shape, not just colour.
- Inside a linear gauge the meter's warn/peak bands are sized to the track (they are sized
  to the fill in a bare `.meter`, see the core note in the report).
- Tokens: `--gauge-target` (`var(--text)`), `--gauge-warn` (`var(--warning-text, var(--warning))`),
  `--gauge-minmax` and `--gauge-mark-fg` (`var(--muted)`), `--gauge-linear-label-room`
  (`1.35rem`), `--gauge-linear-label-size` (`0.75rem`), plus all `--meter-*` tokens.
- Labels closer than their width overlap; keep marks apart on narrow screens.

## Compass `.compass` and heading strip `.compass-strip`

```html
<div class="compass" style="--heading:215" role="img" aria-label="Heading 215°, south-west">
  <ol class="gauge-ticks" aria-hidden="true"><li>N</li><li>NE</li><li>E</li><li>SE</li><li>S</li><li>SW</li><li>W</li><li>NW</li></ol>
  <span class="gauge-needle"></span>
</div>
<div class="compass is-north-up" style="--heading:72" role="img" aria-label="Heading 72°">…</div>

<ol class="compass-strip" style="--heading:215" role="img" aria-label="Heading 215°. Gate at 250°.">
  <li>N</li><li>NE</li><li>E</li><li>SE</li><li>S</li><li>SW</li><li>W</li><li>NW</li>
  <li class="is-marker" data-series="2" style="--at:250"><svg class="icon"><use href="assets/icons/icons.svg#icon-map-pin"/></svg></li>
</ol>
```

- `.compass` is the dial face over 360°: the rose turns by `--heading` (degrees) and the
  needle points at the heading (heading-up). `.is-north-up` keeps the rose still and turns
  the needle. The first `li` (N) is coloured. Use 4 or 8 letters.
- `.compass-strip`: letters every `--compass-step` degrees (45); items with `--at` are
  markers at their own bearing (`.is-marker`, coloured by `data-series`). It shows
  `--compass-strip-span` degrees across its width (180) and wraps round 360°.
- Tokens: `--compass-needle` (`var(--danger)`), `--compass-needle-tail` (`var(--muted)`),
  `--compass-needle-length` (`70%`), `--compass-needle-tail-length` (`30%`),
  `--compass-north` (`var(--danger-text, var(--danger))`); strip: `--compass-strip-bg`
  (`var(--surface-2)`), `-fg`, `-border`, `-border-width`, `-radius`, `-height` (`2.5rem`),
  `--compass-strip-mask` (`none`; e.g. a fade-out `linear-gradient` for Skyrim),
  `--compass-tick`, `--compass-tick-minor`, `--compass-lubber` (`var(--accent)`).
- Needs CSS `mod()` (Baseline 2024).

## Map frame `.map`, pins `.map-pin`, legend `.map-legend`

```html
<figure class="map">
  <img src="tiles/harbour.png" alt="Street map of the harbour district">  <!-- or <svg>, <iframe>, <canvas> -->
  <button class="map-pin" style="--x:22%; --y:40%" data-series="1" popovertarget="pin-depot">
    <span class="map-pin-label">North depot</span></button>
  <button class="map-pin" style="--x:74%; --y:68%" data-series="3" popovertarget="pin-crane" aria-label="Crane 4, fault"></button>
  <span class="map-north" role="img" aria-label="North">N</span>
  <div class="map-controls">
    <button class="btn btn-icon" aria-label="Zoom in"><svg class="icon"><use href="assets/icons/icons.svg#icon-zoom-in"/></svg></button>
    <button class="btn btn-icon" aria-label="Zoom out"><svg class="icon"><use href="assets/icons/icons.svg#icon-zoom-out"/></svg></button>
  </div>
  <ul class="legend map-legend"><li data-series="1">Depot</li><li data-series="3">Fault</li></ul>
  <span class="map-scale" style="--map-scale-width:5rem">200 m</span>
  <figcaption class="map-attribution">Map data © …</figcaption>
</figure>
<div class="popover" popover id="pin-depot">…</div>
```

- Not a map engine. The first `img|svg|iframe|canvas|video` child fills the frame
  (`object-fit: cover`); overlays sit on a grid: north top-start, controls top-end,
  legend above the scale bottom-start, attribution bottom-end.
- Pins: `--x`/`--y` are percentages of the frame; the pin's tip sits on the point. The hit
  area is `--tap-min` square (44px on touch tiers); the drawn pin is `--map-pin-size`.
  Selected: `aria-expanded="true"`, `.is-active` or `aria-current` (bigger, outlined).
  The popover is core's top-layer `.popover[popover]`, anchored to the pin where anchor
  positioning exists. A pin without a visible label needs `aria-label`.
- `--map-bearing` (degrees) turns the north arrow when the map is rotated.
- `.map-legend` outside a `.map` is a normal legend (use it below the map on phones).
- Value API: `--map-ratio` (`16 / 10`), `--map-scale-width`, `--x`, `--y`, `--map-bearing`.
- Tokens: `--map-bg`, `--map-border`, `--map-border-width`, `--map-radius`, `--map-shadow`,
  `--map-pad` (`var(--space-xs)`), `--map-min-height` (`14rem`), `--map-media-filter`
  (`none`; dark themes can dim a light map, e.g. `invert(1) hue-rotate(180deg) brightness(.85)`),
  `--map-overlay-bg` (88% `--surface`), `--map-overlay-fg`, `--map-overlay-radius`,
  `--map-overlay-size`, `--map-attribution-fg` (`var(--muted)`), `--map-north`
  (`var(--danger)`), `--map-scale-fg`, `--map-pin-size` (`1.4rem`), `--map-pin-bg`
  (`var(--accent)`, overridden by `data-series`), `--map-pin-border`, `--map-pin-border-active`,
  `--map-pin-dot`, `--map-pin-shadow`.
- No `container-type` on `.map`: it holds popovers.

## Progress ring `.progress-ring`

```html
<div class="progress-ring" role="progressbar" aria-label="Upload" aria-valuenow="64"
     aria-valuemin="0" aria-valuemax="100" style="--value:.64">64%</div>
<div class="progress-ring" role="progressbar" aria-label="Loading"></div>  <!-- indeterminate -->
```

Indeterminate: `.is-indeterminate`, or a `role="progressbar"` with no `aria-valuenow`
(spins under no-preference motion, a static quarter arc otherwise). States `.is-success`,
`.is-error` (pair them with an icon or text). Tokens: `--progress-ring-size` (`3rem`),
`--progress-ring-width` (`0.3rem`), `--progress-ring-fill` (`var(--progress-fill, var(--accent))`),
`--progress-ring-track` (`var(--progress-bg, var(--surface-2))`), `--progress-ring-fg`,
`--progress-ring-text` (`0.75rem`).

## Sparkline `.sparkline`

```html
<svg class="sparkline is-up" viewBox="0 0 100 24" preserveAspectRatio="none" role="img" aria-label="Requests rising">
  <polygon class="sparkline-area" points="0,24 … 100,24"/><polyline points="0,20 … 100,2"/>
</svg>
```

Styling only; the stroke stays `--sparkline-line-width` (1.5) at any size. `.is-up` /
`.is-down` use the success/danger text colours; always pair them with a `.stat-trend` arrow
or text. Optional `.sparkline-area`, `.sparkline-baseline`. Tokens: `--sparkline-stroke`
(`var(--chart-series-1)`), `--sparkline-width` (`6em`), `--sparkline-height` (`1.5em`),
`--sparkline-area-opacity` (`0.16`).

## Donut `.donut`

```html
<div class="donut" style="--seg-1:42%; --seg-2:28%; --seg-3:18%; --seg-4:12%"
     role="img" aria-label="Traffic: Direct 42%, Search 28%, Social 18%, Email 12%">
  <span><strong>18.4k</strong>visits</span>
</div>
<ul class="legend"><li data-series="1">Direct 42%</li>…</ul>
```

`--seg-1`…`--seg-6` are percentages, coloured `--chart-series-1..6` in order (the
declarative form of the plan's `--segments`). Unused space shows `--donut-track`.
`--donut-hole: 0%` makes a pie. Tokens: `--donut-size` (`9rem`), `--donut-hole` (`58%`),
`--donut-gap` (`0.4%`), `--donut-gap-color` (`var(--surface)`), `--donut-track`
(`var(--surface-2)`), `--donut-fg`, `--donut-value-fg`. Always add a legend and a data table.

## Chart legend `.legend` / `.chart-legend`

```html
<ul class="legend"><li data-series="1">Revenue</li><li data-series="2">Cost</li></ul>
<ul class="legend is-line">…</ul>                       <!-- line swatches -->
<ul class="legend"><li data-series="2"><button aria-pressed="false">App</button></li></ul>  <!-- toggles -->
<ul class="legend is-scale"><li style="--v:0">Less</li><li style="--v:.5"></li><li style="--v:1">More</li></ul>
```

`.is-vertical` stacks. A toggle button grows to `--tap-min`; `aria-pressed="false"` strikes
the label through and dims the swatch (not colour alone). Tokens: `--legend-size`
(`0.85em`), `--legend-fg`, `--legend-swatch-size` (`0.8em`), `--legend-swatch-radius` (`2px`).

## Heatmap `.heatmap`

```html
<ol class="heatmap" role="img" aria-label="Commits per day, 12 weeks. See the data table.">
  <li style="--v:.4" title="Week 1, Mon: 6 commits"></li>…   <!-- column by column, 7 rows -->
</ol>
<ol class="heatmap is-diverging" style="--heatmap-rows:3"><li style="--v:-.6"></li>…</ol>
```

`--v` 0–1 mixes `--chart-seq-0` → `--chart-seq-8`; `.is-diverging` takes −1…1 across
`--chart-div-neg` / `-mid` / `-pos`. `.is-empty` = no data (dashed). Cells flow down
`--heatmap-rows` (7) then across; the grid scrolls sideways inside itself. Tokens:
`--heatmap-cell` (`0.85rem`), `--heatmap-gap` (`3px`), `--heatmap-radius` (`2px`). Colour
is the only encoding inside the grid, so a data table is required; give focusable cells
`tabindex="0"` if the app shows per-cell detail.

## Timeline `.timeline`

```html
<ol class="timeline">
  <li class="is-done"><time datetime="2026-09-28">28 Sep</time><strong>Order placed</strong><p>Paid.</p></li>
  <li aria-current="step"><time>1 Oct</time><strong>Out for delivery</strong></li>
  <li class="is-warn">…</li> <li class="is-error">…</li> <li>…</li>
</ol>
<ol class="timeline is-horizontal">…</ol>
```

Dots carry glyphs (✓, !, ✕) and the current one a ring, so state isn't colour alone.
`.is-horizontal` runs across from 901px up and scrolls inside itself if narrow; below that
it stays vertical. Tokens: `--timeline-gap`, `--timeline-dot-size` (1rem), `--timeline-dot-bg`,
`--timeline-dot-border`, `--timeline-dot-fg`, `--timeline-line`, `--timeline-done`,
`--timeline-current`, `--timeline-current-ring`, `--timeline-time-fg`.

## Property grid `dl.props`

```html
<dl class="props">
  <dt>Name</dt><dd>pump-station-04</dd>
  <div><dt>Owner</dt><dd>Ava Thompson</dd></div>   <!-- row wrappers allowed -->
</dl>
```

Keys take up to 40% of the width; long values (hashes, URLs) wrap. Tokens: `--props-size`,
`--props-pad-x`, `--props-pad-y`, `--props-rule` (`var(--hairline)`), `--props-key-fg`
(`var(--muted)`), `--props-value-fg`.

## Battery `.battery` and signal `.signal`

```html
<span class="battery" role="img" aria-label="Battery 64%" style="--value:.64"></span>
<span class="battery is-low" …></span> <span class="battery is-charging" …></span>
<span class="signal" role="img" aria-label="Signal 3 of 4" data-bars="3"></span>
```

Sized in `em`, drawn in `currentColor`, so they fit any status strip. Tokens:
`--battery-width`, `--battery-height`, `--battery-border`, `--battery-border-width`,
`--battery-radius`, `--battery-fill`, `--battery-nub`, `--battery-bolt` (`var(--warning)`);
`--signal-fg`, `--signal-off-fg`, `--signal-width`, `--signal-height`.

## Clock `.clock` and countdown `.countdown`

```html
<div class="clock" style="--h:10; --m:9; --s:30" role="img" aria-label="London, 10:09">
  <ol class="gauge-ticks" aria-hidden="true"><li>12</li><li>1</li>…<li>11</li></ol>
  <span class="clock-hand is-hour"></span><span class="clock-hand is-minute"></span><span class="clock-hand is-second"></span>
</div>

<div class="countdown" role="timer" aria-label="Launch in 2 days, 4 hours">
  <span data-unit="days">02</span><span data-unit="hrs">04</span><span data-unit="min">17</span>
</div>
```

The clock is the dial face (360°, 12 majors, 5 minors); the app updates `--h`, `--m`, `--s`
(and the `aria-label`). Empty `li`s give a 12/3/6/9 face. Tokens: all `--gauge-*` face
tokens, plus `--clock-hand` (`var(--text)`), `--clock-second-hand` (`var(--danger)`),
`--clock-hand-width`, `--clock-hour-width`, `--clock-second-width`.
Countdown parts use the readout look; `data-unit` prints the unit under each part.
`.is-urgent` (danger text) and `.is-done` (muted); change the text too. Tokens:
`--countdown-fg` (`var(--readout-fg, var(--accent))`), `--countdown-font`, `--countdown-size`
(`1.75rem`), `--countdown-gap`, `--countdown-unit-fg`, `--countdown-glow` (`var(--readout-glow)`).
Update the `aria-label` at a calm rate; `role="timer"` is not announced on every tick.

---

## Charts: the library-neutral contract (§18)

ftl-themes picks no chart library. A chart in any theme is: a `.chart` container, the theme
tokens, and class hooks on plain SVG.

```html
<figure class="chart">
  <figcaption>Weekly active users</figcaption>
  <ul class="chart-legend is-line"><li data-series="1">Web</li><li data-series="2">App</li></ul>
  <svg viewBox="0 0 400 228" role="img" aria-labelledby="t d">
    <title id="t">Weekly active users by channel</title><desc id="d">Web leads, 42k to 74k.</desc>
    <g class="chart-grid"><line x1="40" x2="380" y1="100" y2="100"/>…</g>
    <g class="chart-axis"><line …/><text x="34" y="104" text-anchor="end">40</text>…</g>
    <g class="chart-series" data-series="1">
      <polygon class="is-area" points="…"/><polyline points="…"/>
      <circle class="chart-point" cx="…" cy="…" r="4"/>
    </g>
    <g class="chart-series" data-series="2"><rect x="…" y="…" width="26" height="…" rx="2"/></g>
    <text class="chart-label" x="…" y="…">Web</text>
  </svg>
  <div class="chart-tooltip" style="--x:60%; --y:27%">May · Web 66k</div>
  <details class="accordion-item"><summary class="accordion-trigger">Data table</summary>
    <div class="table-wrap"><table class="table">…</table></div></details>
</figure>
```

| Hook | Styled as |
|---|---|
| `.chart` | `color: var(--chart-fg, var(--chart-text))` so `currentColor` axes, ticks and labels follow the theme; transparent `--chart-bg`. |
| `.chart-grid` | `stroke: var(--chart-grid)`, 1px, crisp. |
| `.chart-axis` | `stroke: var(--chart-axis, currentColor)`; its `text` is `currentColor`. |
| `.chart-series[data-series="1..6"]` | `color: var(--series)`; lines stroke it (`--chart-line-width`, 2), dashed by `--chart-dash-n`; `rect`s fill it; `.is-area` fills it at `--chart-area-opacity` (0.16). |
| `.chart-point` | series fill with a `--chart-point-ring` (surface) ring; `:focus-visible`, `.is-active`, `[aria-selected=true]` and hover outline it in `--chart-highlight`. |
| `.chart-label` | direct labels in `--chart-label-fg` (`--text`); never the series colour. |
| `.chart-frame`, `.chart-crosshair`, `.chart-annotation`, `.chart-selection` | `--chart-plot-bg`/`--chart-frame`, `--chart-crosshair` (dashed `--muted`), `--chart-annotation` (`--flare`) + `--chart-annotation-fg`, `--chart-selection` (14% accent). |
| `.chart-tooltip` | HTML, placed by the app at `--x`/`--y` inside `.chart`; reuses `--tooltip-bg/-fg/-border/-border-width/-radius`. |
| `.chart-legend` | the `.legend` above. |

SVG text is sized in user units (`--chart-text-size`, 11px) and grows to
`--chart-text-size-narrow` (16px) in a 480px-or-narrower container or viewport, so it stays
readable when the chart shrinks on a phone.

**Tokens.** Existing: `--chart-series-1..6`, `--chart-text`, `--chart-grid` (core.css).
New, with defaults derived from them so every theme works today:

| Token | Default |
|---|---|
| `--chart-seq-0` … `--chart-seq-8` | `--chart-seq-hue` (`--chart-series-1`) mixed into `--chart-seq-base` (`--surface`) at 8, 18, 30, 42, 54, 66, 78, 90, 100% |
| `--chart-div-neg` / `-mid` / `-pos` | `--chart-series-4` / `--surface-2` / `--chart-series-1` |
| `--chart-dash-1` … `-6` | `none` (themes with tiny palettes set e.g. `6 3`, `2 3`) |

Sequential scales are one hue, low = near the surface, so they read correctly in light and
dark themes. Diverging scales are two hues with a neutral middle.

**Every chart needs an accessible data table** (and a `<title>`/`<desc>` or `aria-label`
that states the takeaway). For two or more series show a legend, and direct-label up to
four. Colour never carries meaning alone: use labels, the table, and `--chart-dash-n`.

### Adapter recipes (no library ships in ftl-themes)

All of them read the same tokens; re-read after a theme switch (`theme-loader.js` swaps the
stylesheet, so listen for its change, or re-render on `load` of `#theme-link`).

**TanStack Charts** (alpha; its colours are CSS custom properties that inherit, so map them
once on `.chart` and check names against the version you install):

```css
.chart {
  --ts-chart-1: var(--chart-series-1); --ts-chart-2: var(--chart-series-2);
  --ts-chart-3: var(--chart-series-3); --ts-chart-4: var(--chart-series-4);
  --ts-chart-5: var(--chart-series-5); --ts-chart-6: var(--chart-series-6);
  --ts-chart-tooltip-bg: var(--tooltip-bg, var(--surface));
  --ts-chart-tooltip-fg: var(--tooltip-fg, var(--text));
  --ts-chart-tooltip-border: var(--tooltip-border, var(--border));
  --ts-chart-tooltip-radius: var(--tooltip-radius, var(--radius));
}
```

It already draws axes in `currentColor` on a transparent background, which `.chart` sets.

**Chart.js** (canvas, can't see CSS: read the tokens):

```js
const css = getComputedStyle(document.documentElement);
const t = (n) => css.getPropertyValue(n).trim();
Chart.defaults.color = t('--chart-text');
Chart.defaults.borderColor = t('--chart-grid');
Chart.defaults.font.family = t('--font');
const series = [1, 2, 3, 4, 5, 6].map(i => t(`--chart-series-${i}`));
const dash = [1, 2, 3, 4, 5, 6].map(i => (t(`--chart-dash-${i}`) || 'none') === 'none' ? [] : t(`--chart-dash-${i}`).split(/\s+/).map(Number));
// datasets[i].borderColor = series[i]; datasets[i].borderDash = dash[i];
Chart.defaults.plugins.tooltip.backgroundColor = t('--tooltip-bg') || t('--surface');
Chart.defaults.plugins.tooltip.titleColor = Chart.defaults.plugins.tooltip.bodyColor = t('--tooltip-fg') || t('--text');
```

`getComputedStyle` returns `color-mix()` values resolved in modern engines; for the
`--chart-seq-*` defaults, read them from an element that uses them (e.g. set
`el.style.color = 'var(--chart-seq-4)'` and read `getComputedStyle(el).color`).

**ECharts:**

```js
const t = (n) => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
chart.setOption({
  color: [1, 2, 3, 4, 5, 6].map(i => t(`--chart-series-${i}`)),
  backgroundColor: 'transparent',
  textStyle: { color: t('--chart-text'), fontFamily: t('--font') },
  xAxis: { axisLine: { lineStyle: { color: t('--chart-text') } }, splitLine: { lineStyle: { color: t('--chart-grid') } } },
  yAxis: { axisLine: { lineStyle: { color: t('--chart-text') } }, splitLine: { lineStyle: { color: t('--chart-grid') } } },
  tooltip: { backgroundColor: t('--tooltip-bg') || t('--surface'), borderColor: t('--tooltip-border') || t('--border'),
             textStyle: { color: t('--tooltip-fg') || t('--text') } },
  visualMap: { inRange: { color: [0, 2, 4, 6, 8].map(i => t(`--chart-seq-${i}`)) } },
});
```

(Render with the SVG renderer if you want the class hooks; the canvas renderer needs the
values above.)

**Observable Plot and D3** emit SVG, so use the class hooks and let CSS do the colour:

```js
// Plot: give marks the hook classes; colours come from the theme, not the spec.
Plot.plot({ className: 'chart', style: { background: 'transparent', color: 'currentColor' },
  marks: [ Plot.gridY({ className: 'chart-grid' }), Plot.axisX({ className: 'chart-axis' }),
           Plot.lineY(web, { x: 'month', y: 'users', className: 'chart-series', stroke: 'currentColor' }) ] });
// then set data-series on each series group: svg.querySelectorAll('.chart-series')[i].dataset.series = i + 1

// D3
g.append('path').attr('class', 'chart-series').attr('data-series', 1).attr('d', line(data));
g.call(d3.axisLeft(y)).attr('class', 'chart-axis');   // d3 axes draw with currentColor
```

### CSS-only charts

`.bar-chart` (core) and `.donut` (above) cover bar, column and donut with no JS.
