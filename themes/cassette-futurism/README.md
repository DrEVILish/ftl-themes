# Cassette Futurism

> The 1970s-80s imagined future as chunky hardware: beige moulded plastic, dark recessed windows with seven-segment numerals, colour-coded keycaps, bat-handle toggles, racing stripes and Dymo tape.

**Requires: L1**: sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The **outside of the machine**: the Commodore PET, a TR-808, a Technics
cassette deck, an HP-35, the Atari 2600, and the Nostromo consoles that
borrowed from all of them. It is a **light** theme (`color-scheme: light`).
The body is warm beige ABS. Anything that shows information is a dark,
recessed window set into that body, lit in VFD teal or LED red/green/amber.
References and credits: `references/cassette-futurism/RESEARCH.md`.

How it differs from its neighbours:

- `weyland-yutani` is the **screen**: dark warm-black UI, amber CRT text,
  a beige plate used only as a label. This theme is the **housing**: the
  page is beige plastic and the dark glass sits inside it.
- `international-rescue` is 1960s Thunderbirds: cream and navy, heavy
  italic, gold, round bezelled lamps, hard navy offsets. This theme has no
  navy or gold. Its colour comes from the 808's red/orange/yellow/cream
  keycaps and a brown/orange stripe, and its type is upright silk-screen
  caps.
- `blue-future` is a dark neon HUD. Nothing here glows except digits behind
  glass.

## Core values

1. **Beige is the housing, dark glass is a window.** `--bg`/`--surface` are
   warm beige and off-white. Dark (`--cf-window` `#17140f`) is used only for
   recessed displays: `.readout`, `.meter`, `.input`/`.select`, `.log`,
   `.scribble`, the status strip. Dark brown (`--cf-choc`) is the top deck:
   app bar, table head, modal title, transport.
2. **Digits are segments.** `.readout` sets DSEG7 Classic Bold Italic in
   VFD teal with a soft glow. `unicode-range` limits it to digits and
   `: . -`, so units and letters fall back to mono. Don't widen it.
3. **Keys are keycaps.** `.btn` is a sculpted square cap: radius 3px, a
   lighter top, a darker skirt (`inset 0 -4px`) and a 2px hard drop. It
   presses 2px on `:active`. Colour comes from the cap, as on the 808:
   primary orange, danger red, success green, GO yellow.
4. **`.switch` is a bat-handle toggle, never a pill.** It is a chrome ball
   on a shaft with a pivot nut at the track centre, on a slotted plate. Off
   throws the ball left over a dark slot. On throws it right and the slot
   lights orange. Position and colour both carry the state.
5. **The stripe is trim, used three times.** Yellow, orange, red and brown,
   in that order: under the app bar, as the swatch at the top of the rail,
   and under `h1`. Don't put it on buttons, panels or backgrounds.
6. **Labels are Dymo tape.** `.badge`, `.tooltip` and the bar brand are
   embossed tape: bold tracked capitals with an emboss text-shadow. Black
   tape by default; red, green, orange and yellow for the semantic badges.
7. **Silk-screen voice.** Headings, buttons, table heads and panel titles
   are upright bold caps in a Helvetica/Univers stack with tracking. Never
   italic, never a script.

## Signature details

- **Shell = a deck housing**: dark top deck with a 4-band stripe (stacked
  hard box-shadows), an inset off-white main panel with a moulded ledge, a
  **ribbed vent grille rail on the right** (3.25rem) topped by a stripe
  swatch, and a dark VFD status window.
- Panel headers start with five black vent slots before the title.
- LED meter ladders (green, amber, red) on dark glass. Progress is an
  orange segmented bar.
- Lamps are round LEDs in a 2px chrome bezel; off lamps are dark domes.
- Inputs are CRT wells with VFD-teal mono entry and a teal caret.
- Sliders and faders have a cream cap with a dark centre line, like a
  mixer fader cap.
- The dark surfaces (`.app-bar`, `.transport`) re-point `--text`/`--muted`/
  `--link` locally so text on them stays legible.

## Typography

- `--font`: `"Helvetica Neue", Helvetica, "Nimbus Sans", Univers,
  "Liberation Sans", Arial`. Not vendored.
- `--font-mono`: Share Tech Mono (already vendored in `assets/fonts/`,
  OFL), then IBM Plex Mono and DejaVu Sans Mono.
- Readout digits: **DSEG7 Classic Bold Italic** by keshikan (SIL OFL 1.1),
  vendored in `assets/fonts/` (licence in `assets/fonts/DSEG-LICENSE.txt`,
  credit in `assets/fonts/NOTICE.md`).
  Without it the readouts fall back to mono and still work.

## Contrast honesty

WCAG 2.x, as computed by `scripts/check.py`. All floors pass except one
warning:

- `--accent` `#cc5a0a` on the beige `--bg` `#d3c9b3` is 2.5:1, below the
  3:1 advisory floor. The bare backdrop only shows in the shell's gutters
  and never carries accent text. Text links use `--link` `#8f3b00` and
  `--accent-text` `#9a4100`. On `--surface` the accent passes.
- `--on-accent` is black on the orange keycap. White on `--danger`
  `#c0200d` and on `--success` `#2c7a30`.
- Yellow (`--warning`, GO) carries dark text only. `--warning-text`
  `#775300` is used for text.
- The focus ring is blue (`#1f6fd1`, 3px plus a soft halo). It is the only
  cool colour in the palette, so it shows up on beige, orange keys and dark
  windows.

## Don'ts

- Don't make the page dark. That is `weyland-yutani`.
- Don't add navy, gold, italic headings or pill shapes. That is
  `international-rescue`.
- Don't add glow to anything that isn't a digit or LED behind glass.
- Don't put the stripe on buttons, panels or backgrounds.
- Don't turn `.switch` back into a rounded pill, or drop the slot colour
  change.
- Don't set `background`/`color` on base component selectors (lint).

## Tell-tales of an inauthentic result

- A flat light theme with orange buttons: the keycap sculpt and drop shadow
  are missing.
- Readouts in a proportional or plain mono face instead of segments.
- A pill switch, or one whose state shows only by colour.
- Grey `#c0c0c0` bevels: that is `windows95`, not moulded beige plastic.
- Rainbow stripes or neon gradients: the stripe is four flat earthy bands.
- Light input fields: the CRT well has gone.

## Print

The stipple, glow, dark readout and input windows and the bar stripe are
neutralised in a small `@media print` block.

## Reference status

Sixteen free-licensed Commons photographs of real period hardware are in
`references/cassette-futurism/` with credits. Palette sampled from the
TR-808, PET, VFD and DSKY photos and then adjusted for contrast (see
RESEARCH.md). The genre definition comes from search summaries, because the
Aesthetics Wiki fetch was refused. No *Alien* set photographs are included.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** it renders correctly recoloured, but in the shell's
default arrangement. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status`
shell (CONTRACT.md "The app shell" / "Adoption levels") for the deck
housing with the right-hand vent rail at **L1**. Without the rail element,
the rail column collapses (core degrade rule).
