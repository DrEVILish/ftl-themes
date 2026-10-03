# Cyberpunk 2077: research notes

These notes cover the palette, shape language and type for
`themes/cyberpunk-2077`. The images in this folder are in-game screenshots
of *Cyberpunk 2077* (© 2020 CD PROJEKT S.A.; developed by CD PROJEKT RED),
as collected and published by *Interface In Game*
(https://interfaceingame.com/games/cyberpunk-2077/), a reference library of
video game UI. They are filed here only as design references for comparison
(fair-use study material, not redistributed in any bundle). The theme
reproduces none of them, and no logo, wordmark, corporation mark or game art
ships in the theme. Some frames show the game's yellow logo or corporation
names in the scene; the theme takes none of that.

Research was done in this session (2026-10-02). The Cyberpunk Fandom wiki and
Game UI Database returned 403 / Cloudflare challenges and could not be
fetched. Interface In Game served the original 1920×1080 PNGs; each was
resized to 1600px wide WebP (quality 72), and one (`hudBar-health-segments`)
is a crop of the top-left of its frame.

## Primary direction

**The pause-menu screens (inventory, character, journal, database,
crafting, settings) plus the breach-protocol minigame for tables and the
combat HUD for `.hud-*`.** The menus are the screens every player spends
time in and they share one consistent language (red ink on maroon-black,
cyan for live state, cut corners), so they define the theme. The breach
screen supplies the table style that PLAN.md §21 asks for, and the HUD
frame supplies the health bar, XP bar and RAM pips. The phone/messages
overlay and the cyan tutorial pop-ups back toasts and conversation.

## Images

All images: source page `https://interfaceingame.com/screenshots/cyberpunk-2077-<name>/`, image `https://interfaceingame.com/wp-content/uploads/cyberpunk-2077/cyberpunk-2077-<name>.png`, © CD PROJEKT S.A., via Interface In Game.

| File | Source / credit | What it shows |
|---|---|---|
| `appBar-tabs-inventorySlots.webp` | `<name>` = `backpack` | The menu top bar: LEVEL / STREET CRED with pip bars, the `[1]` `[3]` bumper key boxes, tabs (JOURNAL CRAFTING **INVENTORY** MAP CHARACTER) with the active one cyan, the long red rule broken by the cyan "BACKPACK" sub-title, weight and eddies at the right, then COMPONENTS / FILTERS / SORTING and item slots. |
| `settingsTabs-slider-switch-sectionHeader.webp` | `controls` | Settings: tab row (SOUND **CONTROLS** GAMEPLAY …) between key boxes, red labels left, value tracks (navy, red rule, cut corner) with a red parallelogram thumb and a cyan value, OFF/ON block pairs, white section headers on a dark band with a cyan hairline, GAMMA CORRECTION / CONTROL SCHEME buttons. |
| `stepper-switch-tabs.webp` | `graphics` | Graphics settings: ◁ value ▷ steppers, OFF (red slab) / ON (cyan slab) toggles, a value slider, DEFAULTS button, the bottom key-hint strip. |
| `breachGrid-table-panel-cornerBrackets.webp` | `breach-protocol` | The breach-protocol minigame: BREACH TIME REMAINING with a yellow-green bar and a boxed 999.00, the BUFFER slots, the CODE MATRIX panel (yellow-green filled header bar, dark teal grid of hex codes, a highlighted steel row band), cyan corner brackets, SEQUENCE REQUIRED TO UPLOAD, and the teal tutorial pop-up. |
| `modal-btn-kbd.webp` | `confirm-save` | The overwrite-save confirmation: a translucent red panel with a cut corner and a side notch, and CONFIRM / CANCEL buttons (dark red plates with cyan `↵` / `ESC` key caps, cut bottom-right corners). |
| `list-selectedItem-panel.webp` | `character-database` | The database: category list rows as dark plates in red rules with a cut corner, a ▽ disclosure, yellow NEW tags, the selected row as a solid red fill, the cyan cursor box, and the detail column (red title, red body text). |
| `segmented-cardImage-modalTitle.webp` | `select-difficulty-level` | SELECT DIFFICULTY LEVEL: a centred caps title with a key glyph, a framed artwork card, and an EASY / NORMAL / **HARD** / VERY HARD segmented row with the selected item filled red. |
| `list-prose-panel.webp` | `journal` | The journal: MAIN JOBS list with the selected job in a red plate, the quest title and objectives, and a long red body text column with a red scroll rule. |
| `inventoryGrid-rarity-btn.webp` | `crafting` | Crafting: category icon row, the item grid with slots outlined in rarity colours, a weapon stat card (DPS in cyan, stat lines), and the cyan-outlined CRAFT button. |
| `hudBar-health-segments.webp` | `driving` (crop of the top-left) | The combat HUD: a cyan level box with a cut corner, the cyan XP line, the red health bar with a glow and an angled end, the value "69" with a small max, and the cyan RAM pips beneath. |
| `toast-levelUp-minimap.webp` | `level-up` | LEVEL UP!: a cyan plate with a dark title, ATTRIBUTE / PERK POINTS lines, "OPEN PERKS [Z]" in red with a cyan key cap, and the cyan-framed minimap with "AREA: PUBLIC". |
| `menuList-pauseMenu.webp` | `pause` | The pause menu: a vertical list of red caps items (RESUME, SAVE GAME, … QUIT GAME) at the left over the dimmed scene (the game logo appears above it; not used). |
| `messages-list-panel.webp` | `messages` | The phone messages overlay: a cyan-framed conversation list with unread markers and the message body in white on dark teal-black. |
| `table-stats-readout.webp` | `stats` | The stats screen: label / value rows (cyan numbers beside red labels), STREET CRED progress, TOTAL PLAY TIME readout. |
| `alert-tutorialPopup-questTracker.webp` | `job-objectives` | A cyan tutorial pop-up (JOB OBJECTIVES) with a filled title strip and body text, the job tracker in the HUD corner (yellow quest marker, red objective text), and the minimap. |

## Sampled palette

Sampled with ImageMagick (`-colors N -format %c histogram:info:` over small
crops of the 1920×1080 originals). Anti-aliased text samples read darker
than the true glyph colour.

| Role | Sampled | Theme token |
|---|---|---|
| Menu backdrop | `#0e0e13` | `--bg #0e0d12` |
| Top-of-screen maroon wash | `#301218` / `#2a1018` | page and bar gradient `#1c0d12`–`#301218` |
| Value track / panel navy | `#16111f` | `--input-bg #16111f`, `--surface #1a1119` (pulled warm) |
| Red rule (long bar rule) | `#e9524b` | `--cp-red #ff5f58` |
| Red label text (anti-aliased) | `#d7443d` / `#f75a52` | `--text #ff8a82` (lifted to 8:1, so text dimmed to 0.7 still reads), `--muted #e3645d` |
| Red slider thumb / OFF slab | `#dc4643` / `#932d2a` | slider thumb `--cp-red`, `--switch-bg #3a1418` |
| Modal red tint | `#491d23`, border `#e64129` | modal wash `rgba(255,95,88,.14)` |
| Cyan values / active tab | `#47c7cc` (AA) – `#6ab2b7`; true colour ≈ `#5ef6ff` | `--accent #5ef6ff` |
| Button key-cap border | `#4cabb5` | `--kbd-border` cyan |
| Street cred green | `#23ba67` | `--success #2bd97c` |
| Eddies orange-yellow | `#d76e3b` | (not used) |
| Breach head bar / codes | `#cfec58` / `#c3e053` | `--flare` / `--table-head-bg #cfec58` |
| Breach matrix | `#121f1f` | `--table-bg #121f1f` |
| Breach highlighted row | `#29353d` | `--row-hover-bg #29353d` |
| Breach corner bracket | `#86f186` (green-cyan) | cyan brackets `#5ef6ff` |
| Tutorial pop-up teal | `#06e5c3` | (toast uses the cyan) |
| Brand yellow | `#fcee0a` (known brand value; tags too small to sample) | `--accent-2`, `--warning #fcee0a` |

Theme-only choices: `--danger #ff2a3d` (a hotter red than the ink, so a
danger fill is distinct from normal text) and `--danger-text #ff4d7a`
(pink-red). The chart palette is not sampled; it was run through the
dataviz validator (dark mode on `--surface`) and keeps the game's hue
order: cyan, red, yellow, violet, orange, green.

## Typography

All menu text is one squared, condensed technical sans: uppercase for
titles, tabs, buttons and labels, sentence case for descriptions, with
tabular figures. The community identifies it as Blender Pro (Binnenland);
this could not be verified from the game files in this session. Blender Pro
is commercial, so the theme vendors **Rajdhani** (Indian Type Foundry, SIL
OFL 1.1, licence checked in the `google/fonts` repo `ofl/rajdhani/OFL.txt`),
Medium and Bold, Latin subset woff2 from Google Fonts. Code and logs reuse
the vendored Share Tech Mono.

## Component mapping

| Component | Reference | Treatment |
|---|---|---|
| Page | all menus | Near-black with a maroon wash from the top and faint scanlines |
| `.app-bar` | `appBar-tabs-inventorySlots`, `list-selectedItem-panel` | Maroon strip ended by one long glowing red rule; brand cyan, nav red, active cyan |
| `.app-rail` | screen-edge micro print in every menu frame | Tick marks and short code bars in dim red |
| `.app-status` / `kbd` | `stepper-switch-tabs`, `modal-btn-kbd` | Key-hint strip; `kbd` a cyan outlined key cap |
| `.panel` / `.card` | `list-selectedItem-panel`, `modal-btn-kbd` | Red 1px frame in the background, cut bottom-right corner with a diagonal, 3px red tab top-left, red wash |
| `.modal` | `modal-btn-kbd` | The same frame plus scanlines and a stronger wash |
| Modal close | `modal-btn-kbd`, every menu's `[ESC] Close` hint | `--btn-close-glyph: "ESC"` as a cyan key cap; min/max as cyan boxes |
| `.btn` | `modal-btn-kbd`, `inventoryGrid-rarity-btn` | Dark red plate, red rule, clipped corner with a diagonal; hover cyan |
| `.btn-primary` | `segmented-cardImage-modalTitle` (selected HARD) | Solid red slab, cyan on hover |
| `.tabs` / `.nav` | `settingsTabs-slider-switch-sectionHeader` | Tracked caps, red inactive, cyan active with a cyan underline |
| `.table` | `breachGrid-table-panel-cornerBrackets` | Breach grid: yellow-green head bar, teal matrix, steel hover band, cyan selection, cyan corner brackets on `.table-wrap` |
| `.input` / `.select` | `settingsTabs-slider-switch-sectionHeader` | Navy track, dim red rule, cyan value |
| `.segmented` / `.switch` | `stepper-switch-tabs` | OFF red / ON cyan blocks, square |
| `.slider` | `settingsTabs-slider-switch-sectionHeader` | Navy track, red slab thumb with a glow |
| `.progress` / `.meter` | `hudBar-health-segments` | Flat red fill, angled end |
| `.hud-bar` / `.hud-slot` | `hudBar-health-segments`, `inventoryGrid-rarity-btn` | Glow in the fill colour, angled end; slots glow in rarity colours |
| `.toast` | `toast-levelUp-minimap`, `alert-tutorialPopup-questTracker` | Cyan-edged teal plate |
| `.alert` | `modal-btn-kbd` | Red-tinted plate with a 4px state bar |
| `.badge` | `list-selectedItem-panel` (NEW tags) | Clipped tag, caps |
| `.list` | `list-selectedItem-panel`, `list-prose-panel` | Hairline rows, cyan active marker |
| `.readout` / `.stat-value` | `table-stats-readout` | Cyan figures beside red labels |
| `.message` | `messages-list-panel` | Dark plates; own messages cyan-edged teal |

## Gaps

- **Typeface:** Blender Pro is an unverified community identification.
- **Quickhack wheel, scanner overlay and the full combat HUD** (ammo
  counter, quick-access slots) are not referenced beyond the health/XP/RAM
  crop; `.hud-slot`, the quest tracker and floating numbers are
  interpretations in the same language.
- **Dropdown / context menus:** the game has almost none (it uses steppers
  and radial wheels); the hairline cut-corner menu is an interpretation.
- **Tooltips:** the game's item-compare cards are richer than a tooltip;
  the dark plate with a cyan rule is an interpretation.
- **Charts:** no in-game chart exists; series colours are validated, not
  sampled.
