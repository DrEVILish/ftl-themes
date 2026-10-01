# iOS (Skeuomorphic): research notes

Reference images for `themes/ios-skeuomorphic`, the iPhone OS 1 to iOS 6
(2007-2012) theme. Its flat iOS 7-18 sibling is `ios-flat`; nothing here
should be read as guidance for that theme. Research done 2026-10-01 by web
search and direct download. Every screenshot is Apple's UI. They are kept here
as design reference only. No pixels from them are used in the theme, which
draws every texture in CSS.

## Images

| File | Source / credit | What it shows |
|---|---|---|
| `groupedTable-switch-navBar-badge.webp` | Martin Nobel, "iOS 6 Revisited", https://www.martinnobel.com/techresearch/ios-6-screenshots (IMG_0051, iPhone 5 on iOS 6) | Settings. This is the main reference for the pinstripe backdrop, rounded grouped cells, bold black labels, blue value-1 detail text ("Nobel WiFi", "On"), gray-blue count badge, OFF switches and the blue nav bar with an embossed title. |
| `groupedTable-pinstripe-tabBar-navBar.webp` | Wikimedia Commons, "Cydia corriendo en iOS 6 con un iPhone 3GS.png", FanHabbo, BSD licence, https://commons.wikimedia.org/wiki/File:Cydia_corriendo_en_iOS_6_con_un_iPhone_3GS.png | A full-height UIKit page with nav bar capsule buttons, grouped cells with chevrons, section header text with a white emboss, and the black glossy tab bar whose selected item sits in a lit square with a blue icon. |
| `navBar-backBtn-barBtn.webp` | Wikimedia Commons, "IOS 6 Menu Bar.png", TheMostAmazingTechnik / Apple, marked public domain, https://commons.wikimedia.org/wiki/File:IOS_6_Menu_Bar.png | A close-up of the nav bar: the arrow-shaped back button, the bordered bar button and the embossed white title. |
| `linen-drawer.webp` | Martin Nobel (IMG_0015) | Notification Center: the dark slate linen, a darker linen header and a white embossed label. |
| `notesPaper-textarea-navBar.webp` | Martin Nobel (IMG_0032) | Notes: the yellow legal pad with ruled lines, a red margin, the brown leather nav bar and the glossy keyboard. |
| `feltTexture-hero-input.webp` | Martin Nobel (IMG_0050) | Game Center: green felt baize, a wood rim, inset fields and yellow-felt buttons. |
| `toolbar-segmented.webp` | Martin Nobel (IMG_0016) | Calendar day view: the blue nav bar, a blue toolbar with bordered bar buttons and the Today/List/Day/Month segmented control. |
| `tabBar-navBar-list.webp` | Martin Nobel (IMG_0038) | World Clock: list cells under the nav bar, with the black tab bar (World Clock selected, blue glow). |
| `avatar-btnSecondary-card.webp` | Martin Nobel (IMG_0053) | Contact Info: a photo placeholder in a framed rounded square, a grouped value cell and three white rounded-rect buttons with blue bold labels. |
| `messageBubble-input-btnSend.webp` | Martin Nobel (IMG_0072) | Messages: a green glossy SMS bubble, a recessed capsule text field, the green glossy Send button, and the nav bar back and Edit buttons. |
| `transport-slider.webp` | Wikimedia Commons, "IOS 6 music player buttons.jpg", Apple, screenshot by PuffFilms, marked public domain, https://commons.wikimedia.org/wiki/File:IOS_6_music_player_buttons.jpg | Music app transport: black glossy segments, white glyphs, and the silver knob on a chrome track. |
| `modal-input.webp` | Use Your Loaf, "UIAlertView changes in iOS 5", https://useyourloaf.com/blog/uialertview-changes-in-ios-5/ (002.png) | UIAlertView: a navy glass body with a lighter gloss band at the top, a white rim, white centered title and message, a white text field, and dark glossy Cancel next to a lighter OK. The page behind it is purple, so the hue is tinted; the true alert is navy blue. |
| `actionSheet-btn.webp` | Redmond Pie, "iOS 7 vs iOS 6 - Side By Side Visual Comparison", https://www.redmondpie.com/ios-7-vs-ios-6-side-by-side-visual-comparison-images/ (Mail.png, iOS 6 half cropped) | Action sheet: white glossy capsule buttons with bold dark labels and a dark Cancel, over a dimmed sheet. |
| `switchOn-groupedTable.webp` | Redmond Pie, same article (Settings-app.png, iOS 6 half cropped) | The ON state of the switch (orange because it is Airplane Mode; ordinary switches are blue) and the OFF state, inside grouped cells. |
| `readout-btnSuccess-tabBar.webp` | Martin Nobel (IMG_0040) | Stopwatch: large Helvetica figures on a dark gradient, a green glossy Start button, a gray Reset and the black tab bar. |

## Sampled palette (from the iOS 6 Settings screenshot unless noted)

| Role | Hex | Notes |
|---|---|---|
| Pinstripe base / stripe | `#d2d7e0` / `#cfd4de` | Vertical stripes about 7px apart at 1x. The theme uses `#d1d6df` / `#cbd1da` so the stripe stays visible on a desktop monitor. |
| Nav bar gradient | `#bdcbdc` → `#597498` | Highlight line `#eff2f7` on top. The theme starts at `#5b779c` instead (see the contrast note below). |
| Grouped cell / border / separator | `#f7f7f7` / `#afb3bb` / `#cacaca` | Cell corner radius is about 10px at 1x. |
| Detail-label blue | `#385487` | The value-1 cell style, e.g. the "On" next to Bluetooth. |
| Count badge | `#8795af` | The theme darkens it to `#67779a` so the white digit stays legible. |
| Chevron | `#7b7b7b` | |
| Linen (Notification Center) | `#434852` average | The weave varies from `#383b44` to `#474a56`. |
| Notes paper | `#f2ef9a` to `#fcf9af` | Nav bar leather runs `#875c4e` → `#48312b`. |
| Alert body / buttons (`modal-input`) | `#2a3961` body; buttons `#384467` → `#2b3a61`; OK `#747d96` | Sampled over a purple backdrop, so treat them as approximate. |
| Tab bar | `#424242` → `#2a2a2a` on the upper half, then `#000` | The selected cell sits around `#484848` → `#252525`. |

## Typography

The UI face is Helvetica (iPhone OS 1-4) and then Helvetica Neue (iOS 5-6).
Labels are bold. A 1px emboss is everywhere: white *below* the text on a
light ground, dark *above* it on a colored one. Notes used Marker Felt (later
Noteworthy). Nothing is vendored: the stack is Helvetica Neue / Helvetica /
Arial / Liberation Sans.

## Component mapping

| ftl-themes component | iOS source |
|---|---|
| `.app-bar`, `.nav`, `.toolbar` | UINavigationBar / UIToolbar (blue gloss, embossed title); `.app-bar` also carries the black status strip |
| `.nav-item`, buttons inside bars | Bordered UIBarButtonItem capsules; the active one is the "Done" blue |
| `.app-status`, `.tabs` | The black glossy UITabBar, with a lit square and blue glow on the selected item |
| `.btn` / `.btn-secondary` | Action-sheet glossy white button / rounded-rect UIButton with a blue label |
| `.btn-primary` / `-danger` / `-success` | Done blue / destructive red / Call-and-Start green gloss |
| `.panel`, `.card`, `.list`, `.field-row` | Grouped UITableView cells on the pinstripe |
| `.panel-header`, `.table th` | The plain-table section header gradient |
| `.table tr.is-selected`, `.list-item.is-active` | The selected-cell blue gradient (`#058cf5` → `#015fe6`) |
| `.switch` | The iOS 5/6 UISwitch with ON / OFF lettering |
| `.segmented` | UISegmentedControl, bordered style |
| `.modal` | UIAlertView |
| `.popover` | The iPad popover's navy frame |
| `.toast` | The iOS 5 notification banner |
| `.drawer` | Notification Center linen |
| `.textarea` | Notes legal pad |
| `.hero` | Game Center felt and wood rim |
| `.band.is-tinted` | Calendar / Find My Friends stitched leather |
| `.readout`, `.transport` | Stopwatch figures, Music app transport |
| `.message-bubble` | Messages SMS (green) and received (gray) bubbles |
| `kbd` | The iOS keyboard key |

## Honest gaps

- **The blue ON switch** comes from memory. The only ON switch in the set
  is Airplane Mode's orange one.
- **The alert view's colour** was sampled over a purple backdrop.
- **The iPad popover, the notification banner (toast) and the leather
  Calendar header** have no reference image here. They are drawn from memory.
- **Contrast deviations, on purpose:** the nav bar gradient is darker than
  the real one (white text has to reach 4.5:1), and so are the count badge
  and the section-header gradient.
