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
   with a blue underline glowing beneath it
   (`:is(.nav-item, .menubar > li > button).is-active::after`), a slim 2px
   line with a 6px glow so the white label carries the focus. Toggle
   buttons and segmented items select with a lighter glass and a blue edge,
   not a blue fill; so do the current page, active filter chips, a range
   picker's chosen button and selected table/list rows (opaque `#26292d`
   with the blue edge marker).
2. **Blue backdrop, neutral chrome.** The page is a blue radial
   (`#0a6aa8` → `#044070` → `#03265c` → navy `#001542` at the edges) under a
   bright cyan-white bloom above centre under a field of
   saturated royal-blue bokeh discs and soft diagonal light rays; surfaces are neutral
   `#121314` / `#1d1f22` glass, not blue-tinted.
3. **One blue, used as light.** `--accent` (`#1e90ff`) is a glow colour;
   only primary buttons still fill with it.

## Signature details

- The backdrop: a fixed, viewport-sized `body::before` layer
  (`contain: strict`, so scrolling never repaints it) holding lens bokeh at
  three depths: 14 near discs of 1.5-9rem — a dim `rgba(20,80,215,.16)`
  centre brightening to royal blue `rgba(20,80,215,.42)` /
  `rgba(25,95,225,.32)`, overlapping in a cluster upper right, one small
  bright cyan `rgba(70,190,240,.5)` — each with a soft 4-5px edge (a
  `rgba(90,170,250,.5)` rim fading through a `.15` halo); five far discs
  (fill `.12`, rim `.2`); and four fully defocused solid blobs melting into
  the field. Over them a bright cyan-white bloom above centre (an 18rem by
  12rem ellipse of `rgba(120,200,255,.35)` at 50% 30%, cyan haze around
  it), soft blue blobs and two 60° light rays (`rgba(80,170,255,.12-.14)`),
  all over the blue radial. Phones draw six discs on the radial only (no
  rays or haze).
- The menu strip: a tall 4rem band,
  `--app-bar-bg: linear-gradient(180deg, #232323, #141414 50%, #050505)`
  with a bevelled lip (1px `rgba(255,255,255,.28)` top, a fainter bottom
  hairline, `0 2px 0 #000` and a soft drop shadow under it); items in large
  (`clamp(1rem, 1.6vw, 1.75rem)`, so 28px caps fill the band on wide
  screens as 'VIDEOS' does) uppercase bold neutral `#8e8e8e` with a
  `0 1px 0 #000` emboss, in equal cells (up to 14rem) centred across the band, split by 1px faint
  separators. On phones the strip scrolls sideways and the tools stay on
  one row, the theme picker shrinking so the account button stays visible.
- The active item's underline: 2px `--accent`,
  `box-shadow: 0 0 6px 1px rgba(30,144,255,.8)`.
- Tabs inside a window, dialog, panel or card step down to 0.75rem caps
  on one sideways-scrolling row, so a dialog's buttons stay in its frame.
- Page-level text straight on the backdrop (title, lede, breadcrumbs, the
  control rows) carries a dark `0 1px 2px #000, 0 0 4px` shadow halo.
- The submenu shelf: `.segmented` is a black gradient whose bottom corners
  are cut on a 1.25rem diagonal by `clip-path` (the 'Dateien | Addons'
  trapezoid), 1.5rem end padding, dark separators, and regular-weight
  sentence-case `#c4cad0` items, as 'Dateien' is.
- The bottom bar: `.app-status` is a tall grey glass band (at least 3.5rem,
  `linear-gradient(180deg, #3a3a3a, #1a1a1a)`, 1rem padding) with a light
  top hairline; its icon buttons are framed glass squares (1px `#000`,
  inset top highlight).
- Flat rectangles: square slider thumb and switch knobs, a grey `#70767e`
  slider track; icon buttons, badges/chips and avatars take `--radius`;
  status, carousel (including the native `::scroll-marker` dots and
  `::scroll-button` arrows), dock and page dots are small squares (no
  circles or pills).
- Phone home screen and dock: framed black-glass keys
  (`linear-gradient(180deg,#2a2d31,#141517)`, `--radius`, white glyphs), as
  the star and power keys; no coloured squircles, square dock.

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
Extended (non-core) icons such as `coin-*`, `camera-*`, `map-pin-*` and
`circle-caret-*` still come from the generic outline set and keep their
circles; redrawing them is open work.

## Typography

`--font` is `"DejaVu Sans", Roboto, "Segoe UI", Arial, sans-serif`:
Confluence draws strip, shelf, search and ticker in one face, Kodi's
bundled DejaVu-derived sans (shipped as `arial.ttf`). Headings are 700.
Strip items and tabs are the same face, uppercase 700, no extra tracking;
segmented items (the submenu shelf) are 400 in sentence case. KPI values
use the bold sans too (`--readout-font: var(--font)`, tabular numbers), as
Confluence's clock does. `--font-mono` is
`Consolas, "DejaVu Sans Mono", "Liberation Mono", monospace`.

## Contrast honesty

- `--accent` `#1e90ff` is a glow on black glass; `--on-accent` `#04101f`
  carries text on the few accent fills. `--accent-text` `#2d98ff` clears
  4.5:1 on its own 20% badge tint.
- Text `#e8e8e8` and muted `#c4cad0` sit on neutral `#121314` / `#1d1f22`;
  muted is lifted above the reference's darker grey so it also clears 4.5:1
  on the backdrop's brightest blue. Links use `--accent-2` `#7fc4ff` for
  the same reason.
- The backdrop's open centre is `#0a6aa8` under the bloom, reaching about
  `#1e71b8`, near the capture's `#0b8cc8`. Muted `#c4cad0` over that is
  about 3:1 by colour alone; page-level text there carries a dark shadow
  halo instead of the backdrop being dimmed (the reference's brightness
  wins). Text on surfaces is on opaque `#121314` / `#1d1f22` glass and is
  unaffected.
- The discs are royal blue (hue ~220), which is vivid but low in luminance,
  so muted text over a disc still clears 4.5:1. The capture's bright cyan
  discs (`#057ac9`, `#38bbd9`) would not; only one small cyan disc is kept,
  and text that happens to cross it can fall below 4.5:1.
- Strip labels `#8e8e8e` (neutral, no blue cast) clear 4.5:1 on the strip's lightest stop; the
  brand is white, as the KODI wordmark is.
- The backdrop and strip hexes are sampled from `xbmc-confluence-14.jpg`
  (strip `#191919`-`#2c2c2c`, backdrop `#0365a2` → `#043e6c` → `#031637`);
  the strip label is lifted from the capture's `#4d4d4d`-`#515151` to
  `#8e8e8e`, the darkest neutral grey that keeps 4.5:1.

## Reference status

`references/xbmc/` holds 3 captures plus `RESEARCH.md`:

- `xbmc-main-screen-era.png` — an XBMC 2007 home screen: a stack of dark angled blade menu items (Programs/Pictures/Videos/Music/Weather), a clock and date, a green LED marking the selection. Backs the menu-item language and home-theatre darkness.
- `xbmc-musik.jpg` — a German 2007 skin variant with the same blades plus system-information and now-playing widgets. Backs the widget layout and dark glass panels.
- `xbmc-confluence-14.jpg` — Kodi 14 Confluence: a horizontal caps menu strip with a sub-menu drop under a blue bokeh backdrop. Backs the horizontal top menu, on which the theme's layout is based.

Not backed: the glowing blue underline itself (Confluence marks focus by whitening the label; the 2007 skins use a green LED) — it is kept as the theme's remote-focus cue, under the white label the capture does show. The 2007 blade/LED language is not used. (An earlier note here saying no `references/xbmc/` folder exists was wrong.)

## v5 layout

- **Tiers.** Desktop and tablet are the same shell (there is no rail to
  drop). On mobile the category tiles lose the big home-screen padding and
  their outer blur shadow, cards and panels go opaque and drop their outer
  shadow (cheaper scrolling), segmented
  and toggle rows scroll sideways instead of wrapping a label,
  the strip's caps step down to 0.8rem so the strip stays one row (a plain
  `.nav` in the bar scrolls sideways instead of wrapping), the bar's tool
  cluster stays one row and scrolls sideways, and the taskbar
  tray keeps a small inline-end margin off the status-bar edge. A number field in a
  table cell keeps at least `--tap-min` of width.
- **Nesting.** The home-screen tile look (big padding, centred label,
  black glass with a light top edge, hover glow and lift) is for top-level
  cards. A card nested in a panel, card, dialog or drawer steps down to
  normal padding, left-aligned text and a hairline frame; a card holding a
  table, form, list or KPI (`.stat-*`, `.sparkline`) stays left-aligned. The hover lift only applies on
  devices that can hover.
- **XL gutter art.** More of the out-of-focus backdrop: faint bokeh discs,
  within about 1.2:1 of `--bg`. Still.
