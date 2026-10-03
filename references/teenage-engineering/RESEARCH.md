# Teenage Engineering: research notes

The theme is *inspired by* the Teenage Engineering OP-1 (2011), OP-1 field
(2022) and OP-Z (2018): an off-white anodised-aluminium body, rounded
light-grey keys, a small dark display window with playful vector screen art,
and the four colour-coded encoders (blue, green, white, orange) that every
screen colours its parameters by. No company logos or wordmarks are used in
the theme. Where a photo shows printing on the hardware or packaging (the
model name on the case), it stays in the reference only.

All images are from Wikimedia Commons. They were fetched through the Commons
API on 2026-10-02 at 1280px, resized to at most 1200px and saved as WebP
(quality 78), each under 400 KB. Credits and licences are as stated on each
file page. `appBar-display-encoderRow.webp` was cropped to drop the
manufacturer's printed box behind the device.

## Images

| File | Source | Credit / licence | What it shows |
|---|---|---|---|
| `hardwareBody-encoderRow-btnGrid.webp` | https://commons.wikimedia.org/wiki/File:OP-1,_portable_synthesizer_and_sequencer_-_Jun_21,_2011.jpg | Shuichi KODAMA, CC BY 2.0 | The whole OP-1 from above at an angle: the aluminium frame, the speaker grille top left, the volume knob, the display, the four encoders and the key grid. Source for the body, the frame gaps between keys and the shell layout. |
| `appBar-display-encoderRow.webp` | https://commons.wikimedia.org/wiki/File:Teenage_Engineering_OP-1_Synthesizer_at_SMEM_Playroom.jpg | 1904.CC, CC BY 4.0 (cropped) | Straight-on view of the top row: grille, display window with a thin red line graph, then blue / green / white / orange encoders each sitting in its own square key, then the mode keys with line icons in colour. The bar, the rail grille and the four-colour accent order. |
| `displayArt-encoderRow-iconBtn.webp` | https://commons.wikimedia.org/wiki/File:OP-1_Sequencer_Concept.png | Isaac Henry, CC BY 2.0 | **A fan concept render, not the hardware or its firmware.** A flat vector OP-1 face: used only for clean encoder colours, key proportions and the silkscreen icon style. Its on-screen sequencer art is the author's own idea and is not presented as the real UI. |
| `display-tapeReadout-knob.webp` | https://commons.wikimedia.org/wiki/File:OP-1_Synth.jpg | uploader "OP-1 Synth", CC BY-SA 3.0 | Close-up of the display: the tape screen's two reels as thin white and blue line art on black, a `0:00:00` time readout and a boxed track number. Source for `.readout` and the display window's line-art style. |
| `display-transport.webp` | https://commons.wikimedia.org/wiki/File:Teenage_Engineering_OP-1_in_blue_-_Pulsn_-_engineroom_14_-_2013-03-06_08.39.25_(by_GeschnittenBrot).jpg | GeschnittenBrot, CC BY-SA 2.0 | The tape screen lit at a gig: reels, a red playhead line and the time counter, with the transport keys beside it. The `.transport` and status-strip treatment. |
| `display-meter-readout.webp` | https://commons.wikimedia.org/wiki/File:Teenage_Engineering_OP-1%27s_ultra_punchy_compressor.jpg | j bizzie, CC BY 2.0 | The compressor screen: a boxer drawn in teal and red outline, "PUNCH 45 / POWER 84 / ROUNDS 19" in big thin numerals, and a short white bar-graph meter. Source for the limited display colours, `.meter` segments and readout numerals. |
| `knob-encoderCap.webp` | https://commons.wikimedia.org/wiki/File:Teenage_Engineering_OP-1_with_FM_radio_rod_antenna_-_Rafa%C3%ABl_Reverdy-Carrasco%27s_musique_maison_(2016-03-02_10.17.50_by_Rafa%C3%ABl_Reverdy-Carrasco_@Flickr_33385036518).jpg | Rafaël Reverdy-Carrasco, CC BY 2.0 | Encoder caps in profile: short coloured cylinders with a flat top and a single slot across it, on a raised collar. Source for the `.knob` cap, its side shadow and the pointer slot. |
| `knob-btnGrid-darkBody.webp` | https://commons.wikimedia.org/wiki/File:OP-Z_in_da_house_(32659021107).jpg | Audiotecna Música, CC0 | OP-Z from above: dark grey body, round keys, and four encoders in green / blue / yellow / red inside thin circular wells with a cross-slot. The OP-Z's alternative encoder palette (yellow, red) that extends the chart series. |
| `knob-rail-darkBody.webp` | https://commons.wikimedia.org/wiki/File:OP-Z_in_da_house_(40635130363).jpg | Audiotecna Música, CC0 | The OP-Z standing vertically: the encoder wells stacked down one side like a rail, tiny silkscreen icons beside each key. |
| `iconStrip-badge-colourDots.webp` | https://commons.wikimedia.org/wiki/File:OP-Z_and_friends_(48873495257).jpg | Audiotecna Música, CC0 | The OP-Z printed guide and app: rows of colour dots keyed to the encoders, thin line icons, tight grotesque text. Source for the tab colour dots, badges and the silkscreen label voice. |

## Sampled palette

Sampled with ImageMagick (6px averages and 6-8 colour quantisation). The
photos are warm and unevenly lit, so the theme tunes toward the clean
concept-render values and checks them for contrast.

| Material | Concept render | Photos | Theme |
|---|---|---|---|
| Blue encoder | `#0098D4` | `#4DA9DF` | `--te-blue` `#0a8fd0` (fill), `--accent-text` `#00669a` |
| Green encoder | `#01BB00` | `#53B76C` | `--te-green` `#2a9d2a` |
| White encoder | `#FFFFFF` | `#E5E8E6` | `--te-white` `#f7f8f8` cap, `#26282a` where it must read on the body |
| Orange encoder | `#FE4E00` | `#C9754B` | `--te-orange` `#f25a12`, `--flare` |
| Body / frame between keys | `#C3C9C9` | `#C0BFBB` | `--bg` `#c4c9cb` |
| Key faces | `#DAE4E5` `#DEE8E9` | `#D6D9DD` `#D8DADE` | `--surface` `#e8ebec`, `--surface-2` `#dadfe1` |
| Black note dots | `#1E1E1E` `#121212` | `#2B2C29` | `--te-dot` `#1d1f21` (close button, menu highlight) |
| Display glass | `#000000` | `#22242A` `#100E11` | `--te-screen` `#131416` |
| Display glyphs | — | `#F8F8F4` white, `#43CEBF` teal, `#6E8ECC` blue, `#925E73`/red | `--te-glyph` `#f2f2ee`, `--te-teal` `#43cebf` |
| OP-Z extra encoders | — | yellow, red (OP-Z caps) | chart series 5-6 (pink `#d8408f`, ochre `#b48600`, tuned for the validator) |

## Typography identified

- Silkscreen and packaging type is a tight, neo-grotesque sans (the
  manufacturer uses its own faces; not free). The theme uses the system
  grotesque stack (Helvetica Neue, Helvetica, Arial / Liberation Sans) with
  slightly negative tracking. Nothing is vendored.
- Hardware labels are tiny: single words or symbols ("COM", "M1", "shift"),
  often lower case. Panel and table heads follow that: 0.7rem, medium
  weight, tracked, muted.
- The display uses thin, wide numerals and a small monospaced/pixel-ish
  face. The theme puts `--font-mono` (SF Mono / JetBrains Mono / Menlo /
  DejaVu Sans Mono) on every display surface.

## Component mapping

| Component | Reference | Treatment |
|---|---|---|
| Page, XL gutters | hardwareBody-encoderRow-btnGrid | Bead-blasted aluminium `--bg`; the gutters continue the key grid and a speaker grille, embossed a few percent off `--bg`. |
| `.app-rail` | appBar-display-encoderRow, knob-rail-darkBody | A key-face column: the speaker dot grille on top, the four encoder dots below it. |
| `.app-bar` | appBar-display-encoderRow | A key-face strip; the brand sits in a small dark display window. |
| `.app-status` | display-transport | A dark display strip with mono glyphs in white and teal. |
| `.panel`, `.card`, `.modal` | hardwareBody-encoderRow-btnGrid | Rounded light keys separated by the aluminium frame, a 2px key-side shadow. |
| `.btn` | appBar-display-encoderRow | Light key; primary is the blue encoder colour, GO is the orange record key. |
| `.btn-close` | hardwareBody-encoderRow-btnGrid | One of the black round note dots with a white ×. |
| `.knob` | knob-encoderCap, knob-btnGrid-darkBody | Flat coloured cylinder cap with a slot, in a recessed collar; the four band colours are the encoders. |
| `.tab`, `.segmented`, slider thumbs | iconStrip-badge-colourDots | Each position carries its encoder colour (blue, green, white, orange, repeating). |
| `.readout`, `.meter`, `.scribble`, `pre`, `.chart`, `.toast` | display-tapeReadout-knob, display-meter-readout | The dark display window: black glass, white and teal mono glyphs, encoder-coloured series. |
| `.dropdown`, `.context-menu` hover | display-meter-readout | The highlighted item is a black display bar with white text. |
| `.badge`, `.tag` | iconStrip-badge-colourDots | Small key-face pills with a colour dot. |

## Gaps (missing references)

No licence-clear photos or screenshots were found for:

- The OP-1 field (2022) itself. Its body and encoders match the OP-1 closely
  enough that the OP-1 photos stand in.
- On-screen menus, lists, dialogs and text entry (the OP-1 has almost none).
  Tables, forms, menus, modals, toasts and tooltips are interpretations of
  the hardware and screen language, not copies of a real screen.
- The companion app UIs, beyond the partial view in
  `iconStrip-badge-colourDots.webp`.
