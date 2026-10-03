# Tables (v5)

Source: `core/components/tables.css`. Example page: `components-tables.html`.
Covers PLAN.md §7 (editable tables, tables on small screens), §18 (advanced
tables) and §9 #48 (table in a modal).

These build on core's `.table`, `.is-sticky`, `.is-striped`, `aria-sort`,
`tr.is-selected` / `tr.is-active`, `.table-wrap` and `--sticky-top`. Apps
provide the behaviour (open an editor, save, resize, reorder, select,
collapse); ftl-themes styles every state.

Shared tokens:

| Token | Default | Meaning |
|---|---|---|
| `--cell-pad-y` / `--cell-pad-x` | `calc(0.5em * var(--density))` / `calc(0.75em * var(--density))` | Cell padding (same values as v4). In-cell editors read them, so set them here, not `padding` on `td`. |
| `--table-bg` | `var(--surface)` | The opaque fill of frozen cells while the table is scrolled. Must be an opaque colour. |

---

## Editable cells

```html
<td class="is-editable" tabindex="0">Road trip</td>                       <!-- idle -->
<td class="is-editing"><input class="input" value="Road trip" aria-label="Trip"></td>
<td class="is-editing"><select class="select" aria-label="Status">…</select></td>
<td class="is-editing"><input class="input" type="date" aria-label="Departs"></td>
<td class="is-editing"><input class="input" type="number" aria-label="Nights"></td>
<td class="is-editing"><label class="check"><input type="checkbox" class="checkbox"><span class="visually-hidden">Paid</span></label></td>
<td class="is-dirty">Road trip 2</td>                                     <!-- changed, unsaved -->
<td class="is-saving" aria-busy="true">Road trip 2</td>                   <!-- or class="htmx-request" -->
<td class="is-saved">Road trip 2</td>                                     <!-- remove after ~2s -->
<td class="is-editing">
  <input class="input" aria-invalid="true" aria-describedby="e1" aria-label="Trip">
  <span class="field-error" id="e1">A name is required.</span>
</td>
<td class="is-editable is-readonly">Locked</td>                  <!-- read-only -->
```

Whole row in edit mode, with its actions in the last cell:

```html
<tr class="is-editing">
  <td><input class="input" value="Porto" aria-label="Trip"></td>
  <td><select class="select" aria-label="Status">…</select></td>
  <td><span class="btn-group"><button class="btn btn-sm btn-primary">Save</button><button class="btn btn-sm btn-ghost">Cancel</button></span></td>
</tr>
```

States:

| State | Look (never colour alone) |
|---|---|
| `td.is-editable` | Text cursor. Dotted underline on hover and focus (desktop). On touch tiers a pencil glyph after the text. |
| `td.is-editing`, `tr.is-editing > td` | The `.input`/`.select`/`.textarea` fills the cell: the cell's padding moves onto the control (less its border), same font and line height, `field-sizing: content`. A text or number editor causes no row-height or column-width jump. A select's arrow and a date input's picker icon need about 1.5em more, so those columns may widen slightly; give the column a width (`<col>` or a `th` width) if it must not move. On touch devices editors are 16px (iOS zoom), inside rows already 44px tall. |
| `tr.is-editing` | Accent tint on every cell and a leading marker bar. |
| `.is-dirty` | Warning tint plus a bar on the cell's leading edge. |
| `.is-saving` / `.htmx-request` | Dimmed text plus a spinner (spins only with motion allowed). |
| `.is-saved` | Success tint plus a tick; the tint flashes then settles (motion allowed). |
| error | `aria-invalid="true"` on the control (or the `td`): a 2px danger ring and tint on the cell, core's invalid input look, and the `.field-error` text below the control (the row grows by one line). |
| `.is-readonly` | Muted text, arrow cursor, no underline or pencil. In a `role="grid"` table use `aria-readonly="true"` instead (also styled); it is not allowed on a plain `<td>`. |
| `td[tabindex]` | Focus ring drawn inside the cell (not clipped by `.table-wrap`), for spreadsheet-style arrow-key navigation. |

Dropdown, date and combobox in a cell:

- A native `<select>`, `<input type="date">` or `<input list>` + `<datalist>`
  opens OS UI, which no scroller can clip.
- A custom list: give it `popover` so it sits in the top layer. Where anchor
  positioning is supported it opens under its own cell, at least as wide as
  the cell; elsewhere core centres it.
  ```html
  <td class="is-editing">
    <button class="select" popovertarget="city" aria-haspopup="listbox">Faro</button>
    <div class="dropdown" popover id="city" role="listbox">…</div>
  </td>
  ```
  (An `<input role="combobox">` opening the list with `showPopover()` works the same.)

Tokens:

| Token | Default |
|---|---|
| `--cell-editable-underline` | `var(--muted)` |
| `--cell-edit-glyph` / `--cell-edit-glyph-fg` | `"\270E"` (✎) / `var(--muted)` |
| `--cell-input-bg` | `var(--input-bg, var(--surface))` |
| `--cell-input-radius` | `0` |
| `--cell-editing-border` | `var(--accent)` |
| `--row-editing-bg` / `--row-editing-marker` | accent 8% / `var(--accent)` |
| `--cell-dirty-bg` / `--cell-dirty-marker` | warning 14% / `var(--warning)` |
| `--pending-opacity` (saving text), `--indicator-fg` / `--indicator-track` (spinner) | core values (`--pending-opacity` defaults to 0.8 so saving text keeps 4.5:1 in most themes) |
| `--cell-saved-bg` / `--cell-saved-flash` / `--cell-saved-glyph` / `--cell-saved-fg` | success 14% / success 35% / `"\2713"` / `var(--success-text)` |
| `--cell-error-bg` / `--cell-error-border` | danger 10% / `var(--danger)` |
| `--cell-readonly-fg` | `var(--muted)` |

Touch and accessibility:

- `dblclick` is unreliable on touch: open the editor on tap of an
  `.is-editable` cell on touch tiers. Editable, editing and focusable cells
  are at least `--tap-min` tall (44px on touch).
- Label every editor (`aria-label` or `aria-labelledby` to the column
  header). Link `.field-error` with `aria-describedby`; add `role="alert"`
  when it is injected.
- For a full spreadsheet, use `role="grid"` on the table and move focus with
  the arrow keys; Enter opens the editor, Esc cancels.
- Set `aria-busy="true"` on a saving cell.

---

## Tables on small screens

**Default: scroll sideways with the first column frozen.**

```html
<div class="table-wrap" tabindex="0" role="region" aria-label="Station readings">
  <table class="table">…</table>
</div>
```

The first column of a table in a `.table-wrap` stays in view while the table
scrolls. At rest it looks exactly like an unfrozen table; once scrolled it
fills with `--table-bg` and casts an edge shadow (scroll-driven animation
where supported; elsewhere, and under `data-motion="reduced"`, the column is
always opaque). The wrap is also the containing block for absolutely
positioned content (a `.visually-hidden` checkbox name would otherwise escape
it and widen the page). Make the wrap focusable (`tabindex="0"`, a role and a
label) so keyboard users can scroll it.

**Opt-in: stacked cards.**

```html
<table class="table is-stacked">
  <thead><tr><th>Ticket</th><th>Status</th></tr></thead>
  <tbody>
    <tr><td data-label="Ticket">#4821</td><td data-label="Status" class="is-editable">Pending</td></tr>
  </tbody>
</table>
```

At 480px and below (of the nearest `.modal`, `.drawer` or `.cq` container,
or of the viewport when there is none), each row becomes a card and each
cell shows its column name from `data-label` beside the value. The header
stays in the accessibility tree (visually hidden). Editable cells keep every
state; a selected row's labels follow `--row-selected-fg` (or the cell text colour). A stacked table is
not frozen. Rows with `hidden` stay hidden.

| Token | Default |
|---|---|
| `--table-card-bg` / `--table-card-border` / `--table-card-radius` | `transparent` / `var(--border)` / `var(--radius)` |
| `--table-label-size` | `38%` (label column) |
| `--table-label-fg` | `var(--table-head-fg, var(--muted))` |

Note: `display: block` on table parts removes table semantics in some
browsers (older Safari). If that matters, add `role="table"`, `row`, `cell`
and `columnheader` to the markup.

---

## Frozen columns

```html
<div class="table-wrap scroll" style="--scroll-max: 20rem">
  <table class="table is-frozen-2 is-sticky">…</table>
</div>
```

- `.is-frozen-1` freezes the first column in any scroller (not only a
  `.table-wrap`), with a hairline edge.
- `.is-frozen-2` freezes the first two. The first must be a narrow column
  (a selection checkbox) of width `--table-frozen-1-size` (default
  `calc(var(--tap-min) + 1.5rem)`); set it if your first column is wider.
- With `.is-sticky` the top-left header cells stay above both the sticky
  header and the frozen body cells.
- Row hover, stripes, selection and active state show on frozen cells too
  (mirrored from core's row tokens), and theme row markers (`box-shadow`) are
  kept.

| Token | Default |
|---|---|
| `--table-bg` | `var(--surface)` (opaque!) |
| `--table-frozen-edge` | `var(--hairline)` |
| `--table-frozen-shadow` | `rgb(0 0 0 / 0.4)` |
| `--table-frozen-1-size` | `calc(var(--tap-min) + 1.5rem)` |

---

## Column resize and reorder

```html
<th class="is-resizable" draggable="true" aria-sort="ascending">
  Name
  <span class="table-resizer" role="separator" aria-orientation="vertical"
        aria-label="Resize Name column" aria-valuenow="180" tabindex="0"></span>
</th>
```

- `th.is-resizable` draws a grip on its trailing edge (a `col-resize`
  strip `--tap-min` wide with a 2px line). Add the focusable `.table-resizer`
  for keyboard resizing (arrow keys, handled by the app); it replaces the
  drawn grip. `.is-resizing` on the `th` while dragging.
- `th[draggable="true"]` gets the grab cursor. While dragging, `.is-dragging`
  on the source column's cells (a dashed outline; `--table-drag-opacity` dims them, default 1 so header text keeps its contrast) and `.is-drop-before`
  / `.is-drop-after` on the target column's cells (a 3px accent bar). The
  browser draws the drag ghost.

| Token | Default |
|---|---|
| `--table-resizer-fg` / `--table-resizer-fg-active` | `var(--hairline)` / `var(--accent)` |
| `--table-resizer-size` | `var(--tap-min)` |
| `--table-drop-marker` | `var(--accent)` |

Touch: header cells with a grip are `--tap-min` tall; native drag and drop
on touch needs a long press.

---

## Row groups

```html
<tbody class="table-group">
  <tr class="table-group-header"><th colspan="3" scope="rowgroup">
    <button class="table-toggle" aria-expanded="true">Europe <span class="badge">3</span></button>
  </th></tr>
  <tr><td>Lisbon</td><td>48</td><td>€412,000</td></tr>
  <tr class="table-group-total"><th scope="row">Europe total</th><td>195</td><td>€1,790,700</td></tr>
</tbody>
```

`aria-expanded="false"` on the toggle collapses the group's rows (the totals
row stays). The app flips the attribute. `.table-toggle` is a bare button
with a rotating caret, `--tap-min` tall.

| Token | Default |
|---|---|
| `--table-group-bg` / `--table-group-fg` | `var(--surface-2)` / `var(--text)` |
| `--table-total-border` | `var(--border)` |
| `--table-toggle-glyph` / `--table-toggle-fg` | `"\25B8"` (▸) / `var(--muted)` |

## Tree rows

```html
<table class="table" role="treegrid">
  <tr data-level="1" aria-expanded="true"><td><button class="table-toggle" aria-expanded="true">src</button></td>…</tr>
  <tr data-level="2"><td>core.css</td>…</tr>
</table>
```

`data-level` (or `aria-level`) 1–7 indents the first cell by
`--table-indent` (1.25rem) per level; leaf rows line up with their siblings'
text. The app hides a collapsed branch's rows with `hidden`.

---

## Selection column and bulk-action bar

```html
<div class="bulk-bar" role="toolbar" aria-label="Bulk actions">
  <span class="bulk-bar-count" aria-live="polite">2 selected</span>
  <button class="btn btn-sm">Archive</button>
  <button class="btn btn-sm btn-danger">Delete</button>
  <button class="btn-close" aria-label="Clear selection"></button>
</div>
<div class="table-wrap">
  <table class="table">
    <tr class="is-selected" aria-selected="true">
      <td><label class="check"><input type="checkbox" class="checkbox" checked><span class="visually-hidden">Select</span></label></td>…
```

- Rows select with core's `tr.is-selected` (add `aria-selected` in a grid).
- A checkbox-only first column shrinks to its content; a labelled row
  checkbox gets a `--tap-min` wide target at every tier.
- A `.bulk-bar` placed before its table (or the table's `.table-wrap`) is
  shown only while a row in that table is selected. Placed anywhere else,
  the app shows and hides it. The app writes the count.

| Token | Default |
|---|---|
| `--bulk-bar-bg` / `--bulk-bar-fg` / `--bulk-bar-border` | accent 14% over surface / `var(--text)` / `var(--accent)` |
| `--bulk-bar-pad` / `--bulk-bar-radius` | `var(--space-2xs) var(--space-s)` / `var(--radius)` |

---

## Loading, empty and load-more

```html
<table class="table is-loading" aria-busy="true">…rows…</table>

<tr class="table-empty"><td colspan="3"><div class="empty-state">…</div></td></tr>

<tr class="table-more"><td colspan="3"><span class="spinner" aria-hidden="true"></span>Loading more…</td></tr>
```

- `.table.is-loading` hides every body cell's content and draws a skeleton
  bar in its place (varying widths), keeping row sizes; it shimmers with
  motion allowed (`--skeleton-bg`).
- `.table-empty` holds core's `.empty-state`; no hover or stripe.
- `.table-more` is the infinite-scroll row: centred, muted, no hover. Use it
  with htmx's `hx-trigger="revealed"`, or put a "Load more" button in it.

---

## Density

`.table.is-compact` (padding `max(var(--space-2xs), 0.25em)` × `0.5em`) and
`.table.is-comfortable` (`0.85em` × `1em`), both times `--density`, so they
follow a theme's density and the user's `data-density`. Editors in cells
follow the same padding.

---

## Table in a modal

```html
<div class="modal modal-lg" popover id="totals">
  <div class="modal-header">Monthly totals <button class="btn-close" …></button></div>
  <div class="table-wrap"><table class="table is-sticky">…</table></div>
  <div class="modal-footer">…</div>
</div>
```

A `.modal` whose direct child is a `.table-wrap` becomes a flex column: the
header and footer stay put, the wrap is the scrolling body (both axes), and
the sticky header sticks to its top. Widths follow the modal size. The rule
has zero specificity and applies only while the modal is shown, so
`.is-minimized`, closed popovers and dialogs, and theme rules still win.
A table placed directly in the modal (no wrap) keeps v4 behaviour: the whole
modal scrolls and core's `--sticky-top` handles the header.
