# Liquid Glass

> Apple's 2025 design language (iOS 26, iPadOS 26, macOS Tahoe 26): translucent capsule controls with bright specular rims, floating inset over a vivid wallpaper while the content scrolls underneath.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

**Family:** iOS; extends [iOS (Flat)](../ios-flat/README.md) with `Inherit: none`.

## What this theme is trying to achieve

**Liquid Glass** as shipped at WWDC 2025. Apple separates the UI into two
layers: a **content layer**, and a **functional layer** of controls and
navigation made of a glass that "has no inherent color, and instead takes
on colors from the content directly behind it" (HIG, Color). The glass
floats: tab bars and toolbars are capsules inset from the screen edges,
sidebars are large rounded panes standing off the window, buttons are
pills or circles with a lit rim, and the content scrolls under all of it.
Recognisable at a glance by: capsules everywhere, a thin bright edge on
every piece of glass, the wallpaper's colour bleeding through, and nothing
touching the edge of the screen.

## Core values

1. **Glass is the functional layer only.** Bars, buttons, tabs, menus,
   sheets, toasts and the sidebar are Liquid Glass (blur + saturate +
   specular rim). Panels and cards in the content are a frosted *standard*
   material with a soft shadow and **no rim** — HIG: "Don't use Liquid
   Glass in the content layer."
2. **Float, never dock.** Every bar is inset from every edge with its own
   radius. A bar flush with the window edge, or a hairline under a bar, is
   iOS 7–18 (`ios-flat`), not this.
3. **Capsules and concentric corners.** Controls are `999px` capsules or
   circles; containers use radii that equal the child's radius plus the
   inset around it (window 28px around 0.6rem-inset capsules; menu 18px
   around 12px items with 6px padding).
4. **Content scrolls under the glass.** The toolbar and tab bar are
   `position: sticky` over the window, and the wallpaper is a fixed layer
   (`html::after`, so the compositor paints it once instead of a
   `background-attachment: fixed` repaint every frame), so the blur always
   has moving, colourful content behind it. Glass over a flat colour is just a grey pill.
5. **Legibility beats transparency.** Small controls use the *clear*
   weight; anything carrying body text uses the *regular* weight (a 70–80%
   white scrim), and the window pane under the content is 80–84% white
   (enough for the wallpaper to tint it; `--muted` still measures 4.7:1
   over the darkest light-wallpaper blue `#0a2fa8`),
   blurred without the saturate boost (unblurred up to 900px, where only the soft wallpaper is behind it), so the content layer reads as white
   and `--muted` text holds 4.5:1 over the darkest wallpaper blue. Headings
   that can land on the wallpaper carry a faint white halo. Text never sits
   on the bare wallpaper: an L0 page (no app shell) and any block beside
   the shell get the window pane's scrim.
6. **Colour is sparing.** One tint (systemBlue) for the prominent button,
   selected labels and focus; selection is a grey lens with a blue label
   (or, in segmented controls, toggle groups and a `.btn-group`'s
   `.btn-primary`, a lifted white lens on a grey track), not a blue fill.
   Lists, sidebars and selected filter chips (`.badge-button.is-active`)
   select the same way; only table multi-select keeps a pale blue band, as
   Finder does.

## Signature details

- `--lg-rim`: five inset shadows — a full-white top-left and a softer
  bottom-right specular edge (light catching the curved bezel), a 0.06
  black lower inner edge (the lens's shaded side), a 0.5px white hairline,
  and a soft inner glow standing in for the refraction band. `--lg-lift`
  adds a 0.5px `rgba(0,0,0,0.11)` outer ring so the rim reads against the
  near-white window.
- Clear glass is a faint grey (`rgba(244,244,247,0.66)` to
  `rgba(232,232,237,0.56)`), not white: over the white pane it reads as the
  reference's `#ededed` bar. The selection lens is `rgba(120,120,128,0.18)`
  (about `#dadadc` over the grey glass, near the sampled `#e1e1e3`).
- `backdrop-filter: blur(14px) saturate(160%) brightness(1.08)` on clear
  glass; `blur(28px)` on sheets and the window (no backdrop pass on the
  window up to 900px: it is the content layer over a soft gradient, and
  that pass was most of a phone's scroll cost). The saturate is what makes controls pick up the wallpaper's
  colour. Glass inside a blurred bar, and anything inside the window pane
  on phones and tablets, skips its own backdrop pass: there is nothing new
  behind it to blur.
- Prominent buttons are *tinted glass*: the accent fill keeps the rim and
  a lit top edge and casts a coloured bloom. The `.btn-go` trigger is the
  same tinted-glass capsule (`--go-*` tokens), sentence case and semibold,
  not tracked caps. On press glass **swells** (`scale(1.04)`) instead of
  sinking.
- Tabs, the nav, the scrollspy nav and the status strip read as the iOS 26
  tab bar: a glass capsule whose selected item is a grey lens with a blue
  label. The capsule never wraps; it scrolls sideways.
- Lists are inset grouped lists: 6px padding, rows as 12px lenses
  (concentric with the 18px list), hairlines starting after the leading
  icon.
- Input groups stay capsules: the leading addon and the trailing field or
  button are rounded, only the inner sides are square.
- The switch is the iOS 26 one: wider track, a capsule knob wider than it
  is tall, systemGreen when on. The slider is Control Center's: a 0.6rem
  capsule track (`rgba(120,120,128,0.36)`) filled in systemBlue from the
  start to a white capsule thumb (`::-moz-range-progress` in Firefox, a
  left-only thumb border image in Chromium; the hit area stays
  `--tap-min`). A vertical slider is the same thin capsule standing up,
  filled from the bottom: the theme pads it with physical left/right
  padding, because core's logical padding lands top and bottom under
  `writing-mode: vertical-lr`. The switch never flex-shrinks in a row.
- The traffic lights (`#ff5f57 #febc2e #28c840`, 12px discs with a 0.5px
  ring) sit bare at the start of the toolbar, as in Safari on Tahoe. Above
  900px the toolbar is not one long pill: it is a soft scroll-edge fog of
  the pane colour (`--lg-edge-fog`, no rim or shadow), and its controls
  float on it as separate glass capsules (the nav, the theme picker, the
  search button, icon buttons as glass circles). Desktop
  windows, and any `.modal` window with `.btn-min` / `.btn-max`, get real
  ones: close, minimise and zoom at the start of a clear
  title bar, glyphs only on hover, each in a `--tap-min` hit box; the title
  is 13px semibold and centred; no window icon and no menu-bar strip.
- An in-window sidebar (`.nav-rail`) is the Tahoe sidebar: a 20px rounded
  pane of clear glass, no divider, rows as 10px grey lenses with a blue
  selected label and no edge marker.
- Segmented controls and toggle groups: a grey capsule track with a lifted
  white lens on the selected item. Labels never wrap; a track too wide for
  the screen scrolls sideways.
- Editable table cells (dirty, saving, saved, editing, invalid) are 8px
  rounded lenses, the dirty bar curving with the corner; `.log` rows sit
  6px inside the rounded console so their level bars are not clipped;
  a log row rounds only its trailing corners (2px 6px 6px 2px), so the
  3px level bar stays straight instead of curling into a "(".
- The sidebar (`.nav-rail`) and the floating tab bar pick up a faint
  blue-to-peach cast from the wallpaper (`--lg-pickup`, about 8-10%
  alpha) over the clear glass; reduced transparency and high contrast
  drop it.
- A tab capsule or segmented track too wide for the screen fades out over
  its trailing 28px (a scroll-driven mask, so it is inert when it fits),
  reading as "more to scroll" rather than a clipped label.
- Readouts are 16px-radius grey pills with `max(0.25em, 6px)` block
  padding and a 1.25 line height, so digits clear the pill edge by 4px+.
- A vertical tab capsule keeps its width beside a form; a truncating list
  row (`.list-item.text-truncate`) is a block so its label ellipsizes
  instead of running into the row edge.
- Pagination items are 2.35em (about 32px) circles, `--tap-min` on touch; selected desktop
  icon labels are 5px-rounded highlights, as in Finder.
- Section headers (`.field-group-title`) are sentence-case semibold grey
  with no rule under them. Only tiny stat labels stay uppercase.
- Alerts and toasts are Lock Screen notifications: rounded glass with the
  rim, no coloured stroke; a leading status dot carries the meaning.
- Numbers (`.stat-value`, `.readout-lg`) are SF Pro bold with tabular
  figures, not the monospace; so are money and time table columns
  (`.table td.mono`). Logs and code keep SF Mono.
- The page is a CSS sketch of the Tahoe wallpaper: pale sand top-left,
  deep blue sweeping waves, thin white crest arcs.

## Layout

A macOS Tahoe window over the desktop, standing 1.5rem off the screen
edge above 900px so the wallpaper frames it. The content **window** is one large
frosted pane (radius 28px) that spans all three shell rows; the capsule
**toolbar** (bare traffic lights and title at its start, its controls as
separate glass capsules) floats inside its top edge and
the capsule **tab bar** (`.app-status`) floats centred inside its bottom
edge, only as wide as its items. Both bars are sticky, so content scrolls
under them. The decorative `.app-rail` is not drawn: it is empty by
contract, and an empty pane of glass read as a loading skeleton. Real
sidebars are the app's own `.nav-rail`, drawn as glass inside the window.
Up to 900px the toolbar sits above the window instead of over it and wraps
to two lines (as a 26px rounded rectangle).

## Variants

- `dark` — the same material over the Tahoe night wallpaper: smoked glass
  (`rgba(30–60,…,0.4–0.5)`), dimmer cool rims, dark HIG label colours
  (`#f5f5f7` / `#a1a1a6`, accent text `#6cb4ff`, light enough for 4.5:1 on the grey lens). The window pane is a
  76–80% smoked navy (`rgba(28,30,40,…)`), so the night wallpaper's blue
  shows through, and the floating bars take a blue-teal pickup. It declares
  `color-scheme: dark` so native controls follow it.

## Tell-tales of an inauthentic result

- Bars or the sidebar touching the window edge, or rectangular bars.
- Windows-style `_ □ ✕` caption buttons on the right of a window.
- Status shown as a coloured outline around an alert or toast.
- A hairline border under the toolbar or above the tab bar.
- Glass with no rim highlight, or a rim that is a uniform 1px grey border.
- Blue-filled selected tabs or nav items (that is iOS 7–18 or Material).
- Opaque grey buttons; square or 6px-radius buttons.
- Specular rims on content cards and panels (glass leaking into the
  content layer).
- A flat solid page background with nothing for the glass to refract.
- Linen, gloss gradients or stitching (that is `ios-skeuomorphic`).

## Don'ts

- **Don't remove `backdrop-filter`** from the glass (bars, controls,
  menus, sheets) to "fix" a perf report; use
  `prefers-reduced-transparency`, which this theme already honours. The
  one exception is the phone/tablet window pane, which is content layer.
- **Don't lower the white scrims** on `--lg-regular` or `--app-main-bg`
  below their current 70% / 80%; they are what keeps `--muted` at 4.5:1
  over the dark wallpaper.
- **Don't set `--accent` to `#0088ff`** (iOS 26 systemBlue): white text
  on it is 3.5:1. It is used where no text sits on it (focus, progress,
  the switch caret, `--accent-2`).

## Typography

`--font` is `-apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro",
Inter, "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif`;
`--font-mono` starts with `"SF Mono", ui-monospace, Menlo`. SF Pro is
Apple-licensed and not vendored, so it renders only on Apple platforms;
elsewhere Inter stands in: the closest open grotesque to SF Pro, vendored
as `assets/fonts/InterVariable-Latin.woff2` (OFL, a 45 KB Latin subset of
Inter 4.0's variable font, wght 400-700 with the opsz axis, so large
titles get Inter Display's tighter cut; see `assets/fonts/NOTICE.md`). Body text runs at -0.012em, as
apple.com sets SF Text (code keeps normal spacing). Headings are bold with
slight negative tracking (the large-title voice); table headers are sentence-case
semibold, never uppercase.

## Contrast honesty

- `--accent` `#0071e3` (Apple's web action blue) under white text: 4.7:1.
  The iOS 26 systemBlue `#0088ff` (3.5:1 under white) is kept as
  `--accent-2` and `--focus`.
- `--danger` `#e0262b` is systemRed `#ff383c` deepened to 4.7:1 under
  white. `--success` keeps systemGreen `#34c759` with **dark** text
  (`#06240f`, 7.5:1) because white on it is 2.2:1.
- Glass surfaces are translucent; the lint measures text against the
  opaque `--surface` / `--surface-2` equivalents. The scrims are tuned so
  the rendered glass is at least as light as those over the wallpaper's
  darkest blue.
- `prefers-reduced-transparency: reduce` and `data-contrast="high"` swap
  every glass fill for the opaque surface.

## Reference status

`references/liquid-glass/` holds 14 Apple Newsroom WWDC25 press images
(12 shared, 2 in `dark/`) plus `RESEARCH.md` with credits, sampled hexes
and a component mapping. They cover the tab bar, toolbar, sidebar,
Control Center switches and sliders, menus, sheets, list/table, messages
and notifications. No reference shows a web-style data table header, a
meter, a toast in the ftl-themes sense or a form with validation errors.

## v5 layout

- **Tiers.** Phones and tablets (up to 900px): no traffic lights, the toolbar stops overlapping the window and becomes a 26px rounded rectangle with the brand and actions on line 1 and the nav on line 2; on phones the theme picker narrows and the search button collapses to a glass circle so the bar stays at two lines. Tray text in the floating tab bar ellipsizes instead of escaping the capsule. The window no longer sets `overflow: visible`, so wide content is clipped by core instead of spilling past the screen. The floating bars sit on the `--z-sticky` layer, and the capsule buttons grow to `--tap-min` (44px) on touch tiers instead of holding their 1.85–2.25rem desktop height.
- **Nesting.** Glass on glass already steps down through the material tokens; no extra rules.
- **XL gutter art (1801px+).** Drops of clear glass resting on the wallpaper, soft lenses with brighter rims, white at low alpha so both the day and night wallpapers show through.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders recoloured
with glass controls over the wallpaper, but without the window, sidebar
and floating bars. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status`
shell (CONTRACT.md "The app shell" / "Adoption levels") for the real
layout at **L1**.

The window starts below the toolbar's row and reaches up under it by the
toolbar's single-line footprint (`--lg-bar-reach`, 3.6rem), so a toolbar
that wraps pushes the content down instead of covering it. The theme
draws no `.app-rail`; put navigation in a `.nav-rail` inside `.app-main`
to get the glass sidebar.

This theme is in the iOS family but declares `Inherit: none`: its bundle
carries none of `ios-flat`'s or `ios-skeuomorphic`'s rules.

`backdrop-filter` support: without it, every glass surface falls back to
its translucent white (or smoked, in `dark`) fill: no blur, still legible.
Real Liquid Glass also *refracts* (bends the content at the rim). An SVG
`feDisplacementMap` in `backdrop-filter` can fake that, but only Chromium
supports it and it needs inline SVG in the page, so this theme suggests
the lens with rim highlights instead.

## Icons

`icons.svg` redraws the whole core icon set (178/178) in the weight of
current SF-style symbols, drawn for this project (not Apple's SF Symbols
artwork):

- **Grid:** 24×24 viewBox, glyphs kept inside roughly 2.5–21.5.
- **Stroke:** 2.0 (regular weight), round caps and round joins, generous
  1.5–3 corner radii.
- **Fill vs line:** two layers, like SF Symbols' hierarchical rendering.
  Every closed body (envelope, folder, bell, document, device…) is
  outlined at full strength and tinted inside with `currentColor` at 22%
  opacity; interior detail is drawn on top at full strength. Dots, carets
  and transport glyphs are solid.
- **Colour:** `currentColor` only, so the tint layer reads as the same hue
  on glass, on tinted capsules and in selected (white-on-blue) items.

The file is generated from one geometry source shared with `ios-flat` and
`ios-skeuomorphic`, each rendered in its own language (here: heavier line
plus a translucent fill).
