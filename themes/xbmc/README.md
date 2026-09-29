# XBMC

> The original Xbox Media Center: a near-black home-theatre shell, a wide horizontal top menu, and a glowing blue underline marking whichever item is selected — driven by a remote, not a mouse.

**Requires: L1** — sets `--app-*` layout properties (the wide top menu bar); recolours correctly at L0 but the horizontal-menu-plus-underline composition needs the app shell.

## What this theme is trying to achieve

XBMC (later renamed Kodi) ran a horizontal top-level menu — Pictures,
Music, Videos, Weather, Programs, System — navigated with a d-pad/remote
from a couch, not a mouse from a desk. Its brand colour was always a
clean, saturated blue, carried through as a glow rather than a filled
highlight, against a near-black "home theatre" backdrop that vignettes
toward the edges.

## Core values

1. **The underline is the selection state, not a filled pill.** A glowing
   blue line beneath the active label, never a solid background block —
   see `.nav-item.is-active::after`.
2. **Near-black, not pure black, and vignetted.** The frame should read
   as a dim room, darkening toward the edges via the radial-gradient page
   background, not a flat single colour.
3. **One blue, used as light, not as fill.** `--accent` (`#1e90ff`)
   is a glow colour — box-shadow and border-highlight — more often than a
   background fill.

## Signature details

- The glowing underline on the active top-menu item
  (`box-shadow: 0 0 8px rgba(30,144,255,0.8)`).
- The vignette page background (radial-gradient darkening from top-centre
  outward).
- Thin, quiet chrome: 1px borders, small border-radius, no gloss or
  gradient buttons — a remote-driven UI has no hover state to sell with
  gloss.

## Tell-tales of an inauthentic result

- A filled/solid highlight block on the active nav item instead of an
  underline glow.
- A flat, unvignetted background — the "home theatre" read depends on the
  edges going darker than the centre.
- Rounded, glossy buttons — this UI's affordances are flat rectangles with
  a border, not skeuomorphic buttons.

## Don'ts

- **No filled highlight block on the active menu item**; the selection is a glowing underline.
- **No flat, unvignetted backdrop.**
- **No gloss, gradient buttons or large radii.** Flat rectangles with a border.
- **No second brand colour.** One blue, used as light.
- **No saturated pure black**; the shell is a blue-tinted near-black.

## Typography

`--font` is `"Segoe UI", "Helvetica Neue", Arial, sans-serif`; `--font-mono` is `Consolas, monospace`. **System fonts, nothing vendored.** The captures show wide-tracked bold/condensed caps on the menu (`xbmc-confluence-14.jpg`: grey all-caps blade labels; the 2007 skins: bold sans labels) (the theme sets some menu text at weight 300 instead). No face was identified from the captures, so the stack is a neutral sans, not a match.

## Contrast honesty

- **Blue on near-black is comfortable:** `--accent` `#1e90ff` is 5.98:1 on `--bg` `#0a0e14` and 5.61:1 on `--surface`; `--on-accent` `#04101f` is 5.90:1 on it. No lift was needed.
- **Muted** `#93a7c7` is 7.43:1 on `--surface`; text `#dbe6f5` is 14.4:1.
- **Reference vs shipped colour (uncertain).** `RESEARCH.md` says "dark blue-grey" blades; the two 2007-skin captures show neutral charcoal/black brushed panels with a lime-green selection LED, and only `xbmc-confluence-14.jpg` shows the blue (a blue bokeh backdrop with a black horizontal strip). So `#1e90ff` follows the Kodi/Confluence-era brand blue for the selection glow, not the 2007 blade colours, and the blue-tinted `#0a0e14` is a compromise between them. The hexes were not sampled.

## Reference status

`references/xbmc/` holds 3 captures plus `RESEARCH.md`:

- `xbmc-main-screen-era.png` — an XBMC 2007 home screen: a stack of dark angled blade menu items (Programs/Pictures/Videos/Music/Weather), a clock and date, a green LED marking the selection. Backs the menu-item language and home-theatre darkness.
- `xbmc-musik.jpg` — a German 2007 skin variant with the same blades plus system-information and now-playing widgets. Backs the widget layout and dark glass panels.
- `xbmc-confluence-14.jpg` — Kodi 14 Confluence: a horizontal caps menu strip with a sub-menu drop under a blue bokeh backdrop. Backs the horizontal top menu, on which the theme's layout is based.

Not backed: the theme's glowing underline itself (none of the captures shows one — selection is a green LED or a lighter blade) and the specific hexes. (An earlier note here saying no `references/xbmc/` folder exists was wrong.)
