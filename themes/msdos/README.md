# MS-DOS (Norton Commander)

> Classic blue-and-white text-mode with double-line borders and bright cyan.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The 16-colour VGA text-mode look of Norton Commander: a solid blue field,
white double-line box borders, and bright cyan/yellow used exactly the way
DOS text mode used them — as the two "bright" colours in an otherwise flat
16-colour palette.

## Core values

1. **Sixteen colours, flat.** No gradients, no glow, no anti-aliasing feel.
2. **Double-line borders everywhere a real border is drawn** — inputs,
   buttons, toggles, switches, panels, modals, menus, popovers, list
   boxes, alerts and toasts — the defining Norton Commander visual.
3. **Uppercase for titles, mixed case for text.** Headings, column heads,
   buttons and title tabs are uppercase; body text, menus and lists are
   mixed case, as on the DOS setup screens in the references.
4. **Cyan is the bright accent; yellow is reserved further still** (used
   only as `--flare` and warning) — this is a two-tier bright system,
   not a rainbow.
5. **Zero radius.** Text-mode has no curves: badges, switches, avatars,
   presence dots, carousel dots and arrows, notification dots, the
   saving marker, icon buttons, status dots and the slider thumb are
   square cells; checkboxes and radios are `[X]` and `(•)` text;
   spinners are the stepped `| / - \` text cursor.
6. **One weight.** The VGA font has no bold, so faux bold is switched off
   (`font-synthesis-weight: none`); emphasis is colour.
7. **One cell size.** The 9x16 glyphs are drawn at 16px (h1 and stat
   figures at 32px), never at a fractional size that smears the pixels;
   labels, hints, badges, table heads, buttons, menubars, logs, legends,
   chart text, tree rows, desktop icon labels, readouts, price units,
   carousel arrows and page numbers, schedule chips, meter labels and the
   sticky header are all 16px (a large readout or price is 32px).

## Signature details

- `border-style: double` at 3px is set on every bordered component
  (`.input`, `.select`, `.textarea`, `.btn`, `.panel`, `.modal`,
  `.dropdown`, `.context-menu`, `.popover`, `.list`, `.alert`, `.toast`,
  `.toggle-btn`, the switch track) — alerts and toasts keep their state
  colour as the line colour on the plain `#0000aa` field.
- `#0000aa` is the exact classic DOS/VGA "blue" palette index, not an
  approximation — this theme's background is a real 16-color EGA/VGA value.
- The app bar and every in-window menubar are EDIT's grey `#aaaaaa` menu
  bar with black items; the status strip is black with Norton's F-key row
  of black-on-cyan label blocks. Cyan becomes a fill only for the cursor
  bar (selected rows, the active tab, the current nav or folder-rail
  link) and the
  panel title tab, always with black text — the `[X]` glyph included.
- Badges are reverse-video VGA cells: black on grey, cyan, light red,
  light green or yellow. Lamps are lit cells with no glow; GO is the
  yellow primary block with the button's hard shadow.
- Desktop windows have no title icon: the `[■]` close box sits at the
  left of the title bar, as in DOS dialogs.
- Progress bars are the DOS 5 setup bar: a yellow block run in a white
  box. Meters keep their green/yellow/red ramp.
- The phone home screen and dock are flat reverse-video cells (each app's
  VGA colour, black glyph): no squircle, gloss, shadow or round page
  dots, and 16px names that wrap only between words.
- Presence is a half-cell block standing off the avatar's corner, clear of
  the initials. A button attached in an `.input-group` drops its shadow.
- Tables draw cyan box-drawing column rules (│) and no row hairlines.
- A dialog's title is cut into its inner double line, centred on a grey
  patch, as DOS and Norton dialogs drew it.
- No tinted state washes: invalid fields keep the blue field (the red
  double line carries it), an answered list card keeps its card fill, the
  bulk-selection bar is black, and the modal backdrop is a black 50%
  dither (the ░ shade) instead of translucent black.

## Layout

A grey EDIT menu bar on top, the DOS-blue work area, and a black status
strip carrying the Norton Commander function-key bar along the bottom.

## Tell-tales of an inauthentic result

- Single-line or no borders on panels/buttons → the double-line is the
  entire visual signature.
- Lowercase headings.
- Any softness — gradients, shadows, rounded corners — none of it existed
  in text mode.

## Don'ts

- **No radius, no shadow, no gradient, no transitions.** Text-mode cells only.
- **No colour outside the 16-colour VGA set.** Blue, cyan, white, yellow, light greys, light red/green.
- **No single-line borders** where the double-line box characters belong.
- **No proportional font.** No smooth weights.
- **No white cursor bar:** the selection is cyan with black text.

## Icons

`themes/msdos/icons.svg` covers the full core set (178/178). Style rules:
24 grid; uniform 2.5px stroke, square caps, miter joins, `fill: none`;
no arcs anywhere, like a text-mode character cell: circles become squares,
curves become stepped or 45 degree runs (the cloud and moon are stepped
outlines, reused by cloud-bolt, cloud-off and moon-stars); dots are 2x2
stroked cells; nothing is filled. Colour is `currentColor` only.
Extended icon families outside the core set (coins, clocks, message
bubbles, hearts, cloud variants) still fall back to the shared rounded
outline set.

## Typography

`--font` and `--font-mono` are **Px437 IBM VGA 9x16**, vendored (`assets/fonts/Web437_IBM_VGA_9x16.woff2`): VileR's pixel-exact reproduction of the IBM VGA ROM font in the 9x16 cell that 720x400 text mode actually drew, from the Ultimate Oldschool PC Font Pack. Licensed **CC BY-SA 4.0** (not OFL like most of `assets/fonts/`) — attribution in `assets/fonts/NOTICE.md`. It renders crisply at 16px and its multiples.

## Contrast honesty

The palette is the standard 16-colour VGA text palette (blue `#0000aa`, cyan `#00aaaa`, light grey `#aaaaaa`, light yellow `#ffff55`, light red `#ff5555`, light green `#55ff55`, light cyan `#55ffff`). These are the well-known VGA values, not sampled from the captures (`RESEARCH.md` records no hex).

- **Cyan on blue:** `--accent` `#00aaaa` on `#0000aa` is 4.64:1 (passes AA by a hair). The Norton cursor bar puts black on cyan, 7.33:1.
- **Yellow on blue:** `#ffff55` is 12.46:1; light cyan `#55ffff` is 10.84:1.
- **Cyan as text:** the dim cyan `#00aaaa` is only 4.64:1 on the blue, so links, `--accent-text` (code keywords) and outlined-button labels use light cyan `#55ffff`; badges are solid cells with black ink (black on cyan 7.33:1). Inside a reverse-video panel title tab every word is black on cyan (VGA greys and brights are 1.2-2.2:1 there), and sheets and the command palette take the grey dialog's black ink.
- **Grey on blue:** `--muted` `#aaaaaa` is 5.72:1 on `#0000aa` and 9.04:1 on `--surface-2`, which is VGA black `#000000` (hover cells, code chips, tracks), not an off-palette brighter blue.
- **Disabled buttons** are VGA dark grey `#555555` on black, below 4.5:1 on purpose: disabled controls are exempt, and that is how DOS greyed them.
- **Body text stays white:** the DOS setup screens run their text in light grey `#aaaaaa`, but that is 5.72:1 on the blue, under the 7:1 body-text floor, so `--text` is white `#ffffff` (8.6:1) and grey is kept for muted text.
- **The one deviation:** real light red `#ff5555` is only 4.23:1 on the blue, so text uses `--danger-text` `#ff7e7e` (5.40:1) and the raw hex is fill-only.

## Reference status

`references/msdos/` has 6 captures plus `RESEARCH.md`: an icon-library grid, MS-DOS 6.22 VirtualBox setup and welcome screens, a `moricons.dll` picker dialog, an MS-DOS 2.0 floppy photo and a DOS 5.0 setup screen. They back the blue text-mode field and box chrome. `RESEARCH.md` states there is **no Norton Commander two-panel capture**, so the twin-panel layout, cyan cursor bar and F-key bar are described in RESEARCH text, not shown in any file.

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). Phone and tablet keep the grey menu bar, blue work area and F-key strip. On a phone the brand keeps its full name on the bar's first line, and a bar button with a shortcut hint folds to its icon so the controls fit one line. Nested titled boxes leave headroom for their title tab. Boxes inside a grey dialog take the screen's white-on-blue inks back, and a drawer or `.scroll` panel puts its title tab inside the box rather than on its top edge, where scrolling would clip it. On XL the gutters show the Turbo Vision desktop: the CP437 light-shade fill (░) as hard-edged 1px cells in dim blue, about 1.4:1 against `--bg`.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

## Shell and chrome (2026-09 pass)

- **Menu bar:** the app bar is EDIT/QBasic's grey `#aaaaaa` menu bar with
  black items; the open item is inverted (black, grey text).
- **Boxes:** panels, cards and the work area are cyan `#55ffff`
  double-line boxes, with the panel title set *into* the top line,
  centred, reverse video — Norton's drive tab.
- **Headings and column heads** are bright yellow `#ffff55`, no fills
  (an `h1` on a grey dialog, sheet or bar turns VGA blue `#0000aa`).
- **Charts and loaders** are flat: no translucent area fills, chart
  strokes are drawn with `shape-rendering: crispEdges`, and a
  skeleton is a still ░ shade block instead of a shimmer.
- **Buttons** are solid blocks with a hard black shadow one cell
  down-right, dropped when pressed; primary is yellow.
- **Dialogs** are grey with black text, an inset white double line and a
  hard black drop shadow; red text inside them is `#800000` (VGA
  `#aa0000` is only 3.3:1 on the grey).
- **F-key bar:** the status strip opens with Norton's `1Help … 10Quit`
  row — grey key numbers on black, black labels on cyan blocks, drawn as
  two overlaid monospaced pseudo-element strings. From the desktop tier
  the ten cells divide the strip's full width evenly (tab stops at
  `10cqi`), as Norton's spanned all 80 columns; below it the keys run at
  8 cells each and clip. The row is decorative (empty alt text, so screen
  readers skip it) and is left off the desktop page, whose Start taskbar
  is the status strip.
- **Font:** the real IBM VGA 9x16 text-mode glyphs (Px437, CC BY-SA 4.0).

