# Hot Wheels

> Hot Wheels blue, orange track, a hard-edged red/orange/yellow flame, checkered flag — no subtlety.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The **Hot Wheels game-menu and 1999 PC-set look**: an electric royal-blue
field, orange track as trim and fills, the PC's yellow band with red and
orange pinstripes, the hard-edged flame logo, condensed heavy italic caps,
and a checkered-flag finish — built to feel loud and fast, like a toy-car
menu, not a calm productivity tool.

## Core values

1. **Blue is the field, orange is the track.** `--bg` `#12309a`,
   `--surface` `#1c44bc`, `--surface-2` `#224dcc` and the bar's
   `--hw-blue` `#1f4fd1` follow the electric royal blue of the PC set's
   plastic and the menu backdrop. The main well has the menu backdrop's
   depth: a radial lift to `#1f4cc4` near the top, sinking to `--bg` at
   the edges, so panels lift off the field. Every tinted surface stays a
   saturated blue (`--hw-lift` `#2a5ad6` for the own-message bubble, bulk
   bar, kanban drop and similar; translucent `#4a8cf5` for row hover and
   ranges; the self-mention is the yellow band): core's default of mixing
   the yellow accent into the blue greys it to slate. Orange (`#ff5f00`, and `#ff8a1a` as
   `--hw-flame`/`--accent-2`) is every fill and the track lip, never the
   background and never small text; `--accent` is the flame's yellow core
   `#ffd21a`, because core paints the accent as text (links, active tabs,
   GO, readouts). A washed-out or brown orange has missed the point.
2. **Semi-condensed, heavy, italic, uppercase.** Headings, buttons, nav,
   tabs and the brand use Barlow Semi Condensed ExtraBold Italic (800, a
   true italic), white with a hard dark drop
   `2px 2px 0` shadow with no blur (h1 in flame yellow), like the menu's `MULTIPLAYER / BASEMENT` labels.
   Panel and dialog headers, toggle buttons, filter chips (`.badge-button`),
   segmented items, disclosure summaries and popover titles take the same
   bold italic caps; panel headers carry a `1px 1px 0` drop. Button labels
   never go below `0.875rem`. Window and dialog controls (close,
   minimize, maximize) drop back to the upright body face at `1rem` so the
   glyphs stay legible (their wider glyph box applies to fine pointers
  only; touch keeps core's 44px tap size). Table header cells, KPI values
  (`.stat-value`, 800 at `1.85rem`) and `.readout` timecodes also take
  the heavy italic display face, like the menu's currency counters; mono
  is kept for code and log lines. No glow.
3. **Angles, not curves.** `--radius: 0.2rem`; badges and avatars
   `0.15rem`, switches `0.2rem`, switch and slider thumbs `0.1rem`, icon
   buttons follow `--radius` (no circles). The primary button carries the
   angled (`135deg`) flame gradient (`#ffb400` to `#ff5f00`) with dark
   ink; default buttons sit on `--surface-2` with a 1px orange track rim,
   so the flame marks the one main action. Disabled buttons are a dull
   blue `#3a4f8f` with `#b9c6ee` text, not a faded grey.
4. **The flame, the band and the checkered flag are the signature shapes.**
   The brand badge is the flame logo; the bar sits on the PC set's yellow
   band with orange and red pinstripes; the status strip is a checkered
   flag.
5. **Dark text on the bright fills.** `--on-accent`/`-danger`/`-success`
   are near-black; yellow fills carry deep-blue text.

## Signature details

- The brand badge carries the flame: three curved tongues (red
  `#e3171b`, orange `#ff5f00`, yellow core `#ffcc00`) sweeping about 3rem
  back to sharp, curved points on the left with red showing between them,
  the inner tongues tapering into a red
  body (`#e3171b` to `#b0080c` top to bottom, kept red so the white
  wordmark holds 4.77:1) that ends in a point on the right, all outlined
  in a 1.5px `#ffcc00` line. It is two inline SVG backgrounds, so nothing
  decorative ever sits behind nav text. The wordmark starts `3.4rem` in,
  clear of the yellow core, and the badge is at least `7.5rem` wide so
  short names get a full body; below 600px the tail shortens to `2.6rem`
  and nav strips tighten their gap to `0.5rem`.
- Dialog headers carry a second flame: the same three tongues at the
  start edge of the yellow band, with the title padded clear of it.
- The app bar is solid `--hw-blue` with a 4px yellow rule and orange then
  red 3px pinstripes under it, the PC monitor's band. Dialog headers are
  the same yellow band with the pinstripes along their bottom edge.
- The selected nav item and tab are the game menu's slanted bright-blue
  plate (`#2a64e8` with a lighter `#3f7cf0` upper half and a 2px pale cyan
  `#a8dcff` top edge, so it reads as glossy; painted as backgrounds with
  angled ends, not clip-path, so focus rings are never clipped) with white
  italic text; rail items keep `0.9rem` of end padding so trailing counts
  sit on the flat part of the plate. Selected rows in a sidebar list
  (`nav .list-item`) take the same plate, and single-line sidebar rows the
  display face, so every sidebar selects alike; selected table rows use
  the same blue.
- Table headers are the yellow band with deep-blue display italic caps
  (`0.85rem`, `0.03em` tracking).
- The horizontal tab strip runs along a length of orange track: a 4px
  `#ff5f00` border with a 2px `#ffa040` upper lip and a 2px `#b84400`
  lower lip, the one large orange mass on the blue page.
- Alerts are track panels too: the `--border` dark-blue edge all round and
  a 4px bottom lip in the state colour (orange by default, `#a8dcff` info,
  `#29d17a` success, `#ffcc00` warning, `#e3171b` danger), not thin
  coloured keylines.
- Panels, cards, popovers and dialogs are edged in a darker blue
  (`--border` `#0d2a80`) and carry one heavy 4px orange track lip along
  their bottom edge (`--panel-shadow`/`--card-shadow`), not thin orange
  keylines all round.
- Status badges are solid flame fills with dark ink: accent orange, warning
  yellow with deep-blue text, danger `#e3171b` with white, success green.
- The slider is a length of orange track with 2px lighter and darker lips
  (`background-origin: content-box`, so core's tap-size padding keeps the
  lips on the drawn track) and a yellow thumb.
- The bar chart's highlight bar is the flame's yellow core under a short
  checkered finish-line cap.
- The status bar is `--hw-blue` with the checkered flag as one `0.5rem`
  cap along its top edge (the same on a desktop taskbar), a trim rather
  than a chessboard; readouts sit straight on the blue. The checkers are
  a tiny SVG tile, not a conic gradient, to keep scrolling cheap.
- Heatmaps run up the flame (deep red `#7a1800` to yellow, through orange)
  instead of greying out on a blue-to-yellow mix; chart area fills sink to
  a deeper blue well (`#0a2170`) under the line.
- Checkboxes and radios use the light native scheme: white boxes on the
  blue, yellow when checked.

## Layout

The app shell becomes a **blue track panel**: a blue bar with the flame
logo badge, a yellow rule with orange/red pinstripes under it, a royal-blue
main well, and a blue status strip capped with a checkered flag.

## Tell-tales of an inauthentic result

- A black or grey field instead of the Hot Wheels blue.
- Pastel, muted or brown orange instead of the saturated flame color.
- A soft, blurred glow streak instead of a hard-edged flame.
- Upright, regular-weight headings instead of bold italic uppercase.
- Rounded pill shapes anywhere — this is angles, not Barbie's curves.
- White text on the bright accent/danger/success fills.

## Don'ts

- **No white text on the orange, danger-red or green fills.** Use the near-black `--on-*` tokens (the brand badge's darker flame red `#e3171b` carries white at 4.77:1).
- **No pastel or muted orange, and no black field.**
- **No rounded pills or circles**; radius is `0.2rem`.
- **No upright, regular-weight, title-case headings.** Bold italic uppercase only.
- **No vertical gradients on buttons;** the flame runs at `135deg`.
- **No brand colours beyond blue, orange, yellow and flame red.**

## Icons

`icons.svg` redraws the full core set (178/178). Rules: 24 grid, heavy 2.6px
stroke with core's round caps/joins, plain sharp rects, a few boxy shapes
leaning into a slanted parallelogram edge, and short 1.4px speed lines
trailing motion icons (play, check, download, upload). Line only: nothing is
filled, marker dots are r1.2 rings, colour is always `currentColor`.

## Typography

`--font-display` is Barlow Semi Condensed ExtraBold Italic (OFL, vendored in `assets/fonts/`, see `NOTICE.md`), falling back to Antonio Bold (vendored for lcars, slanted by the browser), then `"Arial Narrow", "Liberation Sans Narrow", Impact`; it sets headings, buttons, nav items, the app bar's menubar links, tabs, the brand, panel headers, dialog headers, table header cells, KPI values and readouts at weight 800 with `0.01em` tracking. Labels inside buttons, nav items and tabs get `0.15em` of end padding so the italic's last letter is never clipped. It is the closest free match to the game menu's heavy, squarish semi-condensed italic caps (`MULTIPLAYER`, `BASEMENT`), not the real logo lettering. Body `--font` is a plain system sans (`Arial, "Helvetica Neue", "Liberation Sans"`); `--font-mono` is `"Courier New", Consolas, monospace`.

## Contrast honesty

- **Orange is not text on the bright blue.** `#ff8a1a` is 3.42:1 on `--surface` and 2.97:1 on `--surface-2`, so `--accent` (links, secondary buttons, GO, readouts, active tabs, the current breadcrumb) is the flame yellow `#ffd21a`: 4.68:1 on the bar, 4.83:1 on `--surface-2`, 5.5:1 on `--surface`. h1 uses `#ffcc00`. Orange stays a fill (buttons, avatars, pagination, accent badges, progress) and the track lip. Code blocks and their inserted/deleted lines sit in a darker `#0f2c88` well so token colours keep their margin; highlighted lines are a solid `#1a3d9c` (the yellow accent token holds 6.6:1 on it).
- **Dark text on the fills.** `--on-accent` `#1a0900` is 8.22:1 on `#ff8a1a`; `--on-danger` `#1a0000` 5.23:1 on `#ff2d2d`. Yellow fills (table header, dialog header) carry `#0a1a4a` at 11.0:1.
- **On the blues** `--text` white is 8.07:1 on `--surface` and 7.00:1 on `--surface-2`; `--muted` `#dbe4ff` is 6.36:1 on `--surface`, 5.52:1 on `--surface-2` and 5.34:1 on the bar. White on the selection blue `#2a64e8` is 5.14:1 and on the brand red `#e3171b` 4.77:1. On `--hw-lift` `#2a5ad6` white is 5.95:1 and `--muted` 4.69:1. Dark ink `#1a0900` on the primary flame's darkest stop `#ff5f00` is 6.36:1. The disabled `#b9c6ee` on `#3a4f8f` is 4.59:1.
- **Badges** are solid: `#1a0900` on `#ff8a1a` 8.22:1, `#0a1a4a` on `#ffcc00` 11.0:1, white on `#e3171b` 4.77:1, `#04220f` on `#29d17a` 8.46:1.
- **State colours as text:** `--danger-text` `#ffcccc` is 5.67:1 on `--surface`, `--success-text` `#9dffc8` 6.75:1.
- **The hexes are read off the captures by eye, not measured:** `RESEARCH.md` records no hex values.

## Reference status

`references/hot-wheels/` has 3 captures plus `RESEARCH.md`: `Hot-Wheels-Unleashed05282022-…jpg` (game menu: flame logo, orange track, italic chrome type), `aa470424….jpg` (flame-logo wallpaper) and the 1999 PC set webp (blue/yellow flame hardware). They back the orange track, flame motif and italic type. `RESEARCH.md` states there is no blister-pack card capture, so the blister-pack colours are not backed by a file, and although the outsider read in `RESEARCH.md` names a checkered-flag finish, no capture is described as showing one (unverified).

## v5 layout

- **Tiers.** No rail at any size. On phones and tablets (up to 900px) core puts the brand and the app's actions on the bar's first line and the nav on a second line. Core's rule makes that line a non-wrapping, sideways-scrolling strip when the nav is a direct child of the bar; on the demo dashboard the items still wrap onto a second row (the same in every theme), so this is not a theme override. The flame badge keeps its own width instead of stretching across the free space. The bar is plain blue at every width, so nothing turns into vertical slabs when it grows taller.
- **Nesting.** Each surface draws only its darker-blue edge and its bottom orange lip, so nested panels and cards need no step-down rules.
- **XL gutter art (1801px+).** A length of burnt-orange track (`#b84400` lips, `#8a3300` body) runs down each side, one repeating gradient.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
