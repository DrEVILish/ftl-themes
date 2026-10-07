# Graphs: telemetry grid, uPlot bridge, system pane

Source: `core/components/graphs.css`. Example page: `media-decks.html` (open the **System** pane).

## Graph grid `.graph-grid` / `.graph-card`

```html
<div class="graph-grid">
  <figure class="graph-card">
    <figcaption class="graph-card-title">CPU per core <span class="graph-card-value">avg 38%</span></figcaption>
    <div class="graph-card-plot chart">
      <svg viewBox="0 0 120 40" preserveAspectRatio="none" role="img" aria-label="CPU per core, last 4 minutes …">
        <path class="chart-grid" d="M0 10.5H120M0 20H120M0 29.5H120"/>
        <polyline class="chart-series" data-series="1" points="…"/>
      </svg>
    </div>
    <ul class="chart-legend is-line"><li data-series="1">core 0</li>…</ul>
  </figure>
</div>
```

- Cards wrap onto more rows (`repeat(auto-fill, minmax(min(100%, --graph-card-min), 1fr))`)
  instead of shrinking. `.graph-card.is-full` spans the row, `.is-tall` uses the tall height.
- The plot slot is a `.chart`, so all chart hooks apply (`.chart-grid`, `.chart-series[data-series]`,
  `.is-area`, `.chart-annotation`…). An inline SVG fills the slot; strokes don't scale.
- Accessibility: the `<figcaption>` names the graph; give the SVG or canvas an `aria-label`
  describing the trend (a canvas is invisible to screen readers otherwise).

| Token | Default |
|---|---|
| `--graph-card-min` | `16rem` |
| `--graph-card-height`, `--graph-card-height-tall` | `6.5rem`, `10rem` (plot height) |
| `--graph-grid-gap` | `var(--space-s)` |
| `--graph-card-bg`, `--graph-card-border`, `--graph-card-radius`, `--graph-card-shadow`, `--graph-card-padding` | surface, border, radius, none, `.6rem .75rem` |
| `--graph-card-title-size`, `--graph-card-title-fg`, `--graph-card-plot-bg` | `.8rem`, text, `--chart-plot-bg` |

## uPlot bridge

uPlot draws lines, grid and axes on a canvas, so their colours must go into its options; CSS
styles the DOM parts (`.u-title`, `.u-legend` table with `.u-series`, `.u-marker`, `.u-value`,
`.u-off`, `.u-select`, `.u-cursor-x/y`) inside `.graph-card` or `.chart`. Load this library
after `uPlot.min.css`. Mount uPlot in the `.graph-card-plot` and read the theme tokens:

```js
// Resolve a token to a colour canvas accepts (tokens may be color-mix() or var() chains).
const probe = document.body.appendChild(document.createElement('i'));
const tok = name => { probe.style.color = `var(${name})`; return getComputedStyle(probe).color; };

function uplotTheme() {
  const axis = { stroke: tok('--chart-text'), grid: { stroke: tok('--chart-grid'), width: 1 },
                 ticks: { stroke: tok('--chart-grid') }, font: getComputedStyle(document.body).font };
  return {
    series: n => tok(`--chart-series-${(n - 1) % 6 + 1}`),
    axes: [axis, axis],
  };
}
const t = uplotTheme();
const opts = { width, height, axes: t.axes,
  series: [{}, { label: 'core 0', stroke: t.series(1) }, { label: 'core 1', stroke: t.series(2) }] };
```

Re-read after a theme switch (theme-loader swaps `#theme-link`; listen for its `load` event)
and call `u.destroy()` + recreate, or set `u.series[i].stroke` and `u.redraw()`.
Size it from the slot with a `ResizeObserver` on `.graph-card-plot`.

## System pane `.system-pane`

```html
<details class="system-pane">
  <summary><strong>System</strong> <span class="deck-lamp is-on" data-lamp="sys">Healthy</span> CPU 38% …</summary>
  <div class="system-pane-body"><div class="graph-grid">…</div></div>
</details>
```

Last child of `.app-main`, right above `.app-status`: a full-width bar that opens into the graph grid
right above the footer. It stays in flow on purpose: some themes (ios-flat) make the footer sticky. Native `<details>`, no script;
the summary is keyboard-operable. Tokens: `--system-pane-bg` (surface),
`--system-pane-border`, `--system-pane-radius`, `--system-pane-shadow`, `--system-pane-max`
(`60vh`, body scrolls beyond).
