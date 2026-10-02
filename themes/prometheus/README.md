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

1. **Every panel is a bracket.** A rounded 3px "[" in the accent runs down
   the left edge (`--panel-shadow: inset 3px 0 0`, `--panel-radius:
   0.7rem 0 0 0.7rem`); the right side stays open.
2. **Names sit on pill tabs.** A panel header's first child, the modal
   title and the app brand are filled accent tabs with dark text, like
   "TAG.NM" or "SUM EVA".
3. **Wide squared capitals for labels, plain for reading.** Michroma for
   headings, buttons, tabs, badges and table heads; Share Tech for body;
   Share Tech Mono for data and inputs.
4. **Controls are outlined pills.** Buttons and the segmented control are
   1.5px outlined pills ("ENG HUL FRA"); primary is the filled pill.
5. **Values live in dark boxes.** `.readout` is a small darker-blue value
   box with glowing cyan digits ("986", "030").
6. **The glass has a grid.** The page background is navy with a faint
   lattice of dashes and crosses.

## Signature details

- Bracketed panels with filled pill title tabs; pill-tab modal title.
- Holo grid of dashes and crosses on a navy glow behind the whole shell.
- Orange edge codes ("0034529", "963409IN_CHY0432") running up the
  empty rail, drawn in CSS.
- A thin cyan rule under the top bar; the brand is a pill tab.
- Micro-caps status line in the label face ("ENDO SY OS / MUTHUR").

### Variants

| Variant | Label | What changes |
|---|---|---|
| (default) | Prometheus | Hologram cyan `#4fd2ff` with teal second series. |
| `suit` | Suit Room (amber) | Amber `#ffb51f` UI over teal-blue glass, cyan values, as on the suit-room "RAVEL" screen. |

## Typography

Michroma (headings and labels), Share Tech (body) and Share Tech Mono
(data) are vendored under SIL OFL; see `assets/fonts/NOTICE.md`. The
film's own face is a custom wide squared sans; Michroma is the closest
open match. It has one weight, so headings are not bold.

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
- Neon glow on everything: only headings and readouts glow.

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). The edge-code rail is hidden up to 900px, because content width matters more there. On touch tiers the brand tab stays as wide as its text, so it doesn't stretch across the first line. A header that is only a title is drawn as the filled pill tab. Nested glass steps down: a thinner, dimmer bracket and an outlined tab. A table standing straight on the page gets a glass wash, so the tick grid doesn't run through its rows. On XL the gutters show the Engineers' star map: a dim orrery of thin orbit rings in each gutter among hologram stars, in cyan (amber for `suit`), about 1.0:1.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** it renders recoloured in the shell's default
arrangement; adopt the app shell (CONTRACT.md "The app shell" /
"Adoption levels") for the rail codes and console bar at **L1**.
