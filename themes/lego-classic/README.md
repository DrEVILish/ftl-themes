# LEGO Classic

> Primary colour blocks, thick borders, and circular studs.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The brick itself as a UI: primary colours, thick black outlines on
everything, and a chunky "pressable" 3D shadow that a button visibly loses
when clicked — a physical toy, not a flat icon of one.

## Core values

1. **Thick black outlines, always 3px.** Every control is outlined like a
   brick's moulding line.
2. **A button has a shadow it loses on press.** `--btn-shadow` is a
   hard offset shadow; `:active` drops it and nudges the button down —
   the brick physically depresses.
3. **Primary colours only** — red, yellow, blue, green — no intermediate
   tints. `--flare` (blue) carries structural chrome (nav, table
   heads) so red stays reserved for actions/danger.
4. **Bold, geometric type.** Heavy weight headings.
5. **Studs are big and everywhere a brick's top face would show one** —
   the app bar, every panel/card top, and every panel/modal header, all
   carrying large two-tone discs, not a thin accent line easy to miss.

## Signature details

- Studs are large (~18-20px) two-tone `radial-gradient` discs — a bright
  offset highlight inside a darker rim — tiled every 32-36px, not
  individual `<span>` elements: zero markup, purely decorative CSS. A
  faint pinprick-sized dot doesn't read as a brick stud at a glance; a
  disc this size does.
- The app bar carries its own stud row along its bottom edge, since it's
  the single largest, most-visible brick-top surface on the page.
- `.btn:active` drops the shadow to `0 1px 0` and nudges the button
  `translateY(2px)` — the brick visibly sinks into the plate, not just
  darkens.
- `--flare` (moulding blue, `#0055bf`) carries the app bar, status
  strip, and table headers — structural chrome is always blue regardless
  of which primary color a button uses.

## Layout

A solid blue bar and status strip with a thick black rule — a base plate
in a specific colour, with the white content area as the build surface on
top of it.

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

## Typography

`--font` is `"Futura", "Century Gothic", Arial, sans-serif`; `--font-mono` is `Consolas, monospace`. Futura and Century Gothic are **system fonts, not vendored**: Futura is on macOS, Century Gothic on Windows/Office, and most Linux installs fall to Arial. `RESEARCH.md` names no face, and the booklet captures show a geometric sans that Futura only approximates. Buttons use weight 800.

## Contrast honesty

- **Filled primaries carry white text:** red `--danger` `#d0111b` is 5.56:1 under white (`--accent` is a hair darker, `#cc111a`, 5.7:1, so red links clear 4.5:1 on the `#e6e6e6` grey too); green `--success` `#237841` is 5.48:1. No before-hex is recorded for these (`RESEARCH.md` gives no LEGO hex, and I did not verify them against official brick colours), so treat them as darkened-enough-for-white primaries, not sampled values.
- **Yellow `#f5c400`** is only 1.47:1 on `--bg` and 1.64:1 on white: it is never text. Text on yellow is dark, and copy that needs the yellow's meaning uses `--warning-text` `#6e5700` (6.94:1 on white).
- **Red as small text** uses `--danger-text` `#b80f18` / `--accent-text` `#a50d15`.
- `--muted` `#5a5a5a` is 6.90:1 on white, 6.16:1 on `--bg`.

## Reference status

`references/lego-classic/` has 3 captures plus `RESEARCH.md`: `lego-928-booklet-steps.jpg` (numbered build steps with parts callouts) and `lego-928-booklet-interior.jpg` (steps 4–7 crop) from the 1979 set 928 booklet, and `original-*.webp`, modern printed control-panel tiles that `RESEARCH.md` itself calls a weak era match. The booklet cover and a build video frame mentioned in older notes are not in the folder. Studs macro and Classic Space set photos are absent (minifig-heavy pages were rejected), so the corner studs are backed by the brick/booklet idea rather than a capture.

## v5 layout

- **Tiers.** No rail. The studded blue bar works unchanged on phones and tablets, where core stacks the brand and actions over a scrolling nav line above the stud row.
- **Nesting.** A panel or card reserves room for its 26px stud strip, so content starts below the studs instead of under them. A brick inside a brick keeps its thick outline and drop shadow but loses its studs: one row of studs per stack. Stacked-table labels use `--muted`.
- **XL gutter art (1801px+).** The page sits on a light-grey baseplate of studs, within about 1.2:1 of `--bg`.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
