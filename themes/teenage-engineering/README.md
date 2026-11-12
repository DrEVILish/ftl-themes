# Teenage Engineering

> A pocket synthesizer seen from above: off-white anodised aluminium, rounded light-grey keys, a small dark display window, and four colour-coded encoders.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The top face of a Teenage Engineering OP-1 / OP-1 field / OP-Z (inspired
by, never branded): a bead-blasted aluminium body, a grid of rounded light
keys separated by the frame, one small black display window where all the
fun happens (thin white and teal line art, big thin numerals), and the four
encoders in blue, green, white and orange that colour whatever the screen is
showing. It should feel precise, toy-like and calm: mostly grey and white,
with colour only where an encoder would put it. Sources and the reference
mapping are in `references/teenage-engineering/RESEARCH.md`.

## Core values

1. **Light hardware, dark screen.** Surfaces are light keys on an aluminium
   frame. Only things that show a machine value are dark display glass:
   readouts, meters, gauges, clocks, charts, code blocks, scribble strips,
   toasts, tooltips, the status strip and the brand window. Panels, tables
   and forms stay light. Do not "dark mode" the body.
2. **Four encoder colours, in order.** Blue, green, white, orange — knobs,
   tab dots, slider thumbs, fader cap lines and the first chart series
   follow that order by position (`--te-hue` / `--te-ink`, cycled with
   zero-specificity `:where()` rules so band classes and app values win).
   No other saturated colour is decoration; red-orange means record/danger.
3. **Keys are rounded rectangles with a 2px side.** Buttons, panels,
   cards, the bar and the rail are keys: `0.5-0.75rem` corners, a hairline
   key-edge border and a hard 2px shadow underneath. A page-level
   `.toolbar` and the folder rail are keys too. Pressing moves a key
   down 1px. No gradients that read as gloss. The primary button is the
   black note key with a white legend: the hardware has no blue keys.
4. **Black means selected.** Active nav items, segmented items, pagination,
   active badges, the highlighted menu item and command row, checked toggle
   buttons, the selected calendar day (its range is pressed keys) and the
   selected desktop icon label are the black of the OP-1's
   note dots with white text, not the accent colour. Selected list, inbox and
   table rows are a pressed (darker) key with a black edge bar. The bulk
   selection bar is a strip of display glass; an accent badge is a white key
   with a blue dot; an unsaved cell is a white key with an orange edge bar.
5. **Light grotesque, silkscreen labels.** Headings are regular/medium
   (h1 400, h2-h4 500) with negative tracking, so the display numerals stay
   the loudest type; panel heads, table heads and form labels are tiny tracked caps
   like the printing beside a key. Display numerals (`.readout`,
   `.stat-value`) are thin and wide like the OP-1 screen: a light grotesque
   (300, tracked 0.05em, tabular) pared down further by a hairline stroke in
   the glass colour, so they stay thin even where no light cut exists. Code,
   the brand window and the status strip use the monospace.

## Signature details

- `.knob` is the OP-1 encoder: a flat coloured cylinder cap with one slot,
  standing in a recessed collar, with a thin value arc around it. The
  cylinder's side (2px, darker shade of the cap) and its shadow are painted
  on the dial, which doesn't turn, so they stay underneath at any value.
  `.knob-hf/-hmf/-lmf/-lf` are the four encoders. The cap top is a flat
  matte fill with only a 1px lighter rim, no highlight.
- The rail is a key-face column: the speaker grille (an SVG dot field) on
  top, the four encoder dots under it, then four black round note keys.
- Every page has a screen: a KPI `.stat-value` sits in a small display
  window. Every panel and card is a labelled key: its header's first item,
  or a plain `h2`/`h3` that opens it, carries an encoder colour dot (blue,
  green, white, orange by position).
- The page is a flat near-white aluminium (`#d5d9da`); keys read by their
  key-edge seams and 2px side, not by a dark field around them.
- The bar's brand sits in a tiny display window (black glass, mono, white).
- The status strip is display glass. On a phone it wraps to two lines
  rather than cutting items to one glyph.
- The slider is a thin, square-cut black slot (0.3rem) under a small
  encoder-cap thumb; the hit area stays at core's tap minimum (the content-box
  clip that keeps it there leaves no room for rounded ends).
- Level meters (`.visualizer`) and `.trace` are small glass windows with
  white bars and a teal line. A `.bar-chart` on a light key prints its bars
  in note-key black; sparklines are a thin line with no tinted area.
- The inbox folder rail and a tinted `.band` are keys too (rounded, key-edge
  border, 2px side).
- Every tab carries its encoder's colour dot; the active one is larger and
  pops in three stepped frames (motion-gated), with an underline in its ink.
- The modal close is one of the black round note keys with a white ×; it
  turns orange on hover.
- Charts are drawn on the display glass, with series blue, green, violet,
  orange, pink, ochre (validated with the dataviz palette validator on
  `#131416`: lightness band, chroma floor, CVD and normal-vision separation,
  3:1 contrast). The white encoder can't carry a series (no hue), so it is
  the chart's ink and violet takes its slot.
- Code blocks are display glass with their own palette, re-scoped with the
  other display tokens; inline code stays a light key.

## Layout

The shell is the instrument. `.app` is the aluminium frame (0.6rem
padding and gap); the rail (4.25rem) runs the full height on the left; the
bar, the key bed (`.app-main`, transparent) and the dark status strip stack
to its right.

### v5 layout

- **Desktop (901-1800px):** the full device: rail, bar, main, status.
- **Tablet (481-900px):** `--app-areas-tablet` / `--app-columns-tablet`
  drop the rail; bar, main and status in one column; main inset
  `0.4rem 0.25rem`.
- **Mobile (≤ 480px):** the same single column with a thinner frame
  (0.35rem, set through `@container style(--tier: mobile)`, never a width
  query) and main inset `0.4rem 0.3rem`. The brand window stays a small
  window (content width, at most 60%, truncating first) instead of stretching
  across its line, the bar's `kbd` shortcut hints are hidden, and the
  action cluster (picker, search, bell, avatar) keeps to one row with the
  picker giving way, so the bar is three rows: brand, nav, actions.
- **XL (≥ 1801px):** the shell caps at 1800px; the gutters continue the key
  bed: rounded key outlines with a round dot, embossed a few percent off
  `--bg` (well within 1.5:1), still.
- Touch targets are core's; segmented items get `min-inline-size:
  var(--tap-min)` so one-word segments stay full size.

## Icons

`icons.svg` redraws 178 of core's 1020 symbols as OP-1 silkscreen
pictograms (see the key legends in `references/teenage-engineering/`); the
rest are core fallbacks, drawn at the same 1.5 stroke via
`--icon-stroke-width`:

- 24×24 grid, 1.5 monoline stroke, round caps and round joins.
- True circles and arcs; boxes get soft 2-unit corners like the keys.
- Outline only. Tiny dots, level bars and the caret triangles are the
  only solids.
- `currentColor` everywhere, so icons follow the key-face ink, the blue
  selection and the dark display window. No product marks.

## Tell-tales of an inauthentic result

- Dark panels or a dark page: the body is light aluminium.
- The encoder colours used as large fills, gradients or glows.
- Glossy or domed knob caps, or a knob whose side shadow swings round as it
  turns.
- Accent-blue selected states where the hardware would show black.
- Rounded "pill" panels or sharp 0-radius keys.
- Any logo, wordmark or the model name printed in the UI.

## Adoption

- **L0 (tokens only):** keys, display surfaces, encoder knobs, tabs and
  charts all work; the device frame and rail are lost.
- **L1 (app shell):** the frame, the grille-and-encoder rail, the display
  brand window and the status display strip.
- Fonts: the manufacturer's grotesque is not free; the system stack
  (Helvetica Neue, Helvetica, Arimo, Arial, Liberation Sans, Nimbus Sans,
  TeX Gyre Heros, FreeSans) stands in. Nothing is vendored, so a machine
  with none of these (a bare Linux box) falls back to its default sans,
  usually DejaVu Sans, which runs wide; the light heading weights keep it
  calm.

## Reference status

Ten images: nine openly licensed photos and one fan concept render (credited as such),
in `references/teenage-engineering/`. Missing: the OP-1 field itself, and
anything for on-screen menus, lists, dialogs, tables and text entry (the
hardware has almost none); those components are interpretations of the
hardware and screen language.
