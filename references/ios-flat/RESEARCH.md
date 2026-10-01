# iOS (Flat): research notes

Scope: iOS 7 (2013) to iOS 18 (2024), before Liquid Glass. Research done
2026-10-01. Apple's live Human Interface Guidelines now show iOS 26 (Liquid
Glass) artwork, so every image here comes from **archived** HIG pages on
the Wayback Machine. The 2020 snapshots show iOS 13/14; the one 2024 image
shows iOS 17. Images are Apple's and are kept here as design references
only; none is shipped in a theme bundle.

Wikipedia's per-version iOS screenshots (en.wikipedia.org, "IOS 7" …
"IOS 18") were checked but are non-free files downscaled to about 237px
wide, too small to sample, so none was kept.

## Images

All files are `.webp`, converted from Apple's PNGs (quality 85).
"HIG 2020" means
`https://web.archive.org/web/2020/https://developer.apple.com/design/human-interface-guidelines/ios/images/<file>`,
found through the archived page named in the row.

| File | Source | What it shows |
|---|---|---|
| `navBar-largeTitle-searchBar-list.webp` | HIG 2020, `light-mode.png` (Visual Design > Dark Mode) | Mail inbox, light: back button "‹ Mailboxes" and "Edit" in tint blue, 34pt bold large title, grey search field, list rows with unread dot and grey chevrons. |
| `dark/navBar-largeTitle-searchBar-list.webp` | HIG 2020, `dark-mode.png` (same page) | The same screen in Dark Mode: black page, `#1c1c1e`-ish search field, white text, `#0a84ff` tint. Backs the `dark` variant. |
| `alert.webp` | HIG 2020, `Alerts.png` (Views > Alerts) | Maps "Current Location Not Available" alert: centred bold title, small centred message, one full-width "OK" button under a hairline, frosted panel on a dimmed map. |
| `actionSheet.webp` | HIG 2020, `action-sheets.png` (Views > Action Sheets) | Mail draft action sheet: grouped rounded buttons, red "Delete Draft", blue "Save Draft", separate bold "Cancel". |
| `segmentedControl-ios7.webp` | HIG 2020, `segmented-controls.png` (Controls > Segmented Controls) | Phone Recents with the pre-iOS 13 segmented control: blue outline, blue-filled selected segment "All / Missed". Shown for contrast; the theme follows the iOS 13+ style. |
| `segmentedControl-largeTitle-list.webp` | HIG 2024 (archived JSON `developer.apple.com/tutorials/data/design/human-interface-guidelines/segmented-controls.json`), image `https://docs-assets.developer.apple.com/published/7e73d6b155162202f8d031a2182dfdf9/segmented-controls-phone-recents@2x.png` | iOS 17 Recents: grey segmented track with white selected pill, large title, rows with blue info buttons, red missed-call names. |
| `switch-groupedList.webp` | HIG 2020, `switches-default.png` (Controls > Switches) | Settings > Sounds & Haptics: green on / white off switches, uppercase section headers, slider with speaker icons, footer text. |
| `groupedList-sectionHeader-footer.webp` | HIG 2020, `tables-grouped.png` (Views > Tables) | Maps > Driving & Navigation: grouped table, uppercase grey section headers, switches, grey footer text. |
| `groupedList-value-chevron.webp` | HIG 2020, `tables-value1-row.png` (Views > Tables) | Settings > Notes: value1 rows (label left, grey value right, grey chevron), navigation bar with "‹ Settings". |
| `insetGroupedList-sidebar.webp` | HIG 2020, `tables-inset-grouped-landscape.png` (Views > Tables) | iPad Settings: inset grouped list (rounded white groups on grey), coloured icon tiles, blue-filled selected sidebar row. |
| `tabBar.webp` | HIG 2020, `TabBar.png` (Bars > Tab Bars) | Photos tab bar: translucent blur over content, grey glyph+label items, active "Albums" in blue. |
| `slider.webp` | HIG 2020, `sliders.png` (Controls > Sliders) | Brightness slider: thin track, blue minimum side, large white knob with soft shadow. |
| `stepper.webp` | HIG 2020, `steppers.png` (Controls > Steppers) | Printer Options stepper: a grey rounded "− | +" pair. |
| `progressBar.webp` | HIG 2020, `Progress_Bar.png` (Controls > Progress Indicators) | Safari load progress: thin blue bar under a translucent address bar. |

## Palette

Apple publishes the system colours in the HIG Color page (archived 2020
and 2024, same values for iOS). Sampled values from the images agree:
`#f2f2f7` grouped background measured exactly, switch green `#34c759` in the 2024 toggle image (`#32c658` in the 2020 one);
`#d0d0d1` separators; `#eeeeef` search fill over white.

| Role | Light | Dark | Used as |
|---|---|---|---|
| systemBlue | `#007aff` | `#0a84ff` | `--ios-blue`; dark tint text. Fills use `#0071e3` (contrast, see theme README). |
| systemGreen | `#34c759` | `#30d158` | toggle, lamps, meter low, `--flare` |
| systemRed | `#ff3b30` | `#ff453a` | badge/meter/record red; text and fills use `#d70015` / `#ff6961` |
| systemOrange | `#ff9500` | `#ff9f0a` | `--warning`, meter mid |
| systemIndigo | `#5856d6` | `#5e5ce6` | `--accent-2` |
| systemTeal (iOS 13) | `#5ac8fa` | `#64d2ff` | second bar-chart series |
| systemGray / Gray4 / Gray5 | `#8e8e93` / `#d1d1d6` / `#e5e5ea` | `#8e8e93` / `#3a3a3c` / `#2c2c2e` | spinner, cell highlight, tracks |
| systemGroupedBackground | `#f2f2f7` | `#000000` | `--bg` |
| secondarySystemGroupedBackground | `#ffffff` | `#1c1c1e` | `--surface` |
| tertiary fill | `rgba(118,118,128,.12)` | `rgba(118,118,128,.24)` | search field, segmented track, gray buttons |
| separator | `rgba(60,60,67,.29)` | `rgba(84,84,88,.65)` | bar rules, alert dividers |

## Typography

SF Pro Text / Display (iOS 9 onward), Helvetica Neue (iOS 7 and 8). Text
styles from the HIG Typography page: Large Title 34, Title 1 28, Title 2
22, Title 3 20, Headline 17 semibold, Body 17, Callout 16, Subheadline 15,
Footnote 13, Caption 12/11. SF Pro is not redistributable, so the theme
uses `-apple-system` and never vendors it. SF Rounded (`ui-rounded`) for
widget numbers, SF Mono (`ui-monospace`) for code.

## Component mapping

| ftl-themes component | iOS original | Reference |
|---|---|---|
| `.app-bar` | Large-title navigation bar, frosted | `navBar-largeTitle-searchBar-list` |
| `.app-bar .nav-item` run | Segmented control in a nav bar | `segmentedControl-largeTitle-list` |
| `.app-status` | Tab bar, frosted | `tabBar` |
| `.panel` / `.panel-header` | Inset grouped section, header above | `insetGroupedList-sidebar`, `groupedList-sectionHeader-footer` |
| `.field-row` | Grouped table cell with switch / value | `switch-groupedList`, `groupedList-value-chevron` |
| `.list` / `.list-item` | Table rows with disclosure chevron | `groupedList-value-chevron` |
| `.switch` | UISwitch | `switch-groupedList` |
| `.segmented` | UISegmentedControl (iOS 13+) | `segmentedControl-largeTitle-list` |
| `.modal` | UIAlertController alert | `alert` |
| `.dropdown`, `.context-menu` | Action sheet / context menu rows | `actionSheet` |
| `.input` | Search field fill | `navBar-largeTitle-searchBar-list` |
| `.slider` | UISlider | `slider` |
| `.progress` | UIProgressView | `progressBar` |
| `.tabs[aria-orientation=vertical]` | iPad sidebar selection | `insetGroupedList-sidebar` |
| `.table` | none (iOS has no data table); styled as a plain list | — |

## Not found

No usable reference for: data tables, toasts / notification banners,
tooltips, meters, badges, the iPad dock (taskbar), message bubbles, a
popover, the keyboard (only a 355px Wikipedia thumbnail of the iOS 11
keyboard), or a high-resolution iOS 7 screen.
