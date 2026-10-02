# XMB

> The PlayStation 3 / PSP dashboard: the Cross Media Bar itself — a horizontal row of glowing category icons over a deep-blue wave, with sub-items dropping straight down from whichever one is selected.

**Requires: L1** — sets `--app-*` layout properties (a centred, transparent app-bar over the wave); recolours correctly at L0 but the actual cross-shaped layout only appears once the app shell is adopted.

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
   94%, `--tooltip-bg` 96%) over a heavy, blurred `--overlay-bg`.
2. **Selection is a glow, not a fill.** The active icon/row gets a soft
   blue glow and a scale-up, not a solid highlight block — see
   `--btn-shadow-hover` and the icon-button hover rule.
3. **The bar is centred, not left-aligned.** Real XMB's icon row runs
   through the horizontal centre of the screen; a left-anchored nav bar
   reads as a generic app, not XMB.

## Signature details

- The layered radial-gradient "wave": a lighter glow low-and-centre and
  upper-left over the deep navy-to-blue base.
- Icon buttons scale up (`transform: scale(1.15)`) on hover/focus — the
  one unmistakable XMB interaction.
- `999px` (pill) radius on buttons, nav items and badges only — real XMB
  info panels were modestly rounded rectangles, not stadium shapes, so
  `--radius` (panels, cards, inputs, alerts, the dropdown, the log)
  is a generous `0.85rem`/`0.9rem` rounded rectangle instead. A base
  radius of 999px produced odd stadium-shaped alert banners and selects
  on large surfaces; interactive pill-shaped chrome keeps its own
  explicit `--btn-radius`/`--nav-item-radius: 999px` regardless.
- Thin/glass borders, no hard rectangular chrome.

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

## Typography

`--font` is `"Segoe UI", "Helvetica Neue", Arial, sans-serif`; `--font-mono` is `Consolas, monospace`. **System fonts, nothing vendored.** Some text is set at weight 300 (see `theme.css`). The captures show a thin, light sans (both `xmb-ps3-screenshot.jpg` and the RetroArch recreation), which the stack approximates with a light weight; the actual PS3 system face is not identified and not vendored.

## Contrast honesty

- **Text on the deep-blue base is very high:** `--text` `#eaf2ff` is 15.82:1 on `--bg` `#0a1730`; `--muted` `#b9cbe8` is 10.84:1; `--accent` `#7ec8ff` is 9.84:1 (no lift needed).
- **Translucent surfaces:** `--surface`/`--surface-2` are white at 8%/14% alpha over the wave, so ratios depend on what is behind; I measured on `--bg` only. The `theme.css` comment asserts `--muted` clears AA on both surfaces; the tint raises luminance only slightly, but I did not composite them.
- **Overlays (measured, rendered pixels, 1280x900, all 7 demo pages):** the modal used to be `--surface` (8% white), so whatever was behind it showed through. On the demo pages the inline copy of the same dialog was readable through the open one, and the "Confirm SCRAM" title was doubled. Now `--modal-bg` `rgba(14,28,58,.94)` over `--overlay-bg` `rgba(0,4,12,.78)` + `--overlay-blur: blur(6px)`: title 12.5:1 (was 8.4-10.3), body/labels in `--muted` 10.4:1 (was 7.7-9.3, and down to 5.6 where page content sat behind), `.btn-secondary` text 9.5:1, `.field-error` 6.2:1 (was 2.8 at worst). The surface itself is only 1.1-1.2:1 against the dimmed page, as on the PS3; what separates it is the 40%-white `--modal-border` at roughly 3.5:1. Toasts: 16:1 on `--toast-bg` (was 4.9-7.7 on 14% white).
- **Glow lifted for legibility:** the selection glow is a bright light-blue halo (`--accent`/`--flare` `#bfe4ff`); the strengthened active-item glow and the blurred, floating bar were added so the bar still reads on the wave, not to meet a text ratio. `--on-accent` `#04162e` on `--accent` is 10.0:1.
- **Hue is a choice.** The PS3 capture (`xmb-ps3-screenshot.jpg`) shows a green wave, the RetroArch capture blue. The XMB wave colour changes by month/setting, so blue is the theme's selection, not the only reference; hexes not sampled.

## Reference status

`references/xmb/` holds 6 captures plus `RESEARCH.md`:

- `xmb-ps3-screenshot.jpg` — a PS3 XMB (green wave variant) with the horizontal icon row and the vertical list dropping from Music. Backs the cross layout, the wave and the thin-type look.
- `xmb-retroarch-main-menu.jpg` — RetroArch's XMB recreation on a blue gradient: rounded-square category icons in a row, a highlighted first icon, a vertical menu list below and a wave. Backs the blue palette, the wave and the cross.

- `modalDialog.jpg`, `modalDialog-form.jpg`, `modalDialog-optionsMenu.jpg`, `toast.jpg` — PS3 user's-guide screens (Yes/No confirm, PSN sign-in form, Options menu, online notification). Back the overlay values above.

Gap (from `RESEARCH.md`): no tooltip reference, and no standalone capture of the "O Enter / X Back" hint footer. The theme doesn't draw that footer; the contract's `.modal-footer` holds real buttons. no people-free game-thumbnail example remains. Not backed by either file: the pill-shaped nav, the blurred floating app-bar capsule and the exact glow values. (An earlier note here claiming no `references/xmb/` folder exists was wrong.)

## Known harness limitation: the app-bar doesn't render centred everywhere

`html[data-theme="xmb"] .nav { justify-content: center }` (and the
same rule on `.app-bar`) is real, is the highest-specificity rule
either QA page applies, and does win — it centres the standalone
`.nav` demo in example.html's "Navigation" section correctly. It has
no visible effect on the QA harness's own *topbar* markup, though:
example.html's `.app-bar` header puts an inline
`<span style="margin-left:auto">` before its breadcrumbs, and
example-2/3.html's `.demo-topbar-spacer` sets `flex: 1`. Either one
absorbs 100% of the row's free space by itself, so `justify-content` has
nothing left to distribute and the brand/items stay pinned flush left.
That's a property of those harness pages' fixed nav markup (which this
theme must not edit to "fix"), not a bug in the theme's centering rule —
an app that lays out its own `.app-bar` without such a spacer gets
the real centred cross-bar. In the meantime the bar leans harder on the
float-and-glow language it's actually judged on: it now renders as its
own floating, blurred, pill-shaped glass capsule with a soft drop shadow
above the wave, and the active nav item's selection glow is stronger —
so the bar still reads unmistakably as XMB even where it can't be
centred.

## v5 layout

- **Tiers.** Desktop is unchanged. Up to 900px the floating bar wraps to
  two lines, so it becomes a rounded glass slab (1.25rem corners) instead
  of a stadium, which would clip both lines' ends; the category row
  scrolls and starts at its first item (`justify-content: safe center`).
  Mobile trades the 1rem shell frame for content width. No rail.
- **Nesting.** Translucent surfaces stack as glass does; window caption
  buttons group at the title bar's right end.
- **XL gutter art.** The wave carries on beside the content: three thin
  translucent light ribbons crossing the gutters, within about 1.3:1 of
  `--bg`. They drift sideways once every two minutes, only with motion
  allowed (`xmb-wave`).
