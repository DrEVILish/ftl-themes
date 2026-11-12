# Westworld

> The Delos tablets and Mesa control room from HBO's *Westworld*: cyan line-work on slate e-paper, condensed bracketed labels, segmented attribute sliders.

**Requires: L1.** The theme sets `--app-*` layout properties. At L0 (tokens only) it recolors correctly, but it only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

This is the on-set and VFX interface of the Delos Destinations staff in
*Westworld* (HBO, 2016-2022), as designed by **Chris Kieffer** (video
graphics supervisor; interviewed by Tobias van Schneider on DESK, 2017).
Its main pieces are the folding host tablets (the attribute matrix, the
diagnostic node graph, the keyboard tablet), the field phones and the
glass consoles in the Mesa control room. The target is a quiet corporate
lab tool, not a sci-fi HUD. It uses thin cyan strokes on a dark slate
sheet, with almost no glow, and it uses colour mainly to show values. No
Delos or HBO logo or artwork is reproduced. Sources are listed in
`references/westworld/RESEARCH.md`.

## Core values

1. **Slate e-paper, not black glass.** Surfaces are a desaturated
   grey-slate, evenly lit like the prop (page `#1d2d33`, panels
   `#24363c`, sampled `#1e2e33` / `#263b43` under set light), and the room
   around them is near-black (`#070b0d`). Do not use pure black panels
   and do not use neon on black.
2. **Cyan is the ink.** One steel-cyan (`#5cbbca`, a low-chroma lift of the sampled `#3f96a6`-`#5c9ba4`) draws outlines, active
   states, table heads and panel titles. Lime (`#a5d65a`) is reserved for
   values (the vitals readout's HR 111 and the dial's outer bars), and
   it serves as the second chart series. The chart ramp is cyan, lime,
   node-graph amber, deep teal `#2f8797`, steel grey and dark steel `#6f8c95`, never
   red; chart ticks are cyan condensed caps and an area under a line is
   only a 0.1 wash.
3. **Condensed caps for every label.** Headings, buttons, tabs, nav,
   menubar items, toggle buttons, settings-style nav
   lists, summaries, legends, scrollspy links, table heads, badges and
   panel headers are set in a DIN-class condensed grotesque (DIN Condensed
   where installed, else vendored Barlow Semi Condensed), uppercase.
   Headings, panel titles and buttons are the Medium cut (600), tracked
   only 0.03em, like ATTRIBUTE MATRIX and SECTOR [17]; h1 is 1.7rem.
   700 is kept for the small 12-13px caps. The status strip, taskbar
   items included, is tracked caps too.
   Small caps (table heads, badges, table status text) never drop below
   12px. Dropdown, context-menu and popover titles use the same face in
   mixed case, like the phone's Contact / Message / Connect menu; folder
   trees stay in mixed case, untracked. Body copy is a plain sans, because
   the tablets never set paragraphs.
4. **Values in brackets.** Badges read `[14]`, `[PAID]` and
   `[LIVE]`, like the matrix's `[14] BULK APPERCEPTION` and the phone's
   `SECTOR [17]`. The brackets sit tight on the value, and a badge after
   a panel title sits half a space away from it. Reaction chips and icon
   badges are controls and carry no brackets.
5. **Levels are stacks of squares.** Meters, progress bars and chart bars
   (stacked progress included) are segmented ladders, like the attribute sliders, horizontal and
   vertical alike; meters keep the cyan / lime / red level bands inside
   the squares. They are never smooth bars.
6. **Outlined caps for buttons.** A button has a 1px cyan-slate outline
   over a faint cyan tint, with small chamfered corners (END / HOLD /
   UPLOAD). The primary button, like HOLD, is a cyan outline over a
   brighter tint with cyan text; active segmented items, toggles, filter
   chips, pagination and selected icons use the same tint, never a solid
   cyan fill. Danger and success buttons, and a checked danger toggle
   (UNMUTE), follow the same rule in their own colour (red-orange or lime outline over a faint tint), never a solid
   block. Hover adds a faint glow, and nothing else glows at rest; dialogs
   cast a plain drop shadow and the overlay dims without a blur.
7. **Red belongs to the room.** Delos red `#c8102e` appears in exactly
   one place: the control room's cove light, drawn as the status strip's
   top rule. Danger states use the separate corrupted-tablet red-orange
   `#ff5a4f`.

## Signature details

- **Tri-fold shell.** The bar, the main area and the rail are separate
  slate panes, rounded on their outer corners, with dark 0.45rem gaps
  between them that read as folds. The main pane has a visible
  centre-fold crease (a 25% dark line with a faint highlight), like the
  attribute-matrix tablet.
- **Attribute-slider rail on the right.** The rail sits on the right, as
  on the matrix tablet. It is drawn in CSS (on the empty rail's
  `::before`) as three segmented sliders (lime, cyan, cyan) that run the
  height of the leaf down to the bottom of the first screen, lit from the
  bottom, each with a triangle marker and framed in a thin
  `--ww-line-hi` outlined channel, a faint tick scale down the right edge
  (one tick per segment, a longer one every five, as the matrix's 0-20
  scale), and cyan COORDINATION /
  AGGRESSION / LOYALTY captions reading bottom-up in the gap right of
  each ladder (`::after`, `writing-mode: sideways-lr`). It is empty and
  `aria-hidden`.
- **DELOS pill brand.** The bar's `.nav-brand` is drawn as an outlined
  pill with a second, concentric arc on its right end, like the DELOS
  wordmark plate on every device (no lettering is reproduced). It never
  truncates: on touch tiers it keeps its width and the bar's actions
  wrap below it.
- **Cut corner on panels.** Each panel's outline is chamfered top-right
  (`corner-shape: bevel`, 1.2rem) with a cyan line inside the slant, like
  the ATTRIBUTE MATRIX window. Browsers without `corner-shape` show a
  small filled cyan corner tab instead. Each panel header starts with a
  short cyan rule. Modals and windows are cut top-right and bottom-left,
  like the S2 CORE PERMISSIONS dialog. Cards echo the cut with a smaller
  0.7rem chamfer and no cyan line.
- **Segmented slider track.** `.slider` draws its track as a row of
  cyan-slate squares (`--ww-line-hi`, 4.4:1 on the page) inside the
  `--tap-min` hit box; on a vertical fader the squares stack as rungs.
- **Chip tabs.** Tabs and `.nav` items are small rounded chips, each with
  its own thin slate outline. The active one gets a cyan outline and a
  cyan tint, like the phone's CODE / HOSTS / SATELLITE row.
- **Chevron pills.** Pagination's prev / next are outlined pills with a
  chevron at text size that the pill hugs, like the phone's `< FOCUS >` /
  `< CONTROL ROOM >` column; the disabled pill keeps a slate outline.
- **Readouts.** Readouts use Share Tech Mono numerals in cyan with a faint
  glow, like the vitals cluster (touch tiers drop the glow so scrolling
  stays cheap).

## Typography

| Role | Stack | Why |
|---|---|---|
| Labels | DIN Condensed, Bahnschrift SemiCondensed, DIN 2014 Narrow, then `Barlow Semi Condensed` (vendored OFL, `assets/fonts`, Medium and Bold), Arial Narrow | The tablets use a tight DIN Condensed-style grotesque with straight-sided rounds and a tall x-height. The real DIN faces come first; Barlow Semi Condensed is the closest free DIN-alike (Rajdhani's wide rounded O/C/S read as a game HUD; Antonio was too tall and narrow and read as LCARS), its Medium cut set at 600 for headings, panel titles and buttons, Bold only for small caps. |
| Body | `Titillium Web` (vendored OFL), then Helvetica Neue, Helvetica, Inter, Roboto, Noto Sans, Arial, Liberation Sans | A plain technical grotesque that ships with the theme, so no platform falls through to the wide DejaVu Sans. The Delos security panel (an ARG site) sets body text in a plain grotesque sans. |
| Mono and readouts | `Share Tech Mono` (vendored OFL, shared with prometheus) | It matches the squared numerals of the vitals and code panes. |

Barlow Semi Condensed (Medium and Bold, Latin woff2) was added to
`assets/fonts` with a `NOTICE.md` entry; the other two faces were already
vendored.

## Contrast honesty

All pairs meet the lint floors. No exemptions are claimed.

| Pair | Ratio |
|---|---|
| `--text` `#d6e6ea` on `--surface` `#24363c` / `--bg` `#1d2d33` | 9.8 / 11.1 |
| `--muted` `#9ab6be` on `--surface` / `--surface-2` `#2a3d43` | 5.9 / 5.3 |
| `--muted` on status strip `#070b0d` | 9.2 |
| `--accent` `#5cbbca` on `--surface` / `--surface-2` | 5.6 / 5.1 |
| `.badge-accent` text `#84d5e2` on its chip (20% cyan over surface) | 5.2 |
| `--ww-line-hi` `#5f939f` (slider track, button outlines) on `--bg` / `--surface` | 4.2 / 3.7 |
| Danger button text `#ffaba4` / success `#9fe06a` on their tints (worst case, tint over a lit row) | 5.1 / 5.8 |
| `--on-accent` `#071014` on accent | 8.6 |
| `--on-danger` on `--danger` `#ff5a4f` | 6.2 |
| `--on-success` on `--success` `#8fd65a` | 10.9 |
| `--danger-text` `#ff8f85` / `--warning-text` `#f2b632` on `--surface` | 5.7 / 6.9 |

`--border` `#3f6570` is 2.1:1 on the surface. It is used as a structural
line only, never as text. Inactive chip outlines (`--ww-line-hi` at 50%)
are decoration; the chip's text carries its contrast.

Note on `references/westworld/RESEARCH.md`: its sampled-palette table
(`#17252b`, `#4fc8dc`, `#3a5c66`) and its mention of Antonio for labels
record the first draft. The shipped tokens and faces are the ones in this
README.

Deviations from the reference: the cyan in the stills is photographed off
an ambient-lit e-paper prop (sampled `#3f96a6` to `#5c9ba4`). It has been
raised only partway toward the brightness the screen would emit. Danger, warning and
success are not established in the show's UI as semantic colours. They
are taken from the corrupted S2 tablet (red), the diagnostic node graph
(amber) and the vitals (lime).

## Layout

The shell is a **tri-fold Delos tablet on a dark console**. It has a
rounded bar pane with a 1px cyan rule, and below it the main pane with
the centre crease and the right-hand slider rail. The status strip is the
room itself: near-black, with the red cove-light rule glowing above it.
At phone width the layout drops to a single column and the rail is
hidden.

## v5 layout

Tiers: mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (the shell is capped at 1800px and centred, with gutter art beside it).

- **Phone (≤480) and tablet (481–900):** the tri-fold tablet folds shut to one leaf: bar, main, status. The attribute-slider rail is switched off up to 900px (its `--app-rail-empty-display` opt-in outranks core's per-tier rail token). The DELOS wordmark pill hugs its text (`max-width: max-content`) instead of stretching across the bar's first line, and keeps its full width (`flex: 0 0 auto`) instead of truncating to an ellipsis; the bar's actions wrap below it.
- **Dense tables:** fields in a table cell keep a minimum width (inputs 3rem, selects 6rem), so a wide native date picker makes the table scroll instead of squeezing a Qty field below the tap target.
- **Main-pane foot:** `--app-main-padding` has 4rem at the bottom so open demo menus end above the status strip.
- **XL gutters (≥1801):** the Maze: concentric rings centred on the screen (behind the tablet) and broken by corridors, in a slate barely above `--bg`. Still.

## Don'ts

- Don't make red an accent, and don't use red anywhere except the status
  rule and danger states.
- Don't add scanlines, CRT curvature, flicker or heavy glow. The show's
  UI is clean, flat e-ink.
- Don't round more than about 0.5rem, except the brand pill and avatars.
  Don't use gradients or bevels on buttons.
- Don't set body paragraphs in the condensed face.
- Don't use a smooth fill for meters or progress bars.
- Don't reproduce the DELOS wordmark, the HBO logo or the Vitruvian host
  artwork.

## Tell-tales of an inauthentic result

- Electric cyan on pure black with neon glow everywhere: that is `tron`,
  not Delos.
- Sentence-case labels in a regular-width sans: the tablet voice is gone.
- Badges without brackets, or meters drawn as smooth bars.
- Red used as a theme colour (a red bar or red buttons): that is the
  control room's wall, not the UI.
- A rail on the left drawn as icon tiles: that is the phone, not the
  tri-fold tablet.

## Print

Glows, the main-pane crease, the panel corner tabs and the status-strip
glow are neutralised in a small `@media print` block.

## Icons

`icons.svg` redraws all 178 core-set icons as Delos tablet line-work
(shapes only, no show marks):

- 24 grid drawn at 84% of the box, so every glyph sits in generous
  negative space.
- 1.4 hairline, butt caps, mitred joins, sharp corners; no filled
  surfaces, only tiny marker dots and level bars.
- Large circles (radius 8.5 and up: clock, info, help, globe) are drawn as
  a four-segment dial ring, gaps on the diagonals, like the tablets'
  radial readouts.
- `currentColor` only. Ids outside the core set fall back to the generic
  outline set at `--icon-stroke-width: 1.6`.

## Reference status

Researched from 14 images: 8 stills from DESK's interview with Kieffer,
5 from the Westworld wiki (two S1E6 attribute-matrix frames, the S2
corrupted tablet, a control-room console, and the Delos Security Panel
ARG page), and one Westworld Awakening VR frame (an official HBO game) for the
vertical attribute sliders. The palette is sampled from those frames.
Exact typefaces are unverified, because no production font list has been
published. See `references/westworld/RESEARCH.md`.

## Adoption

The theme sets `--app-*` layout properties (manifest `shellAware: true`).
At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but in the shell's default arrangement rather than its
intended layout. To get the real layout at **L1**, adopt the
`.app`/`-bar`/`-rail`/`-main`/`-status` shell (see CONTRACT.md, "The app
shell" and "Adoption levels").
