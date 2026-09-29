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
   buttons, panels, modals — the defining Norton Commander visual.
3. **Uppercase, always.** Text-mode software shouted in caps.
4. **Cyan is the bright accent; yellow is reserved further still** (used
   only as `--flare` and warning) — this is a two-tier bright system,
   not a rainbow.
5. **Zero radius.** Text-mode has no curves.

## Signature details

- `border-style: double` at 3px is set on every bordered component in one
  rule (`.input`, `.select`, `.textarea`, `.btn`,
  `.panel`, `.modal`, `.dropdown`) — one declaration carries
  the entire visual signature.
- `#0000aa` is the exact classic DOS/VGA "blue" palette index, not an
  approximation — this theme's background is a real 16-color EGA/VGA value.
- The nav bar, app bar, and status strip all fill solid cyan
  (`--accent`) with black text — the one place a "bright" color
  becomes a background instead of a foreground.

## Layout

A bar and status strip both filled solid cyan with black text — the
Norton Commander function-key bar — with the rest of the shell staying
DOS blue.

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

## Typography

`--font` and `--font-mono` are **Px437 IBM VGA 9x16**, vendored (`assets/fonts/Web437_IBM_VGA_9x16.woff2`): VileR's pixel-exact reproduction of the IBM VGA ROM font in the 9x16 cell that 720x400 text mode actually drew, from the Ultimate Oldschool PC Font Pack. Licensed **CC BY-SA 4.0** (not OFL like most of `assets/fonts/`) — attribution in `assets/fonts/NOTICE.md`. It renders crisply at 16px and its multiples.

## Contrast honesty

The palette is the standard 16-colour VGA text palette (blue `#0000aa`, cyan `#00aaaa`, light grey `#aaaaaa`, light yellow `#ffff55`, light red `#ff5555`, light green `#55ff55`, light cyan `#55ffff`). These are the well-known VGA values, not sampled from the captures (`RESEARCH.md` records no hex).

- **Cyan on blue:** `--accent` `#00aaaa` on `#0000aa` is 4.64:1 (passes AA by a hair). The Norton cursor bar puts black on cyan, 7.33:1.
- **Yellow on blue:** `#ffff55` is 12.46:1; light cyan `#55ffff` is 10.84:1.
- **Grey on blue:** `--muted` `#aaaaaa` is 5.72:1 on `#0000aa`, 4.83:1 on `--surface-2` `#0000cc`.
- **The one deviation:** real light red `#ff5555` is only 4.23:1 on the blue, so text uses `--danger-text` `#ff7e7e` (5.40:1) and the raw hex is fill-only.

## Reference status

`references/msdos/` has 6 captures plus `RESEARCH.md`: an icon-library grid, MS-DOS 6.22 VirtualBox setup and welcome screens, a `moricons.dll` picker dialog, an MS-DOS 2.0 floppy photo and a DOS 5.0 setup screen. They back the blue text-mode field and box chrome. `RESEARCH.md` states there is **no Norton Commander two-panel capture**, so the twin-panel layout, cyan cursor bar and F-key bar are described in RESEARCH text, not shown in any file.

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
- **Headings and column heads** are bright yellow `#ffff55`, no fills.
- **Buttons** are solid blocks with a hard black shadow one cell
  down-right, dropped when pressed; primary is yellow.
- **Dialogs** are grey with black text, an inset white double line and a
  hard black drop shadow; red text inside them is `#800000` (VGA
  `#aa0000` is only 3.3:1 on the grey).
- **F-key bar:** the status strip opens with Norton's `1Help … 10Quit`
  row — grey key numbers on black, black labels on cyan blocks, drawn as
  two overlaid monospaced pseudo-element strings.
- **Font:** the real IBM VGA 9x16 text-mode glyphs (Px437, CC BY-SA 4.0).

