# Theme references

Where to look at the real thing each theme is modelled on. Use these when
reviewing a theme in [`components.html`](../components.html): open the
reference next to the render and compare.

Themes with no local images captured yet (`aperture`, `cue-lab`, `material`,
`nerv`, `pipboy`, `tron`) ship anyway (restored in v4); their
fidelity is not yet scored against source imagery — see
[`branding-guide.md`](../docs/branding-guide.md).

## Folder layout

Every image lives in the folder of the theme it backs: `references/<theme>/`.
Images that back one palette variant only go one level down, in a folder
named for the variant id from `dist/themes.json`
(`references/<theme>/<variant>/`). Each theme folder has a `RESEARCH.md`
describing its files. Today's variant folders:

- `lcars/voyager/` (DS9 panels), `lcars/picard/`. `lcars/tng/` and
  `lcars/tng-films/` split the default look by source gallery, and
  `lcars/INDEX.md` scores every LCARS image.
- `weyland-yutani/mother/`, `weyland-yutani/emergency/`, `weyland-yutani/earth/`
- `winxp-luna/royale/`, `winxp-luna/royale-noir/`, `winxp-luna/zune/`, `winxp-luna/embedded/`
- `prometheus/suit/`

Non-variant subfolders hold asset sets rather than screenshots (each
described in that theme's `RESEARCH.md`): `alienware/icon-packs/`,
`winxp-luna/icons-original/`, `winxp-luna/icons-modern/`,
`winxp-luna/wallpapers/` and `win7-aero/start-orbs/`. Icon packs keep their
`.ico`/`.png`/`.bmp` files; packed resource binaries (7tsp `.res`) are not
kept, since nobody can open them to compare.

Four folders back no theme yet. They are the non-LCARS Star Trek interface
languages from lcars.org.uk, kept for a future theme, each with its own
`INDEX.md`: `star-trek-alien/` (Klingon, Romulan, Cardassian, Ferengi,
Bajoran and others), `star-trek-enterprise/` (NX-01), `star-trek-tos/` (TOS
and TOS films) and `star-trek-kelvin/` (Star Trek 2009 and Into Darkness).

| Theme | Reference | What to compare |
|---|---|---|
| `alienware` | [Alienware Command Center — AlienFX](https://www.dell.com/support/manuals/en-us/alienware-command-center/awcc_ug_6.x/alienfx?guid=guid-1938310a-dcbb-4751-9131-ddd2d9400d4a&lang=en-us) | Matte black chrome, one AlienFX accent colour per lighting zone |
| `aperture` | [Portal (video game)](https://en.wikipedia.org/wiki/Portal_(video_game)), [Aperture Science — Portal Wiki](https://theportalwiki.com/wiki/Aperture_Science) | Off-white test-chamber panels; blue and orange as the only saturated colours |
| `aqua` | [Aqua (user interface)](https://en.wikipedia.org/wiki/Aqua_(user_interface)) | Gel buttons, pinstripes, the pulsing default button |
| `barbie` | [Shades of pink — Barbie pink (Pantone 219C)](https://en.wikipedia.org/wiki/Shades_of_pink) | The brand pink, and how close hot pink can sit to white text |
| `bloomberg` | [Bloomberg Terminal](https://en.wikipedia.org/wiki/Bloomberg_Terminal), [An evolving icon](https://www.bloomberg.com/professional/blog/the-bloomberg-terminal-an-evolving-icon) | Amber-on-black data density, function-key mnemonics, `<GO>` |
| `blue-future` | [Apollo Mission Control Center restoration (NASA)](https://www.nasa.gov/johnson/history/apollo-mcc-restoration/) | Real telemetry consoles: precise, uncluttered, instrument-first |
| `cassette-futurism` | [Commodore PET](https://en.wikipedia.org/wiki/Commodore_PET), [Roland TR-808](https://en.wikipedia.org/wiki/Roland_TR-808), [Vacuum fluorescent display](https://en.wikipedia.org/wiki/Vacuum_fluorescent_display), [Dymo label tape](https://en.wikipedia.org/wiki/Dymo_Corporation) | Keycap colours and sculpt vs the 808/HP-35; readout digits vs the VFD/LED photos; `.switch` vs the bat-handle toggles; beige housing vs the PET; badges vs Dymo tape |
| `cue-lab` | [QLab](https://en.wikipedia.org/wiki/QLab), [QLab 5 docs — Cues](https://qlab.app/docs/v5/fundamentals/cues/) | Cue-list columns, the standing-by playhead, one loud GO |
| `cyber-goth` | [Cybergoth](https://en.wikipedia.org/wiki/Cybergoth) | Black PVC/vinyl with a single UV-reactive neon |
| `cyberpunk-2077` | [RESEARCH.md](cyberpunk-2077/RESEARCH.md), [Interface In Game — Cyberpunk 2077](https://interfaceingame.com/games/cyberpunk-2077/) | Red ink vs the menu labels and rules; cyan active tab and values; cut corners and the save-confirm buttons; breach grid vs the CODE MATRIX; health bar glow and angled end vs the HUD crop; OFF/ON blocks and slider thumb vs settings |
| `death-star` | [DS-1 Orbital Battle Station — Wookieepedia](https://starwars.fandom.com/wiki/DS-1_Orbital_Battle_Station/Legends) | Black panels, no borders, sparse blue/white indicators |
| `hot-wheels` | [Hot Wheels orange track (Mattel)](https://corporate.mattel.com/news/hot-wheels-takes-iconic-orange-track-to-the-next-level-with-new-snap-feature-its-most-significant-innovation-in-50-years), [Hot Wheels logo history](https://logos.fandom.com/wiki/Hot_Wheels) | Track orange, flame logo, chequered-flag finish |
| `imac-g3` | [iMac G3](https://en.wikipedia.org/wiki/IMac_G3) | Translucent Bondi Blue, and the fruit colourways behind the palette variants |
| `ios-flat` | [RESEARCH.md](ios-flat/RESEARCH.md), [Apple HIG (iOS 13–17, archived)](https://web.archive.org/web/2020/https://developer.apple.com/design/human-interface-guidelines/ios/) | Section headers above white rounded groups on #f2f2f7; inset hairlines; green switch; grey segmented track with white pill; centred alert with hairline-divided buttons; frosted bars over content |
| `ios-skeuomorphic` | [iOS 6](https://en.wikipedia.org/wiki/IOS_6), [iOS 6 Revisited (screenshots)](https://www.martinnobel.com/techresearch/ios-6-screenshots) | Nav bar gloss and title emboss, the pinstripe behind rounded cells, ON/OFF switch, tab bar glow, alert view navy, Notification Center linen |
| `lcars` | [LCARS](https://en.wikipedia.org/wiki/LCARS), [Memory Alpha — LCARS](https://memory-alpha.fandom.com/wiki/Library_Computer_Access_and_Retrieval_System) | Elbow sweeps, pill buttons, black text on candy colours |
| `lego-classic` | [LEGO Space history (LEGO.com)](https://www.lego.com/en-us/history/articles/f-lego-space), [Classic Space — Brickipedia](https://brickipedia.fandom.com/wiki/Classic_Space) | Primary brick colours, instruction-booklet layout |
| `liquid-glass` | [Apple — Liquid Glass (Newsroom, WWDC25)](https://www.apple.com/newsroom/2025/06/apple-introduces-a-delightful-and-elegant-new-software-design/), [RESEARCH.md](liquid-glass/RESEARCH.md) | Floating capsule tab bar with a grey highlight under the selected item; inset rounded sidebar with traffic lights; capsule switches and sliders; glass menus; rim highlights on controls but not on content cards |
| `material` | [Material Design](https://en.wikipedia.org/wiki/Material_Design), [Material 2 introduction](https://m2.material.io/design/introduction/) | Elevation, the primary app bar, chips, snackbars |
| `matrix` | [Digital rain](https://en.wikipedia.org/wiki/Digital_rain), [Commons: Matrix digital rain](https://commons.wikimedia.org/wiki/Category:Matrix_digital_rain) | Phosphor green on black, monospace, the operator console |
| `motorsport-telemetry` | [Commons: steering wheel with rev lights](https://commons.wikimedia.org/wiki/File:Alpine_F1_steering_wheel.jpg), [Commons: pit-wall stand](https://commons.wikimedia.org/wiki/File:Ferrari_Pitwall_Control_Centre_-_Mexican_Grand_Prix_22.JPG), [undercut-f1 timing screenshots](https://github.com/JustAman62/undercut-f1/tree/master/docs/screenshots), [AiM dash logger](https://www.flickr.com/photos/40182362@N02/8422479829) | Purple/green/yellow sector use, compound ring colours, rev-light order green→red→blue, carbon weave strength, tabular figures |
| `msdos` | [Norton Commander](https://en.wikipedia.org/wiki/Norton_Commander), [UI Museum: Norton Commander 5.0](https://ilyabirman.net/meanwhile/all/ui-museum-norton-commander-5-0/) | Two blue panels, double-line borders, cyan cursor bar, F-key bar |
| `nerv` | [Neon Genesis Evangelion — Fonts In Use](https://fontsinuse.com/uses/28760/neon-genesis-evangelion), [Neon Genesis Evangelion](https://en.wikipedia.org/wiki/Neon_Genesis_Evangelion) | Heavy serif titling with Helvetica, orange-on-black warnings, the MAGI vote |
| `pipboy` | [Pip-Boy](https://en.wikipedia.org/wiki/Pip-Boy), [Fallout Wiki — Pip-Boy](https://fallout.fandom.com/wiki/Pip-Boy) | Monochrome green phosphor, STAT/INV/DATA tabs, scanlines |
| `proseries` | [RESEARCH.md](proseries/RESEARCH.md) (owner-supplied captures) | Strip blue and dividers vs `.strip`; key colours (mute, solo, SIS, ST, MON); dynamics thumbnails; the rack faceplates and blue assignable-controls panel; patch tiles |
| `silo` | [HUDS+GUIS — Silo Dystopian UI](https://www.hudsandguis.com/home/2025/silo-ui), [Territory Studio — Silo](https://territorystudio.com/project/silo/) | Teal-on-glass boxed field cells with tiny labels, pale-teal header/status plates, yellow-outline selection, yellow-green "authorised" band; `legacy/` for the gold S2 tablet |
| `skyrim` | [UESP Skyrim menu images](https://en.uesp.net/wiki/Category:Skyrim-Menu_Images), [SkyUI - Features Overview (Steam guide)](https://steamcommunity.com/sharedfiles/filedetails/?id=426512192), [SkyUI repo](https://github.com/schlangster/skyui) | Condensed white type, SkyUI column heads and selected-row band, chevron title bar, diamond-capped health/magicka/stamina bars, MCM diamond toggles |
| `steampunk` | [Steampunk](https://en.wikipedia.org/wiki/Steampunk) | Brass, mahogany and copper; gauges rather than numbers |
| `teenage-engineering` | [RESEARCH.md](teenage-engineering/RESEARCH.md), [Commons: OP-1 top view](https://commons.wikimedia.org/wiki/File:OP-1,_portable_synthesizer_and_sequencer_-_Jun_21,_2011.jpg), [OP-1 at SMEM](https://commons.wikimedia.org/wiki/File:Teenage_Engineering_OP-1_Synthesizer_at_SMEM_Playroom.jpg), [OP-Z](https://commons.wikimedia.org/wiki/File:OP-Z_in_da_house_(32659021107).jpg) | Encoder cap colours and slot vs the knobs; key radius and frame gaps vs panels and buttons; display glass, thin white/teal glyphs vs readouts, meters and charts; grille-and-encoder rail |
| `tokie` | [Commons: black leather](https://commons.wikimedia.org/wiki/File:Black_Leather.jpg), [gold-embossed briefcase](https://commons.wikimedia.org/wiki/File:Briefcase_of_a_bank_director_of_Midland_Bank_Ltd._made_of_black_cowhide_leather_around_1925_-_Font_in_gold_letter_embossing_-_Picture_001.jpg), [brushed brass](https://commons.wikimedia.org/wiki/File:Brushed_brass_paint_(Apollo_11)_interior.png), [gilt binding](https://commons.wikimedia.org/wiki/File:Gruel_and_Engelmann_-_Binding_for_a_Book_of_Hours_-_Walters_572167_-_Front_Closed.jpg) | Grain fineness, stitch-in-groove spacing, foil-struck tracked serif caps, satin brushed vs mirror polished gold |
| `tron` | [TRON: Legacy — GMUNK](https://gmunk.com/TRON-Legacy), [TRON Legacy UI — HUDS+GUIS](https://www.hudsandguis.com/home/2011/04/19/tron-legacy-ui) | Cyan line work on black, cut corners, the orange villain accent |
| `vaporwave` | [Vaporwave](https://en.wikipedia.org/wiki/Vaporwave), [Aesthetics Wiki — Vaporwave](https://aesthetics.fandom.com/wiki/Vaporwave) | Pink/cyan gradients, mall nostalgia, full-width type |
| `westworld` | [Behind the scenes of the Westworld UI (DESK, Chris Kieffer interview)](https://vanschneider.com/blog/behind-the-scenes-of-the-westworld-ui/), [Westworld wiki: Tablet](https://westworld.fandom.com/wiki/Tablet) | Slate e-paper with cyan line-work, the attribute matrix's segmented sliders and [bracketed] labels, chip tabs, and the DELOS pill |
| `win7-aero` | [Windows Aero](https://en.wikipedia.org/wiki/Windows_Aero) | Blurred glass frames over the desktop, the glass taskbar |
| `winamp-classic` | [Winamp](https://en.wikipedia.org/wiki/Winamp), [Creating Classic Skins](http://wiki.winamp.com/wiki/Creating_Classic_Skins) | Green LCD readout, bevelled grey buttons, EQ sliders, playlist |
| `windows95` | [Windows 95](https://en.wikipedia.org/wiki/Windows_95), [Commons: Windows 95 screenshots](https://commons.wikimedia.org/wiki/Category:Windows_95_screenshots) | Grey bevels, navy title bar, teal desktop, dotted focus |
| `winxp-luna` | [Windows XP visual styles](https://en.wikipedia.org/wiki/Windows_XP_visual_styles) | Glossy blue title bar, tan content, green Start button |
| `wmp11` | [Windows Media Player](https://en.wikipedia.org/wiki/Windows_Media_Player) | Dark glossy chrome, library breadcrumbs, the round play button |

## Capture targets, by theme

Three images each; see "Local images" above for why they're not here yet.

<details>
<summary><code>alienware</code></summary>

- **`01-alienfx-zones.png`** — AlienFX lighting-zone editor: the per-zone color picker grid (Alien head, keyboard, power button, rails) _(search: Dell AlienFX / Alienware Command Center lighting zones screenshot)_
- **`02-chassis-angles.jpg`** — The matte-black chassis itself: angular vents and cut edges, not the software _(search: Alienware Aurora or laptop chassis product photo, angular vents)_
- **`03-command-center-overview.png`** — Alienware Command Center's full dashboard (FX / Performance tabs) for general chrome/layout _(search: Alienware Command Center dashboard screenshot)_

</details>

<details>
<summary><code>aperture</code></summary>

- **`01-test-chamber.jpg`** — An Aperture Science test chamber: off-white panels, the blue/orange portal pair visible _(search: Portal test chamber screenshot off-white orange blue)_
- **`02-signage.jpg`** — Aperture Science wall signage/stencil typography (the Univers-style lettering) _(search: Aperture Science signage Portal wiki)_
- **`03-glados-panel.jpg`** — A GLaDOS control panel or turret/personality-core interface screen _(search: Portal GLaDOS control panel screenshot)_

</details>

<details>
<summary><code>aqua</code></summary>

- **`01-window-chrome.png`** — A Mac OS X Snow Leopard window: brushed-metal titlebar, pinstripe, traffic-light buttons _(search: Mac OS X Snow Leopard window screenshot brushed metal)_
- **`02-gel-buttons.png`** — Aqua's gel/candy buttons close up, including the pulsing blue default button _(search: Aqua interface gel button pulsing default screenshot)_
- **`03-dock.png`** — The Aqua Dock with reflection, for the gloss/reflection language _(search: Mac OS X Aqua dock screenshot reflection)_

</details>

<details>
<summary><code>barbie</code></summary>

- **`01-dreamhouse-box.jpg`** — Barbie Dreamhouse packaging detail (pink/gold surfaces only, no doll in frame) — the exact brand pink, gold accents _(search: Barbie Dreamhouse box packaging detail)_
- **`02-logo.png`** — The Barbie wordmark/logo (rounded, hot pink, gold sparkle treatment) _(search: Barbie logo pink gold)_
- **`03-app-ui.jpg`** — An official Barbie app or website UI screen with no characters in frame, for pill-chrome/rounded-button reference _(search: Barbie official app screenshot UI)_ — note: app-store captures were rejected (all show Barbie characters); wordmark lockups currently stand in.

</details>

<details>
<summary><code>bloomberg</code></summary>

- **`01-terminal-screen.jpg`** — A real Bloomberg Terminal screen: amber/black data density, function-key row _(search: Bloomberg Terminal screen photo amber black)_
- **`02-keyboard.jpg`** — The Bloomberg keyboard with its colored function keys (GO, HELP, MENU) _(search: Bloomberg terminal keyboard colored keys photo)_
- **`03-multi-monitor.jpg`** — A trader's multi-monitor Bloomberg desk setup, for density/layout reference _(search: Bloomberg terminal trading desk multi monitor photo)_

</details>

<details>
<summary><code>blue-future</code></summary>

- **`01-apollo-console.jpg`** — An Apollo-era Mission Control console: pale-green metal, analog dials, physical switches _(search: NASA Apollo Mission Control restored console photo)_
- **`02-apollo-room-wide.jpg`** — Wide shot of the restored Mission Control room for layout/density reference _(search: NASA Apollo Mission Control Center restoration wide shot)_
- **`03-crt-readout.jpg`** — A period CRT readout/oscilloscope display, for the monospace-readout-glow language _(search: vintage CRT telemetry readout monochrome photo)_

</details>

<details>
<summary><code>cue-lab</code></summary>

- **`01-cue-list.png`** — QLab's cue list: colored cue-type rows, the standing-by playhead triangle _(search: QLab 5 cue list screenshot playhead)_
- **`02-go-button.png`** — QLab's GO button and transport controls close up _(search: QLab GO button screenshot)_
- **`03-workspace-overview.png`** — A full QLab workspace (sidebar + cue list + inspector) for chrome/density reference _(search: QLab workspace overview screenshot)_

</details>

<details>
<summary><code>cyber-goth</code></summary>

- **`01-el-wire.jpg`** — An electroluminescent-wire close-up on black: the single UV-reactive neon, its glow halo and wire weight _(search: EL wire close up black background)_
- **`02-vinyl-texture.jpg`** — A black vinyl/PVC macro: the base-material grain and specular response _(search: black vinyl leather texture macro)_
- **`03-neon-type.jpg`** — Neon-tube signage lettering on a dark wall: tube construction, mounts and glow on matte ground _(search: neon sign typography dark)_

> Policy: no people in any form (cybergoth is NOT cyberpunk — no game UI; no outfits, clubs, or accessories worn by people).

</details>

<details>
<summary><code>death-star</code></summary>

- **`01-control-room.jpg`** — A Death Star control-room set/still: black panels, sparse blue/white indicator lights _(search: Death Star control room Star Wars still)_
- **`02-targeting-computer.jpg`** — The Death Star superlaser targeting console _(search: Death Star targeting computer screen Star Wars)_
- **`03-imperial-console-detail.jpg`** — A close-up Imperial console panel for the indicator-block scale/spacing _(search: Imperial console Star Wars close up indicator lights)_

</details>

<details>
<summary><code>hot-wheels</code></summary>

- **`01-track-orange.jpg`** — The orange Hot Wheels track itself, close up _(search: Hot Wheels orange track photo)_
- **`02-blister-pack.jpg`** — A Hot Wheels blister-pack card, for the flame logo and card typography _(search: Hot Wheels blister pack card photo)_
- **`03-flame-logo.png`** — The Hot Wheels flame logo on its own _(search: Hot Wheels logo flame)_

</details>

<details>
<summary><code>imac-g3</code></summary>

- **`01-bondi-blue-unit.jpg`** — An original Bondi Blue iMac G3, full unit, for the translucent shell color _(search: iMac G3 Bondi Blue photo)_
- **`02-fruit-colorways.jpg`** — The multicolor iMac G3 lineup (Blueberry/Grape/Tangerine/Lime/Strawberry) together _(search: iMac G3 five flavors colorways photo)_
- **`03-setup-assistant.png`** — The Mac OS 8/9 Setup Assistant screen the unit shipped with _(search: Mac OS 9 Setup Assistant screenshot)_

</details>

<details>
<summary><code>lcars</code></summary>

- **`01-tng-bridge-panel.jpg`** — A TNG/DS9-era LCARS console: pill blocks and the elbow-curve rail _(search: LCARS Star Trek TNG console screenshot)_
- **`02-elbow-sweep.jpg`** — A close-up LCARS elbow/sweep corner for the curve geometry _(search: LCARS elbow sweep close up)_
- **`03-full-screen.jpg`** — A full LCARS display screen for the overall color-block density _(search: LCARS display screen Star Trek full)_

</details>

<details>
<summary><code>lego-classic</code></summary>

- **`01-classic-space-set.jpg`** — A Classic Space LEGO set box or built model, for the primary palette _(search: LEGO Classic Space set photo)_
- **`02-brick-studs-macro.jpg`** — A macro shot of brick studs on top of a brick, for the stud texture _(search: LEGO brick studs macro photo)_
- **`03-instruction-booklet.jpg`** — A LEGO instruction-booklet page, for the step/parts-list layout language _(search: LEGO instruction booklet page photo)_

</details>

<details>
<summary><code>material</code></summary>

- **`01-app-bar-elevation.png`** — A Material Design app with a colored app bar and elevation shadow on a card _(search: Material Design app bar elevation card screenshot)_
- **`02-fab-and-snackbar.png`** — A floating action button plus a snackbar, both signature Material components _(search: Material Design FAB snackbar screenshot)_
- **`03-color-system.png`** — Google's own Material color/elevation system diagram _(search: Material Design elevation color system diagram m2.material.io)_

</details>

<details>
<summary><code>matrix</code></summary>

- **`01-digital-rain.jpg`** — The Matrix digital-rain effect itself: green glyphs cascading on black _(search: Matrix digital rain screenshot green)_
- **`02-operator-console.jpg`** — An Operator's monitor wall from the films, monitors only with no actors in frame _(search: Matrix Nebuchadnezzar core monitors green terminal)_ — note: the actor-at-console still was removed under the no-people rule.
- **`03-code-closeup.jpg`** — A close crop of the falling code for the phosphor-glow color reference _(search: Matrix code close up green phosphor)_

</details>

<details>
<summary><code>msdos</code></summary>

- **`01-norton-commander.png`** — Norton Commander's two-panel blue file view, double-line borders _(search: Norton Commander 5.0 screenshot two panel)_
- **`02-fkey-bar.png`** — The F-key bar at the bottom (F1 Help, F2 Menu, ...) close up _(search: Norton Commander function key bar screenshot)_
- **`03-dialog-box.png`** — A Norton Commander dialog/confirmation box for the double-line window chrome _(search: Norton Commander dialog box screenshot)_

</details>

<details>
<summary><code>nerv</code></summary>

- **`01-magi-vote.jpg`** — The MAGI system's three-way vote screen (Melchior/Balthasar/Casper) _(search: Evangelion MAGI system screenshot vote)_
- **`02-nerv-logo-titling.jpg`** — NERV's logo and the show's title-card typography (heavy serif + Helvetica) _(search: Evangelion NERV logo title card typography)_
- **`03-eva-sync-panel.jpg`** — An Evangelion sync-ratio / pilot status panel _(search: Evangelion sync ratio panel screenshot orange)_

</details>

<details>
<summary><code>pipboy</code></summary>

- **`01-pipboy-inventory.jpg`** — The Pip-Boy 3000's inventory/STAT screen, green phosphor with scanlines _(search: Fallout Pip-Boy 3000 inventory screen screenshot)_
- **`02-pipboy-physical.jpg`** — The physical wrist-mounted Pip-Boy prop/model _(search: Pip-Boy 3000 physical prop replica photo)_
- **`03-special-screen.jpg`** — The S.P.E.C.I.A.L. attributes screen _(search: Fallout Pip-Boy SPECIAL screen screenshot)_

</details>

<details>
<summary><code>steampunk</code></summary>

- **`01-brass-gauges-leather.jpg`** — Polished brass pressure gauges set into leather/wood paneling — the exact material pairing this theme should read as _(search: steampunk brass pressure gauge leather panel photo)_
- **`02-sight-glass.jpg`** — A brass-and-glass sight-glass / liquid-level gauge (visible internal fluid + rivets) _(search: steampunk sight glass gauge brass photo)_
- **`03-control-panel.jpg`** — A full steampunk control panel/prop: multiple gauges, brass switches, exposed rivets _(search: steampunk control panel brass gauges rivets prop photo)_

</details>

<details>
<summary><code>tron</code></summary>

- **`01-grid-cycle.jpg`** — The Grid from TRON: Legacy — cyan line-work on black, an identity disc or light cycle _(search: TRON Legacy Grid cyan light cycle screenshot)_
- **`02-cut-corner-ui.jpg`** — A TRON: Legacy interface panel with its angular cut corners _(search: TRON Legacy UI panel cut corner screenshot)_
- **`03-clu-orange.jpg`** — A CLU/Rinzler orange-accent shot, for the villain-accent color pairing _(search: TRON Legacy CLU orange screenshot)_

</details>

<details>
<summary><code>vaporwave</code></summary>

- **`01-grid-horizon.jpg`** — A classic vaporwave grid-horizon/sunset composition (pink/cyan) _(search: vaporwave grid sunset aesthetic image)_
- **`02-statue-glitch.jpg`** — A vaporwave Greek-statue-plus-glitch composition, a defining genre motif _(search: vaporwave greek statue glitch aesthetic)_
- **`03-mall-japanese-text.jpg`** — A vaporwave mall/plaza scene with Japanese katakana text overlay _(search: vaporwave mall aesthetic Japanese text)_

</details>

<details>
<summary><code>win7-aero</code></summary>

- **`01-aero-glass-window.png`** — A Windows 7 window with visible Aero Glass blur/translucency _(search: Windows 7 Aero glass window screenshot)_
- **`02-aero-taskbar.png`** — The Aero glass taskbar with Aero Peek _(search: Windows 7 Aero taskbar glass screenshot)_
- **`03-aero-flip3d.png`** — Aero Flip 3D window switcher, for the glass-depth effect _(search: Windows 7 Aero Flip 3D screenshot)_

</details>

<details>
<summary><code>winamp-classic</code></summary>

- **`01-main-window.png`** — Winamp's classic main window: LCD green readout, bevelled buttons _(search: Winamp classic skin main window screenshot)_
- **`02-equalizer.png`** — The Winamp Equalizer window with its slider bank _(search: Winamp classic equalizer window screenshot)_
- **`03-playlist-editor.png`** — The Winamp Playlist Editor window _(search: Winamp classic playlist editor screenshot)_

</details>

<details>
<summary><code>windows95</code></summary>

- **`01-desktop.png`** — The Windows 95 desktop: teal background, taskbar, Start button _(search: Windows 95 desktop screenshot teal)_
- **`02-dialog-bevels.png`** — A Windows 95 dialog box for the 3D bevel chrome close up _(search: Windows 95 dialog box bevel screenshot)_
- **`03-explorer-window.png`** — A Windows 95 Explorer window with its navy titlebar _(search: Windows 95 Explorer window screenshot)_

</details>

<details>
<summary><code>winxp-luna</code></summary>

- **`01-start-menu.png`** — The Luna Start menu with the green Start button _(search: Windows XP Luna Start menu green screenshot)_
- **`02-bliss-desktop.jpg`** — The default XP desktop with the Bliss wallpaper _(search: Windows XP Bliss wallpaper desktop screenshot)_
- **`03-window-chrome.png`** — An XP window's glossy blue titlebar/chrome close up _(search: Windows XP Luna window titlebar screenshot)_

</details>

<details>
<summary><code>wmp11</code></summary>

- **`01-library-view.png`** — WMP11's Library view with breadcrumbs and the black-glass chrome _(search: Windows Media Player 11 library screenshot)_
- **`02-now-playing.png`** — WMP11's Now Playing view with the round play button _(search: Windows Media Player 11 now playing round button screenshot)_
- **`03-visualization.png`** — A WMP11 visualization for the blue-glow backdrop reference _(search: Windows Media Player 11 visualization screenshot)_

</details>
