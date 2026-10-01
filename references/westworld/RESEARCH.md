# Westworld: research notes

These are screen-captured reference stills of fictional UI from HBO's
*Westworld* (2016-2022), kept for design comparison only. The theme does
not reproduce the DELOS wordmark, HBO marks or any artwork. Research was
done on 2026-10-01. The primary source was fetched in full. Fandom page
HTML is behind a Cloudflare challenge, so wiki images were found through
the MediaWiki API (`api.php?action=query&list=search&srnamespace=6`) and
fetched from `static.wikia.nocookie.net` with a browser User-Agent and
Referer. Medium and Behance returned 403, and nothing from those sites is
used.

**Credit correction:** the brief describes the UI as designed by Tobias
van Schneider's team. It was not. The tablet and phone graphics were
designed by **Chris Kieffer** (video graphics supervisor on *Westworld*;
also *Passengers* and *Interstellar*). Van Schneider *interviewed* him for
DESK magazine, which is the primary reference below.

## Primary source

Tobias van Schneider, "Behind the scenes of the Westworld UI", DESK, 17
June 2017. https://vanschneider.com/blog/behind-the-scenes-of-the-westworld-ui/
Facts used from the article:

- The tri-fold tablets were always done in post (VFX). Some background
  tablets used real tablets or EL paper for interactive light. The UI was
  pre-designed so actors' gestures could be matched afterwards.
- The phone's bottom icon row is described as: device settings,
  tools/utilities, security, host database/logs, and admin controls.
- "Hero" screens must be legible in one or two seconds. This is why the
  UI is high-contrast line-work with large labelled values.

The article also shows *Passengers* (`PASS_SS*`) and *Independence Day:
Resurgence* (`IDR_GFX*`) images. Those are **not Westworld** and are
excluded.

## Images

| File | Source / credit | What it shows |
|---|---|---|
| `attributeMatrix-radialDial-segmentedSlider-layers.jpg` | DESK / Chris Kieffer, `WW_SS027_Layers` | Tri-fold tablet: radial attribute dial with lime and cyan bars, the DELOS pill, UPLOAD / CANCEL caps, a host portrait ring with HR / SpO2 / RR vitals, the right-hand fold of vertical segmented sliders (COORDINATION, AGGRESSION, LOYALTY), and the layer breakdown (radar, node graph). |
| `attributeMatrix-radarChart-vitalsReadout.webp` | Westworld wiki, "Maeves Personality Attributes - The Adversary" (S1E6, HBO) | Full-HD frame of the same tablet in radar mode: `ATTRIBUTE MATRIX: ATRBT GROUP 01`, bracketed values `[14] BULK APPERCEPTION`, MODIFY / CANCEL tabs, a notched window corner, and lime `HR 111` / cyan `SpO2 92`. |
| `radarChart-bracketLabels.webp` | Westworld wiki, "Attribute Matrix" (S1E6) | Close crop of the radar and its condensed uppercase bracketed labels. |
| `mobileTablet-modal-contextMenu-iconBar.jpg` | DESK / Kieffer, `WW_SS010` | Field phone, four frames: a call modal (`00:04 Control Room`), a `POOR CONNECTION` warning banner, END / HOLD buttons (outlined vs tinted active), a context menu (Contact / Message / Connect / Report / Send Data), a `< CONTROL ROOM >` chevron pill, a cyan tool-tile icon bar, and topographic map line-work. |
| `mobileTablet-tabs-sectorMap.jpg` | DESK / Kieffer, `WW_SS021` | Phone sector map: thumbnail strip, chip tab row CODE / HOSTS / SATELLITE (active) / MODS / INFO / DATA, `SECTOR [17]`, and a vertical stack of `< FOCUS >` chevron buttons. |
| `keyboardTablet-hexKeys-codeReadout.jpg` | DESK / Kieffer, `WW_SS004` | Host-programming keyboard tablet: hexagonal outlined keys, a green code listing, a tab row HOSTS / SOFTWARE / MODS / INFO / DATA, and a node-graph inset. |
| `diagnosticTablet-nodeGraph-restrictedPanel.jpg` | DESK / Kieffer, `WW_SS009` | Diagnostic tablet: path header `DELOS/Hosts/AC5000487105`, amber connector node graph, a `RESTRICTED` panel, `CORE CODE FUNCTIONS`, and green code panes. |
| `diagnosticTablet-brainScan.jpg` | DESK / Kieffer, `WW_SS008` | Tablet on the lab table beside Bernard: a blue scan view with a cyan tile column. |
| `controlRoom-mapTable-redWall.jpg` | DESK / Kieffer, `WW_SS007` | The Mesa control room: the red-lit curved wall, the park map table and the console row. |
| `controlRoom-consoleTable.jpg` | DESK / Kieffer, `WW_SS012` | Operator at a glass console: a grid of camera and map tiles under the red cove light. |
| `controlRoom-cameraFeedPanel.webp` | Westworld wiki, "Control Room panel" (S1, HBO) | Console with a large live-feed panel and a thumbnail column with outlined frames. |
| `tablet-glitch-dangerState.webp` | Westworld wiki, "MAEVES TABLET OPENED BY FORD" (S2, HBO) | Darker S2 tablet: `UNLOCKING... CORE PERMISSIONS` modal, red and green bar stacks, and cyan icon tiles. Source for the danger red. |
| `attributeMatrix-verticalSlider-hostCard.webp` | Westworld wiki, "WA05" (*Westworld Awakening* VR, HBO / Survios, 2019) | The game's attribute-matrix pane: segmented vertical sliders (TRUST / SUSPICION) with triangle markers, a host card and SYNCED OBJECTS. This is secondary, because it is the game and not the show. |
| `securityPanel-breadcrumb-navList.webp` | Westworld wiki, "WW.Delos.comms.panel" (discoverwestworld.com ARG, HBO 2016) | The Delos Security Panel web page: DELOS pill, breadcrumb `FLAGGED COMMS > …`, a side nav list with counts, an Admin field, and message rows. The fan's red annotation is not part of the UI. |

## Sampled palette

Samples are 1x1 averages and `-colors N` histograms (ImageMagick) taken
from the frames above. All are photographed values, so the emitted
screen colours are brighter.

| Sample | Hex | Theme token |
|---|---|---|
| Tablet slate (matrix background) | `#1e2e33`, `#263b43`, `#21333b` | `--surface #17252b`, `--surface-2 #1f323a` |
| Deep tablet black at the edges | `#142126` | `--bg #0f191d` |
| Panel and slider line | `#2e4e59`, `#49636a` | `--border #3a5c66` |
| Tablet cyan (radar, labels) | `#3f96a6`, `#5c9ba4`, `#377487` | `--accent #4fc8dc` (lifted) |
| Phone cyan | `#289ea0` | (confirms the hue) |
| Vitals green (HR 111) | `#4fa364` | `--accent-2 #a5d65a`, `--success #8fd65a` |
| Node-graph amber (WW_SS009) | about `#d9b13a` (by eye) | `--warning #f2b632` |
| Control room wall red | `#9e070a`, `#6d0609` | `--flare #c8102e` (status cove rule only) |
| S2 glitch red | about `#e04030` (by eye) | `--danger #ff5a4f` |

## Typography

- **Labels:** a condensed, DIN-like grotesque in uppercase throughout
  (`ATTRIBUTE MATRIX`, `CONTROL ROOM`, `SECTOR [17]`). The production face
  has not been published. Antonio (OFL, already vendored for lcars) is
  used as the closest free condensed face.
- **Wordmark:** DELOS appears in a wide, bold sans inside a pill outline
  with a double arc on its right. Only the pill outline is imitated, on
  `.nav-brand`.
- **Numerals and code:** vitals and code panes use squared mono-like
  digits. Share Tech Mono (OFL, already vendored for prometheus) is used
  for them.
- **Body copy:** the ARG Security Panel sets body text in a plain
  geometric or grotesque sans, so the theme uses a system Helvetica/Arial
  stack.

## Component mapping

| ftl-themes component | Reference | Treatment |
|---|---|---|
| App shell | matrix tablet (tri-fold), control room | Separate rounded slate panes with dark folds between them, a centre crease on main, a right-hand rail of segmented sliders, and a status strip with the red cove-light rule. |
| `.nav-brand` | DELOS pill on every device | Outlined 999px pill, bold, tracked caps. |
| `.btn` | END / HOLD, UPLOAD / CANCEL | 1px outline over a cyan tint, 0.3rem radius, condensed caps. Primary is solid cyan. |
| `.tabs`, `.nav-item`, `.segmented` | phone CODE / HOSTS / SATELLITE row | Chips. The active chip gets a cyan outline and tint. |
| `.panel`, `.card` | matrix window with notched corner | Thin slate border, cyan corner triangle, header led by a cyan rule. |
| `.badge` | `[14] BULK APPERCEPTION`, `SECTOR [17]` | Bracketed caps. |
| `.meter`, `.progress`, bar chart | vertical attribute sliders | Segmented squares in cyan, then lime, then red. |
| `.readout` | HR 111 / SpO2 92 | Mono cyan numerals with a faint glow. |
| `.modal` | phone call modal, S2 `CORE PERMISSIONS` box | Cyan border, slate body, uppercase cyan header. |
| `.dropdown`, context menu | phone context menu | Slate list with hairline rules. |
| `.alert` (warning) | `POOR CONNECTION` banner | Outlined slate box. (The banner is cyan in the source. The theme keeps semantic colours.) |
| `.table` | security panel message rows, matrix value lists | Cyan condensed heads over a 1px cyan rule, hairline rows. |
| `.input` | keyboard tablet fields (inferred) | Recessed well, mono text, cyan caret. |

## Gaps (no good reference found)

There is no clear on-screen reference for: tables with column headers,
toasts, a checkbox or switch, select and textarea fields, pagination,
tooltips, avatars, a horizontal progress bar, or skeleton and empty
states. All of these are extrapolated from the tablet's line-work.
