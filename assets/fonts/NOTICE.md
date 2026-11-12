# Font notices (`assets/fonts/`)

Companion to `docs/icon-license-research.md` and `assets/logos/README.md` —
same idea, different asset class: this records what was actually checked
about each vendored font's license, rather than assuming "it's on Google
Fonts, so it must be SIL OFL" uniformly across every family. Each entry
below was verified against that family's own Google Fonts listing (and,
for the ones mirrored in the `google/fonts` GitHub repo, its `ofl/`
directory placement — Google Fonts sorts fonts into `ofl/`, `apache/` or
`ufl/` by license, so the directory itself is a second confirmation
alongside the specimen page's license line).

All files vendored here except Bedstead (CC0) and Px437 IBM VGA 9x16 (CC BY-SA 4.0), both below, turned out to be **SIL Open Font License,
version 1.1** — but that was verified per family below, not assumed.
OFL 1.1 permits embedding, bundling and redistributing the font (including
as a webfont, including verbatim, including at whatever scale this
library is redistributed to consuming apps) without requiring per-use or
per-page attribution — the one hard restriction is that the font may not
be **sold by itself**, on its own, separate from software; that doesn't
apply to embedding it in a theme's CSS bundle. Reserved font names must
not be reused by a modified version, which is moot here since these
files are vendored unmodified (the Inter subset below is the one modified file, and Inter declares no Reserved Font Name).

## Antonio

- **Family:** Antonio (weights vendored: Regular 400, Bold 700 —
  `Antonio-Regular.woff2`, `Antonio-Bold.woff2`)
- **Designer:** Vernon Adams
- **License:** SIL Open Font License, version 1.1
- **Source:** https://fonts.google.com/specimen/Antonio
- **Used by:** `lcars` (display face for the sweep bar and numeric
  readouts)

## Archivo

- **Family:** Archivo (weight vendored: Bold 700, Latin subset —
  `Archivo-Bold.woff2`, the Google Fonts Latin woff2, unmodified)
- **Designer:** Omnibus-Type (Héctor Gatti)
- **License:** SIL Open Font License, version 1.1 (google/fonts `ofl/archivo`)
- **Source:** https://fonts.google.com/specimen/Archivo
- **Used by:** `imac-g3` (stand-in for Charcoal, the Mac OS 8/9 system
  face, in headings, title bars and the brand)

## Audiowide

- **Family:** Audiowide (weight vendored: Regular 400 —
  `Audiowide-Regular.woff2`)
- **Designer:** Brian J. Bonislawsky, for Astigmatic (AOETI)
- **License:** SIL Open Font License, version 1.1
- **Source:** https://fonts.google.com/specimen/Audiowide
- **Used by:** `vaporwave` (headings-only full-width display face)

## Bedstead

- **Family:** Bedstead (Regular, subset to Latin, arrows, box drawing and
  the teletext sextant mosaics U+1FB00–1FBAF — `Bedstead.woff2`)
- **Designer:** Ben Harris — an outline recreation of the Mullard SAA5050
  teletext character generator
- **License:** CC0 1.0 (public domain dedication), per the author's page
  and the font's `SPDX-License-Identifier: CC0-1.0`. Not OFL — more
  permissive: no conditions at all.
- **Source:** https://bjh21.me.uk/bedstead/ (`bedstead.otf` 3.261,
  converted to WOFF2 with fontTools)
- **Used by:** `teletext` (every glyph on the page)

## Baloo 2

- **Family:** Baloo 2 (variable cut, wght 400-800, Latin subset —
  `Baloo2-Variable.woff2`, subset with fontTools from
  `google/fonts` `ofl/baloo2/Baloo2[wght].ttf`). The older static
  `Baloo2-Bold.woff2` (700) is kept for existing references.
- **Designer:** Ek Type
- **License:** SIL Open Font License, version 1.1 — `google/fonts`
  `ofl/baloo2/` (with `OFL.txt`)
- **Source:** https://fonts.google.com/specimen/Baloo+2
- **Used by:** `barbie` (rounded voice for body, labels, buttons and
  headings, 400-800)

## IM Fell English SC

- **Family:** IM Fell English SC (weight vendored: Regular 400 —
  `IMFellEnglishSC-Regular.woff2`)
- **Designer:** Igino Marini (digitisation of the 17th-century Fell types)
- **License:** SIL Open Font License, version 1.1 — confirmed by its
  placement at `google/fonts` `ofl/imfellenglishsc/` (with `OFL.txt`)
  and `license: "OFL"` in that directory's `METADATA.pb`
- **Source:** https://fonts.google.com/specimen/IM+Fell+English+SC
- **Used by:** `steampunk` (display face: headings, panel nameplates,
  buttons, the app bar)

## Px437 IBM VGA 9x16

- **Family:** Px437 IBM VGA 9x16 (web cut `Web437_IBM_VGA_9x16`, converted
  from the pack's WOFF to WOFF2 with fontTools, glyphs unmodified —
  `Web437_IBM_VGA_9x16.woff2`)
- **Designer:** VileR (int10h.org), reproducing the IBM VGA ROM font
- **License:** Creative Commons Attribution-ShareAlike 4.0 International
  (CC BY-SA 4.0), per the pack's own `LICENSE.TXT` —
  https://creativecommons.org/licenses/by-sa/4.0/. Attribution: "Ultimate
  Oldschool PC Font Pack" by VileR, https://int10h.org/oldschool-pc-fonts/.
  ShareAlike applies to the font file itself (any modified version must
  carry the same license), not to the CSS or apps that load it.
- **Source:** https://int10h.org/oldschool-pc-fonts/ (pack v2.2, web
  edition)
- **Used by:** `msdos` (every glyph on the page); `nokia-3310` (code, kbd, pre and samp only)

## Jost

- **Family:** Jost (variable, `wght` 100-900, Latin subset as served by
  Google Fonts — `Jost-Variable.woff2`)
- **Designer:** Owen Earl (indestructible type*), a Futura-inspired
  geometric sans
- **License:** SIL Open Font License, version 1.1 — the file's own
  copyright string reads "Copyright 2020 The Jost Project Authors
  (https://github.com/indestructible-type/Jost)", and the family sits at
  `google/fonts` `ofl/jost/`
- **Source:** https://fonts.google.com/specimen/Jost
- **Used by:** `lego-classic` (every glyph; Futura is named first when
  installed)

## Michroma

- **Family:** Michroma (weight vendored: Regular 400 —
  `Michroma-Regular.woff2`)
- **Designer:** Vernon Adams
- **License:** SIL Open Font License, version 1.1
- **Source:** https://fonts.google.com/specimen/Michroma
- **Used by:** `prometheus` (wide squared label and heading face)

## Orbitron

- **Family:** Orbitron (weight vendored: Bold 700/800 range —
  `Orbitron-Bold.woff2`)
- **Designer:** Matt McInerney (The League of Moveable Type)
- **License:** SIL Open Font License, version 1.1
- **Source:** https://fonts.google.com/specimen/Orbitron
- **Used by:** `alienware` (AlienFX display/heading face)

## Pacifico

- **Family:** Pacifico (weight vendored: Regular 400 —
  `Pacifico-Regular.woff2`)
- **Designer:** Vernon Adams (commissioned by Google)
- **License:** SIL Open Font License, version 1.1
- **Source:** https://fonts.google.com/specimen/Pacifico
- **Used by:** none currently (`barbie` used it for the brand mark and `h1`,
  as the cursive script signature — never body/button text)

## Shrikhand

- **Family:** Shrikhand (weight vendored: Regular 400, Latin subset —
  `Shrikhand-Regular.woff2`, subset with fontTools from `google/fonts`
  `ofl/shrikhand/Shrikhand-Regular.ttf`; the Gujarati glyphs are dropped)
- **Designer:** Jonny Pinhorn
- **License:** SIL Open Font License, version 1.1 — `google/fonts`
  `ofl/shrikhand/` (with `OFL.txt`); no Reserved Font Name is declared
- **Source:** https://fonts.google.com/specimen/Shrikhand
- **Used by:** `barbie` (wordmark face on the brand mark and `h1` only)

## Inconsolata

- **Family:** Inconsolata (weights vendored: Regular 400, Bold 700, Latin
  subset — `Inconsolata-Regular.woff2`, `Inconsolata-Bold.woff2`)
- **Designer:** Raph Levien (The Inconsolata Project Authors)
- **License:** SIL Open Font License, version 1.1
- **Source:** https://fonts.google.com/specimen/Inconsolata (files from
  the `@fontsource/inconsolata` 5.1.0 Latin subset, unmodified)
- **Used by:** `blue-future` (stand-in for Consolas, the reference face)

## Share Tech and Share Tech Mono

- **Family:** Share Tech (Regular 400 — `ShareTech-Regular.woff2`) and
  Share Tech Mono (Regular 400 — `ShareTechMono-Regular.woff2`)
- **Designer:** Carrois Type Design
- **License:** SIL Open Font License, version 1.1
- **Source:** https://fonts.google.com/specimen/Share+Tech and
  https://fonts.google.com/specimen/Share+Tech+Mono
- **Used by:** `prometheus` (body text and data readouts), `cyberpunk-2077` (Share Tech Mono: code and logs), `bloomberg` (Share Tech Mono: code and readouts)

## Roboto Condensed

- **Family:** Roboto Condensed (Latin subset, weights vendored: Regular 400,
  Bold 700 — `RobotoCondensed-Regular.woff2`, `RobotoCondensed-Bold.woff2`,
  taken unmodified from the `@fontsource/roboto-condensed` 5.0.14 package)
- **Designer:** Christian Robertson (Google)
- **License:** SIL Open Font License, version 1.1
- **Source:** https://fonts.google.com/specimen/Roboto+Condensed
- **Used by:** `bloomberg` (all UI text and figures; open stand-in for the
  terminal's proprietary narrow screen sans, with a real bold)

- **Used by:** `prometheus` (body text and data readouts), `cyberpunk-2077` (Share Tech Mono: code and logs), `matrix` (Share Tech Mono: app bar and headings)

## DSEG7 Classic

- **Family:** DSEG7 Classic (Bold Italic — `DSEG7Classic-BoldItalic.woff2`)
- **Designer:** keshikan
- **License:** SIL Open Font License, version 1.1 (full text in `DSEG-LICENSE.txt`)
- **Source:** https://github.com/keshikan/DSEG
- **Used by:** `cassette-futurism` (seven-segment readout digits)

## Inter

- **Family:** Inter (`InterVariable-Latin.woff2`: Inter 4.0 variable,
  instanced to `wght` 300–700 at `opsz` 14 and subset to Latin with
  fontTools — the one file in this folder that is a modified subset, not
  an unmodified upstream file; Inter's OFL declares no Reserved Font Name,
  and the theme loads it under its own family name, "Aperture Inter")
- **Designer:** Rasmus Andersson / The Inter Project Authors
- **License:** SIL Open Font License, version 1.1 (stated in the font's own
  name table, ID 13/14)
- **Source:** https://github.com/rsms/inter (also
  https://fonts.google.com/specimen/Inter)
- **Used by:** `aperture` (Univers stand-in for chamber signage: Light 300
  headings and numerals, SemiBold 600 labels)

## Titillium Web

- **Family:** Titillium Web (weights vendored: Light 300, Regular 400,
  SemiBold 600, Bold 700, Bold Italic 700 — `TitilliumWeb-Light.woff2`,
  `TitilliumWeb-Regular.woff2`, `TitilliumWeb-SemiBold.woff2`,
  `TitilliumWeb-Bold.woff2`, `TitilliumWeb-BoldItalic.woff2`; Google Fonts'
  Latin subset, unmodified)
- **Designer:** Accademia di Belle Arti di Urbino
- **License:** SIL Open Font License, version 1.1 (verified in
  `google/fonts` `ofl/titilliumweb/OFL.txt` and its `METADATA.pb`,
  `license: "OFL"`)
- **Source:** https://fonts.google.com/specimen/Titillium+Web
- **Used by:** `motorsport-telemetry` (UI, timing figures and readouts; its
  digits are tabular by default, all 560 units wide)

## Rajdhani

- **Family:** Rajdhani (weights vendored: Medium 500, Bold 700 —
  `Rajdhani-Medium.woff2`, `Rajdhani-Bold.woff2`; Latin subset as served
  by Google Fonts)
- **Designer:** Indian Type Foundry
- **License:** SIL Open Font License, version 1.1 (verified in the
  `google/fonts` repo, `ofl/rajdhani/OFL.txt` and `METADATA.pb`
  `license: "OFL"`)
- **Source:** https://fonts.google.com/specimen/Rajdhani
- **Used by:** `cyberpunk-2077` (all UI text; stand-in for the game's
  commercial condensed face)

## Inter

- **Family:** Inter (one variable file, `Inter-Variable.woff2`: weight
  axis 400-700, optical-size axis 14-32)
- **Designer:** Rasmus Andersson and the Inter Project Authors
- **License:** SIL Open Font License, version 1.1 (the font's own name
  table: "This Font Software is licensed under the SIL Open Font License,
  Version 1.1"; Copyright 2016 The Inter Project Authors). No Reserved
  Font Name is declared, so the subset keeps the family name.
- **Source:** https://github.com/rsms/inter (Inter 4.0 variable,
  `InterVariable.woff2`), subset with fontTools to Basic Latin, Latin-1
  and common punctuation, the weight axis limited to 400-700, hinting
  dropped
- **Used by:** `ios-flat` and `liquid-glass` (and the themes that extend them), the open
  stand-in for SF Pro after `-apple-system` and Helvetica Neue

## Roboto and Roboto Mono

- **Family:** Roboto (weights vendored: Regular 400, Medium 500 —
  `Roboto-Regular.woff2`, `Roboto-Medium.woff2`) and Roboto Mono
  (Regular 400 — `RobotoMono-Regular.woff2`); Latin subsets, unmodified
- **Designer:** Christian Robertson, for Google
- **License:** SIL Open Font License, version 1.1 (Roboto 3 moved to
  `google/fonts` `ofl/roboto/`; verified in the files' own source
  package, `@fontsource/roboto@5.2.5` and `@fontsource/roboto-mono@5.2.5`,
  whose `LICENSE` is the OFL 1.1 text and `package.json` says
  `"license": "OFL-1.1"`. Older 5.1.x packages still carried Roboto 2
  under Apache 2.0, so those were not used.)
- **Source:** https://fonts.google.com/specimen/Roboto,
  https://fonts.google.com/specimen/Roboto+Mono (files from the
  Fontsource npm packages above: `roboto-latin-400-normal.woff2`,
  `roboto-latin-500-normal.woff2`, `roboto-mono-latin-400-normal.woff2`)
- **Used by:** `material` (all UI text and the mono face; MD2's own type
  family, Medium for button, tab and title roles)

## Selawik

- **Family:** Selawik (weights vendored: Light 300, Regular 400, Semibold
  600 — `Selawik-Light.woff2`, `Selawik-Regular.woff2`,
  `Selawik-Semibold.woff2`; the release's own Latin woff2 files,
  unmodified)
- **Designer:** Microsoft Corporation (Aaron Bell) — an open,
  metric-compatible fallback for Segoe UI
- **License:** SIL Open Font License, version 1.1, with Reserved Font
  Name "Selawik" (verified in the project's `LICENSE.txt`); vendored
  unmodified, so the name is kept as shipped
- **Source:** https://github.com/microsoft/Selawik (release 1.01,
  `Selawik_Release.zip`: `selawkl.woff2`, `selawk.woff2`, `selawksb.woff2`)
- **Used by:** `windows-live` (all UI text; stand-in for Segoe UI and its
  Light headings)

## Barlow Semi Condensed

- **Family:** Barlow Semi Condensed (weight vendored: ExtraBold Italic 800
  — `BarlowSemiCondensed-ExtraBoldItalic.woff2`; Google Fonts' Latin
  subset, unmodified)
- **Designer:** Jeremy Tribby
- **License:** SIL Open Font License, version 1.1 (verified in
  `google/fonts` `ofl/barlowsemicondensed/METADATA.pb`, `license: "OFL"`)
- **Source:** https://fonts.google.com/specimen/Barlow+Semi+Condensed
- **Used by:** `hot-wheels` (display type: headings, buttons, nav, tabs;
  stand-in for the game menu's heavy semi-condensed italic caps)

## Bottom line

Twenty-two files, sixteen families: fourteen SIL OFL 1.1, Bedstead CC0 and Px437

Twenty-four files, seventeen families: fifteen SIL OFL 1.1, Bedstead CC0 and Px437
CC BY-SA 4.0, all verified per family rather than assumed from "it's on
Google Fonts." Attribution is optional under
OFL (unlike, say, CC BY), but is included here anyway for the same
diligence reasons `docs/icon-license-research.md` and
`assets/logos/README.md` document their sources: so "we checked" isn't
just asserted from memory, and so a future addition to this directory has
a template to follow instead of reinventing the check.

## Noto Serif Display (condensed black instance)

- **Family:** Noto Serif Display, the variable font instanced at
  `wdth=62.5`, `wght=900` and subset to Basic Latin, Latin-1 and common
  punctuation with fontTools (`NotoSerifDisplay-CondensedBlack.woff2`).
  The file is a modified version, so it is served under the CSS family name
  `"NERV Title"`, not the original name.
- **Designer:** Google (Noto project)
- **License:** SIL Open Font License, version 1.1
- **Source:** https://fonts.google.com/specimen/Noto+Serif+Display
  (`google/fonts`, `ofl/notoserifdisplay/`)
- **Used by:** `nerv` (title-card serif for `h1`/`h2`, standing in for
  the proprietary Matisse EB)

## Jersey 15

- **Family:** Jersey 15 (Regular, subset to Latin-1 plus common
  punctuation, arrows and the euro sign — `Jersey15-Regular.woff2`)
- **Designer:** Sarah Cadigan-Fried (The Soft Type Project Authors)
- **License:** SIL Open Font License, version 1.1 (the `OFL.txt` in the
  family's `google/fonts` `ofl/jersey15/` directory)
- **Source:** https://fonts.google.com/specimen/Jersey+15
  (https://github.com/google/fonts/tree/main/ofl/jersey15)
- **Used by:** `nokia-3310` (the pixel face for the whole screen, standing
  in for the 3310's Series-20 screen font)
