# proseries — visual reference notes

The ProSeries theme imitates the touch-screen GUI of a Pro Series live
sound console (Generation-II era, 2010s): a navy-violet desk, bright blue
channel strips, lavender detail panels, a black title bar with the scene
name in yellow, grey bevelled buttons and colour-coded function keys.
Design reference only, 2026-10-07. Three images supplied by the project
owner are kept here. A larger private asset extract was used for visual
study only and is **not** in this repository; nothing from it (images,
fonts, logos) ships in the theme, which is drawn entirely in CSS.

## Primary direction

Input channel bank (8 strips) with gain trim, two dynamics sections with
transfer-curve thumbnails, insert, colour name tag, EQ, an 8-row aux send
block, solo-in-place/stereo/monitor keys, pan, mute, B, fader and meter;
a selected-channel/master column on the right; an effects rack of
faceplates over a blue "assignable controls" panel; the patching grid.

## Images

| File | Source / credit | What it shows |
|---|---|---|
| `inputChannels-gainTrim-dynamics-auxSends-faders.webp` | Supplied by the project owner (photo of a console screen, marketplace listing watermark) | The input channel screen: 8 strips, home bar, scene name, tap tempo, copy/paste/preset buttons, master column |
| `effectsRack-matrixMixer-chamberReverb-channelSidebar.webp` | Supplied by the project owner (screen capture) | The Effects page: rack with matrix mixer, chamber reverb, stereo chorus ×2, dynamic EQ, dual delay ×2, 8-channel dynamics; the channel sidebar (direct output, safes, filters, gain trim, stage box, delay, processing order) |
| `patching-ioTiles-inputChannelGrid.webp` | Supplied by the project owner (photo of a console screen) | Patching: From / To tabs, I/O device blocks with patch tiles, input channel groups of 8 |

## Sampled palette

| Role | Sampled | Theme |
|---|---|---|
| Desk backdrop | `#3d4778` (edges `#191a25`) | `--bg #353f72`, gutters darker |
| Channel strip | `#4379cf`–`#6290ce` | `--strip-bg` gradient `#3d64b4 → #6d93d8` |
| Detail panel | `#6b77aa`, sections `#a2a8ca` | `--surface #5d6aa3`, `--surface-2 #a4aacb` |
| Title bar | `#010103` | `--app-bar-bg #000` |
| Scene name | `#f1eb5b` | `--ps-scene #f1eb5b` |
| Selected channel header | green `#3d915c → #b3ffd2`, yellow tag `#e8d23a` | `--accent` yellow tag, `--success` green |
| Mute | `#dc673c` | `--key-mute #e8642c` |
| Solo | olive `#a8902a` | `--key-solo #c9a636` |
| Dynamics knob | purple `#493178` | `--knob-color` purple on dynamics |
| Pan knob | orange `#9c3d14` | `--ps-pan #c95a26` |

## Typography

Bold humanist sans throughout (the console uses Bitstream Vera Sans Bold).
The theme names `"Bitstream Vera Sans", "DejaVu Sans", Verdana` — free,
commonly installed faces — and vendors nothing.

## Component mapping

| Component | Reference | Treatment |
|---|---|---|
| `.app-bar` | Home bar | Black bar, grey "home" tab, scene field, status, tap tempo |
| `.mixer` / `.strip` | Input channels | Blue gradient strips, dark dividers, black send block |
| `.key` | 48V, TLK, ø, LNK, SIS, ST, MON, AFL, MUTE, SOLO | Small bevelled keys, each lit in its own colour |
| `.knob` | Gain trim, dynamics, pan | Black cap with white pointer; purple and orange caps by role |
| `.fader` | Channel fader | Long slot, grey ribbed cap, dB scale |
| `.rack` / `.rack-unit` | Effects page | Flight-case rack, brass rails, faceplates by unit |
| `.assignable` | Under every effect | Blue panel of 8 knobs with soft-key squares |
| `.geq` | Stereo GEQ | Grey faceplate, black slider slots in 8 groups |
| `.patchbay` | Patching | Device blocks of green / yellow / grey patch tiles |
| `.panel` / sidebar | Channel detail | Lavender sections with bold blue headings |

## Gaps

- No openly licensed photos exist; three owner-supplied images only.
- The console's splash screens and logos are trademarks and are not drawn;
  the splash is a generic "ProSeries" wordmark on a dark-blue sky.
- The console has 16 channel colours; the library has 6 per-user colours.
