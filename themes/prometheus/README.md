# Prometheus

> The USCSS Prometheus's holographic ship displays: cyan holo-glass, bracketed panels, pill title tabs.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The bridge, medipod, airlock and science-wall screens from *Prometheus*
(2012): dense diagnostic glass in hologram cyan over deep navy, with the
suit room's amber interface as a variant. It is the clean, expensive
Weyland Corporation of 2093, not the worn amber-and-beige hardware of the
Nostromo (that is `weyland-yutani`). Frames from the film are in
`references/prometheus/`, with notes in `RESEARCH.md`. No logo is
reproduced.

## Core values

1. **Every panel is a bracket.** A rounded 4px "[" in the accent (2px and dimmer when nested), with a faint halo, with
   short curved returns at top and bottom, stands just off the left edge
   of panels, cards, lists and alerts (a `::before`; `--panel-radius:
   0.7rem 0 0 0.7rem`). On an image card it sits on the edge, over the
   media, since the card clips its corners. Modals, menus and popovers carry it as a 3px inset.
   No hairline closes the other three sides.
2. **Names sit on pill tabs.** A panel header's first child, the modal
   title and the app brand are filled accent tabs with dark text, like
   "TAG.NM" or "SUM EVA": ends rounded to half an em, a thin dark divider
   about half an em in from the left, a soft halo, and the tab's top level
   with the bracket's top return.
3. **Wide squared capitals for labels, plain for reading.** Michroma for
   headings, buttons, tabs, toggle groups, KPI labels, menubar items,
   badges and table heads (nav items at 0.72rem, not page-sized); section
   lists stay in Share Tech but in tracked capitals; Share Tech for body;
   Share Tech Mono for data and inputs.
4. **Controls are outlined pills.** Buttons and the segmented control are
   1.5px outlined pills ("ENG HUL FRA"); primary is the filled pill.
5. **Values live in dark boxes.** `.readout` is a small value box darker
   than the glass with glowing cyan digits ("986", "030"); KPI values
   (`.stat-value`) use the same light glowing digits, never faux bold.
   Level bars are drawn: the slider rail is the accent mixed 60% into the
   input navy (about 3.4:1 on the glass), and checkboxes and radios are
   navy wells with that same lit edge, filled accent when on.
6. **The glass has a grid.** The page background is mid-navy lit glass
   (`--bg: #072235`, panels a step lighter at `#0d3049`) with a faint
   lattice of dashes and crosses. The navy glow scrolls with the page (not
   `fixed`), so touch scrolling does not repaint the whole background.

## Signature details

- Bracketed panels with filled pill title tabs (rounded ends, dark divider
  near the left end); pill-tab modal title.
- Holo grid of dashes and crosses on a navy glow behind the whole shell.
- Orange edge codes ("0034529", "963409IN_CHY0432") running up the
  empty rail, drawn in CSS.
- A thin cyan rule under the top bar; the brand is a pill tab.
- Micro-caps status line in the label face: `.app-status` ends with the
  ship's sign-off "ENDO SY OS / MUTHUR PRQ 12-5 B" (generated, not read
  aloud; hidden on phones).

### Variants

| Variant | Label | What changes |
|---|---|---|
| (default) | Prometheus | Hologram cyan `#4fd2ff` with teal second series. |
| `suit` | Suit Room (amber) | Amber `#ffb51f` UI over teal-blue glass, cyan values, as on the suit-room "RAVEL" screen. |

## Typography

Michroma (headings and labels), Share Tech (body) and Share Tech Mono
(data) are vendored under SIL OFL; see `assets/fonts/NOTICE.md`. The
film's own face is a custom wide squared sans; Michroma is the closest
open match. All three faces have one weight, so `font-synthesis: none`
keeps headings and numbers light. Michroma is too wide for narrow setting
rows, so a switch row's label reads in Share Tech; avatar initials too.
On touch tiers a joined toggle row reads in Share Tech capitals too.

## Contrast honesty

All pairs meet the lint floors; no exemptions are claimed. The holo grid
is decoration under the panels and carries no text.

## Don'ts

- Don't close the right side of panels: the bracket is open.
- Don't use Michroma for paragraphs; it is too wide to read in bulk.
- Don't add clip-path cut corners (`tron`, `alienware`) or the amber and
  beige plates of `weyland-yutani`.
- Don't animate the grid or add flicker.

## Tell-tales of an inauthentic result

- Fully boxed panels with titles in a header strip: generic dashboard.
- Bold condensed type: the labels are wide and light.
- Neon glow on everything: headings and readouts glow; brackets and tabs
  carry only a faint halo.

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). The edge-code rail is hidden up to 900px, because content width matters more there. On touch tiers the brand tab stays as wide as its text: it neither stretches across the first line nor truncates. A button attached in an `.input-group` squares off to match the input. A header that is only a title is drawn as the filled pill tab. Nested glass steps down: a thinner, dimmer bracket and an outlined tab. A table standing straight on the page gets a glass wash, so the tick grid doesn't run through its rows. On XL the gutters show the Engineers' star map: a dim orrery of thin orbit rings in each gutter among hologram stars, in cyan (amber for `suit`), about 1.0:1.

## Icons

`icons.svg` draws the core set as holographic HUD line glyphs (no studio or Weyland marks).

- **Grid and weight.** 24 grid, ultra-thin 1.25px line, round caps and joins, true curves and arcs; boxes have a 1-unit corner radius.
- **Reticles.** Every circle of radius 6 or more (clock, compass, info, globe, disc) carries four short tick marks outside it, like the film's ring readouts.
- **Glass, not ink.** Silhouettes are a 30% `fill-opacity` holo-glass wash under the line instead of a solid fill; only small markers and carets are solid.
- Generated from one shared 24-grid geometry, so every core-set id (178/178) is drawn; everything uses `currentColor`, so icons follow text, accent and selected states (and every variant) with no hard-coded colour. The `suit` variant's amber comes through the same way.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** it renders recoloured in the shell's default
arrangement; adopt the app shell (CONTRACT.md "The app shell" /
"Adoption levels") for the rail codes and console bar at **L1**.
