# XMB

> The PlayStation 3 / PSP dashboard: the Cross Media Bar itself — a horizontal row of glowing category icons over a deep-blue wave, with sub-items dropping straight down from whichever one is selected.

**Requires: L1** — sets `--app-*` layout properties (a centred, smoked-glass app-bar over the wave); recolours correctly at L0 but the actual cross-shaped layout only appears once the app shell is adopted.

## What this theme is trying to achieve

The XMB isn't a window manager or a set of panels — it's one horizontal
row of icons (Users, Settings, Photo, Music, Video, Game, Network,
Friends...) with a vertical list of that category's items appearing
directly below the selected one. Everything floats, translucent, over a
slowly animated blue wave; nothing is opaque or hard-edged. This theme
reproduces the float-and-glow language rather than the wave's motion,
which doesn't translate to a general-purpose page background.

## Core values

1. **Nothing is a filled block.** Every surface — cards, inputs, the nav
   itself — is a translucent tint over the wave gradient, never an opaque
   fill. An opaque panel is the fastest way to look like a generic dark
   dashboard instead of XMB. **Exception: overlays.** A PS3 system dialog
   dims the XMB almost to black and sits on it as a dark smoked-glass box
   with thin white rules (`references/xmb/modalDialog.jpg`), so the modal,
   toast and tooltip are near-opaque navy (`--modal-bg` 94%, `--toast-bg`
   94%, `--tooltip-bg` 96%) over a heavy, near-opaque `--overlay-bg`.
2. **Selection is a glow, not a fill.** The active icon/row gets a soft
   blue glow and a scale-up, not a solid highlight block — see
   `--btn-shadow-hover` and the icon-button hover rule.
3. **The bar is centred, not left-aligned.** Real XMB's icon row runs
   through the horizontal centre of the screen; a left-anchored nav bar
   reads as a generic app, not XMB.

## Signature details

- The wave: royal blue lit from the top right and falling to navy at the
  bottom left (sampled from `xmb-retroarch-main-menu.jpg`: #0056b9 upper
  left, #0398f6 top right, #021059 bottom left), with a translucent white
  ribbon sweeping across the lower middle of the first screen (from 38vh):
  two feathered sheets (5% and 3% white, Gaussian-blurred inside the SVG
  so their edges are soft, as in the captures), two blurred edge strokes,
  one crisp 12% highlight line and a few tiny sparkle dots (the PS3's
  particles). The opacities are held low so `--muted` stays at about
  4.6:1 or better averaged over the band; only the 1.5px highlight line
  dips to about 4.1:1 where a glyph crosses it. The highlight and ribbon are sized to the viewport,
  so a long page doesn't stretch them; the same ribbon continues in the XL
  gutters.
- Glass is tinted the wave's own deep blue (`--surface`
  `rgba(0,22,80,.38)`; the tinted `.band` a lighter `rgba(0,22,80,.18)`), not white, so panels read as blue glass rather than
  grey blocks; the folder rail and toolbars are transparent and rounded.
  Panels and cards have no box edge to speak of: a 10% hairline
  (`--panel-border`) and a top highlight (`--panel-shadow`
  `inset 0 1px 0`), no drop shadow, as content floats on the wave in the
  captures.
- The category row is centred in a smoked-glass capsule: the theme
  neutralises the demo headers' auto-margin spacers so the row takes the
  free space on both sides. The selected category is the lit one, as the
  XMB's selected icon is twice its neighbours' size: 1.35rem white with a
  white halo against 0.95rem pale-blue neighbours. A category that carries
  an icon stacks it (1.6em) over its label. A 1px line of light (1.5rem,
  white fading out) falls from the selected category: the cross's vertical
  arm. On phones the row takes its own line under the brand, and the tools
  share one row beneath it (the theme picker shrinks).
- Current sub-items are marked by light alone, as on the XMB: no side
  stripe (`--row-active-marker`, `--nav-rail-marker` and
  `--tree-selected-marker` are off), a 10-14% white lift and a 12px glow
  (`--list-active-marker`). A list inside a `nav` is the sub-column: no
  box, no rules, 1.1rem rows.
- System dialogs follow `modalDialog.jpg`: a dark band with thin white
  rules above and below (no side edges, 0.25rem corners), the title over a
  35% white rule instead of a header slab, and the footer's secondary
  choices as plain text beside the bright primary ("Yes  No"). Desktop
  windows keep their full frame.
- Every selected state (segmented control, pagination, listbox option,
  calendar day, filter chip, toggle, desktop icon label) is a pale glass
  lift with white text and a blue-white glow (10px). Focus is never a
  coloured fill: `.btn-primary` is a bright white glass lift with navy text
  (the focused "Yes" in `modalDialog.jpg`), and `.btn-danger` is said by
  its `--danger` text and edge on smoked glass, not a salmon block; the
  same goes for a danger `.toggle-btn` when on (14% salmon tint, danger
  edge and a salmon glow).
  `--success` is a pale mint (`#8fe8c0`), not a neon green.
- Sliders: the track is a 55%-white bar (about 3:1 on the wave) (`--slider-bg`) with a white,
  glowing knob; the vertical fader draws it as a thin centred line.
- Icon buttons scale up (`transform: scale(1.15)`) on hover/focus — the
  one unmistakable XMB interaction.
- `999px` (pill) radius on buttons, nav items and badges only — real XMB
  info panels were modestly rounded rectangles, not stadium shapes, so
  `--radius` (panels, cards, inputs, alerts, the dropdown, the log)
  is a generous `0.85rem`/`0.9rem` rounded rectangle instead. A base
  radius of 999px produced odd stadium-shaped alert banners and selects
  on large surfaces; interactive pill-shaped chrome keeps its own
  explicit `--btn-radius`/`--nav-item-radius: 999px` regardless.
- Thin/glass borders, no hard rectangular chrome. Overlapping desktop
  windows are opaque navy (`--modal-bg` inside `.desktop-window`) so the
  window behind never shows through.

## Tell-tales of an inauthentic result

- Any opaque panel or card background (overlays excepted, see Core values).
- A see-through modal: if page text is legible *through* an open dialog, the
  overlay is wrong.
- A left-aligned or edge-anchored navigation bar instead of a centred one.
- Sharp rectangular corners on interactive elements.
- A stadium/pill-shaped info panel, alert or dropdown — those are
  modestly rounded rectangles, not pills; only buttons/nav items/badges
  are pills.


## Don'ts

- **No opaque panels or cards**; everything is a translucent tint over the wave. Overlays (modal, toast, tooltip) are the exception and must be near-opaque.
- **No filled selection block**; selection is a glow plus scale.
- **No left-anchored primary nav** where the layout allows a centred bar.
- **No stadium/pill info panels**; only buttons, nav items and badges are pills.
- **No warm or neutral grey backdrop**; the wave is a deep blue gradient.

## Icons

`icons.svg` redraws the full core set (178/178). Rules: 24 grid, core 2px
stroke with round caps/joins, open line silhouettes, rounded rects (rx 1 to 3
by size) and true circles. The only solids are small dots and badges
(`fill="currentColor" stroke="none"`, r0.9 to 1.2). Colour is always
`currentColor`.

## Typography

`--font` is `"XMB Titillium", "Segoe UI", "Helvetica Neue", Arial, sans-serif`; `--font-mono` is "XMB Mono" (the library's own `ShareTechMono-Regular.woff2`, a narrow, light-stroked mono) then `Consolas, monospace`, kept for code and logs only: KPI values (`.stat-value`), prices, readouts (`--readout-font`) and inline numerals (`.mono`: order numbers, totals, timecodes) use the theme sans at weight 300 with tabular figures, as the PS3 clock does. h4-h6, panel/modal headers, card and list titles and the brand are capped at 400, so Titillium Bold appears only for inline emphasis. "XMB Titillium" is the library's own `assets/fonts/TitilliumWeb-*.woff2` (OFL, see `assets/fonts/NOTICE.md`): without it Linux fell back to DejaVu Sans, wide and heavy. Body, headings and the category row are weight 300. The captures show a thin, light sans (both `xmb-ps3-screenshot.jpg` and the RetroArch recreation); the actual PS3 face (SCE Rodin) isn't free, and Titillium is the closest light, open sans the library ships, not a match.

## Contrast honesty

- **Base:** `--text` `#f2f7ff` and `--muted` `#d3e0f5` on the wave. Measured on rendered pixels at 1280x900: muted is 4.9-7.0:1 over the content area (lowest just under the bar at the top right, #005abe). The brightest part of the wave (#028ceb, top-right corner) only sits behind the app-bar, whose smoked-glass capsule carries its labels.
- **Glass:** `--surface` `rgba(0,22,80,.38)` composites to about #003b8c on `--bg`, where `--muted` is about 7:1; `--surface-2` `rgba(110,180,255,.1)` keeps `--muted` at AA (checked by `scripts/check.sh`). `--danger` was lifted to `#ff9e9e` to clear 4.5:1 on the bluer glass.
- **Keys** use `--text` (`--key-fg`), not `--muted`; a console's grey key sank muted to 4.47:1.
- **Heatmap badges** sit on smoked glass (`rgba(0,16,56,.72)`), so white labels stay legible on the pale positive end of the scale.
- **Overlays:** `--modal-bg` `rgba(14,28,58,.94)` over `--overlay-bg` `rgba(0,4,20,.82)`; no blur (the overlay is opaque enough without it, and the blur cost frames). Toasts are 16:1 on `--toast-bg`.
- **Selection** is a 20%-white lift with white text plus a glow, so the text is lighter than the lift's ground; `.btn-primary` is `#04162e` on 88% white, well above 12:1.
- **Hue is a choice.** The PS3 capture (`xmb-ps3-screenshot.jpg`) shows a green wave, the RetroArch capture blue. The XMB wave colour changes by month/setting; this theme uses the blue one.

## Reference status

`references/xmb/` holds 6 captures plus `RESEARCH.md`:

- `xmb-ps3-screenshot.jpg` — a PS3 XMB (green wave variant) with the horizontal icon row and the vertical list dropping from Music. Backs the cross layout, the wave and the thin-type look.
- `xmb-retroarch-main-menu.jpg` — RetroArch's XMB recreation on a blue gradient: rounded-square category icons in a row, a highlighted first icon, a vertical menu list below and a wave. Backs the blue palette, the wave and the cross.

- `modalDialog.jpg`, `modalDialog-form.jpg`, `modalDialog-optionsMenu.jpg`, `toast.jpg` — PS3 user's-guide screens (Yes/No confirm, PSN sign-in form, Options menu, online notification). Back the overlay values above.

Gap (from `RESEARCH.md`): no tooltip reference, and no standalone capture of the "O Enter / X Back" hint footer. The theme doesn't draw that footer; the contract's `.modal-footer` holds real buttons. no people-free game-thumbnail example remains. Not backed by either file: the pill-shaped nav, the smoked-glass floating app-bar capsule and the exact glow values. (An earlier note here claiming no `references/xmb/` folder exists was wrong.)

## Centring the category row

`.nav`/`.app-bar` centre their content, but the demo headers push their
tools right with an auto-margin spacer (`.push`, an inline
`margin-left:auto` span or `.demo-topbar-spacer`), which pinned the row
flush left. The theme zeroes those spacers inside `.app-bar` and gives
the row `margin-inline: auto`, so it centres between the brand and the
tools. The demo row is text-only (the markup has no category icons), so
the theme marks the selected category by size (1.35rem against 0.95rem),
white text and a halo, the text form of the enlarged icon.

## v5 layout

- **Tiers.** Desktop is unchanged. Up to 900px the floating bar wraps to
  two lines, so it becomes a rounded glass slab (1.25rem corners) instead
  of a stadium, which would clip both lines' ends. Phones put the category
  row on its own line straight under the brand (tools follow), with tighter
  item padding so the four categories fit one line; it doesn't scroll, since
  an overflow container would clip the menubar's drop-down panels.
  Mobile trades the 1rem shell frame for content width. No rail.
- **Nesting.** Translucent surfaces stack as glass does; window caption
  buttons group at the title bar's right end.
- **XL gutter art.** The wave carries on beside the content: three thin
  translucent light ribbons crossing the gutters, the same ribbon as the
  page background. They drift sideways once every two minutes, only with motion
  allowed (`xmb-wave`).
