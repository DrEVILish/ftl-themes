# Silo

> Apple TV+'s *Silo*: teal phosphor on a cramped CRT in a chunky steel bezel, pale-teal header plates, and yellow-green fills that mean "authorised".

**Requires: L1**. The theme sets `--app-*` layout properties. At L0 (tokens only) it recolors correctly, but you only get the monitor-bezel layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The in-set computer screens of a society that has been allowed only old
technology: the IT department's hard-drive browser, Judicial's Relic
Database, the PACT reproduction terminal and SiloMail (Season 1). The UI
is the regime's paperwork turned into a screen. It is cramped, boxed in and
labelled in tracked caps, and it is shown on CRTs set in heavy painted-steel
housings. Frames, sources and sampled colours are in
`references/silo/RESEARCH.md`. No logos are reproduced.

This is not a generic retro terminal. The screens are **teal** rather than
green or amber, information sits in **outlined boxes with tiny labels**
instead of free text, title bars are **solid pale plates**, and the one
saturated fill is a **yellow-green "granted" band**.

## Core values

1. **Teal is the phosphor.** All text and every line is one teal family
   (`--text #3fd6bd`, `--border #1c8a72`) on black glass. Other hues
   are there to carry meaning, never to decorate. The glass itself is a
   near-neutral black (`--bg #03100e`); the teal cast comes from the text
   and a radial bloom, not the base fill.
2. **Yellow-green fill means granted, selected or primary.** Examples are
   `.btn-primary`, the active segment, switch-on, pagination, progress and
   the bulk-selection bar. It is the reference band's muted sage-lime
   (`--accent #9fca6e`, sampled `#91be6c`..`#95c26f`), not a highlighter.
   It never appears as decoration. Danger and
   success buttons, and a pressed danger toggle, are outlined keys in their
   state colour, not fills.
3. **Pale yellow outline means "this one".** The focus ring, active tab,
   active nav entry (in the app bar and in any in-page `.nav`), a selected
   table row (no side bar, only a faint wash), a selected list row and a
   selected desktop icon or drive all use the yellow box the hard-drive
   browser draws around the highlighted file (`--accent-2 #e6dc8c`), with
   the label turned yellow rather than filled.
4. **Title bars are solid pale-teal plates with dark text.** This covers
   the brand, the bar's control group on desktop, the modal header,
   tooltip and status strip. Nothing else is a
   light surface apart from the yellow-green band.
5. **Everything is boxed and labelled.** A form field is one outlined cell
   with a tiny tracked-caps label at its top-left and a large bare value
   below it, panel titles sit between double rules, and buttons are
   outlined keys.
6. **Amber is for numerals and warnings only.** That means the countdown
   readout digits (`--silo-num`) and `--warning`.

## Signature details

- The whole `.app` is a rounded **steel monitor bezel** (`--silo-bezel` `#2b3832`, the
  reference's grey-green painted steel)
  with the bar, main and status on one piece of CRT glass. On desktop the
  housing is chunky (2.2-2.6rem of steel, 1.6rem outer radius) and the
  glass is recessed in it with a dark 2px lip and 1.1rem corners at the top
  of the bar and the bottom of the status strip.
- The top bar is PACT's header. It sits between **pale-yellow double
  rules**, its nav entries and the top-level entries of a menubar in the
  bar are **auto-numbered `01 02 03`** by a CSS counter in tracked caps,
  the active entry is outlined in pale yellow, and the brand is a
  full-height pale-teal plate ("RELIC DATABASE"). On desktop the bar's
  last control group (picker, search, bell, avatar) is a third plate with
  dark ink behind a dark notch ("SYSTEM / RUN"), so plates frame the top
  of the glass as the status strip frames its bottom.
- The **right-hand rail is the screen's scroll track**: a thumb block over
  tick marks.
- The **status strip is three pale-teal plates** ("DISK 10% RAM 40% ...")
  with dark tracked caps: dark glass notches cut it after the first entry
  and before the last, like the Relic Database's bottom band. State
  colours are re-pointed to dark inks inside it.
- The **bulk-selection bar is the yellow-green SEARCH AUTHORIZATION band**:
  a solid fill with dark tracked caps and dark-outlined keys.
- A `.field` with a label and a control is the **Relic Database field
  cell** ("OBJECT DESCRIPTION / DISPENSER, TOY..."): the outline wraps the
  whole field, the label is 0.68rem tracked caps, the control loses its own
  border and its value is set at 1.15rem. The focused cell's outline turns
  pale yellow, an invalid one turns danger; the control keeps its own focus
  ring and its `--tap-min` height. A bare `<fieldset>` takes the same
  `--silo-field` outline instead of the browser's grey groove.
- Popover, card and empty-state titles and `.value-row` labels are tracked
  caps like every other label. Tabs inside a window or dialog track
  0.06em and scroll sideways instead of wrapping to a second row; tree
  nodes track 0.04em and wrap only between words.
- Panel titles sit between 3px double rules with an `×` at the right
  ("RELIC/SEIZED OBJECTS INVENTORY").
- `.btn-primary` is the yellow-green band plus the SEARCH key's outer
  pale-yellow frame.
- Tabs are outlined soft keys with a `›` cue (PACT's MESSAGE / CONTACTS row);
  a tab that already carries a close or icon key takes no cue. On a phone a
  tab row that scrolls fades at its far edge until scrolled to the end.
- Readouts are PACT countdown pills: a rounded teal outline and amber
  numerals with a faint glow.
- Progress, meters and bar charts are hatched yellow-green like the
  CAPACITY bar; the alternate bar is the same hatching in teal.
- Sliders draw their track as a teal rule (`--border`) with the pale
  yellow thumb; the hit area stays the core's `--tap-min` box.
- `kbd` uses the beige keycaps of the pull-out keyboards.
- Static scanlines and a vignette on near-black glass, with the teal cast
  in a radial bloom (`--silo-haze`). Titles and big stat values glow; body
  copy, tables and lists do not. On a phone the scanlines, haze, vignette
  and all glows are dropped, which keeps scrolling cheap.
- Check boxes and radios are outlined cells on the glass (`--border`);
  checked is the yellow-green fill with a dark tick, a radio a square pip.
- At phone width the bezel is 0.8rem and the bar is two rows: the
  full-height brand plate (truncating if it must) shares the first with the picker and actions, the search key
  drops its label and keyboard hint, and the numbered nav is the second.

## Variants

| Variant | Label | Source |
|---|---|---|
| (default) | Silo | Season 1 IT, Judicial and PACT terminals (teal). |
| `legacy` | The Legacy (gold tablet) | Territory Studio's Season 2 Legacy tablet: gold `#f2b84b` on warm black. Not a CRT: no bezel, plates, scanlines or double rules. A hairline gold frame, warm bokeh glow, a cream pill brand ("LIBRARY INTEL UNIT"), nav numbers in circular nodes, panel titles on a single 1px rule with a ring glyph, pill tabs, badges and readouts, circular pagination, field cells reduced to an underline, the status strip as small tracked mono labels in the margin, the scroll-track ladder replaced by one hairline with a vertical mono edge label ("STRUCTURE 02.45"), and stat labels, field labels, header cells and badges in the typewriter mono. References in `references/silo/legacy/`. |

## Typography

Oxanium (UI, headings, plates and field values; a Latin subset of its
400-700 weight axis) and Share Tech Mono (readouts, data) are vendored in
`assets/fonts/` under SIL OFL (see `assets/fonts/NOTICE.md`). The show's
squared, round-cornered all-caps techno face has not been identified;
Oxanium has the same rectangular counters at the screens' width and
weight. Fallbacks: Eurostile, DIN Alternate, Bahnschrift, Arial Narrow.
Headings are 600 with 0.08-0.18em tracking, stat values 600, field-cell
values 500 and keys 500; body copy is 400. Values run about 2.5x their
labels. Headings, labels, tabs, badges, buttons, toggle keys,
segments, chips, selects, menu entries, short list labels, legends,
field labels, summaries, input addons, scrollspy links, an in-page nav
brand and status-strip taskbar keys are uppercase and tracked (keys packed into a row, toggles and segments, track
0.06em, and none on a phone, so the longest label fits), as are status
cells (0.06em). Typed values in inputs and textareas keep the case the
user typed, at rest and while editing; their placeholders are caps. Body copy and titled list rows keep their case so long text stays
readable. In a table cell a control drops its tracking and a date input
tightens so a row of controls fits a narrow modal.

## Contrast

All pairs meet the lint floors and no exemptions are claimed.

| Pair | Ratio |
|---|---|
| `--text` `#3fd6bd` on `--surface` `#061815` / `--bg` `#03100e` | 10.1 / 10.7 |
| `--muted` `#3fb69a` on `--surface` / `--surface-2` `#0a2420` | 7.3 / 6.5 |
| `--accent` `#9fca6e` on `--surface` | 9.7 |
| `--on-accent` `#06201a` on accent | 9.1 |
| `--danger-text` `#ff8a76` / `--success-text` `#5ce89f` on `--surface` (outlined keys) | 8.0 / 11.7 |
| slider track `--border` `#1c8a72` on `--bg` | 4.5 |
| field-cell outline `--silo-field` `#4a7a4c` (olive, sampled `#477544`) on `--surface` | 3.6 |
| waveform marker ink `#d4f8ee` on the tinted chips | 6.6+ |
| tinted avatar chips take the same ink; a lit pad tints at 24% so `--text` stays at 5.1 | 7.3 / 5.1 |
| dark ink `#06201a` / danger ink `#7a1406` on the yellow-green band | 9.1 / 5.8 |
| plate text `#052019` on plate `#8fd3cc` | 10.1 |
| legacy `--text` `#f1dcae` / `--muted` `#c4a46a` on surface | 14.3 / 8.2 |

The real screens are dimmer: the sampled phosphor core is `#28c6aa`. Text
is lifted only a step, to `#3fd6bd` on the same cyan-teal hue, so long
copy reads at 10:1 and stays above 4.5:1 on the tinted chips without
turning minty; links use the brighter `#5fe0c8`.

## Layout

The shell is a monitor. The bezel padding is 2.2-2.6rem of painted steel
around the glass on desktop and XL, 0.75-1rem on tablet and 0.5rem on a
phone. The rail is a 1.4rem scroll track on the **right**, the
opposite side from most rail themes. At ≤720px the bezel thins to 0.5rem
and the rail collapses per core.

## Don'ts

- Don't make the default accent green or amber. Teal plus yellow-green is
  the identity, and amber or green would read as `pipboy` or `bloomberg`.
- Don't fill surfaces. Panels, inputs and buttons are outlines on glass,
  and only the plates and the yellow-green "granted" fill are solid.
- Don't round things beyond 2-6px (icon keys too: they are square) or add gloss or gradients to components.
- Don't animate the scanlines or add flicker. Everything here is static.
- Don't spend the yellow-green on decoration, or the pale-yellow outline
  on anything but selection and focus.

## Icons

`icons.svg` redraws the whole core set (178/178) as stencilled terminal
glyphs, after the outlined document glyphs on the file grids (see
`references/silo/`):

- 24×24 grid, 1.8 stroke (same as `--icon-stroke-width`), butt caps,
  round joins; boxes have round corners like the squared techno type.
- Stencil bridges: outlined boxes 9+ units wide and circles of radius 5+
  are broken at top and bottom.
- Outline only, except small solid plates (stop, pause, grid cells) and
  square pixel dots.
- `currentColor` everywhere, so both the green glass and the gold `legacy` variant
  apply. No show marks.

## Tell-tales of an inauthentic result

- Free-floating green text on black with no boxes: a generic DOS terminal,
  not the Relic Database.
- Dark title bars: the pale-teal plates are missing.
- A selected row or focused control drawn in teal instead of the yellow
  box.
- Sentence-case, untracked labels.
- A flat page with no bezel at L1: the monitor is gone.
- Heavy glow, CRT curvature or animated noise.

## Print

Title bloom, glow, the bezel, scanlines and the meter segment overlay are
dropped in a small `@media print` block.

## Reference status

Researched from HUDS+GUIS's frame captures (primary) and Territory Studio's
project page. 13 stills are filed in `references/silo/` and 2 more in
`references/silo/legacy/`. Hexes are sampled from those frames and then
lifted for contrast. Unverified: the typeface, any danger/error state, and
tables, toasts, switches and sliders (no screen shows them). See
RESEARCH.md.

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). The steel bezel is kept at every size, thinner on phone (0.5rem) and tablet; the scroll-track rail is hidden up to 900px. Per-tier main padding uses `--app-main-padding-mobile` and `--app-main-padding-tablet`. On touch tiers the brand plate stays as wide as its text. The decorative × in a panel header is dropped on nested boxes, whose double rules also become single, and on headers that hold their own controls. On XL the gutters show the silo's poured concrete: formwork board seams and tie-rod holes, a step off `--bg` (about 1.0:1; the same for `legacy`).

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware: true`).
At **L0** it renders correctly recolored, but as the shell's default
arrangement. Adopt the `.app` / `-bar` / `-rail` / `-main` / `-status`
shell to get the monitor bezel at **L1**.
