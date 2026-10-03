# Operations kit (v5)

Source: `core/components/ops.css`. Example pages: `smart-home.html`, `inventory.html`,
`fleet.html`.

Small additions for operations screens (dispatch, smart home, stock rooms) on top of the
instruments group (`.map`, `.legend`) and surfaces (`.card.has-media`). Nothing here
needs JavaScript; values come in through attributes (`data-status`, `data-shape`,
`data-series`) and tokens.

Shared conventions:

- Every colour is a token with a core fallback, so all themes work with no theme edits.
- Status never relies on colour alone: pins and legend items also change **shape**,
  feeds carry a text badge, barcodes print their human-readable text.
- Motion (the live badge's blink) runs only under `prefers-reduced-motion: no-preference`
  and stops under `html[data-motion="reduced"]`.

---

## Status colours `[data-status]`

```html
<button class="map-pin" data-status="error" …></button>
<ul class="legend"><li data-status="warn">Delayed</li></ul>
<g class="chart-series" data-status="ok">…</g>
```

`data-status="ok|warn|error|idle|info"` sets `--series` (the same hook `data-series`
sets), so anything that draws in `--series` (map pins, legend swatches, chart series,
routes) takes a status colour instead of a chart colour.

| Token | Default |
|---|---|
| `--status-ok` | `var(--success)` |
| `--status-warn` | `var(--warning)` |
| `--status-error` | `var(--danger)` |
| `--status-idle` | `var(--muted)` |
| `--status-info` | `var(--accent)` |

Avatars and presence keep their own `data-status="online|away|busy|offline"` (social.css);
the values don't overlap.

## Shaped map pins `.map-pin[data-shape]`

```html
<button class="map-pin" data-shape="triangle" data-status="error" style="--x:78%; --y:26%"
        popovertarget="pin-trk03" aria-label="TRK-03, breakdown"><span class="map-pin-label">TRK-03</span></button>
<ul class="legend map-legend">
  <li data-shape="circle" data-status="ok">Moving</li>
  <li data-status="idle">Idle</li>                       <!-- square: the legend's default swatch -->
  <li data-shape="diamond" data-status="warn">Delayed</li>
  <li data-shape="triangle" data-status="error">Breakdown</li>
</ul>
```

- `data-shape="circle|square|diamond|triangle"` turns the teardrop into a marker
  **centred on** its `--x`/`--y` point (a vehicle, a sensor), not a pin standing above it.
  Without `data-shape` the pin is core's teardrop (a place).
- Size, border, dot, shadow and the selected state (`aria-expanded`, `.is-active`,
  `aria-current`) are core's `--map-pin-*` tokens. The triangle draws its outline with
  `::after` in `--map-pin-border`.
- Legend items take the same `data-shape`, so the legend matches the pins by shape.
- Token: `--map-pin-square-radius` (`3px`, square and diamond corners).
- Touch: the hit area is still core's `--tap-min` square.
- Accessibility: the pin's name says the status in words (`aria-label="VAN-11, delayed"`).

## Sketch map hooks

For a schematic map drawn as the `.map`'s first child (an inline `<svg>`, no tiles):

```html
<figure class="map">
  <svg viewBox="0 0 1000 625" preserveAspectRatio="none" aria-hidden="true">
    <rect class="map-land" width="1000" height="625"/>
    <path class="map-water" d="…"/>  <rect class="map-park" …/>
    <g class="map-block"><rect …/>…</g>
    <path class="map-road" d="M0 100 H1000 …"/>  <path class="map-road is-major" d="M0 400 H1000"/>
    <text class="map-label" x="70" y="60">River Aire</text>
    <path class="map-route is-done" data-series="1" d="M500 512 V400 H360 V212"/>
    <path class="map-route is-planned" data-series="1" d="M360 212 V100 H200"/>
  </svg>
  <button class="map-pin" …></button> …
</figure>
```

Use `preserveAspectRatio="none"` when pins are placed in percentages, so the drawing and
the pins stretch together.

| Hook | Token (default) |
|---|---|
| `.map-land` | `--map-land` (`--surface-2`) |
| `.map-water` | `--map-water` (`--chart-series-1` 28% into `--surface-2`) |
| `.map-park` | `--map-park` (`--success` 22% into `--surface-2`) |
| `.map-block` | `--map-block` (`--text` 9% into `--surface-2`) |
| `.map-road` | `--map-road` (`--muted` 40% into `--surface-2`), `--map-road-width` (`6px`) |
| `.map-road.is-major` | `--map-road-major` (`--warning` 45% into `--surface-2`), `--map-road-major-width` (`10px`) |
| `.map-label` | `--map-label-fg` (`--muted`), `--map-label-size` (`11px`) |

Road and route strokes don't scale with the drawing (`vector-effect: non-scaling-stroke`).

## Route line `.map-route`

A path in the map SVG, coloured by `data-series` or `data-status` (`--map-route`, default
`--accent`, without either). `.is-planned` is dotted (`--map-route-dash`, `2px 7px`),
`.is-done` is faded (`--map-route-done-opacity`, `0.45`), so done, ahead and planned
differ by pattern as well as colour. Width `--map-route-width` (`4px`). Forced colours:
`CanvasText`. Describe routes in text too (the vehicle list, a run table).

## Camera feed `.camera-feed`

A camera or video feed frame: a placeholder scene until the stream paints, scanlines and
a vignette, a corner badge and a caption strip.

```html
<article class="card has-media">
  <div class="card-media camera-feed" role="img" aria-label="Front door camera, live: porch with a parcel">
    <svg viewBox="0 0 160 90" preserveAspectRatio="xMidYMid slice" fill="currentColor">…shapes…</svg>
    <span class="badge badge-danger camera-feed-badge is-live">Live</span>
    <span class="camera-feed-caption"><span>Front door</span><time>19:42:07</time></span>
  </div>
  <div class="card-body">…</div>
</article>
<div class="card-media camera-feed is-offline" …><span class="badge camera-feed-badge">Offline</span>…</div>
```

- The first `<svg>` (or `<img>`/`<video>`) fills the frame. Placeholder shapes drawn in
  `currentColor` take `--camera-feed-fg`, so they read in every theme.
- `.camera-feed-badge.is-live` adds a blinking record dot (motion allowed only); the word "Live"
  is the state. `.is-offline` greys the frame and fades the scene; say "Offline" in the
  badge.
- Tokens: `--camera-feed-ratio` (`16 / 9`; inside a `.card.has-media` the card's
  `--card-media-ratio` wins), `--camera-feed-bg` (a two-tone wall/floor gradient from `--muted`,
  `--text` and `--surface-2`), `--camera-feed-fg`, `--camera-feed-scanline` (`rgb(0 0 0 / .07)`),
  `--camera-feed-vignette` (`rgb(0 0 0 / .35)`), `--camera-feed-caption-bg` (`rgb(0 0 0 / .6)`),
  `--camera-feed-caption-fg` (`#fff`; video overlays stay light-on-dark in every theme).
- Accessibility: `role="img"` and a label that says what the camera sees and whether it
  is live.

## Barcode `.barcode`

```html
<span class="barcode" role="img" aria-label="Barcode AST-2210">AST-2210</span>
```

CSS-drawn stripes over the human-readable text. The stripe pattern is decorative and the
same for every code; for a scannable code render an SVG from a generator inside your own
frame. Tokens: `--barcode-fg` (`--text`), `--barcode-bg` (`--surface`), `--barcode-border`
(`--border`), `--barcode-radius` (`--radius`), `--barcode-width` (`12rem`, never wider
than its box), `--barcode-height` (`3.5rem`). Forced colours: `CanvasText` on `Canvas`.
Always give the code as text (it is the element's content) and an `aria-label`.
