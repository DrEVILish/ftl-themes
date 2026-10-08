# Alienware

> Alienware's AlienGUIse desktop suites for Windows XP: XP's structure, re-skinned per suite.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

**Family:** Windows desktop; extends [Windows XP (Luna)](../winxp-luna/README.md).

## What this theme is trying to achieve

From 2004 to 2008 Alienware shipped its Windows XP machines with
**AlienGUIse**, a theme manager built on Stardock's WindowBlinds and
MyColors. Each "suite" re-skinned XP itself: the title bars and caption
buttons, the two-column Start menu, the taskbar and Start button,
Explorer's task pane and the push buttons, scroll bars and tabs, over
light window contents. This theme is that: XP's structure (it extends
`winxp-luna`) with each suite's own chrome, measured from the suite's
surviving files.

## The suites

| Variant | Suite | Designer, year | Look | Measured from |
|---|---|---|---|---|
| (default) | XenoMorph | Stardock Design, 2006 | Glossy black title bars and taskbar, silver caption buttons, a blue-ringed Start orb; black programs and brushed-silver places in the Start menu; `#d7d7d7` dialog face, `#0093f0` highlight | The suite's own WindowBlinds files (`.uis` colours and bitmaps) |
| `darkstar` | Darkstar | The Skins Factory, 2005 | Gunmetal chrome, grey programs and black places columns, black selection, red LED bars | Lossless AlienGUIse preview |
| `invader` | Invader | The Skins Factory, 2007–08 | Pale silver title bars in black frames, a silver taskbar with a cyan START button | Lossless AlienGUIse preview |
| `alx` | ALXMorph | The Skins Factory, 2004 | Brushed silver-grey chrome with a white lip, `#a8acb1` face | Lossless AlienGUIse preview |
| `alienmorph` | AlienMorph | The Skins Factory, 2004 | Glossy white-to-pale-grey chrome, `#f1f3f3` face | Lossless AlienGUIse preview |
| `area-51` | Alienware Area-51 Superman (TM) edition | The Skins Factory, 2006 | Glossy blue chrome and face, red Start menu columns and selection, yellow on red | Lossless AlienGUIse preview |
| `aurora-dark` | Star Wars – Dark Side (Aurora Star Wars Edition) | The Skins Factory, 2006–07 | Gold-and-orange title bars over beige chrome, an orange Start-menu footer | The suite's own WindowBlinds files and the preview |
| `aurora-light` | Star Wars – Light Side | The Skins Factory, 2006–07 | The same chrome as Dark Side; a teal wallpaper | The suite's own WindowBlinds files and the preview |

The co-branded editions are named after the Alienware systems they shipped
on (Area-51, Aurora), not the licensed properties: the theme reproduces
their chrome, never the DC or Lucasfilm artwork. Every value, its source
and what was derived rather than measured is in
[`references/alienware/RESEARCH.md`](../../references/alienware/RESEARCH.md).

## Core values

1. **XP underneath.** Window chrome, the Start menu, the taskbar and the
   task pane are XP's (`winxp-luna`), re-skinned. Nothing invents a layout
   AlienGUIse didn't have.
2. **Measured, not guessed.** Each suite's colours come from its own skin
   files or its lossless preview. Values that no source shows (task panes
   outside XenoMorph, inactive captions outside XenoMorph) are derived from
   that suite's measured chrome and marked as derived.
3. **Dark chrome, light contents.** Even the black suites drew light
   dialog faces and white panes; only the chrome is dark.
4. **No borrowed artwork.** Wallpapers are CSS impressions of each suite's
   wallpaper; the alien-head marks and co-brand logos are not reproduced.

## Signature details

- Captions use Arial Bold (XenoMorph's `.uis`: `FontName=Arial`,
  `FontWeight=700`, `FontHeight=14`); XenoMorph's caption text glows blue.
- Caption buttons are drawn per suite (`--luna-caption`): silver squares
  with dark glyphs (XenoMorph, ALX, AlienMorph), dark with white or red
  glyphs (Darkstar), black with cyan glyphs (Invader), red with yellow
  (Area-51), beige with an orange close (Aurora).
- The Start button follows the suite: XenoMorph's blue orb in a silver ring,
  the light "START" rectangle (AlienMorph, ALX), Invader's cyan START,
  Darkstar's dark button, Area-51's red, Aurora's gold pill.

## Accessibility notes

The suites' highlight colours were drawn for 2006 CRTs. Where a measured
colour fails WCAG it is kept for fills and glows and a darker or darker-text
companion carries text:

- `--accent-text` is a darker shade of each highlight for links, headings
  and accent text; `--on-accent` is black where XP drew white on a light
  highlight (XenoMorph `#0093f0`, AlienMorph/ALX `#12acfe`, Invader `#01bdfe`).
- Area-51's headings and breadcrumbs are black: its page face is the
  measured blue `#2877cb`, where dark red fails.
- ALX's and Area-51's page app bars use a gentler cut of the caption
  gradient so their text passes 4.5:1 against every stop; windows keep the
  measured gradient. Aurora's status strip drops a 1px dark edge stop into
  an inset line for the same reason.
- The highlight colours stay under 3:1 as UI colour on the light faces
  (`check.sh` warnings), as the originals were.

## Icons

`themes/alienware/icons.svg` keeps the angular single-colour set for the
less-used glyphs, and uses the full-colour XP-style drawings from
`winxp-luna` for the 30 icons on the desktop, in the Start menu and in
Explorer: the suites' previews show XP's colour icons there.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
