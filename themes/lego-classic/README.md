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
   blue dominates the booklet; red stays reserved for buttons and danger.
   Chart series run red, blue, yellow, green, black, grey with no repeats.
4. **Bold, geometric type.** Heavy weight headings.
5. **Studs are big and everywhere a brick's top face would show one** —
   the app bar, every panel/card top, and every panel/modal header. A
   stud is a cylinder in its brick's colour with a darker side wall, packed
   tight, and a strip only ever shows whole studs.

## Signature details

- Studs are 16px cylinders seen slightly from above, drawn as the booklet
  draws them: an elliptical top face in the host colour, a darker side
  wall 3px below it and one black outline round both, at a 22px pitch
  (gap about 0.4x the diameter). Each host colour is one small inline SVG
  tile (`--stud-tile`: white over grey on cards, brick blue over navy on
  the bar), cheap to repaint while scrolling. Tiles use
  `background-repeat: space`, so every strip shows whole, evenly inset
  studs: zero markup, purely decorative CSS.
- The app bar carries its own blue stud row along its bottom edge, since
  it's the single largest, most-visible brick-top surface on the page.
  Desktop window title bars carry no strip, so studs never cross a title.
- Sliders are a white groove with a black moulding line and a square red
  1x1 thumb; switches are square-cornered with a 1x1 knob; filter chips
  are white bricks with a 2px black rule (blue when on); a toggle group's chosen item is the blue
  brick pressed down, the rest white bricks with their shadow.
- Tables are white bricks: a 3px black frame and the 4px drop under the
  blue head. Pagination items and carousel arrows are 1x1 bricks with a
  2px moulding line (the CSS carousel's scroll buttons too); bar-chart
  bars are flat (no gloss sliver). The active tab is a white brick with a
  3px outline on top and sides over the blue underline, and the active nav
  item a white brick with a 2px outline on the blue bar. Disabled items
  stay outlined, only dimmed.
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
- `--flare` (Classic Space blue, `#0a64c2`, a step from LEGO's `#0055bf`
  toward the booklet's lighter print while keeping white text at 5.8:1) carries links, the status
  strip and table headers; the app bar and nav bars take the brighter
  brick blue `#1a78cc` (white text 4.56:1) — structural chrome is always blue regardless
  of which primary color a button uses.

## Layout

A solid blue bar and status strip with a thick black rule — a base plate
in a specific colour. The page ground is the booklet's pale sand
(`#f0e5c2`, warmed toward the print while blue and red text still clear
4.5:1), with white bricks built on it. Toolbars sit straight on the
sand, no white band.

## Tell-tales of an inauthentic result

- Thin or no borders — the moulding line is the entire identity.
- A button with no press-shadow interaction.
- Pastel or muted colours instead of flat primaries.

## Don'ts

- **No pills or fully round buttons**; bricks are square-cornered (`--radius: 0.4rem`).
- **No thin or soft borders.** Borders are thick and near-black.
- **No yellow as text or white on yellow.** Yellow is a fill only.
- **No gradients, gloss or blur.** Flat moulded plastic.
- **No pastel or tinted primaries**; keep red, yellow, blue, green as flat primaries.
- **No modern booklet-promo styling**; the reference is the 1979 Classic Space instruction booklet.

## Icons

`themes/lego-classic/icons.svg` covers the full core set (178/178). Style
rules: 24 grid; a thick uniform 3px stroke with round caps and joins,
`fill: none`, so each glyph reads as an outlined moulded piece; rects rx
1.5; true curves; dots and small marks (more-horizontal, sand in the
hourglass, gamepad buttons) are filled `currentColor` circles, the
"stud" accent the set also puts on grid, trash and music. Dense glyphs
(file-type-png, file-spreadsheet, invoice, thermometer) drop inner frames
so the heavy stroke does not close them up. Colour is `currentColor` only.

## Typography

`--font` is `"Futura", "Jost", "Century Gothic", "URW Gothic", "URW Gothic L", "Avenir Next", Avenir, Arial, sans-serif`; `--font-mono` is `Consolas, monospace`. Futura and Century Gothic are **system fonts, not vendored**: Futura is on macOS, Century Gothic on Windows/Office, and Linux picks up Jost or URW Gothic when installed and otherwise falls to Arial or the platform sans. No geometric OFL face is vendored yet (that needs `assets/fonts/`). `RESEARCH.md` names no face, and the booklet captures show a geometric sans that Futura only approximates. Buttons use weight 800.

## Contrast honesty

- **Filled primaries carry white text:** red `--danger` `#d0111b` is 5.56:1 under white (`--accent` is a hair darker, `#cc111a`, 5.7:1, so red links clear 4.5:1 on the `#e6e6e6` grey too); green `--success` `#237841` is 5.48:1. No before-hex is recorded for these (`RESEARCH.md` gives no LEGO hex, and I did not verify them against official brick colours), so treat them as darkened-enough-for-white primaries, not sampled values.
- **Yellow `#f5c400`** is only 1.47:1 on `--bg` and 1.64:1 on white: it is never text. Text on yellow is dark, and copy that needs the yellow's meaning uses `--warning-text` `#6e5700` (6.94:1 on white).
- **Red as small text** uses `--danger-text` `#b80f18` / `--accent-text` `#a50d15`.
- `--muted` `#5a5a5a` is 6.90:1 on white, 5.48:1 on the sand `--bg`; links are `--flare` `#0a64c2`, 4.62:1 on the sand and 5.82:1 on white.
- Brighter brick blue `#2a85d4` (closer to the booklet print) is used only for non-text fills: chart series 2 and the progress fill (3.9:1 on white).
- On the blue status strip, muted text is `#eef3fa` (5.21:1) and warning words `#ffea8a` (4.81:1); the active pattern-nav link on its red fill is white.

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
