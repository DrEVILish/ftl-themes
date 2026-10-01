# Liquid Glass: research notes

Apple's Liquid Glass design language, announced at WWDC on 9 June 2025 and
shipped in iOS 26, iPadOS 26, macOS Tahoe 26, watchOS 26 and tvOS 26.
Research done 2026-10-01 from Apple's own pages: the Newsroom press
releases (images below) and the Human Interface Guidelines JSON behind
developer.apple.com/design (Color, Materials).

All images are Apple Inc. press images from Apple Newsroom, © Apple Inc.,
downloaded at the `large_2x` size and recompressed (≤1600px wide, JPEG
q80). They are kept here as design references only.

## Images

Shared (`references/liquid-glass/`):

| File | Source | What it shows |
|---|---|---|
| `overview-devices.jpg` | [Apple introduces a delightful and elegant new software design](https://www.apple.com/newsroom/2025/06/apple-introduces-a-delightful-and-elegant-new-software-design/), `Apple-WWDC25-Liquid-Glass-hero-250609` | The design across Apple TV, Mac, iPad, iPhone and Watch: glass Dock, glass widgets, floating tab bars. |
| `desktop-dock-widgets.jpg` | same article, `…Home-Screen-clear-look…` | macOS Tahoe desktop, "clear look": transparent menu bar, glass Dock, glass widgets over a blue wave wallpaper. |
| `lockScreen-notification-transport.jpg` | [Apple elevates the iPhone experience with iOS 26](https://www.apple.com/newsroom/2025/06/apple-elevates-the-iphone-experience-with-ios-26/), `Apple-WWDC25-iOS-26-hero` | Five iPhones: Messages bubbles, a glass Now Playing transport, the glass Lock Screen clock and notification stack, the clear-look Home Screen. |
| `tabBar-list-btnIcon.jpg` | iOS 26 article, `…Phone-unified-layout…` | **The key control reference.** Phone app: floating capsule tab bar (Calls / Contacts / Keypad) with a grey lens behind the blue selected item, a separate circular search button, circular glass "Edit" and filter buttons at the top, inset list with hairlines and circular call buttons. |
| `message-input-btnIcon.jpg` | iOS 26 article, `…Polls-in-Messages…` | Messages: grey and blue bubbles, a poll with tinted capsule choices, circular glass back/video buttons, a glass capsule "Lucky 7" title, a capsule input field and a round "+" button. |
| `modal-sheet-searchField.jpg` | iOS 26 article, `…Maps-Visited-Places…` | Maps: a sheet with large rounded corners floating over the map, circular glass close button, a capsule search field, rounded colour cards. |
| `sidebar-window-transport.jpg` | [macOS Tahoe 26 makes the Mac more capable…](https://www.apple.com/newsroom/2025/06/macos-tahoe-26-makes-the-mac-more-capable-productive-and-intelligent-than-ever/), `…Apple-Music…` | Music on Tahoe: the inset, rounded glass sidebar with traffic lights in its corner, a grey selected-row lens, a floating capsule transport bar over the content, the glass Dock. |
| `switch-slider-btnIcon.jpg` | macOS Tahoe article, `…Control-Center…` | Control Center: circular and capsule glass toggles (on = white), Display/Sound modules with thick capsule sliders, a small "Edit Controls" capsule. |
| `toolbar-addressBar-trafficLights.jpg` | macOS Tahoe article, `…Safari…` | Safari: a single compact toolbar, a capsule back/forward pair sharing one piece of glass, a capsule address field, the window's 26-ish px corner radius. |
| `toast-toolbar-btnGroup.jpg` | macOS Tahoe article, `…Phone-incoming-call…` | An incoming call as a rounded glass card with circular red/green buttons; Preview's toolbar with grouped zoom buttons in one capsule; Calendar's "< Today >" control. |
| `menuBar-dropdown.jpg` | [iPadOS 26 introduces powerful new features…](https://www.apple.com/newsroom/2025/06/ipados-26-introduces-powerful-new-features-that-push-ipad-even-further/), `…menu-bar…` | The iPad menu bar and an Edit menu: large-radius glass menu, rounded grey highlight on the hovered item, a submenu tinted by the content behind it (pink). Circular toolbar buttons. |
| `table-sidebar-toolbar.jpg` | iPadOS 26 article, `…Files-app-List-view…` | Files list view: inset glass sidebar with grey selected-row lens, column headers in sentence case (blue sort column), hairline rows, circular toolbar buttons grouped in capsules. |

Dark (`references/liquid-glass/dark/`):

| File | Source | What it shows |
|---|---|---|
| `dark/desktop-dock-widgets-tinted.jpg` | Liquid Glass article, `…Home-Screen-dark-tint…` | macOS Tahoe with the dark "tinted" look: smoked glass Dock and widgets, orange-tinted icons. |
| `dark/tabBar-btn-dark.jpg` | iOS 26 article, `…Apple-Games-app…` | Games app in dark: the smoked floating capsule tab bar with a lens behind "Home", a separate round search button, a dark glass "Play" capsule. |

## Palette

From the HIG Color page (iOS 26 "updated system color values"; the tables
are images on the page, values as transcribed for the iOS 26 release):

| Role | Light | Dark | Used as |
|---|---|---|---|
| systemBlue | `#0088ff` | `#0091ff` | `--accent-2`, `--focus`, progress, caret |
| systemRed | `#ff383c` | `#ff4245` | basis of `--danger` `#e0262b` (deepened for white text) |
| systemGreen | `#34c759` | `#30d158` | `--success`, switch on |
| systemOrange | `#ff8d28` | `#ff9230` | `--warning` |
| label | `#000000` → `#1d1d1f` | `#ffffff` → `#f5f5f7` | `--text` |
| secondaryLabel | `#3c3c43` @ 60% | `#ebebf5` @ 60% | basis of `--muted` |
| fill (tertiary) | `#767680` @ 12% | `#767680` @ 24% | input, segmented, lens fills |

Apple's web action blue `#0071e3` is used as `--accent` because white on
`#0088ff` is only 3.5:1.

Sampled from the images (6px average, so JPEG-softened):

| Where | Hex |
|---|---|
| Phone tab bar glass over white list | `#ededed` |
| Phone tab bar lens around the selected item | `#e1e1e3` |
| Control Center module glass over the blue wallpaper | `#5493a2`, `#98aee5` |
| Control Center slider fill | `#3684de` |
| Tahoe wallpaper deep blue / mid blue | `#1466c5`, `#1c97b6` |
| Music window content | `#ffffff` |
| Music sidebar selected row | `#ebebeb` |
| Traffic lights (standard macOS values) | `#ff5f57`, `#febc2e`, `#28c840` |

## Typography

SF Pro (Text/Display) everywhere; SF Mono for code. Large titles are bold
with tight tracking ("Home", "Recents", "Visited Places"); list headers
are sentence case; nothing is set in uppercase except tiny stat labels.
SF is Apple-licensed and not vendored.

## Guidance quoted from the HIG (Materials, Color)

- "Liquid Glass forms a distinct functional layer for controls and
  navigation elements — like tab bars and sidebars — that floats above the
  content layer." → glass on bars/controls/menus/sheets; frosted standard
  material on panels/cards.
- "Don't use Liquid Glass in the content layer." → no specular rim on
  `.panel`/`.card`.
- Two variants, *regular* (blurs and adjusts luminosity for legibility;
  most system components) and *clear* ("only … over visually rich
  backgrounds"; consider "a dark dimming layer of 35% opacity" over bright
  content). → `--lg-regular` / `--lg-clear`.
- "Liquid Glass has no inherent color, and instead takes on colors from
  the content directly behind it." → `saturate()` in the backdrop filter.
- "Apply color sparingly to the Liquid Glass material." → one tint, used
  for the prominent button and selected labels.

## Component mapping

| ftl-themes component | Reference | Treatment |
|---|---|---|
| `.app-bar` | Safari toolbar, iPad toolbar | Floating clear-glass capsule inside the window top, sticky. |
| `.app-rail` | Music / Files sidebar | Tall rounded glass pane, traffic lights, selected-row lens. |
| `.app-main` | Music window | One frosted 28px window pane spanning all rows. |
| `.app-status` / `.taskbar` | Phone / Games tab bar | Centred floating capsule; active item in a grey lens. |
| `.btn` | Phone "Edit", Messages back | Clear-glass capsule, rim highlight. |
| `.btn-primary` / `-danger` / `-success` | Phone call buttons, Control Center on-state | Tinted glass: colour fill keeping the rim, coloured bloom. |
| `.btn-icon` | Phone search, Maps close | Glass circle. |
| `.btn-group` | Safari back/forward, Preview zoom | One capsule of glass shared by the buttons. |
| `.tabs`, `.nav-item` | Phone tab bar | Capsule; selected = grey lens + blue label. |
| `.segmented` | Calendar "Today" control, Control Center | Grey capsule track, white lifted lens. |
| `.switch` | Control Center (macOS), iOS Settings | Green track, wide capsule knob. |
| `.slider` | Control Center Display/Sound | Capsule track, white capsule thumb. |
| `.input` | Messages input, Maps search | Grey-filled capsule. |
| `.dropdown`, `.context-menu` | iPad Edit menu | 18px glass menu, 12px rounded item highlight. |
| `.modal` | Maps sheet | 28px glass sheet, round close button. |
| `.toast` | Lock Screen notifications, incoming call | 22px glass card. |
| `.table`, `.list` | Files list view, Phone recents | Sentence-case grey headers, hairline rows, rounded selection. |
| `.message-bubble` | Messages | Grey incoming, blue outgoing, 20px radius. |
| `.transport` | Music mini player, Lock Screen Now Playing | Glass capsule. |
| `.progress`, `.meter` | Control Center slider fill | Thin capsule, systemBlue fill. |

## Not verified / gaps

- The iOS 26 system colour values come from the HIG's colour tables,
  which are images; the hexes above are as commonly transcribed, not read
  from text.
- No reference shows a data table with a header row in a web sense, a
  level meter, a form with validation errors, badges as filter chips,
  a progress bar, an alert banner or a tooltip in Liquid Glass.
- The refraction (lensing at the rim) is visible in Apple's videos, not in
  these stills; it is approximated, not measured.
- The wallpaper in `theme.css` is a CSS sketch of the Tahoe default, not
  the image.
