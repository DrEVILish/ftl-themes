# Silo: research notes

Reference material for `themes/silo`. Research done 2026-10-01 in this
session. All frames are stills of copyrighted screen graphics from *Silo*
(Apple TV+, produced by AMC Studios, 2023-). They are kept here as design
reference only and are not vendored into any bundle.

## Sources

| Source | What it gave |
|---|---|
| HUDS+GUIS, "Silo - Dystopian UI", Jono Yuen, 24 March 2025. https://www.hudsandguis.com/home/2025/silo-ui | Primary reference. Animated GIF captures of every screen sequence (hard drive, reproductive clearance, IT terminal, relic database, video playback, tablet, AI). Article text: "reminiscent of old DOS-based systems", "green monochrome palette, accented with subtle yellow hues", the terminal "leans into efficiency, cutting out any fluff". The single stills here were extracted from those GIFs (coalesced middle and two-thirds frames). |
| Territory Studio, "Silo" project page. https://territorystudio.com/project/silo/ | Credits Territory with Season 2's Legacy tablet UI, cipher visualisations and the sand-particle "Algorithm" for AMC Studios. Source of the two images in `references/silo/legacy/`. |
| IMDb art department credits (search snippet only). https://m.imdb.com/title/tt14688458/fullcredits/art_department | Philippa Broadhurst, lead graphic designer (10 episodes, 2023); Gavin Bocquet, production designer. Not fetched in full; the in-set terminal graphics are uncredited on the HUDS+GUIS page. No designer page for those graphics was found. |
| IndieWire, Silo props feature (search snippet). https://www.indiewire.com/features/craft/silo-props-apple-tv-plus-1234879799/ | The prop master describes the computers as "one steel, flat plate and a simple speaker": deliberately simple, controlled hardware. Basis for the steel bezel shell. |

## Images

All frames except the last two: *Silo* (Apple TV+ / AMC Studios), captured
by Jono Yuen for HUDS+GUIS (URL above). The images in `references/silo/legacy/`
(the `legacy` variant only): Territory Studio (URL above). Everything else
sits in `references/silo/` and backs the default palette and the shared
structure.

| File | Scene | What it shows |
|---|---|---|
| `relicDatabase-headerPlate-fieldGrid-authorizedBand-buttons.jpg` | S1, Judicial's relic database (Sims) | The richest frame. A top bar of three solid pale-teal plates (BACK / RELIC DATABASE / SYSTEM RUN) with dark text; a section title between double rules with an `x` at the right; a grid of outlined field cells, each with a tiny tracked-caps label top-left and a large value; a solid yellow-green "SEARCH AUTHORIZATION / JUDICIAL: SIMS" band; three outlined keys (CLEAR ALL, EDIT, SEARCH), the primary one with a heavier pale-yellow frame; a pale-teal status plate at the bottom ("DISK 10% RAM 40% 33911 BYTES FREE"). |
| `relicDatabase-resultsList-statusPlate-scrollbar.jpg` | S1, relic database results | Two-column list of outlined result cards (OBJECT / LEDGER REF / ORIGIN), a thin scrollbar on the right with a yellow-green thumb, filter chips with `x` at the bottom, the same status plate. |
| `driveBrowser-capacityBar-searchField.jpg` | S1, George's hard drive (Juliette) | DEVICE NAME / TYPE / READ label-value rows, a hatched yellow-green CAPACITY bar, a full-width outlined SEARCH field, BACK / SHOWING FILES row. |
| `fileList-selectionOutline.jpg` | S1, hard drive file grid | Outlined file cards with a small document glyph, name, "SEP 13, SILO YEAR 97" and size. The selected card is outlined in pale yellow and its text turns yellow. |
| `fileList-selectionOutline-sizeColumn.jpg` | S1, hard drive file grid | Same rule on another frame (SILO-BLUEPRINT selected), right-aligned sizes. |
| `levelsMap-loadingProgress-log.jpg` | S1, schematic viewer | "LEVELS 1 - 20" box over a segmented block progress bar ("LOADING UPPER LEVELS...") and a timestamped log pane. Ladder-like rail down the left edge. |
| `terminalLog-commandOutput.jpg` | S1, drive search | Line-numbered command output ("SEARCHING D/DIR/..."), keyword strip below a heavy rule. |
| `monitorBezel-fileGrid-softKeys.jpg` | S1, Juliette's workbench | The hardware: a chunky rounded grey-green CRT bezel, the whole UI on the glass, a row of outlined soft keys along the bottom edge, RUN / ESC-END keys at top right. |
| `pactHeader-numberedNav-countdownReadout-softKeyTabs.jpg` | S1, PACT reproduction terminal | Header between pale-yellow double rules: PACT mark, two rows of numbered menu entries ("01 STATUS", "02 SYSTEM"), clock at right. A row of outlined soft-key tabs with `>` (MESSAGE active in yellow). Centre: "PREGNANCY OPPORTUNITY TIME", a cream rounded block with "342", smaller rounded outlined pills with amber numerals (HRS 22 / MNS 14). |
| `siloMail-modal-headerPlate-warningButton.jpg` | S1, SiloMail | A pale-teal title strip ("1 NEW MESSAGE / CLOSE / SILOMAIL"), a message box with a heavy bright rounded frame, title in teal caps, body in amber caps, an amber filled VIEW key. |
| `progressDialog-openingDrive.jpg` | S1 | A small outlined dialog on a noisy navy screen: "100%", a thin bar, "OPENING DRIVE". |
| `videoPlayer-fileList-scrollRail.jpg` | S1, video playback | PACT header, file list down the left, video window, a column of `x` marks and a scroll track down the right edge. |
| `lossOfSignal-pullOutKeyboard.jpg` | S1, IT terminal | Navy "LOSS OF SIGNAL" screen in cream caps; beige keycaps on the pull-out keyboard. |
| `legacy/legacyTablet-archiveCarousel-list.jpg` | S2, the Legacy tablet (Territory Studio) | Gold-on-black archive UI: book thumbnails in a spiral, gold list rows, thin gold rules, glow and bokeh. |
| `legacy/legacyTablet-cipherNodeGraph.jpg` | S2, the Legacy tablet (Territory Studio) | Numbered gold node graph, tiny mono labels, warm glow. |

## Sampled palette

Averaged from crops of the frames above (ImageMagick `-scale 1x1!` and
`-colors 8` histograms). Theme values are lifted for contrast and are noted.

| Role | Sampled | Theme token |
|---|---|---|
| CRT glass | `#011d15`, `#070d0e` | `--bg #010d0a`, `--surface #03160f` |
| Teal phosphor text/lines | `#0cae93`, `#28c6aa`, `#25c9af` | `--text #6fe8cc` (lifted: the screen blooms), `--border #1c8a72` |
| Dim lines | `#0a6950`, `#094c32` | `--hairline #0c3a2e` |
| Header / status plate | `#88cfcb`, `#83aba9`, `#3d8478` | `--silo-plate #8fd3cc` |
| Yellow-green "authorised" band, capacity bar | `#95c26f`, `#8cb868`, `#87bc75` | `--accent #b9dc78` |
| Pale-yellow rules / selection outline | `#9d9a62`, `#97a48a` (dim in camera) | `--accent-2 #e6dc8c` |
| Cream countdown block | `#b6c085` | (readout numerals use amber instead) |
| Amber VIEW key, body text | `#82622c` (dim) | `--warning #e5a93c`, `--silo-num #f0c060` |
| Field outline | `#477544`, `#3b604c` | `--silo-field #2f6b55` |
| Legacy gold | (read from the Territory frames, not sampled numerically) | `--accent #f2b84b` |

## Typography

- Hard drive / relic database / terminal log: an all-caps squared techno
  sans with rounded corners and open, square counters (C, G, O are
  rectangles). Not identified. Share Tech / Share Tech Mono (SIL OFL,
  vendored in `assets/fonts/`) have the same narrow squared caps and are
  used for UI and data.
- PACT and SiloMail: a DIN-like grotesque (Bahnschrift / DIN class),
  tracked caps. Named as a fallback in the stack only.
- Everything is uppercase with generous tracking; tiny labels sit above
  large values.

## Component mapping

| ftl-themes component | Reference | How it is mapped |
|---|---|---|
| App bar | PACT header | Dark glass between pale-yellow double rules; nav entries auto-numbered `01`, `02` via a CSS counter; the brand is a pale-teal plate like "RELIC DATABASE". |
| App shell | Monitor bezel | Whole `.app` is a rounded steel bezel with the bar, main and status on one CRT glass. |
| Rail | Video player / relic scroll track | Thin right-hand scroll track with a thumb block and tick marks. |
| Status strip | Relic database status plate | Pale-teal plate, dark tracked caps. |
| Buttons | CLEAR ALL / EDIT / SEARCH | Outlined, transparent, tracked caps. Primary = yellow-green fill with the SEARCH key's pale-yellow outer frame. |
| Inputs / select / textarea | Relic field cells, SEARCH field | Transparent, 1px olive-teal outline, mono caps, square. |
| Panels / panel header | "RELIC/SEIZED OBJECTS INVENTORY" | Thin teal box; title between 3px double rules, `x` at right. |
| Modal | SiloMail | Pale-teal header plate, heavy (3px) bright rounded frame, glow. |
| Tooltip | header plates | Pale-teal plate, dark text. |
| Tabs | PACT soft-key row | Outlined keys with a `>` cue; active = pale-yellow outline. |
| Selected row / list item / focus | File-card selection | Pale-yellow outline / marker; focus ring is the same yellow. |
| Progress / meter / bar chart | CAPACITY bar, LOADING blocks | Hatched yellow-green fill in a teal outline; meters segmented. |
| Readout | PACT HRS / MNS pills | Rounded outline pill, amber numerals, slight glow. |
| Kbd | Pull-out keyboard | Beige keycaps. |
| `legacy` variant | Territory's Legacy tablet (`references/silo/legacy/`) | Gold on warm black, cream plate, lighter metal bezel. |

## Honest gaps

- No frame shows a data table with column heads, a toast, a switch, a
  slider, a dropdown menu, a badge, an avatar or pagination. Those follow
  the field-cell and soft-key rules by extension.
- No error/danger state appears on any screen captured. `--danger` is a
  generic red-orange, my addition.
- The scanline overlay is a stylisation; the real frames show grain and
  bloom rather than visible scanlines.
- The designers of the Season 1 in-set screen graphics are not named in any
  source found; only Territory Studio (Season 2 tablet) has a project page.
