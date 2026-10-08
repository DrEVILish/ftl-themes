# alienware — visual reference notes

Outsider read: Matte black chassis + single AlienFX cyan glow per lighting zone. Angular vents/cuts, Command Center FX/Performance tabs.

Capture targets: AlienFX zone editor; chassis angles; Command Center overview.

Sources: Dell AlienFX manual; Alienware Command Center.

Use side-by-side with example.html; local captures are copyrighted originals — this file is the textual checklist.

Audit 2026-09-26: all 8 files inspected, zero people — KEPT all. YT thumbs (maxresdefault, maxresdefault-1, sddefault) are icon-pack/desktop-skin thumbnails, no presenters on screen. Relevance note: most files are third-party icon/desktop skins (Invader/XP-era), not the Dell AlienFX zone editor / Command Center dashboard in capture targets — weakest-relevance set, but no rule violation; proper Dell-manual captures remain a gap.

## The Windows XP factory themes (AlienGUIse), researched 2026-10-07

Alienware shipped its XP-era desktops and laptops with **AlienGUIse**, a
theme manager built on Stardock technology (WindowBlinds, later MyColors).
Every suite bundled a WindowBlinds visual style, a Windows Media Player
skin, an icon set and a wallpaper, and the themes were also free downloads
from alienware.com. Named suites, in release order:

| Suite | Designer | Released | Look | Here |
|---|---|---|---|---|
| **AlienMorph** | The Skins Factory | 27 Aug 2004 (with ALXMorph) | Released as a pair with ALXMorph; 2 WindowBlinds themes, 2 WMP skins, 75+ icons. Exact palette unverified | `alienmorph/alienMorph-desktop-startMenu-titleBar-taskbar.webp` (lossless preview) → variant `alienmorph` |
| **ALXMorph** ("ALX") | The Skins Factory | 27 Aug 2004 | Grey brushed metal, silver gradients, small blue LEDs, the "ALX" wordmark; animated WMP skin | `GGZKPU0XMAE3l44.jpg`, `597ffe4e-…_rw_1920.jpg` → variant `alx` |
| **Darkstar** | The Skins Factory | 18 Mar 2005 | "Black and red", function-responsive LED arrays, audio-enhanced start-up animations; WMP 10 skin | `darkstar/darkstar-desktop-startMenu-titleBar-taskbar.webp` (lossless preview) → variant `darkstar` |
| **Alienware Area-51 Superman** (Superman Special Edition) | The Skins Factory | 2006 | DC Comics co-brand, only on the limited-edition Superman PCs, never a public download | none |
| **Star Wars – Dark Side / Light Side** (Aurora Star Wars Edition) | The Skins Factory | 2006–07 | Rebellion-ship styling, 35 Star Wars icons; only on the Aurora Star Wars Edition systems | none |
| **Redskins Ultimate Fan Xperience** | The Skins Factory | 2006–07 | Washington Redskins co-brand; exclusive to that PC | none |
| **XenoMorph** | Stardock Design | 13 Oct 2006 | Glossy black glass, cyan-blue glow, animated windows and Start menu; WindowBlinds 5, ObjectDock OEM, RSS gadget. Also a **XenoMorph Slim** cut | `3754370_2.jpg` → the default palette |
| **Invader** | The Skins Factory ("7th and final") | 2007; AlienGUIse Invader (MyColors) 25 May 2008, XP and Vista | Black title bars in silver frames, blue LEDs, deep-space starfield | `b2bdcc9c…_600.webp`, `icon-packs/alienware-invader-blue/` → variant `invader` |

Sources: [archive.org: AlienGUIse + all suites](https://archive.org/details/alien-guise),
[archive.org: AlienGUIse XP](https://archive.org/details/alien-guise-alienware-xp),
[The Skins Factory: legacy desktops](https://theskinsfactory.myportfolio.com/legacy-work-windows-desktops),
[Stardock: Xenomorph partnership](https://forums.stardock.com/133429/alienware-and-stardock-corporation-partner-to-deliver-xenomorph-desktop),
[Stardock: AlienGUIse Invader](https://forums.stardock.com/313134/alienguise-invader-mycolors),
[WebWire: Darkstar press release](https://www.webwire.com/ViewPressRel.asp?aId=1858).
Dates for the co-branded editions are from the systems they shipped on, not
a primary source.

## Fan and later work (not factory themes)

- `alienware_evolution_theme_for_windows_10_…_moonnique_…png` — Windows 10
  "Alienware Evolution" skin: black panels, cyan icons and rules.
- `alienware_breed_icons_by_polina110986_…jpg` — "Breed" icon set, dark glass with blue LEDs.
- `alienware_xenomorph_link_rainmeter_windows_xp_…jpg` — a Rainmeter link panel in the Xenomorph style.
- `desktop_december_2008_by_death020899_…jpg` — fan desktop: the Xenomorph orb media player, CPU/RAM gauges, black taskbar.
- `icon-packs/alienware-eclipse/` (Mr Blade, 7tsp; `Pack.ini` holds its task-manager colours `#00ccff` on `#1a1a1a`), `icon-packs/alienware-slate-blue/` (141 .ico: black glass and silver with pale-blue alien heads). The 7tsp `.res` resource dumps were left out: they are not viewable images.

## Audit 2026-10-07 (new files)

All new images and icons inspected: no people. `GGZKPU0XMAE3l44.webp` was
a re-encode of the existing `.jpg` and was not kept.


## AlienGUIse rebuild (2026-10-09)

The theme now **extends `winxp-luna`** and re-skins XP per suite, because
that is what AlienGUIse did: Stardock's Theme Manager (its About box reads
"© 2001–2006 Stardock Corporation, © 2005–2006 Alienware") applying a
WindowBlinds skin, an icon set, a WMP skin and a wallpaper to Windows XP.

### Primary sources (all on archive.org; downloads kept out of the repo)

- [`alien-guise`](https://archive.org/details/alien-guise): eight lossless
  1920×1080 PNG previews, one per suite, each showing the suite's open
  Start menu, taskbar and the Theme Manager window; and `AlienGUIse.7z`,
  whose `Themes.7z` holds three complete `.suite` files (zip):
  `XenoMorph.suite`, `Star Wars - Dark Side.suite`, `Star Wars - Light Side.suite`,
  each with its WindowBlinds `.uis` and bitmaps, IconPackager icons and
  wallpapers. The other suites sit inside the setup program's packed
  payload, which could not be opened without running it (not done).
- [`alien-guise-alienware-xp`](https://archive.org/details/alien-guise-alienware-xp)
  and [`alienware-xenomorph-slim`](https://archive.org/details/alienware-xenomorph-slim):
  800×600 previews of five suites and the Theme Manager.
- [`AlienwareInvader`](https://archive.org/details/AlienwareInvader): The
  Skins Factory promo sheets for the ALX Vortex, Darkstar, Invader and
  Teleport Media Player skins.

The previews are lossless and 1:1: a column through the XenoMorph preview's
title bar matches the suite's own `FrameTop.bmp` pixel for pixel.

### Measurements by suite

| Suite | Caption (top → bottom) | Taskbar | Start menu | Face / highlight |
|---|---|---|---|---|
| XenoMorph (`.uis` + bitmaps) | 29px: `#000` edge, `#bdbdbd` lip, `#717171`→`#464646` gloss over 12 rows, flat `#252525`, `#000`; Arial Bold 14 with a blue glow | 31px: `#adadad` lip, `#6f6f6f`→`#000` | header `#0f1017`; programs `#252525`→`#050505`; places brushed `#bfbfbf`–`#cbcbcb`; footer `#1c1c1c`→`#000` | `#d7d7d7` / `#0093f0`; panes `#fff`; frame `#000/#575757/#1a1a1a` |
| Darkstar (preview) | `#71737f` lip, `#4d5059`→`#393b41`, `#111113` crease, `#1f1f23` | bright bevel `#4a4d55`→`#9da1b0` then `#1a1a1e`→`#1d1e21` | header `#404348`/`#36393e`; programs `#9d9d9d`→`#878787`; places `#25272b`; footer `#2f3136` | `#9d9d9d` / black `#060607` |
| Invader (preview) | `#9f9fa5`→`#ffffff`→`#e9ebf3` (silver) | flat `#d9dbe5`, cyan START | header `#d7dae4`; programs `#e6e8f0`/`#c8cad2`; places `#d2d4de`; footer `#191a1c` | `#d9dbe5` / `#01bdfe` |
| ALXMorph (preview) | `#c7cacd`, `#ffffff` lip, `#f2f2f3`→`#959ba0`→`#b2b6bb`, `#54595e` | `#ffffff`→`#94999f`→`#a7abb1` | header `#959ba0`; columns `#a8acb1`; footer `#696c6f` | `#a8acb1` / `#12acfe` |
| AlienMorph (preview) | `#d5d5d6` lip, `#f8f8f8`→`#dfe2e2`, `#acacad` | same gloss as the caption | header `#e6e9e9`; columns `#f1f3f3` | `#f1f3f3` / `#12acfe` |
| Area-51 Superman (preview) | `#002b58`, `#0465b9`→`#83baff` gloss→`#0085e2`→`#255eb5` | flat `#2877cb` | header `#265baa`; columns `#6e0000`; footer `#2b599b` | `#2877cb` / `#c4211b` |
| Star Wars Dark / Light (files + preview) | gold-orange band `#bd7312`→`#f9bd21`, `#f1e1ae` highlight, `#db8715` | beige `#c6c2b5` with `#f1f1ee` lip | header `#cac7bb`; columns `#ccc9be` / `#b7b4aa`; footer orange `#d6a21c` | `#d1cec5` / `#eaa62f` |

Derived, not measured (no source shows them): the Explorer task pane of
every suite except XenoMorph (from the suite's caption and face colours),
inactive captions except XenoMorph's (the active caption desaturated),
frame colours except XenoMorph's (the caption's edge colour), and the
caption buttons' exact artwork (drawn from the previews' colours).
Wallpapers are CSS impressions. The Dark and Light Side suites share their
chrome; only the wallpaper and second accent differ.

### References added

- `xenoMorph-desktop-startMenu-titleBar-taskbar.webp` and one preview per
  variant folder (`darkstar/`, `invader/`, `alx/`, `alienmorph/`,
  `area-51/`), lossless WebP of the archive.org PNGs.
- `aurora-dark/` and `aurora-light/`: only the Start menu with taskbar
  (user-picture tile painted out) and the title bar. The full previews show
  film stills of actors and are not kept.

### Other Alienware items found (not built)

- **Media Player skins** by The Skins Factory: ALX Vortex (2004), Teleport
  (2004, white and silver, "Mars Attacks"), Darkstar (2005), Invader (2007,
  WMP 11). [archive.org](https://archive.org/details/AlienwareInvader),
  [Darkstar WMP](https://archive.org/details/alienware-darkstar-skinwmp),
  [ALXMorph WMP](https://archive.org/details/alienware-alxmorph-wmpskin),
  [Invader WMP](https://archive.org/details/alienware-invader-wmpskin).
- **XenoMorph Slim**, a lighter XenoMorph cut, and the **AW Red Glyph**
  wallpaper ([archive.org](https://archive.org/details/alienware-xenomorph-slim)).
- **Breed**, the Windows 7-era AlienGUIse theme, and the Vista/Windows 7
  AlienGUIse builds in the [HyperDesk Theme Collection](https://archive.org/details/hyperdesk-theme-collectionnot-complete).
- Third-party remakes sold today (skinpacks.com "4 ALIENWARE" bundle) are
  not sources.

### Non-Alienware skins found along the way

- **Official Xbox WindowBlinds theme** (The Skins Factory for Microsoft,
  2002): examples and measured colours in `references/xbox-windowblinds/`.
- **Doppler** and **Quagmire** by Skinplant, **Toon-XP** by Stardock and
  **UniverseMetal (2004)** by Pixtudio.com (a Stardock premium suite based
  on Pixtudio's Universe Metal): listed in the AlienGUIse Theme Manager in
  the previews, bundled as extra suites. No usable capture found yet
  (WinCustomize, which hosted them, refuses automated access).
- **Windows XP Desktop**: the Theme Manager's entry that restores Luna.

Audit 2026-10-09: all new images inspected; no people (Aurora crops
painted out as above).
