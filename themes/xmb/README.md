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
  ribbon (two filled bands, three thin strokes) sweeping across the middle
  of the first screen. The highlight and ribbon are sized to the viewport,
  so a long page doesn't stretch them; the same ribbon continues in the XL
  gutters.
- Glass is tinted the wave's own deep blue (`--surface`
  `rgba(0,22,80,.3)`), not white, so panels read as blue glass rather than
  grey blocks; the folder rail and toolbars are transparent and rounded.
- The category row is centred in a smoked-glass capsule: the theme
  neutralises the demo headers' auto-margin spacers so the row takes the
  free space on both sides, and the selected category is white with a
  soft halo.
- Every selected state (segmented control, pagination, listbox option,
  calendar day, filter chip, toggle, desktop icon label) is a pale glass
  lift with white text and a blue-white glow; solid accent is kept for
  `.btn-primary` only.
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

`--font` is `"XMB Titillium", "Segoe UI", "Helvetica Neue", Arial, sans-serif`; `--font-mono` is `Consolas, monospace`. "XMB Titillium" is the library's own `assets/fonts/TitilliumWeb-*.woff2` (OFL, see `assets/fonts/NOTICE.md`): without it Linux fell back to DejaVu Sans, wide and heavy. Body, headings and the category row are weight 300. The captures show a thin, light sans (both `xmb-ps3-screenshot.jpg` and the RetroArch recreation); the actual PS3 face (SCE Rodin) isn't free, and Titillium is the closest light, open sans the library ships, not a match.

## Contrast honesty

- **Base:** `--text` `#f2f7ff` and `--muted` `#d3e0f5` on the wave. Measured on rendered pixels at 1280x900: muted is 4.9-7.0:1 over the content area (lowest just under the bar at the top right, #005abe). The brightest part of the wave (#028ceb, top-right corner) only sits behind the app-bar, whose smoked-glass capsule carries its labels.
- **Glass:** `--surface` `rgba(0,22,80,.3)` composites to about #003f93 on `--bg`, where `--muted` is about 7:1; `--surface-2` `rgba(110,180,255,.1)` keeps `--muted` at AA (checked by `scripts/check.sh`). `--danger` was lifted to `#ff9e9e` to clear 4.5:1 on the bluer glass.
- **Keys** use `--text` (`--key-fg`), not `--muted`; a console's grey key sank muted to 4.47:1.
- **Heatmap badges** sit on smoked glass (`rgba(0,16,56,.72)`), so white labels stay legible on the pale positive end of the scale.
- **Overlays:** `--modal-bg` `rgba(14,28,58,.94)` over `--overlay-bg` `rgba(0,4,20,.82)`; no blur (the overlay is opaque enough without it, and the blur cost frames). Toasts are 16:1 on `--toast-bg`.
- **Selection** is a 20%-white lift with white text plus a glow, so the text is lighter than the lift's ground; `--on-accent` `#04162e` on `--accent` is 10.0:1 for `.btn-primary`.
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
the theme marks the selected category with white text and a halo rather
than an enlarged icon.

## v5 layout

- **Tiers.** Desktop is unchanged. Up to 900px the floating bar wraps to
  two lines, so it becomes a rounded glass slab (1.25rem corners) instead
  of a stadium, which would clip both lines' ends; the category row
  scrolls and starts at its first item (`justify-content: safe center`).
  Mobile trades the 1rem shell frame for content width. No rail.
- **Nesting.** Translucent surfaces stack as glass does; window caption
  buttons group at the title bar's right end.
- **XL gutter art.** The wave carries on beside the content: three thin
  translucent light ribbons crossing the gutters, the same ribbon as the
  page background. They drift sideways once every two minutes, only with motion
  allowed (`xmb-wave`).
