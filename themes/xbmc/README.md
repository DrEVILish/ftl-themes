# XBMC

> XBMC in its Confluence skin (Kodi 14): a deep blue bokeh backdrop, a black glass menu strip of bold grey caps, and the focused label turning white over a glowing blue underline — driven by a remote, not a mouse.

**Requires: L1** — sets `--app-*` layout properties (the menu strip and bottom bar); recolours correctly at L0 but the strip-plus-underline composition needs the app shell.

## What this theme is trying to achieve

XBMC (later renamed Kodi) ran a horizontal top-level menu — Pictures,
Music, Videos, Programs, System — navigated with a d-pad/remote from a
couch. The theme commits to the Confluence era (`xbmc-confluence-14.jpg`):
the blue lives in the out-of-focus backdrop, the chrome over it is neutral
black glass with grey labels, and `#1e90ff` appears only as light — focus,
hover glow and the selection underline.

## Core values

1. **The focused label is white over a glowing underline, never a filled
   block.** Strip items are grey bold caps; the active one turns white
   with a 3px blue underline glowing beneath it
   (`:is(.nav-item, .menubar > li > button).is-active::after`). Toggle
   buttons and segmented items select with a lighter glass and a blue edge,
   not a blue fill.
2. **Blue backdrop, neutral chrome.** The page is a deep blue radial
   (`#0b3a80` → `#072659` → `#020a1a`) with faint bokeh discs, darkening
   toward the edges; surfaces are neutral `#121314` / `#1d1f22` glass, not
   blue-tinted.
3. **One blue, used as light.** `--accent` (`#1e90ff`) is a glow colour;
   only primary buttons still fill with it.

## Signature details

- The menu strip: `--app-bar-bg: linear-gradient(180deg, #2a2d31, #0b0c0e 45%, #000)`
  with a 1px `rgba(255,255,255,.18)` top hairline; items in uppercase bold
  `#9aa0a6`, 1.1rem, split by 1px faint separators.
- The active item's underline: 3px `--accent`,
  `box-shadow: 0 0 12px 2px rgba(30,144,255,.9)`.
- The submenu shelf: `.segmented` is a black gradient whose bottom corners
  are cut by `clip-path` (the 'Dateien | Addons' trapezoid), with dark
  separators between items.
- The bottom bar: `.app-status` is grey glass
  (`linear-gradient(180deg, #3a3d41, #141516)`) with a light top hairline.
- Flat rectangles: square slider thumb and switch knobs, a grey `#70767e`
  slider track.

## Tell-tales of an inauthentic result

- A filled blue block on the active nav item instead of a white label and
  underline glow.
- Blue-tinted panels — the chrome is neutral black glass; the blue is the
  backdrop.
- A flat, unvignetted backdrop.
- Thin or light-weight menu type — Confluence labels are bold caps.
- Round, glossy buttons or knobs.

## Don'ts

- **No filled highlight block on the active menu item.**
- **No blue-tinted surfaces**; keep chrome neutral.
- **No flat, unvignetted backdrop.**
- **No large radii or circles** on affordances.
- **No second brand colour.** One blue, used as light.

## Icons

`icons.svg` redraws the full core set (178/178). Rules: 24 grid, core 2px
stroke, `square` caps and `miter` joins set on each `<symbol>`, flat
rectangular geometry with no circles (round things become squares, the cloud
is stepped). Solid accents (note heads, dots, sand, pause bars, chart bars)
are `fill="currentColor" stroke="none"` rects; several nav/media icons carry
the 1px glowing-underline accent bar. Colour is always `currentColor`.

## Typography

`--font` is `"Titillium Web", "Arial Narrow", "Segoe UI", sans-serif`;
`--font-mono` is `Consolas, monospace`. Titillium Web (OFL, already vendored
in `assets/fonts/`) stands in for Confluence's bold, slightly condensed
sans; the skin's own face is not named. Headings are 700; strip items, tabs
and segmented items are uppercase 700 with 0.02em tracking.

## Contrast honesty

- `--accent` `#1e90ff` is a glow on black glass; `--on-accent` `#04101f`
  carries text on the few accent fills. `--accent-text` `#2d98ff` clears
  4.5:1 on its own 20% badge tint.
- Text `#e8e8e8` and muted `#aab0b6` sit on neutral `#121314` / `#1d1f22`;
  muted is lifted above the reference's darker grey so it also clears 4.5:1
  on the backdrop's brightest blue.
- Strip labels `#9aa0a6` clear 4.5:1 on the strip's lightest stop; the
  brand is white, as the KODI wordmark is.
- The hexes are eyeballed from `xbmc-confluence-14.jpg`, not sampled.

## Reference status

`references/xbmc/` holds 3 captures plus `RESEARCH.md`:

- `xbmc-main-screen-era.png` — an XBMC 2007 home screen: a stack of dark angled blade menu items (Programs/Pictures/Videos/Music/Weather), a clock and date, a green LED marking the selection. Backs the menu-item language and home-theatre darkness.
- `xbmc-musik.jpg` — a German 2007 skin variant with the same blades plus system-information and now-playing widgets. Backs the widget layout and dark glass panels.
- `xbmc-confluence-14.jpg` — Kodi 14 Confluence: a horizontal caps menu strip with a sub-menu drop under a blue bokeh backdrop. Backs the horizontal top menu, on which the theme's layout is based.

Not backed: the glowing blue underline itself (Confluence marks focus by whitening the label; the 2007 skins use a green LED) — it is kept as the theme's remote-focus cue, under the white label the capture does show. The 2007 blade/LED language is not used. (An earlier note here saying no `references/xbmc/` folder exists was wrong.)

## v5 layout

- **Tiers.** Desktop and tablet are the same shell (there is no rail to
  drop). On mobile the category tiles lose the big home-screen padding,
  the strip's caps step down to 0.95rem, and the taskbar tray keeps a
  small inline-end margin off the status-bar edge. A number field in a
  table cell keeps at least `--tap-min` of width.
- **Nesting.** The home-screen tile look (big padding, centred label,
  black glass with a light top edge, hover glow and lift) is for top-level
  cards. A card nested in a panel, card, dialog or drawer steps down to
  normal padding, left-aligned text and a hairline frame; a card holding a
  table, form or list stays left-aligned. The hover lift only applies on
  devices that can hover.
- **XL gutter art.** More of the out-of-focus backdrop: faint bokeh discs,
  within about 1.2:1 of `--bg`. Still.
