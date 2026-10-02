# iOS (Flat)

> Apple iOS 7 to iOS 18: system colours on grouped grey, inset grouped lists, frosted bars, the green toggle.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The iPhone between iOS 7 (2013) and iOS 18 (2024): the flat era that
replaced iOS 6's leather and linen and came before iOS 26's Liquid Glass.
What makes it recognisable is a short list: a light-grey grouped page
(`#f2f2f7`), white rounded cells with hairline separators that start 16pt
in, uppercase footnote section headers *above* each group, blue tint text
for anything tappable, grey disclosure chevrons, the green toggle, the
grey segmented control with a white sliding pill, centred alerts with
edge-to-edge buttons, and frosted bars at the top and bottom that content
scrolls under. The visual reference is Apple's own Human Interface
Guidelines from the iOS 13 and 14 years; sources are in
`references/ios-flat/RESEARCH.md`.

Its siblings cover the other two eras: `ios-skeuomorphic` (iOS 6) and
`liquid-glass` (iOS and macOS 26). This theme must not drift into either.

## Core values

1. **Three materials only.** Grouped grey for the page, white cells for
   content, and the frosted bar material (`backdrop-filter:
   saturate(180%) blur(20px)`) for the nav bar, tab bar, alerts, menus and
   banners. Nothing else is translucent.
2. **Flat means flat.** No gradients, gloss, bevels or inner shadows. The
   only gradient is the Contacts monogram disc behind `.avatar`. Resting
   surfaces (panels, cards, lists, field rows) have no border and no
   shadow. Shadows exist only on things that float: the switch thumb, the
   segmented pill, the slider knob, alerts, menus, banners.
3. **Tint colour means tappable.** Links, ghost and secondary buttons,
   nav items, the select chevron and alert buttons are blue text. Body
   text is black. Don't tint static text.
4. **Section headers sit outside the cell.** `.panel-header` is drawn
   above the white panel in 13px uppercase grey, the way UITableView's
   grouped headers are. Don't put it back inside a header strip.
5. **Inset grouped rows merge.** Consecutive `.field-row`s become one
   group: corners only at the ends, a hairline between rows that starts
   1rem in. Tappable `.list-item`s get a grey chevron.
6. **The toggle is green.** `#34c759`, 51 by 31 with a white thumb that
   carries the iOS shadow. It is not the accent colour.
7. **System colours, system fonts.** The palette is the HIG's system
   colours; type is `-apple-system`. SF Pro is never vendored.

## Signature details

- The app bar is a large-title navigation bar: a top row of controls with
  the page nav drawn as one iOS 13 segmented control, and the brand below
  it as a 34px bold large title. It is sticky and frosted.
- The status strip is a tab bar: 49px, frosted, sticky to the bottom,
  items spaced evenly in 12px medium text.
- Modals are iOS alerts: 14px corners, frosted, title and body centred,
  buttons spanning the bottom edge with hairline dividers, the preferred
  (primary) one bold, the destructive one red. With window controls the
  header turns into an iPad sheet bar (title leading, round grey buttons
  trailing).
- Checkboxes and radios are the round blue checkmark from Mail and
  Reminders' edit mode; iOS has no square checkbox.
- Table selection is the grey cell highlight (`#d1d1d6`), and the active
  row carries a trailing blue checkmark as well as the leading marker.
- Buttons follow iOS 15's styles: primary is "filled", secondary is
  "tinted" (a wash of the tint), ghost is "plain" text, the default is
  "gray". A tap dims to 55% opacity instead of moving.
- `.btn-sm` is a capsule (the App Store "GET" button).
- Toasts are notification banners with a small coloured app-icon tile.
- Badges are capsules; the danger badge is the red notification badge.
- Readouts use thin (300) tabular digits like the Stopwatch; stat values
  use SF Rounded (`ui-rounded`) like iOS 14 widgets.
- Mixer pieces borrow from the system: faders are Control Center slabs,
  console keys are keyboard keys, `.btn-go` is the Voice Memos record
  button.
- Messages are iMessage bubbles (blue own, grey others, 18px radius).
- Meters use the Settings > Storage bar colours (green, orange, red).

### Variants

| Variant | Label | What changes |
|---|---|---|
| (default) | iOS (Flat) | Light mode. |
| `dark` | Dark Mode | The iOS 13+ dark system colours: black page, `#1c1c1e` cells, `#2c2c2e` fills, `#38383a` separators, dark-mode systemBlue `#0a84ff` for tint text, `#30d158` toggle, `#636366` segmented pill. |

The dark variant declares `color-scheme: dark` so native controls follow it.

## Typography

Stack: `-apple-system, BlinkMacSystemFont, "Helvetica Neue", "Segoe UI",
Roboto, "Noto Sans", Arial, sans-serif`. On Apple platforms that is SF Pro
(iOS 9 onward); Helvetica Neue is the iOS 7 and 8 system face, so it is
the right first fallback. Nothing is vendored: SF Pro's licence does not
allow redistribution. Monospace: `ui-monospace, "SF Mono", Menlo, …`.

The root font size is 17px (Body). Headings follow the text styles:
`h1` Large Title 34 bold, `h2` Title 2 22 bold, `h3` Headline 17
semibold; section headers and segmented labels are Footnote 13.

## Contrast honesty

| Pair | Ratio |
|---|---|
| `--text` `#000` on `--surface` `#fff` / `--bg` `#f2f2f7` | 21 / 18.8 |
| `--muted` `#6c6c70` on surface / surface-2 `#eeeeef` | 5.2 / 4.5 |
| `--on-accent` white on `--accent` `#0071e3` | 4.7 |
| white on `--danger` `#d70015` / `--success` `#1e7e34` | 5.4 / 5.1 |
| `--warning-text` `#c93400` on surface | 5.3 |
| `--accent-text` `#0062c4` on the tinted button wash | 5.0 |
| dark: `--muted` `#98989f` on `#1c1c1e` / `#2c2c2e` | 5.9 / 4.9 |
| dark: `--danger-text` `#ff6961`, `--success-text` `#30d158` on `#1c1c1e` | 6.0 / 8.4 |

Deviations from Apple's values, all made for the contrast floors:

- **Accent.** systemBlue `#007aff` with white text is 4.0:1. The accent
  is `#0071e3`, the blue Apple uses for its own web buttons (4.7:1). The
  pure `#007aff` stays as `--ios-blue` for chart series and bars, where
  no text sits on it.
- **Red and green fills.** systemRed `#ff3b30` (3.6:1 with white) becomes
  `#d70015`, the HIG's Increase Contrast red. systemGreen `#34c759` is
  2.2:1 with white, so `--success` is a darker `#1e7e34`. The real
  `#34c759` is still the toggle, lamp and meter green.
- **Secondary label.** secondaryLabel (60% `#3c3c43`) is 3.3:1 on white;
  `--muted` is `#6c6c70`, close to systemGray's accessible value.
- **Toggle off track.** `#e9e9ea` on white is low contrast, as it is on
  the device. The thumb's shadow and position carry the state.

## Layout

The shell becomes an iPhone screen stretched wide: frosted large-title nav
bar at the top, grouped grey content, frosted tab bar at the bottom. Both
bars are sticky so content scrolls under the blur. There is no rail: the
phone shell has no sidebar, and an empty iPad sidebar would be a fake.
At phone width the large title drops to 28px and the segmented nav scrolls
sideways.

## Don'ts

- Don't add gradients or gloss to buttons or bars (that's
  `ios-skeuomorphic`), or refraction, specular rims or floating capsule
  bars (that's `liquid-glass`).
- Don't put borders or drop shadows on panels, cards or lists.
- Don't make the toggle blue, or the segmented control's selected segment
  blue. (The blue-outlined segmented control is iOS 7 to 12; this theme
  follows the iOS 13+ one so the light and dark variants match.)
- Don't name SF Pro in the stack as if it were vendored, and don't vendor
  it.
- Don't use uppercase or tracked labels anywhere except section and table
  headers.

## Tell-tales of an inauthentic result

- Section titles inside a coloured header strip on the card.
- Cards with outlines or shadows: that's Material or Bootstrap, not iOS.
- Square checkboxes.
- A blue toggle, or a toggle with a visible border.
- Opaque, solid-colour nav and tab bars.
- Grey body text, or black links.
- A segmented control with a blue fill behind the selected segment.
- Large rounded "pill" bars floating over content (Liquid Glass).

## Print

The bars stop being sticky and lose their blur in a small `@media print`
block.

## Reference status

Researched from Apple's Human Interface Guidelines as archived in
2020 (iOS 13/14 screenshots) and 2024 (iOS 17/18), via the Wayback Machine.
14 images are filed in `references/ios-flat/`, one of them in `dark/`. The
system colour values match Apple's published table. Not found: a good
reference for tables (iOS has none), toasts, tooltips, meters, the dock,
or anything from iOS 7 itself in a resolution worth keeping.

## v5 layout

- **Tiers.** Phones and tablets (up to 900px): the large title moves up beside the trailing buttons, as the Photos and App Store tabs do (30px, 26px on phones, truncating), and the segmented nav takes its own line and scrolls sideways instead of wrapping into a second row of segments. The bars sit on the `--z-sticky` layer.
- **Nesting.** Grouped sections are flat by design; nested panels need no step-down rules.
- **XL gutter art (1801px+).** The home screen beside the app: its icon grid reduced to faint squircles (white ones on the dark variant).

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
