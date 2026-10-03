# Live data and dashboards (v5)

Source: `core/components/live.css`. Example pages: `trading.html`, `mission-control.html`.
Covers PLAN.md §18 "Live-data states" and "Dashboard widget grid".

Shared conventions:

- These are **state classes the app toggles** as data streams in: `.is-updated` (on for
  about a second after a value changes, then removed), `.is-paused` on a feed,
  `.is-editing` on a dashboard. ftl-themes styles every state; it never times or moves
  anything itself.
- Every look reads a `--live-*`, `--connection-*`, `--feed-*`, `--depth-*`,
  `--dashboard-*` or `--widget-*` token with a fallback to the base tokens, so all 45
  themes work with no theme edits. Themes override at root scope.
- Motion (the flash, the feed slide-in, the connection lamp) runs only under
  `prefers-reduced-motion: no-preference` and stops under `html[data-motion="reduced"]`
  and `"none"`. Without motion each state has a static look.
- No state is colour alone: arrows, markers, outline styles and lamp shapes carry it too.

---

## Value changed `.is-updated`

```html
<td class="mono is-updated">412.18</td>
<span class="readout is-updated">49.6</span>
```

- **Motion:** a brief flash, a low-alpha tint of `--flare` (falling back to `--accent`)
  so text keeps its contrast. **Reduced motion:** a static 2px underline in `--accent`
  for as long as the class is on.
- **The app adds the class when the value changes and removes it after ~1s.** To
  re-trigger on the next tick, remove it, force a reflow (or wait a frame), add it again.
- **Demo loop, no JS:** `.is-demo-ticking` on any ancestor repeats every flash forever
  (every `--live-tick`, 5s), each offset by its own inline `--tick-delay`. For demos and
  screenshots only.

```html
<div class="dashboard is-demo-ticking">
  … <td class="is-updated" style="--tick-delay:1.3s">412.18</td> …
</div>
```

| Token | Default |
|---|---|
| `--live-flash-bg` | `color-mix(in srgb, var(--flare, var(--accent)) 28%, transparent)` |
| `--live-flash-fg` | `inherit` (`msdos`-style inverse flash: set bg to `--text`, fg to `--bg`) |
| `--live-flash-shadow` | `none` (a glow for `blue-future`) |
| `--live-flash-duration` | `1.2s` |
| `--live-mark`, `--live-mark-style` | `var(--accent)`, `solid` (the reduced-motion underline) |
| `--live-tick` | `5s` (demo loop period) |

## Direction `.is-up` / `.is-down` / `.is-flat`

```html
<td class="mono is-up">6.42</td>  <td class="mono is-down">1.12</td>  <span class="is-flat">0.00%</span>
```

Semantic colour (`--success-text` / `--danger-text`) **plus a ▲ / ▼ glyph** drawn before
the value (and announced as "up" / "down"). `.is-flat` prints a neutral dash. Don't type
your own arrow. Works on any element except `tr`, `tbody`, `table` and SVG.

- Existing `.stat-trend.is-up` (core) keeps its own colour and the arrow you type in its
  text; `.sparkline.is-up` keeps recolouring its stroke (instruments.css). Neither gets a
  second arrow.
- Tokens: `--live-up`, `--live-down` (colours), `--live-up-glyph`, `--live-down-glyph`
  (strings, default `"\25B2"` / `"\25BC"`). Both set `--state-fg`.

## Stale `.is-stale` + `data-age`

```html
<td class="mono is-stale" data-age="15m">8.62</td>
<span class="is-stale" data-age="47m">Balloon 1132Z</span>
<tr class="is-stale">…</tr>   <!-- a "stale" marker lands in the first cell -->
```

Muted text (a contrast-checked token, never `opacity`), a dashed outline, and a clock
marker chip printing `data-age` (screen readers hear "out of date, 15m"). Without
`data-age` the chip says "stale". The app updates `data-age`.

Tokens: `--live-stale-fg` (`var(--muted)`), `--live-stale-border` (`var(--muted)`),
`--live-stale-border-width` (`1px`), `--live-stale-style` (`normal`; `italic` for print
themes), `--live-stale-mark-bg` (`var(--surface-2)`), `--live-stale-mark-fg`
(`var(--text)`).

The marker is `::after`; on a `.widget` in edit mode `::after` is the resize corner, so
mark the widget's title or values instead of the widget.

## Connection `.connection[data-state]`

```html
<span class="connection" data-state="live" role="status">Market data live</span>
<span class="connection" data-state="reconnecting">Madrid DSS-63</span>
<span class="connection" data-state="offline">Goldstone DSS-14</span>
```

A lamp plus the element's own text (translatable; never generated). Each state has its
own shape: live = filled lamp (slow pulse), reconnecting = dotted ring (turning),
offline = crossed ring. Fits a bar, a status strip (`.app-status`) or a panel header.
Put `role="status"` on the one that should announce changes.

Tokens: `--connection-live` (`var(--lamp-on, var(--success))`), `--connection-reconnecting`
(`var(--warning)`), `--connection-offline` (`var(--danger)`), `--connection-fg`,
`--connection-size` (`0.85em`); also reads `--lamp-size`, `--lamp-radius`, `--lamp-glow`.

## Last updated `time.updated`

```html
<time class="updated" datetime="2026-10-03T14:22:19Z">Updated 5s ago</time>
```

Small muted text with a ↻ glyph and tabular numbers. The app rewrites the text and keeps
`datetime` current; don't make it a live region (it changes every second).
Token: `--live-updated-fg` (`var(--muted)`).

## Streaming feed `.feed`

```html
<ol class="feed" tabindex="0" aria-label="Market news">
  <li><span class="feed-time">14:04</span><span class="feed-source">Macro</span><span>Yields slip after soft PMI.</span></li>
  <li data-level="warn">…</li>
  <li class="is-new">…</li>           <!-- just arrived: slides in, accent edge -->
</ol>
<ol class="feed is-paused" data-new="3">…</ol>   <!-- reader scrolled up -->
```

- Items are any content; `.feed-time` and `.feed-source` are optional parts; the last
  child takes the remaining width. `data-level="warn|error"` adds a coloured edge.
- `.is-new` slides the item in (motion) and marks it with an accent edge (always).
- **Auto-scroll pause:** CSS can't see the scroll position. The app sets `.is-paused` (and
  `data-new="n"`) while the reader has scrolled away from the newest item; a sticky
  marker "↓ 3 new · paused" shows at the end. Works on `.log` too.
- Scrolls inside itself (`--feed-height`, 20rem); give it `tabindex="0"` and a label.

Tokens: `--feed-height`, `--feed-size` (`0.88em`), `--feed-pad`, `--feed-rule`
(`var(--hairline)`), `--feed-time-fg` (`var(--muted)`), `--feed-source-fg`, `--feed-new`
(`var(--accent)`), `--feed-in-duration` (`0.35s`), `--feed-paused-bg` / `-fg`
(`var(--accent)` / `var(--on-accent)`).

## Depth bar `.depth-bar`

```html
<td><span class="depth-bar is-bid" style="--depth:.6" aria-hidden="true"></span></td>
<td class="mono">412.16</td>
<td><span class="depth-bar is-ask" style="--depth:.9" aria-hidden="true"></span></td>
```

An order-book (or queue) depth bar of `--depth` (0–1) of its cell. `.is-bid` grows from
the inline end towards the price column, `.is-ask` from the start, so side reads by
position as well as colour. Decorative: keep the size as text in a neighbouring cell.
Tokens: `--depth-bid` (`var(--success)`), `--depth-ask` (`var(--danger)`),
`--depth-fill`, `--depth-track` (`transparent`), `--depth-bar-height` (`0.9em`),
`--depth-bar-min` (`3rem`), `--depth-radius` (`0`).

---

## Dashboard grid `.dashboard` and `.widget`

```html
<div class="dashboard">
  <div class="dashboard-bar">                       <!-- optional, first child -->
    <label class="toggle-btn"><input type="checkbox" class="dashboard-edit">
      <span class="toggle-btn-off">Edit layout</span><span class="toggle-btn-on">Done editing</span></label>
    <span class="dashboard-dirty" role="status">Unsaved layout</span>
    <button class="btn btn-secondary btn-sm dashboard-edit-only" type="button">Reset to default</button>
    <span class="is-pushed">…</span>
  </div>
  <section class="panel widget" style="--cols:8; --rows:2">…</section>
  <section class="panel widget" style="--cols:4">…</section>
  <div class="widget-placeholder" style="--cols:6">Drop here</div>
  <button class="widget-add" type="button" style="--cols:6"><svg class="icon">…</svg>Add widget</button>
</div>
```

- **Grid:** 12 columns on Desktop and XL, 2 on Tablet, 1 on Mobile. `--cols` (1–12,
  default 3) and `--rows` (default 1) set the span; spans are clamped to the tier's
  columns, so a wide widget never overflows. On Tablet a widget of 1–6 columns takes one
  of the two, 7–12 both (`--cols-tablet` overrides). On Mobile `--rows` is dropped.
  `grid-auto-flow: dense` back-fills holes. Rows are at least `--dashboard-row-min`
  (9rem) and grow with content.
- **Surface:** `.widget` is placement only; take the surface from `.panel`
  (`class="panel widget"`), so every theme's panel styling applies. `.widget-body` fills
  the rest and scrolls.
- **Container queries inside widgets:** each `.widget` is an inline-size container.
  `.widget-split` puts two parts side by side from 28rem of *widget* width (a donut and
  its legend, a clock and its readouts) and stacks them below; `.widget-wide` shows a
  part only from 28rem. Write your own `@container (min-width: …)` rules for anything
  else.
- **Edit mode:** `.dashboard.is-editing`, or with no JS a checked `input.dashboard-edit`
  anywhere inside the dashboard (`:has()`). It shows column guides behind the grid, a
  dashed outline per widget, a grab handle centred on each widget's top edge, a resize
  corner (end-end, `cursor: nwse-resize`), and reveals `.widget-add`,
  `.widget-placeholder`, `.dashboard-dirty` and `.dashboard-edit-only` (all hidden
  outside edit mode). **The app moves and resizes;** it also sets `.widget.is-dragging`
  (lifted, tilted) on the widget in flight and inserts the `.widget-placeholder` where it
  will drop.
- **Saved-layout states:** `.dashboard-dirty` is the unsaved-changes marker (a warning
  dot plus your text; give it `role="status"`), `.dashboard-edit-only` holds controls such
  as "Reset to default".

| Token | Default |
|---|---|
| `--dashboard-gap` | `var(--space-m)` |
| `--dashboard-row`, `--dashboard-row-min` | `minmax(var(--dashboard-row-min), auto)`, `9rem` |
| `--dashboard-edit-line` | `var(--accent)` (outlines, handle, corner, guides) |
| `--cols`, `--rows`, `--cols-tablet` | per widget (inline) |

- **Touch:** the grab handle is at least 3rem × 0.9rem and the resize corner at least
  60% of `--tap-min`; an app that supports touch dragging should make the handle a real
  `<button>` (with a label) the size of `--tap-min`. `.widget-add` is at least `--tap-min`.
- **Accessibility:** handles are drawn (empty `content`), so they say nothing to screen
  readers; offer keyboard move/resize commands (for example in a widget menu). Label
  each widget (`aria-labelledby` its title). Scroll regions inside widgets need
  `tabindex="0"` and a label.
