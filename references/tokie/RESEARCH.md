# Tokie: research notes

Tokie is an original concept, not a reproduction of one product: black
full-grain leather with saddle stitching, gold-foil debossing, and gold
hardware in brushed and polished finishes, in the manner of a luxury watch
box or bespoke leather goods. The references are therefore photographs of
the materials and objects. All images are from Wikimedia Commons, were
fetched through the Commons API on 2026-10-01, and were resized to at most
1600px at JPEG quality 70-80. Credits and licences are as stated on each
file page.

## Images

| File | Source | Credit / licence | What it shows |
|---|---|---|---|
| `leatherGrain-page.jpg` | https://commons.wikimedia.org/wiki/File:Black_Leather.jpg | Cbobdude, CC BY-SA 4.0 | Even, tight black pebble grain, the target for `--tokie-grain`. Neutral near-black, no brown cast. |
| `leatherGrain-panel.jpg` | https://commons.wikimedia.org/wiki/File:BLACK_LEATHER_TEXTURE_(7241544232).jpg | THOR (Flickr), CC BY 2.0 | Larger, creased full-grain with soft highlights: how leather catches light on a raised panel. |
| `stitching-panelEdge.jpg` | https://commons.wikimedia.org/wiki/File:RM_Williams_Kintore_Saddle_Stitch_shoes.jpg | Nick-D, CC BY-SA 4.0 | Hand saddle stitch running parallel to a leather edge in a creased channel. Source for the stitch-in-groove. |
| `stitching-switch-btnHardware.jpg` | https://commons.wikimedia.org/wiki/File:Leather_dog_collar_made_by_Les_cuirs_d%27Agathe_(DSC06406).jpg | Trougnouf (Benoit Brummer), CC BY 4.0 | Contrast saddle stitch about 3mm in from the edge, plus a metal buckle and D-ring. Hardware as the thing you operate. |
| `brushedGold-appBar-meter.jpg` | https://commons.wikimedia.org/wiki/File:Brushed_brass_paint_(Apollo_11)_interior.png | NASA / Smithsonian, CC0 | Satin brushed-brass surface with fine directional hairlines and low contrast. Source for `--tokie-brushed`. |
| `polishedGold-btn.jpg` | https://commons.wikimedia.org/wiki/File:Capuli_gold_pendant.jpg | Metropolitan Museum of Art, CC0 | Polished gold sheet: bright highlights, deep amber shadows, hard transitions. Source for `--tokie-polished`. |
| `polishedGold-readout-knob.jpg` | https://commons.wikimedia.org/wiki/File:Pair-case_watch_MET_DP168596.jpg | Thomas Tompion (maker), Metropolitan Museum, CC0 | Gilt watch movement and dial with engraved, mirror-polished gold. Shows polished gold as a watch's material, behind readouts and the knob crown. |
| `goldDeboss-panelHeader.jpg` | https://commons.wikimedia.org/wiki/File:Briefcase_of_a_bank_director_of_Midland_Bank_Ltd._made_of_black_cowhide_leather_around_1925_-_Font_in_gold_letter_embossing_-_Picture_001.jpg | Lupus in Saxonia, CC BY-SA 4.0 | "MIDLAND BANK LIMITED" in gold foil, struck in tracked serif capitals into black cowhide beside an edge stitch. The panel-title voice. |
| `goldDeboss-navBrand.jpg` | https://commons.wikimedia.org/wiki/File:Briefcase_of_a_bank_director_of_Midland_Bank_Ltd._made_of_black_cowhide_leather_around_1925_-_Font_in_gold_letter_embossing_-_Picture_002.jpg | Lupus in Saxonia, CC BY-SA 4.0 | The same foil lettering at a wider angle, with creased edge lines and stitching. The brand mark. |
| `giltTooling-modal.jpg` | https://commons.wikimedia.org/wiki/File:Gruel_and_Engelmann_-_Binding_for_a_Book_of_Hours_-_Walters_572167_-_Front_Closed.jpg | Gruel and Engelmann, Walters Art Museum, public domain | Gilt-tooled binding with gold fillet frames around a central panel. Source for the double gilt fillet under dialog and panel titles. Its ornament level is the ceiling, not the target. |
| `cornerHardware-card.jpg` | https://commons.wikimedia.org/wiki/File:Doctor%E2%80%99s_medical_case_02.jpg | Commons user (see file page), CC0 | Black leather case with polished gold corner protectors, clasp and a blind-debossed emblem. The overall "black leather + gold hardware" balance. |
| `blindEmboss-card.jpg` | https://commons.wikimedia.org/wiki/File:Black_jewelry_box_in_embossed_leather_imitation_2.jpg | W.carter, CC BY-SA 4.0 | Black jewellery box with blind-embossed scrollwork and a polished clasp. Tone-on-tone relief on black. |
| `linedTray-table-dropdown.jpg` | https://commons.wikimedia.org/wiki/File:Black_jewelry_box_in_embossed_leather_imitation_1.jpg | W.carter, CC BY-SA 4.0 | The same box open: stacked drawers and lined, divided trays. The recessed `.app-main` tray and table/list compartments. |

## Sampled palette

Sampled with ImageMagick 5-colour quantisation on the reference images.
Theme values are tuned from these for contrast.

| Material | Sampled | Theme |
|---|---|---|
| Black pebble leather | `#1E1E1E` `#262626` `#313131` | `--bg` `#0b0a09`, `--surface` `#151311`, `--surface-2` `#1d1a17` (darker, with grain lightening it back up) |
| Creased leather highlight | `#45454E` | panel top-edge highlight `rgba(255,240,210,.06)` |
| Brushed brass/gold | `#807C5E` `#9E9B70` `#C0B47E` `#C3BF94` | `--tokie-brushed` `#d8bc78` → `#bf9d55` → `#a9873f` (warmed towards gold) |
| Polished gold | `#EED284` `#BE9E54` `#8F7434` | `--tokie-polished` highlight `#f3d98f`, body `#d9b45c`, horizon `#7a5718` |
| Gilt dial / movement | `#D7B459` `#765C32` | `--accent` `#d6b25e`, readout numerals `#e9c977` |
| Gold foil lettering | (light on `#2C2C2C`) | `--tokie-foil` `#dcbc6d` |

## Typography identified

- Foil lettering on the briefcase and the binding: high-contrast serif
  capitals, widely tracked. Display stack is Didot / Bodoni (Didone),
  uppercase, 0.16-0.28em tracking.
- Luxury packaging and engraved plates often use a flared humanist sans
  (Optima-class). UI stack: Optima, Candara, then the system sans.
- Nothing is vendored. No OFL Didone was needed badly enough to ship one.

## Component mapping

| Component | Reference | Treatment |
|---|---|---|
| Page / `.app` | leatherGrain-page | Pebble-grain black leather. |
| `.panel`, `.card`, `.modal`, `.drawer` | leatherGrain-panel, stitching-panelEdge | Raised leather, saddle stitch 7px in, 10px radius, soft drop shadow. |
| `.panel-header`, `.modal-header`, headings | goldDeboss-*, giltTooling-modal | Gold-foil Didone caps, deboss shadow, double gilt fillet below. |
| `.app-bar` | stitching-panelEdge, brushedGold | Stitched leather lid strip on a brushed-gold hinge rail. |
| `.app-rail` | brushedGold, cornerHardware-card | Brushed-gold spine with polished screw heads. |
| `.app-main` | linedTray-table-dropdown | Recessed lined tray. |
| `.app-status` | brushedGold | Brushed-gold nameplate, engraved dark lettering. |
| `.btn-primary`, `.btn-go`, active segmented/pagination/badge | polishedGold-btn, cornerHardware-card | Polished mirror gold, engraved dark text. |
| `.btn` default / danger / success | stitching-switch-btnHardware | Leather key with gold bezel; oxblood / bottle-green enamelled leather. |
| `.input`, `.select`, `.textarea`, `.switch` track, `.meter`/`.progress` track | blindEmboss-card | Debossed (inset) leather. |
| `.switch` thumb, `.slider` thumb, `.knob` | polishedGold-readout-knob | Polished gold domes; fluted crown knob. |
| `.readout` | polishedGold-readout-knob | Black lacquer dial, applied gold Didone numerals, thin chapter ring. |
| `.table` head | goldDeboss-panelHeader | Foil caps over a 2px brushed-gold rule. |
| `.tooltip`, own `.message`, scribble strip | brushedGold | Brushed-gold plates with engraved text. |

## Gaps

No licence-clear screenshots of luxury *software* UIs (watch-maker
apps, Vertu phone UI, luxury car infotainment) were found. Table,
modal, toast, tabs, form-input, meter and switch treatments are
interpretations of the physical materials, not copies of a reference UI.
