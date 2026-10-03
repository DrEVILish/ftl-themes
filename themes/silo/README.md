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
   (`--text #6fe8cc`, `--border #1c8a72`) on green-black glass. Other hues
   are there to carry meaning, never to decorate.
2. **Yellow-green fill means granted, selected or primary.** Examples are
   `.btn-primary`, the active segment, switch-on, pagination and progress.
   It never appears as decoration.
3. **Pale yellow outline means "this one".** The focus ring, active tab,
   active nav entry and selected row all use the yellow box the hard-drive
   browser draws around the highlighted file (`--accent-2 #e6dc8c`).
4. **Title bars are solid pale-teal plates with dark text.** This covers
   the brand, modal header, tooltip and status strip. Nothing else is a
   light surface.
5. **Everything is boxed and labelled.** Inputs are outlined cells with
   tiny tracked-caps labels, panel titles sit between double rules, and
   buttons are outlined keys.
6. **Amber is for numerals and warnings only.** That means the countdown
   readout digits (`--silo-num`) and `--warning`.

## Signature details

- The whole `.app` is a rounded **steel monitor bezel** (`--silo-bezel`)
  with the bar, main and status on one piece of CRT glass. The glass is
  rounded at the top of the bar and the bottom of the status strip.
- The top bar is PACT's header. It sits between **pale-yellow double
  rules**, its nav entries are **auto-numbered `01 02 03`** by a CSS
  counter, and the brand is a pale-teal plate ("RELIC DATABASE").
- The **right-hand rail is the screen's scroll track**: a thumb block over
  tick marks.
- The **status strip is a pale-teal plate** ("DISK 10% RAM 40% ...") with
  dark tracked caps. State colours are re-pointed to dark inks inside it.
- Panel titles sit between 3px double rules with an `×` at the right
  ("RELIC/SEIZED OBJECTS INVENTORY").
- `.btn-primary` is the yellow-green band plus the SEARCH key's outer
  pale-yellow frame.
- Tabs are outlined soft keys with a `›` cue (PACT's MESSAGE / CONTACTS row).
- Readouts are PACT countdown pills: a rounded teal outline and amber
  numerals with a faint glow.
- Progress, meters and bar charts are hatched yellow-green like the
  CAPACITY bar.
- `kbd` uses the beige keycaps of the pull-out keyboards.
- Static scanlines, a vignette and a faint bloom on all text.

### Variants

| Variant | Label | Source |
|---|---|---|
| (default) | Silo | Season 1 IT, Judicial and PACT terminals (teal). |
| `legacy` | The Legacy (gold tablet) | Territory Studio's Season 2 Legacy tablet: gold `#f2b84b` on warm black, cream plate, lighter brushed-metal bezel. References in `references/silo/legacy/`. |

## Typography

Share Tech (UI) and Share Tech Mono (inputs, readouts, data) are already
vendored in `assets/fonts/` under SIL OFL (see `assets/fonts/NOTICE.md`).
They are the closest open match to the show's squared, round-cornered
all-caps techno face, which has not been identified. Fallbacks: Eurostile,
DIN Alternate, Bahnschrift, Arial Narrow. Headings, labels, tabs, badges,
buttons and inputs are uppercase and tracked. Body copy keeps its case so
long text stays readable.

## Contrast

All pairs meet the lint floors and no exemptions are claimed.

| Pair | Ratio |
|---|---|
| `--text` `#6fe8cc` on `--surface` `#03160f` / `--bg` | 12.5 / 13.3 |
| `--muted` `#3fb69a` on `--surface` / `--surface-2` | 7.4 / 6.7 |
| `--accent` `#b9dc78` on `--surface` | 12.1 |
| `--on-accent` `#06201a` on accent | 11.0 |
| `--on-danger` on `--danger` `#ff6b55` | 7.0 |
| `--on-success` on `--success` `#43e08f` | 10.6 |
| plate text `#052019` on plate `#8fd3cc` | 10.1 |
| legacy `--text` `#f1dcae` / `--muted` `#c4a46a` on surface | 14.3 / 8.2 |

The real screens are dimmer: the sampled phosphor core is `#28c6aa`. Text
is lifted to read like the bloom of a lit CRT.

## Layout

The shell is a monitor. The bezel padding is 1.4-1.8rem of painted steel
around the glass. The rail is a 1.4rem scroll track on the **right**, the
opposite side from most rail themes. At ≤720px the bezel thins to 0.5rem
and the rail collapses per core.

## Don'ts

- Don't make the default accent green or amber. Teal plus yellow-green is
  the identity, and amber or green would read as `pipboy` or `bloomberg`.
- Don't fill surfaces. Panels, inputs and buttons are outlines on glass,
  and only the plates and the yellow-green "granted" fill are solid.
- Don't round things beyond 2-6px or add gloss or gradients to components.
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

Bloom, glow, the bezel, scanlines and the meter segment overlay are
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
