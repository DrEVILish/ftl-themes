# LEGO Classic

> Primary colour blocks, thick borders, and circular studs.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The brick itself as a UI: primary colours, thick black outlines on
everything, and a chunky "pressable" 3D shadow that a button visibly loses
when clicked — a physical toy, not a flat icon of one.

## Core values

1. **Thick black outlines, always 3px.** Every control, card, list group,
   list card, table, menu, dropdown and popover is outlined like a brick's
   moulding line (badges, avatars, icon buttons, close buttons and
   pagination bricks take 2px). No control is round: icon and close
   buttons are 1x1 bricks.
2. **A button has a shadow it loses on press.** `--btn-shadow` is a
   hard offset shadow; `:active` drops it and nudges the button down —
   the brick physically depresses.
3. **Primary colours only** — red, yellow, blue, green — no intermediate
   tints: coloured badges are solid fills, never 20% tints; own messages,
   answered or saved items, callouts and invalid fields stay white and show their
   state by a stripe or outline; sparklines carry no area fill. `--flare`
   (blue) carries structure and selection (nav, table heads, links, the
   active tab, segment, toggle, filter chip and page, info alerts), as
   blue dominates the booklet; red stays reserved for the one primary action per view and danger; plain buttons are white bricks.
   Chart series run blue, red, yellow, green, black, grey with no repeats;
   bar charts are blue bricks, line charts have no area fill, and heatmaps
   step through solid grey, yellow, blue and black instead of a tint ramp.
4. **Bold, geometric type.** Jost (a Futura revival) at 800-900 for headings, stat values and step numerals.
5. **Studs are big and everywhere a brick's top face would show one** —
   the app bar, every panel/card top, and every panel/modal header. A
   stud is a cylinder in its brick's colour with a darker side wall, on the
   real stud-to-pitch proportion, and a strip only ever shows whole studs. A second header lower in
   the same panel is a section label and carries no strip.

## Signature details

- Studs are 16px cylinders seen slightly from above, drawn as the booklet
  draws them: an elliptical top face in the host colour, a darker side
  wall 3px below it and one black outline round both, at a 27px pitch
  (gap about 0.64x the diameter, the real 4.8mm-stud-on-8mm-pitch
  proportion). Each host colour is one small inline SVG
  tile (`--stud-tile`: a white `#ffffff` top over a `#9a9a9a` wall on the white
  cards, so the stud is the card's own colour, raised; a lighter `#1a9be0` top face over navy on the bar, so each reads as a raised cylinder), cheap to repaint while scrolling. Tiles use
  `background-repeat: space`, so every strip shows whole, evenly inset
  studs: zero markup, purely decorative CSS.
- The app bar carries its own blue stud row along its bottom edge, since
  it's the single largest, most-visible brick-top surface on the page. The
  row sits on a band of the booklet's lit `#0090dc` face; the bar's text
  stays on the deeper `--flare`. Unfilled bar buttons keep the black
  moulding line.
  Desktop window title bars carry no strip, so studs never cross a title.
- Sliders are a white groove with a black moulding line and a square red
  1x1 thumb; switches are square-cornered with a 1x1 knob, the track blue (`--flare`)
  with a white knob when on; filter chips
  are white bricks with a 2px black rule (blue when on); a toggle group's chosen item is the blue
  brick pressed down, the rest white bricks with their shadow.
- Callouts borrow the booklet's parts-callout box: no fill, a 2px black
  frame and the state stripe, no drop. Fieldsets and logs take the same
  2px small-piece line; the 3px brick line stays on cards and controls.
- Tables are white bricks: a 3px black frame and the 4px drop under the
  blue head. Pagination items and carousel arrows are 1x1 bricks with a
  2px moulding line (the CSS carousel's scroll buttons too); bar-chart
  bars are flat (no gloss sliver). The active tab is a white brick with a
  3px outline on top and sides over the blue underline, and the active nav
  item a white brick with a 2px outline on the blue bar. Disabled items
  stay outlined, only dimmed; a disabled button is a baseplate-grey brick
  (`#a0a3a6`, `#3a3a3a` text, outline kept), never a faded pink.
- Plain buttons are white bricks; red is kept for the one primary action
  per view. Tertiary and ghost buttons are unpainted bricks: the full 3px
  moulding line on the sand (borderless only on the blue bar and table
  head).
- Field rows, accordion items, the tinted `.band` and the meters carry the
  black moulding line (3px; 2px on meter tracks); the scrollspy strip
  sits on the sand over a 3px rule. The inbox folder rail is a blue base
  plate like the bar (white items, white active brick) with a 3px rule
  and the 4px drop. Desktop icons are blue structure, not red.
- Desktop windows: the close button is a red 1x1 brick; an inactive
  window keeps flat colours and its close brick turns baseplate grey.
- Focus is an opaque blue ring (`--flare`) over a 2px ground-coloured
  gap, so it shows next to the black outlines.
- Alerts and toasts get the 3px black outline with the state colour as a
  thick left stripe. Page titles and stat values are weight 900, tight;
  stat values use the sans, not the mono, to echo the step numerals.
- `.btn:active` drops the shadow to `0 1px 0` and nudges the button
  `translateY(2px)` — the brick visibly sinks into the plate, not just
  darkens.
- Classic Space blue comes in three steps of one cyan-blue hue, sampled
  from the booklet's `#0090dc` print: `--brick-blue` `#0090dc` fills
  everything without text (chart series 1, bar chart, progress, carousel
  dot); `--flare` `#007ac0` is the bar, table heads and active
  segment/page/toggle (white text 4.62:1); `--flare-text` `#064a8f` is
  the link and active-tab ink. The status strip uses the same `--flare`
  as the bar, with white text. Structural chrome is always blue regardless of which
  primary colour a button uses.

## Layout

A solid blue bar and status strip with a thick black rule — a base plate
in a specific colour. The page ground is the booklet's yellow sand
(`#dcc95a`, sampled from the print's `#d8c451`-`#ddc94e`; the text tokens
are darkened, not the sand lifted, so blue, red and grey text clear 4.5:1), with white bricks built on it. Toolbars sit straight on the
sand, no white band.

## Tell-tales of an inauthentic result

- Thin or no borders — the moulding line is the entire identity.
- A button with no press-shadow interaction.
- Pastel or muted colours instead of flat primaries.

## Don'ts

- **No pills or fully round buttons**; bricks are near-square (`--radius: 0.125rem`, 2px; nav items 0).
- **No thin or soft borders.** Borders are thick and near-black.
- **No yellow as text or white on yellow.** Yellow is a fill only.
- **No gradients, gloss or blur.** Flat moulded plastic.
- **No pastel or tinted primaries**; keep red, yellow, blue, green as flat primaries.
- **No modern booklet-promo styling**; the reference is the 1979 Classic Space instruction booklet.

## Icons

`themes/lego-classic/icons.svg` covers the full core set (178/178). Style
rules: 24 grid; a thick uniform 3px stroke (glyphs from the generic
sprite take `--icon-stroke-width: 2.5` so file-type letters, pins and badge
marks stay open) with round caps and joins,
`fill: none`, so each glyph reads as an outlined moulded piece; rects rx
1.5; true curves; dots and small marks (more-horizontal, sand in the
hourglass, gamepad buttons) are filled `currentColor` circles, the
"stud" accent the set also puts on grid, trash and music. Dense glyphs
(file-type-png, file-spreadsheet, invoice, thermometer) drop inner frames
so the heavy stroke does not close them up. Colour is `currentColor` only.

## Typography

`--font` is `"Futura", "Jost", "Century Gothic", "URW Gothic", "URW Gothic L", "Avenir Next", Avenir, Arial, sans-serif`; `--font-mono` is `Consolas, "Liberation Mono", "Courier New", monospace`. Futura (macOS) is named first as the booklet-era geometric face; **Jost** (OFL, a Futura revival) is vendored as one variable Latin woff2 (`assets/fonts/Jost-Variable.woff2`, weights 100-900), so every platform without Futura gets the geometric face rather than Arial. `RESEARCH.md` names no face; the booklet's heavy step numerals are matched with Jost 900 on page titles, stat values and step markers. Buttons use 800, stat labels 700, body copy 500 so it holds up beside the 3px rules. The @font-face trims Jost's tall 1.45em line box to Arial's 1.12em (ascent/descent overrides) so text keeps its padding inside fixed-height bricks.

## Contrast honesty

- **Filled primaries carry white text:** red `--danger` `#d0111b` is 5.56:1 under white (`--accent` is a step darker, `#b80f18`, 6.73:1, so it holds white text with room; red text uses `--accent-text`); green `--success` `#237841` is 5.48:1. No before-hex is recorded for these (`RESEARCH.md` gives no LEGO hex, and I did not verify them against official brick colours), so treat them as darkened-enough-for-white primaries, not sampled values.
- **Yellow `#f2d43a`** (the booklet's lemon brick yellow) is near 1.3:1 on `--bg` and 1.5:1 on white: it is never text. Text on yellow is dark, and copy that needs the yellow's meaning uses `--warning-text` `#5e4a00` (8.6:1 on white).
- **Red as small text** uses `--danger-text` / `--accent-text` `#9a0c14` (5.15:1 on the sand).
- `--muted` `#474747` is 5.55:1 on the sand `--bg`; links are `--flare-text` `#064a8f`, 5.26:1 on the sand; `--success-text` is `#1a5a31` (4.92:1 on sand); `--warning-text` `#5e4a00` is 5.11:1 on sand; `--code-function` is `#5a4818` (5.28:1).
- The booklet's brick blue `#0090dc` is used only for non-text fills (3.5:1 on white); white text sits on `--flare` `#007ac0` (4.62:1). The focus ring is `--flare-text`, 5.26:1 on the sand. The bar stays `#007ac0` rather than the booklet's brighter `#0090dc`, which carries white text at only 3.49:1.
- On the blue status strip (`#007ac0`), muted text and state words are white (4.62:1); the active pattern-nav link on its red fill is white.

## Reference status

`references/lego-classic/` has 3 captures plus `RESEARCH.md`: `lego-928-booklet-steps.jpg` (numbered build steps with parts callouts) and `lego-928-booklet-interior.jpg` (steps 4–7 crop) from the 1979 set 928 booklet, and `original-*.webp`, modern printed control-panel tiles that `RESEARCH.md` itself calls a weak era match. The booklet cover and a build video frame mentioned in older notes are not in the folder. Studs macro and Classic Space set photos are absent (minifig-heavy pages were rejected), so the corner studs are backed by the brick/booklet idea rather than a capture.

## v5 layout

- **Tiers.** No rail. The studded blue bar works unchanged on phones and tablets, where core stacks the brand and actions over a scrolling nav line above the stud row.
- **Nesting.** A panel or card reserves room for its 26px stud strip, so content starts below the studs instead of under them. A brick inside a brick keeps its thick outline and drop shadow but loses its studs: one row of studs per stack. Stacked-table labels use `--muted`.
- **XL gutter art (1801px+).** The page sits on the booklet's grey baseplate (`#a0a3a6`): grey studs on grey, drawn by their rims. The baseplate runs right up to the page column with a hard edge (`--app-gutter-fade: 0px`) and the column carries a 3px black side line.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
