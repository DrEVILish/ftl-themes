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
   blue-slate (`#17252b`, sampled `#1e2e33` under set light), and the room
   around them is near-black (`#070b0d`). Do not use pure black panels
   and do not use neon on black.
2. **Cyan is the ink.** One cyan (`#4fc8dc`) draws outlines, active
   states, table heads and panel titles. Lime (`#a5d65a`) is reserved for
   values (the vitals readout's HR 111 and the dial's outer bars), and
   it serves as the second chart series.
3. **Condensed caps for every label.** Headings, buttons, tabs, nav,
   table heads, badges and panel headers are set in a condensed
   DIN-like face (Antonio), uppercase. Body copy is a plain sans, because
   the tablets never set paragraphs.
4. **Values in brackets.** Badges read `[14]`, `[PAID]` and
   `[LIVE]`, like the matrix's `[14] BULK APPERCEPTION` and the phone's
   `SECTOR [17]`.
5. **Levels are stacks of squares.** Meters, progress bars and chart bars
   are segmented ladders, like the attribute sliders. They are never
   smooth bars.
6. **Outlined caps for buttons.** A button has a 1px cyan-slate outline
   over a faint cyan tint, with a small 0.3rem radius (END / HOLD /
   UPLOAD). Primary buttons are solid cyan. Hover adds a faint glow, and
   nothing else glows at rest.
7. **Red belongs to the room.** Delos red `#c8102e` appears in exactly
   one place: the control room's cove light, drawn as the status strip's
   top rule. Danger states use the separate corrupted-tablet red-orange
   `#ff5a4f`.

## Signature details

- **Tri-fold shell.** The bar, the main area and the rail are separate
  slate panes, rounded on their outer corners, with dark 0.45rem gaps
  between them that read as folds. The main pane has a faint
  centre-fold crease, like the attribute-matrix tablet.
- **Attribute-slider rail on the right.** The rail sits on the right, as
  on the matrix tablet. It is drawn in CSS as three segmented sliders
  (lime, cyan, cyan), lit from the bottom, each with a triangle marker.
  It is empty and `aria-hidden`.
- **DELOS pill brand.** The bar's `.nav-brand` is drawn as an outlined
  pill, like the DELOS wordmark plate on every device.
- **Corner tab on panels.** Each panel has a small filled cyan triangle in
  its top-right corner, and each panel header starts with a short cyan
  rule.
- **Chip tabs.** Tabs and nav items are small rounded chips. The active
  one gets a cyan outline and a cyan tint, like the phone's
  CODE / HOSTS / SATELLITE row.
- **Readouts.** Readouts use Share Tech Mono numerals in cyan with a faint
  glow, like the vitals cluster.

## Typography

| Role | Stack | Why |
|---|---|---|
| Labels | `Antonio` (vendored OFL, `assets/fonts`, shared with lcars), then Bahnschrift SemiCondensed, DIN Condensed, Arial Narrow | The tablets use a condensed DIN-class grotesque. Antonio is the closest free condensed face already in the repo. |
| Body | Helvetica Neue, Helvetica, Arial, Liberation Sans | The Delos security panel (an ARG site) sets body text in a plain geometric or grotesque sans. |
| Mono and readouts | `Share Tech Mono` (vendored OFL, shared with prometheus) | It matches the squared numerals of the vitals and code panes. |

No new font files were added.

## Contrast honesty

All pairs meet the lint floors. No exemptions are claimed.

| Pair | Ratio |
|---|---|
| `--text` `#d6e6ea` on `--surface` `#17252b` / `--bg` `#0f191d` | 12.3 / 13.9 |
| `--muted` `#8eaab2` on `--surface` / `--surface-2` `#1f323a` | 6.4 / 5.4 |
| `--muted` on status strip `#070b0d` | 8.0 |
| `--accent` `#4fc8dc` on `--surface` | 8.0 |
| `--on-accent` `#071014` on accent | 9.7 |
| `--on-danger` on `--danger` `#ff5a4f` | 6.2 |
| `--on-success` on `--success` `#8fd65a` | 10.9 |
| `--danger-text` `#ff7a70` / `--warning-text` `#f2b632` on `--surface` | 6.2 / 8.6 |

`--border` `#3a5c66` is 2.2:1 on the surface. It is used as a structural
line only, never as text.

Deviations from the reference: the cyan in the stills is photographed off
an ambient-lit e-paper prop (sampled `#3f96a6` to `#5c9ba4`). It has been
raised to the brightness the screen would emit. Danger, warning and
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

- **Phone (≤480) and tablet (481–900):** the tri-fold tablet folds shut to one leaf: bar, main, status. The attribute-slider rail is switched off up to 900px (its `--app-rail-empty-display` opt-in outranks core's per-tier rail token). The DELOS wordmark pill hugs its text (`max-width: max-content`) instead of stretching across the bar's first line.
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

`themes/westworld/icons.svg` is the unmodified scaffold. Every icon falls
back to the generic outline set at `--icon-stroke-width: 1.6`, which
already matches the tablets' thin line-work. A custom set could be added
later, based on the phone's tool-tile glyphs (wrench/hammer, hand, gear,
droplet) seen in `references/westworld/mobileTablet-modal-contextMenu-iconBar.jpg`.

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
