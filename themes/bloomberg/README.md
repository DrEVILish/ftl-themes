# Bloomberg Terminal

> Black-and-amber data density in the terminal's narrow screen sans.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

**The financial data terminal look**: amber-on-black narrow sans at
maximum density, function-key yellow, and a second cyan data category —
built for scanning a wall of numbers fast, not for looking friendly. This
is the catalog's extreme-density stress test as much as a period theme.

## Core values

1. **The screen's narrow sans, tabular figures.** `--font` is Share
   Tech, a narrow proportional sans like the modern terminal's labels,
   names, headers and figures ('British Pound Spot Curncy', 'DOW JONES'
   in `EngineeringValue_EP3_Preview.webp`), with `tabular-nums` so columns
   of figures align. `--font-mono` (Share Tech Mono) stays for code and
   readouts. An all-mono UI reads as a retro clone, not the real screen.
2. **Amber is the workhorse, yellow is the function key.** `--text` is
   amber; `--accent` is a brighter function-key yellow reserved for
   interactive elements. Losing that split makes everything read as one
   flat color.
3. **Cyan is the second data category.** `--accent-2` exists so a
   second kind of information (a different data feed, an idle state) can
   be color-coded distinctly from the primary amber — real terminals code
   meaning into color, never decoration.
4. **Density over chrome.** `--density: 0.7` — the tightest theme in
   the catalog on purpose. No decorative rail, minimal padding, a data
   wall rather than a spacious dashboard.
5. **Zero radius, zero gloss.** Every corner is square, including core's
   round defaults (icon buttons, switches, avatars, status dots, slider
   thumbs, carousel dots, `<kbd>` caps); every fill is flat, and skeletons
   blink in steps instead of shimmering. Native checkboxes keep the
   browser's own slight rounding (squaring them would mean redrawing the
   control), and line-chart points stay circles (core draws them as SVG
   `<circle>`). This is a data terminal, not a consumer app.
6. **Color by role, like the screen.** Labels and names are amber, data
   values (`.stat-value`, `td.mono`) are terminal white `#e8e8e8` except
   up/down cells, which keep the green-up / red-down net-change colour;
   column headers are mixed-case light grey `#c8c8c8` at data size on a
   grey `#2a2a2a` bar, and panel/modal headers are the crimson `#800414`
   section bar (sampled from the reference, rgb 129,4,19) with white text.
7. **Amber window frames.** Panels, modals and desktop windows carry the
   terminal window's thin amber outer frame (`#cc7a00`); inputs, cards and
   hairlines stay grey `#3a3a3a`.

## Signature details

- Buttons are outlined amber-on-black at rest and invert to filled yellow
  with black text on hover — the terminal function-key press.
- Table cells get vertical rules between columns (`border-right`) and no
  visible horizontal row rules (`--table-rule: #0a0a0a`, 1.1:1 on black):
  the terminal's column grid, not boxed cells.
- The status strip text is cyan, not amber — a second information channel,
  distinct at a glance from the primary data color. The colored
  function-key strip sits in its flow (not over its text), and is left off
  taskbars so it never covers the Start button.
- Grouped buttons (`.btn-group`) are filled function-key caps at rest:
  green navigation keys with black text, the selected/primary one yellow,
  like the reference's MSG / PgFd / PgBk row.
- `.btn-go` is the keyboard's filled green `<GO>` key with black text.
- The app bar's nav and menubar items are the same green key caps with
  black text (yellow when hovered, focused or current), the reference's
  MSG / PgFd / PgBk row across the top of the window. Vertical nav lists
  (rails, mail folders) are amber text rows with only the selected one a
  yellow cap, so green caps stay a horizontal key row.
- Focus is white (`--focus: #ffffff`), so cyan stays a data colour and
  yellow the function key.
- Badges never drop under 12px (`max(0.75em, 0.75rem)`).
- Dropdowns (`.select`) are filled amber fields with black text and a
  black arrow, like the reference's "Standard" select (about 10:1).
- Data rows are tight (`0.25rem` block padding, the 4px edge floor, line-height 1.25) and
  panels inset only `0.25rem`, so grids run nearly edge to edge under the
  red section bar.
- Screen titles are small and regular weight (h1 1.3rem, h2 1.1rem,
  h3 1rem): the terminal sets titles at about the size of the data.
- Sliders draw a dim-amber `0.3rem` track (`#8a5c00`, 3.6:1 on black)
  under a square 1rem yellow block-cursor thumb, inside core's full
  `--tap-min` hit area.
- Chart series 3 is the function-key purple `#b05cff` (the key at the
  right of the reference's zoomed row), since `--warning` equals
  `--accent` and would repeat series 1.

## Layout

The shell becomes a **data wall**: a thin 1.8rem function-key bar, no
rail at all (density wins over chrome), and a status strip that
reads as another data row rather than a conventional status bar.

## v5 layout

- **Tiers.** No tier draws a rail (no reference shows a vertical key
  strip); the function-key row is the bar's key caps and the status
  strip. On phone the bar's gaps tighten and the bar's select narrows to
  8.5rem so brand plus nav take one line and the actions one more.
- **XL gutter art.** More of the data wall, out of focus: rows of dim amber
  readout cells on the terminal's row rules, like neighbouring monitors on
  a trading floor. Still, and within about 1.3:1 of black.

## Tell-tales of an inauthentic result

- A wide or all-monospace UI face (the clone look), or proportional
  figures that make columns of numbers jitter.
- Rounded corners or a gradient/gloss fill on any control.
- Generous padding or a spacious, low-density layout — this theme should
  feel cramped by this catalog's normal standards, deliberately.
- Cyan and amber used interchangeably instead of coding distinct meaning.

## Don'ts

- **No wide or decorative face.** Keep the narrow screen sans with tabular figures; do not add letter-spacing.
- **No rounded corners, gradients or gloss.** `--radius: 0`.
- **No spacious layout.** Do not raise `--density` above `0.7` to be friendly.
- **No decorative colour.** Amber, yellow and cyan each mean something; do not use cyan as an accent for buttons or amber for a second category.
- **No green/red for good/bad as body colour.** Green and red live in the function-key strip and state lamps, not in prose.

## Typography

`--font` is `"Share Tech", "Arial Narrow", "Roboto Condensed", "Liberation Sans Narrow", sans-serif` with `font-variant-numeric: tabular-nums` on the body; `--font-mono` is `"Share Tech Mono", Consolas, "Liberation Mono", monospace` for code and readouts. Both Share Tech faces (SIL OFL, already vendored in `assets/fonts/`, Regular only, so bold is synthesized) load on every platform, keeping dense columns, the bar and table-cell inputs the same width everywhere. The real terminal's face is a proprietary screen font that no capture in `references/bloomberg/` lets us name, so Share Tech is a stand-in chosen for the same narrow, slightly squared proportional shape seen in `EngineeringValue_EP3_Preview.webp`. Column headers are mixed case at data size with no tracking, like the reference's 'Index' / '2 Day' / '%YTD' bar.

## Contrast honesty

- **Amber `#ff9900` is the theme's choice.** `RESEARCH.md` gives no hex for the terminal amber, so it is not a measured reference value. It is 9.81:1 on `--bg`, 9.25:1 on `--surface`, 8.6:1 on `--surface-2`: comfortably AA/AAA.
- **`--muted` was lifted.** The dimmer amber `#b36b00` (4.4:1) was under the floor; `#b86e00` (4.97:1 on `--surface`) still fell to about 4:1 on the tinted schedule and unread-notification fills, so shipped `#cc7a00` is 6.35:1 on black and at least 4.8:1 on those tints. Yellow highlight tints (`--mark-bg`, `--mention-self-bg`, comment anchors) are lighter than core's so amber text keeps 4.5:1 on them.
- **Yellow `#ffcc00` (`--accent`)** is 13.9:1 on black and carries black text (`--on-accent`) on filled controls; no deviation. **Cyan `#00ccff`** (second data category) is 10.45:1 on `--surface`.
- **Green GO.** The reference keyboard's `<GO>` key is green (`bloomberg-keyboard-function-keys.jpg`). `.btn-go` and grouped buttons are filled `#2ecc40` with black text (about 10:1); `--accent` stays yellow for primary interaction and the second category is cyan.
- **Lit tints.** Core's 30% yellow mix on lit pads put amber text at 3.99:1, so `--pad-lit-alpha` is 18%; waveform-marker labels are white on their tint. Muted text inside the red section bars is lifted to `#f0c8a0`.
- `--danger` `#ff3333` is 5.77:1 on black.

## Reference status

`references/bloomberg/` has 4 captures plus `RESEARCH.md`. `bloomberg-keyboard-function-keys.jpg` (real keyboard, red/yellow/green function-key rows, green GO key) backs the function-key strip and the colour-coded `<kbd>`. `EngineeringValue_EP3_Preview.webp` backs amber-on-black screen type and the function-key row; its red section bar was sampled at rgb(129,4,19) and its header text at `#c8c8c8`. `images.jpg` is a third-party dense data-grid dashboard, and `1_ka17MqtycuFqVq5i28WB2w.png` is a third-party clone ("FincepT Terminal"), not real Bloomberg — the weakest of the set per `RESEARCH.md`. The amber and key colours are not sampled values.

## Icons

`themes/bloomberg/icons.svg` redraws the 178 core glyphs as blocky
character-cell glyphs; the extended (Tabler-batch) set inherits core and
keeps its curves:

- 24×24 grid, line only: no fills, colour from `currentColor`; weight comes
  from the theme's global `--icon-stroke-width: 1.4`, never per symbol.
- Every symbol wraps its paths in `stroke-linecap="square"` +
  `stroke-linejoin="miter"`.
- Zero curves: no `<circle>`, no arc/bezier commands. Circles become plain
  squares, arcs become straight or pixel-staircase runs, boxes are plain
  right-angle rects (no rounding, no chamfers).
- Dots are 1×1 stroked squares; weather icons reuse the two-rect cloud.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
