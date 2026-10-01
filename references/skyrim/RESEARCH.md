# Skyrim: research notes

These notes cover the palette, shape language and type for `themes/skyrim`. The
images in this folder are screenshots of *The Elder Scrolls V: Skyrim*
(© Bethesda Softworks / ZeniMax Media) and of the SkyUI mod (© the SkyUI
team: schlangster, snakster, Mardoxx, T3T and others). They are filed here
only as design references for comparison. The theme reproduces none of
them, and no logo, emblem or game art ships in the theme.

Research was done in this session (2026-10-01). Nexus Mods, PCGamingWiki
image hosting and the Elder Scrolls Fandom image CDN returned Cloudflare
challenges and could not be fetched. UESP image files only downloaded with
a browser User-Agent and a UESP Referer header.

## Primary direction

**Vanilla menu chrome + SkyUI tables.** SkyUI is the de-facto PC
inventory (it is among the most downloaded Skyrim mods), and its column
lists map directly onto `.table`. Vanilla supplies everything else: the
chevron title bar, the attribute bars, sliders, the key-hint strip and
the knotwork. The vanilla parchment journal is noted as a gap, because
no image of it could be fetched.

## Images

| File | Source / credit | What it shows |
|---|---|---|
| `table-tabs-selectedRow.webp` | Steam guide "SkyUI - Features Overview", https://steamcommunity.com/sharedfiles/filedetails/?id=426512192 (image https://images.steamusercontent.com/ugc/714161423405263125/4E2FE14FA4091FB377DF2B1136CCD1554DC25124/). SkyUI screenshot. | Container menu, Apparel and Weapons. Category icon row with a caret under the active icon, the FILTER box, tiny uppercase column heads (NAME TYPE CLASS ARM WGT VAL) with a sort arrow, right-aligned numbers, the selected row as a fading light band ending in an arrow tip, legendary gold stars and blue enchant bolts, knotwork corners on a thin silver frame, and the bottom "WARDROBE ◈ GRAYSON" name bar. |
| `table-infoCard.webp` | Same guide (ugc/714161423405425139). SkyUI. | The Magic menu list (NAME SCHOOL LEVEL COST) and the spell info card: a smoke panel with knotwork corners, an uppercase title over a rule, and "Expert / COST 285" in large condensed type. |
| `table-categoryIcons-badge.webp` | Same guide (ugc/714161423405226663). SkyUI. | Inventory ALL and POTIONS lists: a long category-icon strip, coloured item icons, and a scroll bar. |
| `form-switch-sectionHeader.webp` | Same guide (ugc/716413856113140961). SkyUI's Mod Configuration Menu. | The MCM: a "GENERAL" title tab with chevron caps, the left page list with a ◈ marker, section headers followed by a rule ending in a chevron, diamond toggles (◇ off, ◈ on), uppercase right-aligned values, and the key-hint strip ("Enter Select", "R Default", "Tab Back"). |
| `list-favorites-badge.webp` | Same guide (ugc/716413856113146805). SkyUI. | Favorites menu and favorite groups: a smoke column, filter icons, boxed group numbers 1/2/4 (badges), and the hot-key slot bar. |
| `searchInput-list-statusBar.webp` | Same guide (ugc/714161423405177220). SkyUI map search. | A search field with chevron end caps, a result list with icons, and the map's bottom key-hint strip ("L Local Map  J Journal  Wheel Zoom…"). |
| `compass-hud.webp` | Same guide (ugc/716413856113154912). SkyUI active-effects HUD. | Top-left: a crop of the vanilla compass bar (dark strip, silver rule, chevron end caps, "E" heading). Right: active-effect icons with small vertical timers. |
| `skillsMenu-meter-appBar.webp` | UESP, https://en.uesp.net/wiki/File:SR-menu-Skills_Menu.jpg | The skills menu: top info bar (NAME / LEVEL with the frost-blue level bar / RACE) with chevron end caps, a "Perks to increase" plate, the constellation, skill names with underline plates, and the bottom MAGICKA / HEALTH / STAMINA bars with diamond end caps. |
| `progressBar-healthBar.png` | UESP, https://en.uesp.net/wiki/File:SR-menu-Health.png | The health bar on its own: "HEALTH 200/200", a red fill with a pale highlight line, and a double-chevron frame. |
| `tabs-list-selectedItem.webp` | UESP, https://en.uesp.net/wiki/File:SR-menu-Character_Creation.jpg | Character creation: a title bar with "◁ Race ▷ Body Head" (active tab flanked by chevrons, others dimmed), a vertical list with the selected item enlarged and marked by a knot-chevron, a description in white condensed type, and the bottom strip "R Done … NAME Prisoner RACE Nord". |
| `slider-tabs-keyHints.webp` | Steam guide "Guide To An Immersive Skyrim", https://steamcommunity.com/sharedfiles/filedetails/?id=253523389 (ugc/792941440006403678). Vanilla. | Character-creation sliders: a thin track with diamond end caps and a small pointer thumb under the label, the same chevron tab bar, and the key-hint box "R Done". |
| `panel-tabs-journal.webp` | UESP, https://en.uesp.net/wiki/File:SR-menu-Statistics.jpg | The journal's General Stats page: a "QUESTS ◁ GENERAL STATS ▷ SYSTEM" title bar, a smoke panel with a thin silver frame and knotwork corners, a right-aligned category list (GENERAL / QUEST / COMBAT…), a label/value list, a scroll bar, and the bottom level bar with the date line. |
| `panelHeader-knotwork.png` | UESP, https://en.uesp.net/wiki/File:SR-qico-Main.png ("Quest icon for the main game quests") | The black-ink Nordic knotwork dragon used as a quest-type header in the journal. Basis for the "knotwork corners" idea. It is not reproduced. |
| `iconStrip-categoryTabs.png` | SkyUI repository, https://github.com/schlangster/skyui/blob/master/misc/Icon%20Themes/Straight,%20by%20T3T/preview.png (icons by T3T) | The SkyUI category-icon strip inside the vanilla knotwork-cornered frame: favourites, all, weapons, armour, potions, scrolls, food, ingredients, books, keys, misc. |
| `dialogue-subtitle.webp` | "Guide To An Immersive Skyrim" (ugc/792941440006472221). Vanilla. | A dialogue subtitle: small white condensed text with a grey speaker name, centred low on screen, with no box. |

## Palette (sampled)

Sampled with ImageMagick (`-colors N histogram` over small crops).

| Role | Hex | From |
|---|---|---|
| List smoke | `#161512` / `#24231f` / `#282723` | SkyUI list body (`table-tabs-selectedRow`) |
| Selected-row band | `#403e39` average, highlight to ~`#5f5f5f` | Same, selected row |
| Frame rule | `#5f5f5f`–`#80807f`, highlight `#a7a7a7` | Frame and heads |
| Column heads / dim text | `#a7a7a7` | Head row |
| Info-card smoke | `#1a2020` | `table-infoCard` |
| Health | `#b33e3f` / `#ae1e1e`, highlight `#d39d9e`, dark `#791b1b` | Skills-menu bottom bar; `progressBar-healthBar` `#ab3232` |
| Magicka | `#2433ac` / `#1c2caa`, highlight `#989fd4` | Skills-menu bottom bar |
| Stamina | `#1f6636` / `#338d5c`, highlight `#97bba5` | Skills-menu bottom bar |
| Level / XP bar | `#aec0d5` | Skills-menu top bar |
| Legendary star | ~`#e3c35a` (eyeballed; too small to sample cleanly) | `table-tabs-selectedRow` |

Theme mapping: `--surface #161512`, `--border #6f6f6c`, `--muted #a7a7a5`,
`--accent #aec0d5` (level bar), `--danger #b33e3f`, `--success #2a7a4b`
(stamina, darkened so white text passes), `--warning`/`--flare #e3c35a`,
`--accent-2 #8f9fe6` (magicka highlight, lifted from `#2433ac` for
legibility).

## Typography

All menu text is one condensed sans. Uppercase is used for titles and
column heads, sentence case for items and descriptions, and large
condensed numerals for values. The modding community identifies it as
Futura Condensed (Futura Std Condensed Light/Medium). I could not verify
this from the game's own font files in this session. Futura is
commercial, so the theme falls back to the repo's vendored Antonio
(Vernon Adams, SIL OFL 1.1).

## Component mapping

| ftl-themes component | Reference | Treatment |
|---|---|---|
| `.app-bar` | `tabs-list-selectedItem`, `skillsMenu-meter-appBar`, `panel-tabs-journal` | An inset strip with chevron-pointed ends (clip-path) and silver top/bottom rules |
| `.app-status` / `kbd` | `form-switch-sectionHeader`, `searchInput-list-statusBar`, `tabs-list-selectedItem` | A dark key-hint strip. `kbd` is a white-outlined key box |
| `.app-rail` | Vanilla inventory category column (no image fetched), `panel-tabs-journal` | A smoke strip with a vertical silver divider and a diamond |
| `.tabs` / `.tab.is-active` | `tabs-list-selectedItem`, `panel-tabs-journal` | `◁ ACTIVE ▷`, others dimmed |
| `.table` | `table-tabs-selectedRow`, `table-infoCard` | Tiny grey caps heads over one rule, no row rules, a fading white selected band with an arrow tip |
| `.panel` / `.panel-header` | `panel-tabs-journal`, `form-switch-sectionHeader` | Smoke, thin silver frame with an inner second rule, knotwork corners, and a header rule ending in a diamond |
| `.modal` | `table-infoCard` | The spell info card: centred uppercase title over a rule |
| `.progress` / `.meter` | `progressBar-healthBar`, `skillsMenu-meter-appBar` | Diamond end caps. Frost-steel fill. Meter bands are stamina, gold, health |
| `.slider` | `slider-tabs-keyHints` | Thin track, small white square thumb |
| `.checkbox` / `.switch` | `form-switch-sectionHeader` | Diamond toggles |
| `.input` / `.select` | `table-tabs-selectedRow` (FILTER box), `searchInput-list-statusBar` | Black field, thin silver rule |
| `.badge` | `list-favorites-badge` | A small boxed label on black |
| `.list` / `.dropdown` | `list-favorites-badge`, `searchInput-list-statusBar` | Smoke list, white band for the active item |
| Toast / alert | none (Skyrim's top-left notification text has no box) | A smoke plate with a state-coloured rule (an interpretation) |

## Gaps

- **Quest journal (vanilla parchment book):** no fetchable screenshot was
  found, and it is not modelled. The UESP statistics frame
  (`panel-tabs-journal`) shows the dark journal chrome instead.
- **Compass bar:** only the partial crop in `compass-hud.webp`.
- **Dialogue menu (the topic list):** only the subtitle frame.
- **Vanilla inventory (pre-SkyUI category column + item list):** not
  fetched. The rail treatment is from memory of it, not from an image.
- **Notifications, message boxes ("Are you sure?"), level-up, loading screen
  text:** not referenced. Toast, alert and modal button rows are
  interpretations.
