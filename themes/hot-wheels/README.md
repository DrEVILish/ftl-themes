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

1. **Blue is the field, orange is the track.** `--bg` `#0a1a4a`,
   `--surface` `#12267a`, `--surface-2` `#183090` and the bar's
   `--hw-blue` `#1f4fd1` follow the blue that dominates every capture.
   Orange (`#ff5f00` outlines and fills, `#ff8a1a` as `--accent` text) is
   trim, never the background. A washed-out or brown orange has missed the
   point.
2. **Condensed, heavy, italic, uppercase.** Headings, buttons, nav, tabs
   and the brand use Antonio Bold slanted, white with a hard dark drop
   shadow (h1 in orange), like the menu's `MULTIPLAYER / BASEMENT` labels.
   No glow.
3. **Angles, not curves.** `--radius: 0.35rem`; badges `0.15rem`, switches
   `0.2rem`. Buttons use an angled (`135deg`) flame gradient.
4. **The flame, the band and the checkered flag are the signature shapes.**
   The brand badge is the flame logo; the bar sits on the PC set's yellow
   band with orange and red pinstripes; the status strip is a checkered
   flag.
5. **Dark text on the bright fills.** `--on-accent`/`-danger`/`-success`
   are near-black; yellow fills carry deep-blue text.

## Signature details

- The brand badge carries the flame: three hard-edged tongues (red
  `#e3171b`, orange `#ff5f00`, yellow core `#ffcc00`) swept back to points
  on the left, a red body behind the white wordmark, a slanted right edge.
  It is an inline SVG background, so nothing decorative ever sits behind
  nav text.
- The app bar is solid `--hw-blue` with a 4px yellow rule and orange then
  red 3px pinstripes under it, the PC monitor's band. Dialog headers are
  the same yellow band with the pinstripes along their bottom edge.
- The selected nav item and tab are the game menu's slanted bright-blue bar
  (`#2a64e8`, painted as a background with angled ends, not clip-path, so
  focus rings are never clipped) with white italic text; selected table
  and list rows use the same blue.
- Table headers are the yellow band with deep-blue text.
- The slider is a length of orange track with lighter and darker lips and
  a yellow thumb.
- The status bar's checkered flag uses a small `0.6rem` tile so it reads
  as a flag trim, not a chessboard.

## Layout

The app shell becomes a **blue track panel**: a blue bar with the flame
logo badge, a yellow rule with orange/red pinstripes under it, a deep-blue
main well, and a checkered-flag status strip along the bottom.

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
- **No rounded pills**; radius is `0.35rem`.
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

`--font-display` is Antonio Bold (OFL, vendored in `assets/fonts/` for lcars), slanted by the browser, falling back to `"Arial Narrow", "Liberation Sans Narrow", Impact`; it sets headings, buttons, nav items, tabs, the brand and dialog headers. It is the closest free condensed heavy face to the game menu's italic caps, not the real logo lettering. Body `--font` is a plain system sans (`Arial, "Helvetica Neue", "Liberation Sans"`); `--font-mono` is `"Courier New", Consolas, monospace`.

## Contrast honesty

- **Orange as text was lifted, orange as a fill was not.** `#ff5f00` is only 4.35:1 on `--surface` and 3.70:1 on `--surface-2`, so `--accent` (used by core for links, active tabs and breadcrumbs) is `#ff8a1a`: 5.62:1 on `--surface`, 4.78:1 on `--surface-2`, 7.07:1 on `--bg`. Outlines, buttons and the slider keep `#ff5f00`.
- **Dark text on the fills.** `--on-accent` `#1a0900` is 8.22:1 on `#ff8a1a`; `--on-danger` `#1a0000` 5.23:1 on `#ff2d2d`. Yellow fills (table header, dialog header) carry `#0a1a4a` at 11.0:1.
- **On the blues** `--text` white is 13.3:1 on `--surface`; `--muted` `#c5d3ff` is 8.9:1 on `--surface`, 7.6:1 on `--surface-2` and 4.56:1 on the bar. White on the selection blue `#2a64e8` is 5.14:1 and on the brand red `#e3171b` 4.77:1.
- **Accent badges:** core tints `.badge-accent` 20% orange into `--surface` (`#413a67`), where `#ff8a1a` is 4.39:1, so `.badge-accent` sets `--badge-fg: #ffa040` (5.11:1).
- **Red as text:** `--danger-text` `#ff8080` is 5.46:1 on `--surface`.
- **The hexes are read off the captures by eye, not measured:** `RESEARCH.md` records no hex values.

## Reference status

`references/hot-wheels/` has 3 captures plus `RESEARCH.md`: `Hot-Wheels-Unleashed05282022-…jpg` (game menu: flame logo, orange track, italic chrome type), `aa470424….jpg` (flame-logo wallpaper) and the 1999 PC set webp (blue/yellow flame hardware). They back the orange track, flame motif and italic type. `RESEARCH.md` states there is no blister-pack card capture, so the blister-pack colours are not backed by a file, and although the outsider read in `RESEARCH.md` names a checkered-flag finish, no capture is described as showing one (unverified).

## v5 layout

- **Tiers.** No rail at any size. On phones and tablets (up to 900px) core puts the brand and the app's actions on the bar's first line and the nav on a second line. Core's rule makes that line a non-wrapping, sideways-scrolling strip when the nav is a direct child of the bar; on the demo dashboard the items still wrap onto a second row (the same in every theme), so this is not a theme override. The flame badge keeps its own width instead of stretching across the free space. The bar is plain blue at every width, so nothing turns into vertical slabs when it grows taller.
- **Nesting.** Nothing is drawn per surface beyond the 1px orange outline, so nested panels and cards need no step-down rules.
- **XL gutter art (1801px+).** A length of orange track runs down each side, raised lips and dark joints every 120px, burnt down close to the deep blue.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
