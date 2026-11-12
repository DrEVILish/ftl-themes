# Weyland-Yutani

> Alien-franchise corporate industrial: bone-beige label plates, amber CRT readouts, hazard tape for danger only.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The hardware of a **used-future commercial freighter** as seen in *Alien*
(1979), *Aliens* (1986) and *Alien: Isolation* (2014): warm near-black
steel, off-white equipment plates with stencil-style tracked capitals, and
amber phosphor CRT readouts. The target is a control room built by a
company that only cares about cargo, not a sci-fi HUD. Sources and honest
gaps are in `references/weyland-yutani/RESEARCH.md`. No logo or artwork is
reproduced.

## Core values

1. **Utilitarian, never glossy.** `--radius: 0`, no gradients, no
   bevels, no blurs. Panels are thin flat outlines.
2. **Labels are stencil.** Headings, buttons, table heads, panel titles,
   badges, table status labels, nav (including the settings section list),
   menubar, segmented keys, window titles and the status
   strip are uppercase with wide tracking (`--label-tracking: 0.14em`).
   Headings, panel titles, table heads, tabs, stat labels, title plates
   and the brand are set in Michroma, an extended Microgramma-class face;
   headings, panel titles, title plates and the brand (0.09em, as the
   wordmark is the heaviest line) take a 0.07em text stroke
   painted under the fill (so counters stay open) so they read as the
   Bold Extended plate lettering, and panel titles are in bone `--text`.
   On phones the heading stroke and the glows are dropped (wider tracking
   instead) to keep scrolling inside the frame budget; the brand keeps it.
   Tabs and stat labels take a lighter 0.04em stroke on desktop so they
   match the stroked titles beside them. A list item's subject (the inbox
   column) stays mixed case at 0.02em; only its meta line is tracked caps.
   Tabs inside desktop windows and on phones, and panel-header badges,
   drop to Share Tech: the extended face wrapped those rows (and its `%`
   draws as `o/o`).
3. **Amber is the phosphor, and only readouts glow.** `.readout`, `.meter`
   and stat-tile values (the header rows' values) are in the phosphor with a
   faint 4px glow; only readouts get scanlines and meters are segmented. A readout is
   a boxed counter cell: a lit `--wy-line-hi` outline 1px inside its glass
   frame, after the outlined digit boxes of the Romulus colony contract.
4. **Hazard striping is a danger signal, not a palette.** Yellow/black
   45deg stripes appear on `.btn-danger`, `.alert-danger`, `.toast-danger`,
   `.badge-danger` and `.status-error` only, as a leading strap. Text never
   sits on the stripes.
5. **The beige plate is the one light element.** The app bar, modal title
   bar and tooltips are bone-beige with near-black text, like a riveted
   label plate on dark equipment.
6. **Buttons are chunky caps.** 2px edge, dark underside lip, drops 2px on
   press. Primary is a solid amber block; success is a lit green outline
   on glass black, not a green slab. Icon buttons are square
   (`--btn-icon-radius: 0`), as are the FAB (flat lip, no blur), carousel
   markers, the spinner, the htmx indicator, the busy-button and saving-cell
   spinners, count badges and avatar presence marks (in the small bar
   avatar the mark is shrunk and pushed out past the corner so the initials
   stay clear). Checkboxes and radios are square keys: glass black in a
   `--wy-line-hi` frame, amber with a dark tick when checked; the radio's
   mark is a square block, drawn centred so core's taller target is kept.

## Signature details

- Heavy beige top bar over a 6px amber double rule (the terminals' double
  frame rules), with a matching 4px double rule over the status strip; a 3rem left rail drawn in CSS
  as a ruler of tick marks with an amber marker block (empty, `aria-hidden`).
- Two registration corner marks (top-left, bottom-right) on every panel
  (the top-left one is drawn on the panel header when there is one); a
  solid amber square before each panel title. A second header further down
  a panel (a sub-section) has no plate or mark of its own.
- Stat tiles are the terminals' header rows: muted label stacked over the
  amber phosphor value, over one long double rule in `--wy-line-hi`, with no box
  (both `.card > .stat-value` and `.card > .stat` markup; a `.stat` puts its
  label first).
- Ghost buttons keep a lit `--wy-line-hi` underside lip (amber on hover) so
  they still read as soft keys.
- Segmented LED-style meter bars (amber, then pale amber, then red) with a
  segment gaps (one gradient layer); amber mono readouts on glass-black.
- Selected rows and edited cells are an opaque inverse-video amber
  (`--accent` 22% into `--surface`), not a translucent tint.
- Modals and windows cast a hard 4px machined drop, no blur.
- Modal and window title plates are set small (0.9rem, 0.02em tracking)
  and panel titles track at 0.06em, so titles fit one line; on phones the
  brand shares the bar's first row with the menubar and truncates first,
  keeping the plate to two rows.
- Inputs are recessed with a heavy amber underline and amber caret.
- Slider tracks are drawn in `--wy-line-hi` on the content box (about
  3.2:1 on the bay black), inside core's transparent 24/44px hit area.
- Status strip in tracked micro-caps, its items drawn as a row of
  outlined soft keys like the terminals' function-key row; the first one
  is lit in the accent. The desktop taskbar gets the same outlined soft
  keys (Start and the focused window's key lit in the accent); an unfocused
  window's title bar is an unlit dark plate, the focused one the beige plate.
- The rail's tick ruler is a 0.5rem tile repeated down (cheap to scroll),
  and the rail and meters are paint-contained.

### Variants

The default is the hardware. The variants are the screens, one phosphor
each, from the frames in `references/weyland-yutani/` (see RESEARCH.md).
In every variant the beige plate becomes an inverse-video phosphor band
(modal title, tooltips), the top bar becomes the screen's header row
(phosphor text on black over a phosphor rule), panels get thin phosphor
outlines, and headings and readouts glow. Short UI lines (table cells,
helper text, list items, breadcrumbs) go to tracked caps like the
screens; paragraphs and inputs stay mixed case for reading. Body text is a light tint of the
phosphor and the chart series are phosphor shades; backgrounds are near
black with only a trace of the phosphor, so separation comes from the
phosphor outlines, not tinted fills (a saved cell keeps its tick but
drops the green fill); only the status
colours (success, warning, danger) step outside the screen's hue so they
stay distinguishable.

| Variant | Label | Source |
|---|---|---|
| (default) | Weyland-Yutani | Nostromo / Isolation hardware: beige plates, amber CRT. |
| `mother` | MU/TH/UR (green) | The MU/TH/UR 6000 interface: green phosphor `#4dff7c`. |
| `emergency` | Emergency (red) | The red "ENVIRON CTR / PURGE" and Hyperdyne terminals: red `#ff5640`. Danger moves to hazard yellow `#ffd21f` so it stays distinct from the accent. |
| `earth` | Alien: Earth (cyan) | Kirsh's specimen monitors (2025): cyan `#4fe0ff`. |

### Icons

`themes/weyland-yutani/icons.svg` redraws 187 of core's 1020 icons (the
original core set plus the player transport keys) as blocky, machined
stencil glyphs. Every other icon falls back to core's sprite but takes
square caps and miter joins from a theme-wide `.icon` rule, so its line
ends still read as machined:
- 24 grid, stroke only at 2.2 (`--icon-stroke-width`), with
  `stroke-linecap="square"` and `stroke-linejoin="miter"` on every symbol.
- Radius 0 everywhere. Circles become squares (small) or chamfered octagons
  (r >= 5); curves become straight 45-degree runs (bell, cloud, lock shackle).
  The power arc is the one curve kept.
- Nothing is filled; dots are short square-cap ticks (`v1`).
- `currentColor` only.

## Typography

Reference: an extended Eurostile/Microgramma-class sans (the wordmark) plus
a Helvetica/Futura-like face for signage.

- **Labels** (`--font-label`): the vendored **Michroma** (SIL OFL,
  `assets/fonts/Michroma-Regular.woff2`) under the theme-private family
  `"WY Michroma"`, then Eurostile / Bank Gothic. Used for headings, panel
  titles, table heads, modal and window title plates and the brand. It
  ships one weight, declared as 400-700 so labels never get a faked bold.
- **Body** (`--font`): the vendored **Share Tech** (SIL OFL,
  `assets/fonts/ShareTech-Regular.woff2`, family `"WY Share Tech"`), a
  squared Eurostile-spirited grotesque, then Eurostile / Bank Gothic /
  Helvetica Neue / Arial / Liberation Sans, so no system falls through to
  a wide humanist sans. It has one weight, so body bold (`strong`, `b`,
  list-item titles) is the regular cut with a 0.03em under-painted stroke,
  not the browser's smeared synthetic bold.
- **Mono** (readouts, inputs): the vendored **Share Tech Mono** (SIL OFL,
  `"WY Share Tech Mono"`), a square terminal face close to the MU/TH/UR
  screens, then `"Lucida Console", "DejaVu Sans Mono"`.

The wordmark's striped slogan face is not imitated.

## Contrast honesty

All pairs meet the lint floors; no exemptions are claimed.

| Pair | Ratio |
|---|---|
| `--text` `#e4dcc8` on `--surface` `#17150f` / `--bg` `#0e0d0a` | 13.4 / 14.2 |
| `--muted` `#a89f88` on `--surface` / `--surface-2` `#201d15` | 6.9 / 6.4 |
| `--accent` `#ffb92e` on `--surface` | 10.6 |
| `--on-accent` `#0e0d0a` on accent | 11.3 |
| `--warning-text` `#ffe100` on `--surface` | 13.9 |
| `--on-danger` `#0e0d0a` on `--danger` `#ff5a3d` | 6.3 |
| `--on-success` `#0e0d0a` on `--success` `#8fd16a` | 10.6 |
| `--danger-text` `#ff7a5c` on `--surface-2` | 6.6 |
| beige bar `#d4cbb1` with `#14120d` text | above 11 |

Deviations from the reference: the amber, beige and bone values are
chosen for contrast (the amber leans yellow, toward the CRT in
`terminal-amber-destination.jpg`, with hazard yellow `#ffe100` kept purer) and are not sampled from any source (none gives
official hexes). `--border` `#57503f` is 2.3:1 on the surface, deliberately
a structural line only. Danger is safety red-orange `#ff5a3d`, an addition
of mine; the reference's danger cue is hazard yellow/black, which is
carried by the stripes.

## Layout

The shell becomes a **control room**: slim ruled rail on the left, a
heavy beige label-plate bar with an amber rule, flat content on the warm
black, and a stencil status strip. At phone width the rail collapses per
core's default.

## v5 layout

Tiers: mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (the shell is capped at 1800px and centred, with gutter art beside it).

- **Phone (≤480) and tablet (481–900):** bar, main and status in one column. On phones the plate tightens (less padding and tracking, menubar at 0.8em, tighter tool keys, no keyboard-shortcut hint) so it stacks as three short rows: brand, menubar, and the tools on one line. The 3rem equipment rail is switched off up to 900px (its `--app-rail-empty-display` opt-in outranks core's per-tier rail token).
- **Window caption buttons:** minimise, maximise and close follow the title bar's own ink (`--modal-header-close-fg: currentColor`): dark on the beige plate, muted on an inactive window's dark bar.
- **XL gutters (≥1801):** the bay wall: a ruled plotting grid in `--hairline` with the rail's tick-ruler marks, all in the active screen's line colours, so the MU/TH/UR, Emergency and Earth variants follow. Still.

## Don'ts

- Don't stripe anything that is not a danger state, and don't use hazard
  yellow as a background or accent.
- Don't add rounded corners, shadows (beyond the button lip), gradients or
  glass.
- Don't make green or cyan the default accent; they belong to the
  `mother` and `earth` screen variants. Don't use DOS-style boxes
  (`msdos`) or a dense all-orange terminal (`bloomberg`).
- Don't animate the scanlines or add flicker; keep them static so
  `prefers-reduced-motion` needs no special case.
- Don't put text on the striped strap, and don't add the corporate logo.

## Tell-tales of an inauthentic result

- Amber-on-black with rounded corners and no beige plate: a generic retro
  terminal.
- Hazard stripes across headers, rails or backgrounds: costume, not
  signalling.
- Sentence-case, lightly tracked labels: the stencil voice is gone.
- Glossy bevelled buttons instead of flat caps with a dark lip.
- Heavy glow or CRT curvature on ordinary text.

## Print

Scanline overlays, glow, panel corner marks and the readout/meter dark
backgrounds are neutralised in a small `@media print` block.

## Reference status

Researched from search-result summaries only; several primary pages were
blocked. Verified: wordmark set in Eurostile/Microgramma extended, Ron Cobb
as production designer, CRT terminals with scanlines, Isolation's
deliberate 1970s analogue look. Unverified: exact colours, hazard tape
placement on screen, rocker-switch proportions. See RESEARCH.md.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
