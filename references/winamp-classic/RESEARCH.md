# winamp-classic — visual reference notes

Outsider read: Green LCD readout + spectrum on near-black, bevelled grey buttons, yellow EQ faders, playlist editor.

Capture targets: Main window; equalizer; playlist editor.

Sources: Wikipedia Winamp; Classic Skins wiki.

Use side-by-side with example.html; local captures are copyrighted originals — this file is the textual checklist.

Audit 2026-09-26: all 3 kept — WinAmp_5.9.2 (Vista-glass skin, main+EQ+playlist), ddbr1i4 (Classic Modern lite skin, full stack), winamp-classic-screenshot.avif. Pure UI screenshots, zero people, on-target.

## Sampled colours (2026-10-09)

`WinAmp_5.9.2,_Windows_10.png` (267×422, lossless PNG) shows the classic
**base skin** (gold-ridged title bars, silver transport keys, green LCD and
playlist). The real base skin is 275px wide, so this capture is slightly
rescaled and edges are blended: flat areas below are reliable, 1px edges
are indicative. Sampled with ImageMagick (`-crop WxH+X+Y -colors 4
histogram` for areas, `-crop 1x1+X+Y` for single pixels).

| What | Where | Sampled | Theme |
|---|---|---|---|
| Chassis face | areas 60×6+100+108 and 250×12+8+120 | `#313151`–`#32324f` (dominant) | `--surface #32324f` |
| Chassis shadow | 20×40+3+150 | `#1b1b2b` | `--bg`, `--hairline` and dark bevels (were `#1c1c1c`) |
| Chassis mid / highlight | title strip 40×6+110+3; 60×6+100+108 | `#484861`; `#686883` | `--surface-2`, `--border` |
| Stripes beside the title | 250×4+8+12 | `#525266`, `#2f2f4b`, `#161628` | backdrop stripes `#3c3c50` / `#2f2f4b` |
| Title-bar ridges | 60×3+20+7; 100×3+20+5 | gold `#c7b070`, highlight `#ffefa6` | not drawn (they would sit behind nav text) |
| Stop key | column x=84, y=85–101; row y=95 | `#f0ffff` top highlight, `#deeff1` face, `#d2dfe7` foot, `#8e9cad` then `#414f61` lower edge; glyph `#97a8b9` | `--btn-bg`, `.btn` border, `--btn-shadow` |
| Playlist | 200×10+20+260 | black ground, green text (`#00ca00` after rescaling) | `--message-*`, inputs |

Documented, not sampled: the base skin's playlist colours from
[webamp's `baseSkin.json`](https://github.com/captbaritone/webamp/blob/master/packages/webamp/js/baseSkin.json)
(`normal #00FF00`, `current #FFFFFF`, `normalbg #000000`, `selectedbg
#0000FF`, font Arial). The theme takes `selectedbg` for `--row-selected-bg`.

Derived, not measured: the 1px `#8e9cad` shadow standing in for the key's
two-pixel lower edge, the pressed key (the edge mirrored), the default
button drawn as the LCD (green on black), and mapping the old neutral greys
onto the nearest sampled indigo (`#2a2a2a` → `#2f2f4b`, `#454545` →
`#3c3c50`, `#a8a8a8` → `#8e9cad`).
