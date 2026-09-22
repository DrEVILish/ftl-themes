# Theme backlog

Themes not yet authored, in the order recommended for building them
(later entries reuse shapes established by earlier ones, so working in
order minimizes repeated effort). See `docs/authoring-a-theme.md` for the
authoring workflow. Each entry names the reference to design against.

## Batch 2 — requested by name

1. ~~**Windows XP Luna** (blue)~~ — shipped as `winxp-luna`. **Royale**,
   **Olive**, and **Silver** remain cheap palette-only follow-ons (same
   chrome shape, different token values), plus the later **Royale
   Noir**/black variant if wanted.
2. ~~**Windows 7 Aero**~~ — shipped as `win7-aero` (glass blur via
   `backdrop-filter`, distinct from Luna's flat gloss).
3. ~~**Barbie**~~ — shipped as `barbie`.
4. ~~**Alienware**~~ — shipped as `alienware` (matte black, angular
   `clip-path` cuts, AlienFX cyan glow).
5. **Weyland-Yutani** — Alien-franchise corporate/industrial: utilitarian
   stencil type, amber CRT readouts, hazard yellow/black striping on
   danger states specifically (not the whole palette).
6. ~~**Material**~~ — shipped as `material` (elevation shadow stack,
   flat color, underlined text fields).
7. **Ubuntu** — Ambiance: aubergine/orange, Ubuntu font (or a close
   fallback stack if not vendoring the actual font), rounded window
   corners.
8. **Skeuomorphism (general)** — leather/brushed-metal/stitching textures,
   heavy drop shadows; a broader, less-branded companion to Aqua.
9. **iOS — two entries, see open question below.**
10. ~~**Hot Wheels**~~ — shipped as `hot-wheels`.
11. **Coca-Cola Classic** — red/white, Spencerian-script accent font for
    headings only (never body text — legibility), glass-bottle curve
    motif on panel corners.
12. **Cassette Futurism** — 2001/Alien-console retro-futurism: beige
    plastic, LED-segment numeric displays (`--ftl-font-mono` + a
    seven-segment-style font if available), chunky physical-switch
    skeuomorphism reusing the `.ftl-switch` component with a toggle-switch
    look instead of a pill.
13. ~~**Vaporwave / Outrun Synthwave**~~ (promoted from Batch 3) — shipped
    as `vaporwave` (magenta/cyan gradient chrome text on deep purple,
    distinct from `tron`'s clean grid by leaning glow/gradient).
14. ~~**Bloomberg Terminal**~~ (promoted from Batch 3) — shipped as
    `bloomberg` (black/amber monospace, `--ftl-density: 0.7` as an
    intentional extreme-density stress test for `.ftl-table`).

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
- **PlayStation XMB** — horizontal icon strip, blue gradient, PS3-era.
- **Xbox 360 Blades** — green/black panel dashboard.
- **Nokia 3310 / dumbphone** — 1-bit green LCD, huge pixel font; a good
  stress test of the contract at its most minimal (no gradients, no
  shadows, no font weights beyond one).
- **NASA Mission Control** — Apollo-era analog-gauge + CRT green;
  distinct from Matrix/Weyland-Yutani by being optimistic control-room,
  not horror/dystopia.
- **Braun / Dieter Rams minimalism** — cream/orange, geometric, large
  whitespace; a restraint counterpoint to the glow-heavy themes.
- **Cyberpunk Netrunner** — magenta/cyan on black with glitch-line
  accents; distinct from TRON/Matrix/`vaporwave` by leaning glitch/noise
  rather than clean grid or gradient glow.
