# Motorsport Telemetry: research notes

`motorsport-telemetry` is inspired by open-wheel racing's broadcast timing
graphics, the timing screens on a team's pit wall, and the display and rev
lights on a modern car's steering wheel and dash. It is deliberately generic
(PLAN.md §21): no series, team, tyre-maker or broadcaster names, logos or
marks ship in the theme, and its decorative timing tower uses no real driver
codes. The images below are © their photographers and the software authors
named; several show team liveries and the tyre-maker's sidewall lettering,
which is exactly why they stay here as comparison-only design references and
nothing from them is reproduced. Research was done on 2026-10-02 through the
Wikimedia Commons API, Openverse (Flickr) and GitHub; images were resized to
at most 1600px and re-encoded as WebP (quality 78-85), all under 400 KB.
Three sources are not openly licensed for reuse in the usual sense and are
filed under the fair-use reference-still allowance in PLAN.md §21: the AiM
dash photos and the MoTeC i2 screenshot are CC BY-NC-SA 2.0 (non-commercial),
and the five timing screens are screenshots from a GPL-3.0 project's docs.
No still of an actual broadcast timing tower could be found under any open
licence (see Gaps).

## Primary direction

The live-timing screen, as the sport's timing tower and pit-wall monitors
present it, is the primary source: a dense black table of positions, gaps
and sector times in tabular figures, where colour carries meaning and
nothing else does. Purple is the fastest sector or lap overall, green a
personal best, yellow slower; tyre compounds are read from a coloured ring
(soft red, medium yellow, hard white, intermediate green, wet blue). The
open-source `undercut-f1` terminal client is the cleanest available record
of that grammar. From the steering wheel and the dash logger the theme takes
the instruments: the rev-light strip (green, red, blue from left to right),
the rev counter, the gear and lap-time readouts, the coloured rotaries. From
the pit wall and the data-analysis software it takes the surfaces: carbon
fibre, banks of black screens, stacked telemetry traces.

## Images

| File | Source / credit | What it shows |
|---|---|---|
| `pitWallMonitors-timingScreen-panelGrid.webp` | [Commons file page](https://commons.wikimedia.org/wiki/File:Ferrari_Pitwall_Control_Centre_-_Mexican_Grand_Prix_22.JPG), [image](https://upload.wikimedia.org/wikipedia/commons/8/8a/Ferrari_Pitwall_Control_Centre_-_Mexican_Grand_Prix_22.JPG). ProtoplasmaKid, CC BY-SA 4.0. Team branding visible on screen; reference only. | A team's pit-wall stand: a grid of black-bezelled monitors over a row of control panels, timing and data pages in coloured blocks. The shell's "black screens in a carbon frame" and the panel grid. 7/10 |
| `steeringWheel-revLights-display-rotaryDial.webp` | [Commons](https://commons.wikimedia.org/wiki/File:Alpine_F1_steering_wheel.jpg), [image](https://upload.wikimedia.org/wikipedia/commons/3/3a/Alpine_F1_steering_wheel.jpg). Declan M Martin, public domain. Maker's emblem visible; reference only. | A current steering wheel: the LED rev-light row over the display, carbon faceplate, colour-coded buttons and rotary dials with coloured scales. Source for the rev-light strip, the knob, keys and the carbon. 9/10 |
| `steeringWheel-revLights-display-buttonColors.webp` | [Commons](https://commons.wikimedia.org/wiki/File:Formel_1_Lenkrad.jpg), [image](https://upload.wikimedia.org/wikipedia/commons/1/1a/Formel_1_Lenkrad.jpg). Speed-magazin.de, CC BY-SA 4.0. | Another wheel, studio-lit: 15-LED rev strip, black display, purple/teal/yellow rotaries, coloured round keys on carbon. Button colours and the key shape. 8/10 |
| `dashDisplay-revArc-shiftLights-gearReadout.webp` | [Flickr](https://www.flickr.com/photos/40182362@N02/8422479829), [image](https://live.staticflickr.com/8185/8422479829_50f070f3b6_b.jpg). memotec Messtechnik, CC BY-NC-SA 2.0 (fair-use reference). Maker's mark visible. | A dash logger with a red backlight: segmented rev arc, shift-light LEDs round the rim, big gear digit, lap time, tabular figures. Source for the gauge as a rev counter and for readouts. 8/10 |
| `dashDisplay-revArc-lapTime-trackMap.webp` | [Flickr](https://www.flickr.com/photos/40182362@N02/8423574974), [image](https://live.staticflickr.com/8238/8423574974_6812ec62b9_b.jpg). memotec Messtechnik, CC BY-NC-SA 2.0 (fair-use reference). | The same dash in its grey mode with a track map, rolling lap time and best lap. Readout hierarchy: one huge value, small labelled ones around it. 7/10 |
| `telemetryTrace-lineChart-channelList.webp` | [Flickr](https://www.flickr.com/photos/99496537@N00/300533607), [image](https://live.staticflickr.com/100/300533607_24dba1ddc9_b.jpg). chrisdigo, CC BY-NC-SA 2.0 (fair-use reference); a screenshot of MoTeC i2 data-analysis software. | Stacked telemetry channels (engine speed, ground speed, throttle, g-forces) as thin coloured traces on a shared distance axis, with a lap strip and track map. Source for the chart tokens and the XL gutter art. 8/10 |
| `timingTower-sectorColors-tyreChip.webp` | [undercut-f1](https://github.com/JustAman62/undercut-f1), `docs/screenshots/race-timing-screen.png` on `master`, [image](https://raw.githubusercontent.com/JustAman62/undercut-f1/master/docs/screenshots/race-timing-screen.png). © JustAman62, GPL-3.0. Real driver codes visible; reference only. | A race timing screen: position, gap, interval, last/best lap, sectors in purple and green, tyre compound letters on red/yellow/white chips, positions gained and lost. The timing-table grammar. 9/10 |
| `timingTable-sectorColors-bestLap.webp` | undercut-f1, `docs/screenshots/quali-timing-screen.png`, [image](https://raw.githubusercontent.com/JustAman62/undercut-f1/master/docs/screenshots/quali-timing-screen.png). GPL-3.0. | Qualifying: purple, green and yellow sector cells side by side, deltas in italic grey, the knockout line. Sector colours as fills. 8/10 |
| `tyreStint-barChart-tyreChip.webp` | undercut-f1, `docs/screenshots/tyre-stint-screen.png`, [image](https://raw.githubusercontent.com/JustAman62/undercut-f1/master/docs/screenshots/tyre-stint-screen.png). GPL-3.0. | Tyre stints as horizontal bars in compound colours, medium yellow and hard grey-white chips labelled MEDIUM/HARD. Compound colours as data. 7/10 |
| `lineChart-gapTrace-timingTable.webp` | undercut-f1, `docs/screenshots/timing-history-screen.png`, [image](https://raw.githubusercontent.com/JustAman62/undercut-f1/master/docs/screenshots/timing-history-screen.png). GPL-3.0. | Gap-to-leader and lap-time line charts in thin multi-coloured traces on black beside a timing table. Chart density and line weight. 7/10 |
| `deltaBar-timingTower-statusBox.webp` | undercut-f1, `docs/screenshots/compare-drivers.png`, [image](https://raw.githubusercontent.com/JustAman62/undercut-f1/master/docs/screenshots/compare-drivers.png). GPL-3.0. | Lap-by-lap comparison as green/red delta bars with the values at the bar ends; a track-status box ("AllClear") in green. Source for progress/delta bars and the green status rule. 7/10 |
| `tyreCompound-medium-sidewall.webp` | [Commons](https://commons.wikimedia.org/wiki/File:Pirelli_P_Zero_Formula_1_Medium_Slick_Tyre_2026.jpg), [image](https://upload.wikimedia.org/wikipedia/commons/6/62/Pirelli_P_Zero_Formula_1_Medium_Slick_Tyre_2026.jpg). TaurusEmerald, CC BY-SA 4.0. Tyre-maker's lettering visible; reference only. | A real medium slick: the yellow compound band on a black sidewall. The chip is "dark disc, coloured ring". 7/10 |
| `tyreChip-soft-hard.webp` | [Commons red](https://commons.wikimedia.org/wiki/File:F1_tire_Pirelli_PZero_Red_2019.png) and [white](https://commons.wikimedia.org/wiki/File:F1_tire_Pirelli_PZero_White_2019.png), images [red](https://upload.wikimedia.org/wikipedia/commons/3/35/F1_tire_Pirelli_PZero_Red_2019.png) / [white](https://upload.wikimedia.org/wikipedia/commons/0/01/F1_tire_Pirelli_PZero_White_2019.png). MetalDylan, CC BY-SA 4.0; joined side by side. | Flat icons of the soft and hard compounds, as timing graphics draw them. 6/10 |
| `carbonFibre-panel-appBar.webp` | [Commons](https://commons.wikimedia.org/wiki/File:Woven_carbon_fiber_fabric.jpg), [image](https://upload.wikimedia.org/wikipedia/commons/2/2a/Woven_carbon_fiber_fabric.jpg). Acheolg, CC BY-SA 4.0. | Woven carbon fabric under raking light: near-black, blue-grey highlights, a tight diagonal step. Source for `--mt-twill`. 7/10 |

Considered and dropped (under 5, or covered): other pit-wall stands from the
same Mexican GP set (no screens visible), museum steering wheels without
displays, carbon spools and tubes, a live-timing TV set-up shot too small to
read, and a photo of a projected broadcast standings graphic
([Flickr, Ben Sutherland, CC BY 2.0](https://www.flickr.com/photos/60179301@N00/48963026)),
too blurred to sample.

## Sampled palette

Sampled with ImageMagick quantisation (`convert … -colors 16 -format %c
histogram:info:-`) on the full-size originals.

| Role | Sampled | Theme token | Note |
|---|---|---|---|
| Timing-screen black | `#000000`, row stripe `#141615` | `--bg #07080a`, `--surface #111317` | Lifted a step so carbon, panels and rows can stack. |
| Purple sector | `#760076` (fill), `#654866` (dimmed) | `--accent #8b3ff0`, `--accent-text #c18cff` | Broadcast purple is bluer and brighter than the terminal's ANSI magenta; white on it reaches 5.2:1. |
| Green sector | `#04ac04`, `#007600` | `--success`/`--accent-2 #1fcf6b` | Brighter so it reads as text (9.0:1 on surface). |
| Yellow sector / medium | `#fefc7e`, tyre band `#d0cb54` | `--warning #ffd60a` | Saturated broadcast yellow; 13:1 as text. |
| Soft compound red | dash backlight `#fb072a`, `#e52845` | `--danger #e8002d`, `--danger-text #ff4d5e` | Fill keeps the hue; text uses a lighter red for 5.7:1. |
| Hard compound | `#fefefe` / `#c8c9c8` | `--mt-hard #eceae4` | Default badge ring. |
| Wet / shift-light blue | `#4e9ac2`, `#4fc7d3` | `--flare`/`--mt-wet #2fa8ff` | The last five rev lights. |
| Carbon | `#22221f`, `#3c4045`, `#555c62` | `--mt-twill` at 2-35% alpha over `#0f1114`-`#15181c` | Kept within a few percent so the weave never sits behind text as a pattern. |
| Grey text | `#a5aaa2` | `--muted #9ba3ae` | 7.3:1 on surface, 6.8:1 on surface-2. |

Chart series (`--chart-series-1..6`: `#9a5cf5`, `#df4a4a`, `#2b93d9`,
`#169e74`, `#b98a00`, `#c95fb0`) are the telemetry trace hues stepped into
the dark-mode band and ordered so that red never sits beside green; they
pass the dataviz `validate_palette.js` checks (lightness band, chroma,
adjacent CVD and normal-vision separation, contrast) against `--surface`.

## Typography

Broadcast timing graphics use a proprietary bold, slightly extended sans;
dash loggers use LCD segment figures; the timing software uses a monospace.
The theme vendors **Titillium Web** (OFL 1.1, Accademia di Belle Arti di
Urbino; Regular, Bold and Bold Italic, Latin subset, 36.6 KiB in total) as
the one UI and timing face: it is a squared, technical sans in the same
family of shapes, and its figures are tabular by default (every digit is 560
units), so lap times and gaps line up without relying on `font-feature`
support. Headings and panel titles are bold italic caps, the way the
graphics set driver names and session titles; `font-variant-numeric:
tabular-nums` is set on the root as a second guarantee. Code stays in the
system monospace. The proprietary face is not named anywhere.

## Component mapping

| Component | Reference | Treatment |
|---|---|---|
| Page / `.app` | `pitWallMonitors-…`, `carbonFibre-…` | Near-black carbon twill backdrop. |
| App bar | `steeringWheel-revLights-…` | Carbon strip, bold italic brand, purple underline on the active item, a 15-LED rev-light strip (green, red, blue; 11 lit) along its lower edge. |
| Rail | `timingTower-sectorColors-tyreChip` | A painted, abstract timing tower: "LAP 34/57", positions 1-20 (leader boxed in white), neutral stripes, interval bars (one purple), tyre rings. No names. Hidden on phone and tablet. |
| Status strip | `deltaBar-timingTower-statusBox` | Race-control strip on a 2px green "track clear" rule, tracked caps. |
| Panels, cards | `pitWallMonitors-…`, `carbonFibre-…` | Carbon with a faint top sheen; header strip with a slanted purple tab at the left; bold italic caps. |
| Nested surfaces | — | Flat `--surface-2`, hairline, no weave, tab, sheen or shadow. |
| Buttons | `steeringWheel-…-buttonColors` | Dark keys, bold tracked caps; primary purple, danger soft-red, success green. |
| Tables | `timingTower-…`, `timingTable-…` | Black head with a 2px purple rule, tight rows, faint zebra, tabular right-aligned numbers, selected row purple with a 4px purple bar. |
| Tabs, nav | `timingTable-…` | Caps, 3px purple underline. |
| Inputs | — | Recessed black field, hairline border, purple caret and focus. |
| Badges | `tyreCompound-…`, `tyreChip-…`, `tyreStint-…` | Tyre chips: dark disc, 2px coloured ring. Default hard white, warning medium yellow, danger soft red, success intermediate green, accent purple. |
| Modal and close | `steeringWheel-…` | Carbon with a 3px purple top edge; close is a square black key with a cross that lights soft red. |
| Gauge dial / arc | `dashDisplay-revArc-…` | Rev counter: carbon face, white ticks, green working band (yellow warn, red error), red redline, red needle. |
| Readouts, stats, countdown | `dashDisplay-…-gearReadout` | Black window, white bold tabular figures, muted units. |
| Meters | `steeringWheel-revLights-…` | Rev-light order: green, yellow, red, blue peak. |
| Progress, sliders | `deltaBar-…` | Thin hard-edged bars, purple fill; slider thumb a white fader cap. |
| Switch | — | Off black, on green (a system "enabled"), square thumb. |
| Charts, sparklines, heatmap | `telemetryTrace-…`, `lineChart-gapTrace-…` | Thin 2px traces on black, recessive grid, validated six-series order led by purple. |
| Timeline, steps | `timingTable-…` | Done green, current purple. |
| Mixer (knobs, keys, scribble strips) | `steeringWheel-…-rotaryDial` | Rotaries with a purple arc, keys that light purple/red/yellow/green, black scribble strips. |
| Tooltip | broadcast lower thirds | White caption box, black text. |
| XL gutters | `telemetryTrace-…` | Stacked speed/throttle/brake channel traces and dashed sector splits, about 1.2:1 over `--bg`. |

## Gaps

- **Broadcast timing tower stills.** No openly licensed capture of the
  actual on-screen tower (team-colour bars, boxed positions, the purple
  fastest-lap marker) was found; the terminal client is the proxy. The
  rail's abstract tower is drawn from memory of the broadcast layout plus
  that proxy.
- **Pit-wall screen content.** The pit-wall photo shows the monitors but not
  legibly what is on them; layout density comes from the data-analysis
  screenshot instead.
- **A lit shift-light strip.** Every wheel photo shows the LEDs off; the
  green-red-blue order is the documented convention, the lit/unlit balance
  is a design choice.
- **Live-data states** (PLAN.md §18: `.is-updated`, `.is-stale`,
  `.connection`) are not in core yet, so the theme can't style them; the
  sector colours are ready for them.
