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
   `.scribble`, the status strip, the one-time-code window and the KPI
   figure (`.stat-value`, a small recessed readout with segment digits).
   Dark brown (`--cf-choc`) is the top deck:
   app bar, table head, modal title, transport.
2. **Digits are segments.** `.readout` sets DSEG7 Classic Bold Italic in
   VFD teal with a soft glow. `unicode-range` limits it to digits and
   `: . -`, so units and letters fall back to mono. Don't widen it.
3. **Keys are keycaps.** `.btn` is a sculpted square cap: radius 3px, a
   lighter top, a darker skirt (`inset 0 -4px`) and a 2px hard drop. It
   presses 2px on `:active`. Colour comes from the cap, as on the 808:
   primary orange, danger red, success green, GO yellow. Toggle buttons,
   `.segmented` rows (cream keys on the dark deck), tabs (piano-key tops),
   the active nav item and the current page number use the same skirt and
   drop; a latched key is pressed in and lit orange with a black legend.
   Ghost and tertiary buttons are still caps, just quieter: a lower-contrast
   beige face (`#ebe4d4` to `#d6ccb7`, `#8a7e68` edge), and a dark choc cap
   on the dark bands (app bar, transport, hero, table head, window panes).
4. **`.switch` is a bat-handle toggle, never a pill.** It is a chrome ball
   on a thin shaft out of a larger chrome ring nut (dark bore, bright face,
   dark rim) at the track centre, on a 3.6em x 1.6em slotted plate. Off
   throws the ball left over a dark slot. On throws it right and the slot
   lights orange. Position and colour both carry the state.
5. **The stripe is trim, used three times.** Yellow, orange, red and brown,
   in that order: under the app bar, as the swatch at the top of the rail,
   and under `h1`. Don't put it on buttons, panels or backgrounds.
6. **Labels are Dymo tape.** `.badge`, `.tooltip` and the bar brand are
   embossed tape: bold tracked capitals with an emboss text-shadow. Black
   tape by default; red, green, orange and yellow for the semantic badges.
7. **Silk-screen voice.** Headings, buttons, table heads, panel titles,
   modal and window title bars, popover titles and `.nav` keys
   are upright bold caps in a Helvetica/Univers stack with tracking. Never
   italic, never a script.

## Signature details

- **Shell = a deck housing**: dark top deck with a 4-band stripe (stacked
  hard box-shadows), an inset off-white main panel with a moulded edge (lit
  top lip, shaded lower lip, a 2px `#9d917a` ledge then `#b6aa93`), a
  silk-screened `#b6aa93` hairline frame 8px inside it and a fainter copy
  of the housing stipple on the plate (desktop only), a
  **ribbed vent grille rail on the right** (3.25rem) topped by a stripe
  swatch: a block of moulded ribs (3px `#4a4034` slots with a lit
  `#fffdf7` 60% lower edge on a 7px pitch, 40% of the rail, at most
  18rem), not a full-height scale; and a dark VFD status window.
- The deck lettering is silk-screen caps throughout, menubar keys
  included (buttons do not inherit `text-transform`, so the theme passes
  it on). The current top-level menubar key latches orange with the
  same skirt and drop as the active nav key.
- KPI cards: the small-caps legend sits over its recessed readout on
  every card, never inline beside it.
- Panel headers start with five black vent slots before the title (3px
  slots on a 7px pitch, each with a 1px lit right edge so it reads as a
  recess, not ink).
- LED meter ladders (green, amber, red) on dark glass: every `.meter`
  fill is masked into discrete lit cells with dark gaps (the progress
  bar's 0.55rem/0.15rem pitch), counted from the zero end;
  `.is-segmented` keeps core's finer ladder with faint unlit cells
  (`--meter-unlit: 0.16`). Progress is an orange segmented bar.
- Alerts are moulded plates (hairline `#a99d86` housing, lit top lip,
  hard `#b6aa93` ledge) with the message colour as a 0.4rem label strip
  down the lead edge. Alerts and toasts carry a 0.85em lamp: a round LED
  in the chrome bezel, lit in the bright LED of the message's colour
  (info `#ff8a1f`, success `#3fd04a`, warning `#ffc21a`, danger
  `#ff3b25`; a neutral message is an unlit dome). Dropdowns, context menus and popovers sit on the
  same hard `#4f4538` ledge as the keycaps; carousel markers are small
  square keys.
- A `.status` in a table cell keeps the row's font size (core sets 0.85em).
- Phones drop the Dymo emboss text-shadow, the switch's drop-shadow filter
  and the blurred inset shadows of the KPI and status windows (hard insets
  instead), on top of the stipple, glows and soft shadows, for the
  render budget.
- Selected rows and the active list item are a pressed key: a darker
  beige recess (`#e2d6bd`) with an inset shadow and the orange marker,
  never a peach web tint.
- At phone and tablet width the red Dymo brand keeps its whole name
  (tracking 0.1em) and the bar links wrap under it. Icon buttons
  are square keycaps (`--btn-icon-radius: 3px`), never circles.
- Tabs inside a desktop window track tighter (0.03em, 0.78rem) and scroll in one
  row rather than wrap, so the dialog's OK/CANCEL row stays inside it.
- Lamps are round LEDs in a 2px chrome bezel; off lamps are dark domes.
  The live `.connection` lamp is the same LED (bezel, saturated `#3fd04a`
  core) and only dims to 80% when it pulses.
- Inputs are CRT wells with VFD-teal mono entry and a teal caret; a
  floating label resting in the well is dim VFD teal (`#8fb8b0`).
- Sliders and faders have a cream cap with a dark centre line, like a
  mixer fader cap. The slider track is a 6px slot with a shadowed top
  lip (`#8a7e68` over black) and a light lower lip (`#b5a88e` then
  `#fffdf7`, cut into the beige), drawn as a `content-box` background
  inside core's `--tap-min` hit area. The vertical fader is the same
  6px slot: physical left/right padding works round core's vertical-lr
  `padding-inline`, which would otherwise draw it the full hit width.
- The dark surfaces (`.app-bar`, `.transport`, code blocks, the status
  window, countdowns) re-point `--text`/`--muted`/`--link` and the state-text tokens
  locally so text on them stays legible; the hero re-points only accent
  text.
- The hero is the 808's chocolate deck with a 1px orange silk-screen
  pinstripe inset 6px from its edge.

## v5 layout

- **Tiers.** Desktop and XL keep the vent-grille rail on the right. Phone
  (≤480px) and tablet (481–900px) drop it, since it costs a 3.25rem column;
  the dark deck, its four-colour stripe and the LED status window stay.
  Phones get a thinner housing margin and tighter tracking in the status strip, so its tray fits.
  The phone deck fits in three rows: brand with the icon keys, then the
  menubar (0.02em tracking), then the theme picker and search. Settings
  rows track at 0.03em, wrap rather than truncate, and keep 0.85rem of
  air after the toggle. The main plate drops its frame and stipple.
  To stay inside the phone frame budget, phones (≤480px) also drop the
  stipple, the VFD and lamp glows, the soft panel drop and the keycaps'
  top highlight (each keycap keeps two hard shadows: skirt and drop). The housing stipple now sits on the
  page root, so it never covers the XL gutters.
- **Nesting.** A panel inside another surface keeps its moulded header rule
  but drops the vent slots, so only the outer housing reads as vented.
- **XL gutter art.** The beige housing continues past the deck: two banks
  of ribbed vent slots on the stipple, the rail's grille writ large. Still,
  and within about 1.3:1 of `--bg`.

## Typography

- `--font`: `"Helvetica Neue", Helvetica, "Nimbus Sans", Univers, Arimo,
  "Liberation Sans", Arial, sans-serif`. The silk-screen Helvetica/Univers
  voice comes first; Arimo and Liberation Sans are metric-compatible
  stand-ins, and Arial is on every desktop, so no web font is loaded for
  UI text.
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
  and never carries accent text. Darkening the keycap orange to reach
  3:1 (`#b34d06`) would drop its black legend to 4.0:1, so the TR-808
  orange stays and the warning is accepted. Text links use `--link` `#8f3b00` and
  `--accent-text` `#8a3a00`. On `--surface` the accent passes.
  State text (`--accent-text`, `--success-text` `#1f5c25`,
  `--warning-text`) clears 4.5:1 on the bare `--bg` too, since phones
  drop the stipple and show it plainly.
- `--on-accent` is black on the orange keycap. White on `--danger`
  `#c0200d` and on `--success` `#2c7a30`.
- Yellow (`--warning`, GO) carries dark text only. `--warning-text`
  `#6b4b00` is used for text.
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

## Icons

`icons.svg` redraws the whole core set (178/178) as 70s/80s hardware
legends, after the transport-key and panel legends in
`references/cassette-futurism/`:

- 24×24 grid, heavy 2.1 stroke (same as `--icon-stroke-width`), round caps
  and joins. Boxes have big moulded corners (radius up to 3), like
  keycaps and housings.
- Silhouettes are solid. Transport keys use ISO 7000-style solid
  pictograms (play, pause, stop, skip), and power is the ISO 5009 broken
  ring with a bar. Dots are fat. The lettering on file-type glyphs drops
  to 1.4 so it stays legible.
- `currentColor` everywhere, so icons work on the beige housing, the dark
  windows and the keycap colours.
