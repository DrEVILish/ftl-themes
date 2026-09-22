# Theme backlog

Themes not yet authored, in the order recommended for building them
(later entries reuse shapes established by earlier ones, so working in
order minimizes repeated effort). See `docs/authoring-a-theme.md` for the
authoring workflow. Each entry names the reference to design against.

## Batch 2 — requested by name, not yet authored

1. ~~**Windows XP Luna** (blue)~~ — done, see `themes/winxp-luna`.
   **Royale**, **Olive**, and **Silver** are still open as cheap
   palette-only follow-ons (same chrome shape, different token values),
   plus the later **Royale Noir**/black variant if wanted.
2. **Windows 7 Aero** — glass blur, glossy taskbar, more restrained gloss
   than XP; distinct enough from Luna to warrant its own component
   overrides (blur/translucency via `backdrop-filter`, not just gradients).
3. **Barbie** — hot pink, gloss, heavily rounded, y2k-plastic; a good
   "maximalist gloss" companion/contrast to Aqua.
4. **Alienware** — matte black, angular (not rounded — contrast with
   Aqua/Barbie), alien-head accent color, restrained RGB-adjacent glow
   (reuse the TRON glow technique, angular via the same `clip-path`
   corner-cut trick as TRON's buttons).
5. **Weyland-Yutani** — Alien-franchise corporate/industrial: utilitarian
   stencil type, amber CRT readouts, hazard yellow/black striping on
   danger states specifically (not the whole palette).
6. **Material** — Google Material Design: elevation shadows (multiple
   shadow layers by "level", not one flat `box-shadow`), bold flat color,
   ripple-style focus ring animation (opt-in per motion rules).
7. **Ubuntu** — Ambiance: aubergine/orange, Ubuntu font (or a close
   fallback stack if not vendoring the actual font), rounded window
   corners.
8. **Skeuomorphism (general)** — leather/brushed-metal/stitching textures,
   heavy drop shadows; a broader, less-branded companion to Aqua.
9. **iOS — two entries, see open question below.**
10. **Hot Wheels** — racing orange/flame, checkered-flag motif (as a
    repeating background pattern), bold condensed type.
11. **Coca-Cola Classic** — red/white, Spencerian-script accent font for
    headings only (never body text — legibility), glass-bottle curve
    motif on panel corners.
12. **Cassette Futurism** — 2001/Alien-console retro-futurism: beige
    plastic, LED-segment numeric displays (`--ftl-font-mono` + a
    seven-segment-style font if available), chunky physical-switch
    skeuomorphism reusing the `.ftl-switch` component with a toggle-switch
    look instead of a pill.

### Open question: iOS era

Skeuomorphic iOS (iOS 6: glossy buttons, textures, drop shadows) and
modern iOS (iOS 17: flat colors, frosted-glass blur, SF fonts) are visually
incompatible as a single theme. Recommend two catalog entries —
`ios-skeuomorphic` (grouped with the Skeuomorphism batch) and `ios-modern`
(grouped with Material/Ubuntu, sharing the flat-design shape) — pending
the user confirming that split before either is authored.

## Font vendoring (affects existing themes)

`windows95` names MS Sans Serif and `tron` names Eurostile; neither is
web-available, so both silently fall back and don't look like their
reference on a real machine. Vendor an openly-licensed substitute into
`assets/fonts/` with an `@font-face` block, following the pattern the LCARS
chrome now uses (`themes/lcars/chrome.css`) — note that `scripts/build.sh`
rewrites relative asset URLs for the `dist/` bundles, so use
`url("assets/…")` in the theme source. Candidate substitutes: a pixel/bitmap
sans for `windows95`, a squarish grotesque (e.g. Michroma, Saira Condensed)
for `tron`.

## Batch 3 — suggested additions (not committed scope)

- **Amiga Workbench** / **BeOS** — another skeuomorphic-OS pairing, cheap
  alongside Windows 95/Aqua once that bevel/gloss vocabulary exists.
- **Commodore 64 / Teletext (Ceefax)** — chunky 8-color text-mode CRT;
  distinct from Matrix by being multi-color, not green-only.
- **Vaporwave / Outrun Synthwave** — pink/purple grid horizon, chrome
  text; distinct from TRON by leaning gradient/glow over sharp lines.
- **PlayStation XMB** — horizontal icon strip, blue gradient, PS3-era.
- **Xbox 360 Blades** — green/black panel dashboard.
- **Nokia 3310 / dumbphone** — 1-bit green LCD, huge pixel font; a good
  stress test of the contract at its most minimal (no gradients, no
  shadows, no font weights beyond one).
- **NASA Mission Control** — Apollo-era analog-gauge + CRT green;
  distinct from Matrix/Weyland-Yutani by being optimistic control-room,
  not horror/dystopia.
- **Bloomberg Terminal** — black background, dense amber/orange
  monospace data grid; a good "extreme density" stress test for
  `.ftl-table`.
- **Braun / Dieter Rams minimalism** — cream/orange, geometric, large
  whitespace; a restraint counterpoint to the glow-heavy themes.
- **Cyberpunk Netrunner** — magenta/cyan on black with glitch-line
  accents; distinct from TRON/Matrix/Vaporwave by leaning glitch/noise
  rather than clean grid or cascade.
