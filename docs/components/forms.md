# Forms and buttons (v5)

Source: `core/components/forms.css`. Live examples: `components-forms.html`.
Covers PLAN.md §9 #17–#35. Everything builds on core's `.btn`, `.input`,
`.input-group`, `.toggle-btn`, `.slider`, `.list`, `.progress`, `.context-menu`
and the `[popover]` top-layer rules. Apps provide behaviour; CSS styles every
state.

Shared rules for every component here:

- **Touch.** Every control reaches `--tap-min` (44px up to 900px wide or on any
  coarse pointer, 24px otherwise). Where the visual is smaller (tag remove ×,
  rating stars, swatches) the hit area grows through padding or a positioned
  `::before`, so the look doesn't change.
- **Hover** styles sit inside `@media (hover: hover)` and always have a
  `:focus-visible` (or visible-state) equivalent.
- **Motion** (chevron turn, colour fades) only under
  `prefers-reduced-motion: no-preference` and never with
  `html[data-motion="reduced"]`.
- **No container queries** here: nothing in this group changes layout by
  width beyond wrapping, and the popover-holding components must not be
  containers.
- Tokens below are listed as `token: default`. Set them on `html[data-theme="x"]`
  (inherited) as with every other component.

---

## Transparent button `.btn-clear`

```html
<button class="btn btn-clear">Clear</button>
<button class="btn btn-clear"><svg class="icon"><use href="assets/icons/icons.svg#icon-filter"/></svg> Filter</button>
<button class="btn btn-clear" aria-pressed="true">Pressed</button>
```

No fill, no border and no theme button shadow at rest. Hover and keyboard
focus tint it with the accent; `:active`, `aria-pressed="true"` and
`aria-expanded="true"` use a stronger tint. Unlike `.btn-ghost`, which keeps
the theme's button chrome and hovers to an opaque `--surface-2`.

| Token | Default |
|---|---|
| `--btn-clear-fg` | `var(--text)` |
| `--btn-clear-bg-hover` | `color-mix(in srgb, var(--accent) 16%, transparent)` |
| `--btn-clear-bg-active` | `color-mix(in srgb, var(--accent) 28%, transparent)` |

States: hover, `:focus-visible`, `:active`, `[aria-pressed="true"]`,
`[aria-expanded="true"]`, `:disabled` (core's `.btn` dimming).

Note: a theme that styles `.btn`'s border or shadow with a direct
`html[data-theme] .btn` rule (windows95, lcars) outranks the tokens; such a
theme should add its own `.btn-clear` rule (see "Per-theme notes").

## Transparent icon button `.btn-icon.is-clear`

```html
<button class="btn btn-icon is-clear" aria-label="Edit"><svg class="icon"><use href="assets/icons/icons.svg#icon-edit"/></svg></button>
```

Same tokens and states as `.btn-clear`. Always give it an `aria-label`.

## Icon and label in a button

```html
<button class="btn btn-primary"><svg class="icon"><use href="assets/icons/icons.svg#icon-save"/></svg> Save</button>
<button class="btn">Next <svg class="icon"><use href="assets/icons/icons.svg#icon-arrow-right"/></svg></button>
```

Icon-after is just the markup order. The icon scales with the button's font
size (so `.btn-sm` shrinks it), never grows the line box (icon and text
buttons stay the same height), and sits optically flush with the padding edge
next to it. The same sizing applies to icons in `.toggle-btn`.

| Token | Default |
|---|---|
| `--btn-glyph-size` | `1.15em` |
| `--btn-gap` | `0.45em` (gap between icon and label) |

Decorative icons next to a text label need no `aria-hidden`; `<svg>` without a
title is already ignored by most screen readers, but adding
`aria-hidden="true"` is harmless.

## Split button `.btn-split`

```html
<div class="btn-split">
  <button class="btn btn-primary">Save</button>
  <button class="btn btn-primary btn-split-toggle" popovertarget="save-menu"
          aria-haspopup="menu" aria-label="More save options">
    <svg class="icon"><use href="assets/icons/icons.svg#icon-chevron-down"/></svg>
  </button>
  <ul class="context-menu" role="menu" popover id="save-menu">
    <li><button role="menuitem">Save as…</button></li>
    <li><button role="menuitem">Save a copy</button></li>
  </ul>
</div>
```

The two buttons share one joined border; the toggle's start border is a
divider in `currentColor`. The menu is core's top-layer `.context-menu`, so it
opens beside the toggle (anchor positioning, flipping at the screen edge) and
can't be clipped. The caret turns over while the menu is open (no JS: it reads
`:popover-open`), or when the app sets `aria-expanded="true"` on the toggle.

| Token | Default |
|---|---|
| `--btn-split-divider` | `color-mix(in srgb, currentColor 35%, transparent)` |
| `--btn-split-toggle-pad` | `0.55em` |

Touch: the toggle is at least `--tap-min` wide. Disable both buttons together.

## Floating action button `.fab`

```html
<!-- icon only: add .btn-icon -->
<button class="btn btn-primary btn-icon fab" aria-label="New message"><svg class="icon"><use href="assets/icons/icons.svg#icon-plus"/></svg></button>
<!-- with a label -->
<button class="btn btn-primary fab is-extended"><svg class="icon"><use href="assets/icons/icons.svg#icon-edit"/></svg> Compose</button>
```

Fixed to the end corner (bottom right in LTR), clear of the safe area
(`env(safe-area-inset-*)`; use `viewport-fit=cover` in the viewport meta), at
`--z-sticky`. Modifiers: `.is-extended` (label), `.is-start` (start corner),
`.is-contained` (absolute inside a positioned parent such as a map or panel).
An app with a bottom tab bar or status strip lifts it with
`--fab-offset-block`.

| Token | Default |
|---|---|
| `--fab-size` | `3.5rem` (never below `--tap-min`) |
| `--fab-radius` | `999px` |
| `--fab-shadow` | `0 0.25rem 0.9rem rgb(0 0 0 / 0.35)` |
| `--fab-icon-size` | `1.5em` |
| `--fab-offset-block` | `var(--space-l)` (`--space-m` when contained) |
| `--fab-offset-inline` | `var(--space-l)` (`--space-m` when contained) |

Use one FAB per screen, for the screen's primary action. Icon-only needs an
`aria-label`.

## Toggle group `.toggle-group`

```html
<!-- multi-select: checkboxes -->
<div class="toggle-group" role="group" aria-label="Days">
  <label class="toggle-btn"><input type="checkbox" checked>Mon</label>
  <label class="toggle-btn"><input type="checkbox">Tue</label>
</div>
<!-- single-select: radios sharing a name -->
<div class="toggle-group" role="radiogroup" aria-label="View">
  <label class="toggle-btn"><input type="radio" name="view" checked><svg class="icon">…</svg> List</label>
  <label class="toggle-btn"><input type="radio" name="view"><svg class="icon">…</svg> Grid</label>
</div>
```

Joined `.toggle-btn` labels (all `--toggle-btn-*` tokens apply). State is the
inputs' own `:checked`; focus is drawn on the label from
`:has(input:focus-visible)`. Icon-only items need a `.visually-hidden` name.
Compared with `.segmented` (single choice, `.is-active` buttons) this is
form-native and supports multi-select. Items are at least `--tap-min` square.
The group doesn't wrap; keep it to a handful of items on phones.

## Notification dot and count `.has-badge`

```html
<button class="btn btn-icon is-clear has-badge" aria-label="Alerts, new">…</button>
<button class="btn btn-icon has-badge" data-count="8" aria-label="Messages, 8 unread">…</button>
<button class="tab has-badge" role="tab" data-count="4">Mentions<span class="visually-hidden">, 4 unread</span></button>
```

No `data-count` (or an empty one) draws a dot; otherwise the count is drawn as
a pill (format it yourself: `"99+"`). On buttons it hangs off the top end
corner (on `.btn-icon`, off the glyph, so it doesn't drift when touch tiers
grow the hit area). On `.tab`, `.nav-item`, `.segmented-item`, `.list-item`,
`.dropdown-item` and menu items it sits inline after the label, since those
live in scrollers that would clip a corner badge.

| Token | Default |
|---|---|
| `--has-badge-bg` | `var(--danger)` |
| `--has-badge-fg` | `var(--on-danger)` |
| `--has-badge-ring` / `-ring-width` | `var(--surface)` / `2px` |
| `--has-badge-font-size` | `0.68rem` |
| `--has-badge-dot` | `0.6rem` |
| `--has-badge-x` / `-y` | `-0.3rem` (count), `-0.1rem` (dot) |

Accessibility: the generated count is hidden from assistive tech
(`content: … / ""`); put the count or "new" in the accessible name. The ring
gives the badge a shape edge, so it isn't colour alone.
It uses `::after`; an element whose theme already draws an `::after` (silo's
`.tab`) will need a theme override. On an `overflow: hidden` element such as
`.avatar` the corner badge is clipped: put `.has-badge` on a wrapper.

## Leading icon and clear button `.input-icon`, `.input-clear`

```html
<div class="input-group">
  <span class="input-icon"><svg class="icon"><use href="assets/icons/icons.svg#icon-mail"/></svg></span>
  <input class="input" type="email" placeholder="name@example.com">
  <button class="input-clear" type="button" aria-label="Clear email"></button>
</div>
```

The icon and the clear button overlay the field's own padding, so the field
keeps one border, its radius and its native focus ring; addons and buttons
after it still join as usual (`… .input-clear <button class="btn">Go</button>`).
The clear button hides itself while the field is empty, which needs a
`placeholder` (a space is enough). Clearing the value is app script.

| Token | Default |
|---|---|
| `--input-icon-fg` | `var(--muted)` |
| `--input-icon-w` | `2.5em` |
| `--input-clear-w` | `max(var(--tap-min), 2.5em)` |
| `--input-clear-glyph` | `"\00d7"` (or put an `.icon` inside) |

States: field `:disabled`, `[aria-invalid="true"]`, `.input-sm`/`.input-lg`
work unchanged. Touch: the clear button is the field's full height and at
least `--tap-min` wide; icons follow the 16px iOS minimum like the field.

## Search field

```html
<div class="input-group">
  <span class="input-icon"><svg class="icon"><use href="assets/icons/icons.svg#icon-search"/></svg></span>
  <input class="input" type="search" placeholder="Search tickets" aria-keyshortcuts="Control+K">
  <button class="input-clear" type="button" aria-label="Clear search"></button>
  <kbd>Ctrl K</kbd>
</div>
```

`type="search"` loses Safari's rounded native look. The shortcut `<kbd>` must
be the group's last child; it hides once the field has focus or a value (the
clear button takes its place). A bare `<input type="search" class="input">`
keeps the browser's cancel button, redrawn in `--input-icon-fg`; it is hidden
when an `.input-clear` follows.

| Token | Default |
|---|---|
| `--input-kbd-w` | `4.5em` (space reserved for the hint) |

## Date picker (native)

```html
<input class="input" type="date" value="2026-10-02">
<input class="input" type="datetime-local">
<input class="input" type="month">
```

The browser's popup calendar follows the theme's `color-scheme`. Core redraws
the picker indicator (Chromium/WebKit) in `--input-icon-fg` (text on hover,
`--focus` while focused) from a mask a theme can replace, colours the date
separators muted, and paints the focused segment (day, month, hour…) with the
accent. Firefox keeps its own indicator.

| Token | Default |
|---|---|
| `--input-date-icon` | a calendar outline (`url("data:image/svg+xml,…")`) |
| `--input-segment-bg` / `-fg` | `var(--accent)` / `var(--on-accent)` |

States: `:disabled`, `[aria-invalid="true"]`, sizes, as for any `.input`.

## Calendar month grid `.calendar`

```html
<div class="calendar" role="group" aria-labelledby="cal-title">
  <div class="calendar-header">
    <button class="btn btn-icon is-clear btn-sm" aria-label="Previous month">…</button>
    <h4 class="calendar-title" id="cal-title" aria-live="polite">October 2026</h4>
    <button class="btn btn-icon is-clear btn-sm" aria-label="Next month">…</button>
  </div>
  <table class="calendar-grid">
    <thead><tr><th scope="col" abbr="Monday">Mo</th>…</tr></thead>
    <tbody>
      <tr>
        <td><button class="calendar-day is-outside" aria-label="28 September">28</button></td>
        <td><button class="calendar-day" aria-current="date">2</button></td>
        <td class="is-range-start"><button class="calendar-day" aria-pressed="true">12</button></td>
        <td class="is-in-range"><button class="calendar-day">13</button></td>
        <td class="is-range-end"><button class="calendar-day" aria-pressed="true">16</button></td>
        <td><button class="calendar-day" disabled>17</button></td>
      </tr>
    </tbody>
  </table>
  <div class="calendar-footer"><button class="btn btn-clear btn-sm">Today</button>…</div>
</div>
```

For apps that render their own picker. Day state lives on the button:
`aria-current="date"` (today: ring + bold), `aria-pressed="true"` (or
`aria-selected="true"`: accent fill + bold), `disabled` (muted + struck
through), `.is-outside` (another month, muted). Range state lives on the
`<td>` so the band runs through the cells: `.is-range-start`, `.is-in-range`,
`.is-range-end` (RTL mirrored). Inside a `.popover` the calendar drops its own
frame:

```html
<button class="btn" popovertarget="cal-pop" aria-label="Choose date">…</button>
<div class="popover" popover id="cal-pop"><div class="calendar">…</div></div>
```

| Token | Default |
|---|---|
| `--calendar-bg` / `-fg` | `var(--surface)` / `var(--text)` |
| `--calendar-border` / `-border-width` | `var(--border)` / `1px` |
| `--calendar-radius` | `var(--panel-radius, var(--radius))` |
| `--calendar-pad` | `var(--space-s)` |
| `--calendar-day-size` | `2.25em` (never below `--tap-min`) |
| `--calendar-day-radius` | `var(--radius)` |
| `--calendar-day-bg-hover` | `var(--surface-2)` |
| `--calendar-weekday-fg` | `var(--muted)` |
| `--calendar-outside-fg` | `var(--muted)` |
| `--calendar-today-ring` | `var(--accent)` |
| `--calendar-selected-bg` / `-fg` | `var(--accent)` / `var(--on-accent)` |
| `--calendar-range-bg` | `color-mix(in srgb, var(--accent) 22%, transparent)` |

Touch: days are `--tap-min` square (7 × 44px = 308px fits a 393px phone in a
popover). Keyboard: the app moves focus between day buttons with the arrow
keys (APG date picker pattern) and updates `aria-live` on the title.

## Time picker (native)

```html
<input class="input" type="time" value="09:30">
<input class="input" type="time" step="1">
```

Styled like the date input; the indicator is a clock (`--input-time-icon`).

## Date range

```html
<div class="input-group" role="group" aria-labelledby="stay-label">
  <input class="input" type="date" aria-label="Check-in">
  <span class="input-addon" aria-hidden="true">→</span>
  <input class="input" type="date" aria-label="Check-out">
</div>
```

Plain `.input-group`; native date/time inputs in a group may shrink below
their intrinsic width, so two fit side by side on a phone. Pair with a
`.calendar` range for an app-rendered picker. An `.input-icon` may lead.

## Combobox `.combobox` and `.listbox`

Native:

```html
<input class="input" list="cities"><datalist id="cities"><option value="Berlin">…</datalist>
```

The list indicator is a chevron in `--input-icon-fg` (`--input-list-icon`); the
suggestion popup itself is browser chrome.

App-rendered:

```html
<div class="combobox">
  <input class="input" role="combobox" aria-expanded="true" aria-controls="lb"
         aria-autocomplete="list" aria-activedescendant="o2" placeholder="City">
  <ul class="listbox" role="listbox" id="lb" popover="manual" aria-label="Cities">
    <li role="option" id="o1" aria-selected="true"><mark>Be</mark>lgrade</li>
    <li role="option" id="o2" class="is-active"><mark>Be</mark>rlin</li>
    <li role="option" id="o3" aria-disabled="true">Beijing</li>
    <li class="listbox-empty" role="presentation" hidden>No cities match.</li>
  </ul>
</div>
```

With `popover` (open it with `showPopover()` on focus or input) the list lives
in the top layer, anchored under the field and as wide as it, flipping above
near the bottom of the screen; without anchor positioning it opens centred.
Without `popover`, it drops below the field in flow (`--z-dropdown`), which an
`overflow` ancestor can clip. Option states: `.is-active` (the
`aria-activedescendant` one: accent fill), `[aria-selected="true"]` (bold +
check mark), `[aria-disabled="true"]` (muted), hover. `<mark>` highlights the
matched text (bold + underline, no colour). `.listbox-empty` is the
no-results line. `.listbox` also works on its own as a select-like list.

| Token | Default |
|---|---|
| `--listbox-bg` | `var(--dropdown-bg, var(--surface-2))` |
| `--listbox-fg` | `var(--text)` |
| `--listbox-border` / `-border-width` | `var(--dropdown-border, var(--border))` / `1px` |
| `--listbox-radius` | `var(--dropdown-radius, var(--radius))` |
| `--listbox-shadow` | `var(--panel-shadow, …)` |
| `--listbox-pad` | `0.3rem` |
| `--listbox-max` | `16rem` (then it scrolls) |
| `--listbox-option-bg-active` / `-fg-active` | `var(--dropdown-item-bg-hover, var(--accent))` / `var(--dropdown-item-fg-hover, var(--on-accent))` |
| `--listbox-option-bg-hover` | `var(--row-hover-bg, …)` |
| `--listbox-check-glyph` | `"\2713"` |

Touch: options are `--tap-min` tall.

## Tag input `.tag-input` and `.tag`

```html
<div class="tag-input">
  <span class="tag">Design<button class="tag-remove" type="button" aria-label="Remove Design"></button></span>
  <span class="tag is-accent">Priority<button class="tag-remove" type="button" aria-label="Remove Priority"></button></span>
  <input class="tag-input-field" aria-label="Add a label" placeholder="Add a label…">
</div>
```

Looks like an `.input` (same `--input-*` tokens) and shows the focus ring while
anything inside has focus. Chips wrap; long chip text breaks anywhere. App
script turns Enter/comma into a chip, Backspace on an empty field into removing
the last one, and focuses the field when the box is clicked. States:
`aria-invalid="true"` (or `.is-invalid`) on the field reddens the box;
`disabled` on the field dims it. `.tag` works on its own as a static chip.

| Token | Default |
|---|---|
| `--tag-bg` / `-fg` | `var(--surface-2)` / `var(--text)` |
| `--tag-border` / `-border-width` | `var(--border)` / `1px` |
| `--tag-radius` | `var(--radius)` |
| `--tag-remove-fg` | `var(--muted)` |
| `--tag-remove-bg-hover` | `color-mix(in srgb, var(--danger) 20%, transparent)` |

Touch: the field is `--tap-min` tall; the × keeps its small look and gets a
`--tap-min` hit area from a positioned `::before`.

## Number stepper `.stepper`

```html
<div class="input-group stepper" role="group" aria-label="Guests">
  <button class="btn btn-icon" type="button" aria-label="Fewer guests"><svg class="icon"><use href="assets/icons/icons.svg#icon-minus"/></svg></button>
  <input class="input" type="number" value="2" min="1" max="12" aria-label="Guests">
  <button class="btn btn-icon" type="button" aria-label="More guests"><svg class="icon"><use href="assets/icons/icons.svg#icon-plus"/></svg></button>
</div>
```

Built on `.input-group`'s joins, shrink-wrapped. The native spin buttons are
hidden; the − / + buttons are square and at least `--tap-min`. Disable a
button at the limit. An `.input-addon` (unit) may sit between field and +.

| Token | Default |
|---|---|
| `--stepper-btn-size` | `2.4em` (never below `--tap-min`) |
| `--stepper-input-w` | `4.5em` |
| `--stepper-radius` | `var(--input-radius, var(--radius))` |

## Dual-handle range slider `.slider.is-range`

```html
<div class="slider is-range" role="group" aria-labelledby="price" style="--from: 20; --to: 75">
  <input class="slider" type="range" min="0" max="100" value="20" aria-label="Minimum price">
  <input class="slider" type="range" min="0" max="100" value="75" aria-label="Maximum price">
</div>
```

Two range inputs stacked on one track; their thumbs keep core's `--slider-*`
look. `--from` and `--to` (inline value API, percentages 0–100 of the track)
draw the filled band; the app sets them on `input` and keeps the low thumb
below the high one. `:disabled` on the inputs dims the whole control.

| Token | Default |
|---|---|
| `--slider-range-fill` | `var(--accent)` |
| `--slider-height`, `--slider-bg`, `--slider-border`, `--slider-radius`, thumb tokens | as core `.slider` |

Touch: the control is `--tap-min` tall; `touch-action: none` comes from core.
Each input needs its own accessible name. (ponytail: the band runs from thumb
centre to thumb centre in percent; at the extremes it is off by half a thumb.)

## Rating `.rating`

```html
<fieldset class="rating">
  <legend class="visually-hidden">Your rating</legend>
  <label><input type="radio" name="r" value="1"><span class="visually-hidden">1 star</span></label>
  <label><input type="radio" name="r" value="2"><span class="visually-hidden">2 stars</span></label>
  …
</fieldset>
```

Stars up to and including the checked one are filled; hovering previews.
Filled and empty glyphs differ in shape (★ / ☆), not only colour. `disabled`
on the fieldset makes it read-only. A theme (or one instance) can swap the
glyph: `--rating-glyph: "\2665"; --rating-glyph-empty: "\2661"` gives hearts.

| Token | Default |
|---|---|
| `--rating-glyph` / `--rating-glyph-empty` | `"\2605"` / `"\2606"` |
| `--rating-fg` | `var(--warning)` |
| `--rating-empty-fg` | `var(--muted)` |
| `--rating-size` | `1.6em` |

Touch: each label is a `--tap-min` square. Keyboard: arrow keys move between
the radios natively.

## Colour swatches `.swatches`

```html
<fieldset class="swatches">
  <legend class="label">Label colour</legend>
  <label class="swatch" style="--swatch: #2f7cf6"><input type="radio" name="c" value="blue" checked><span class="visually-hidden">Blue</span></label>
  …
</fieldset>
```

`--swatch` is the colour (inline value API). The chosen one gets a ring and a
✓ (shape, not only colour). Checkboxes work too, for multi-select. Disabled
swatches fade. Always give each a colour name.

| Token | Default |
|---|---|
| `--swatch-size` | `1.75rem` (hit area never below `--tap-min`) |
| `--swatch-radius` | `50%` |
| `--swatch-border` | `rgb(128 128 128 / 0.5)` (keeps white/black swatches visible) |
| `--swatch-ring` / `--swatch-gap` | `var(--text)` / `var(--surface)` |
| `--swatch-check-glyph` / `-check-fg` | `"\2713"` / `#fff` with a dark halo |
| `--swatches-gap` | `var(--space-xs)` |

## Upload queue `.file-list`

```html
<div class="dropzone">…</div>
<ul class="list file-list" aria-label="Uploads">
  <li class="is-uploading">
    <svg class="icon" aria-hidden="true"><use href="assets/icons/icons.svg#icon-file-type-pdf"/></svg>
    <span class="list-item-title">report.pdf</span>
    <span class="list-item-meta"><span>2.4 MB</span><span>Uploading · 64%</span></span>
    <progress class="progress" value="64" max="100" aria-label="report.pdf"></progress>
    <button class="btn btn-icon is-clear" aria-label="Cancel report.pdf">…</button>
  </li>
</ul>
```

A `.list` (all `--list-*` tokens apply) whose rows are icon · name/meta/progress
· action. Row states: `.is-queued` (progress kept hidden in place),
`.is-uploading`, `.is-done` (success icon, no bar), `.is-error` (danger icon,
meta and bar, plus an inline-start rule). Write the state in the meta text;
colour only reinforces it. The name truncates with an ellipsis. Follows a
`.dropzone` with a gap.

| Token | Default |
|---|---|
| `--file-icon-fg` | `var(--muted)`; success/danger by state |
| `--progress-fill`, `--list-item-meta-fg` | set per state |

---

## Per-theme notes

- **windows95** (and other bevelled themes) style `.btn`'s border colours
  directly, so `.btn-clear` keeps its bevel. Period-correct: flat at rest,
  raised bevel on hover (IE4 "cool" toolbar buttons).
- **lcars** right/bottom-aligns every non-icon, non-small `.btn` with a large
  min size; use `.btn-icon` for icon-only FABs and stepper buttons (the
  examples do). An extended FAB takes the LCARS pill look.
- Themes with a signature glyph can set `--rating-glyph`, `--swatch-check-glyph`,
  `--listbox-check-glyph` and `--input-clear-glyph`, and swap the date/time
  indicator masks.
