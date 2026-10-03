# Windows 95

> Beveled 3D gray — classic system dialog chrome on teal.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The **Windows 95/98 desktop**: a teal backdrop, battleship-grey controls,
and the 3D bevel language that made every control look physically pressable
on a 256-colour display. The target is a system dialog, not a nostalgia
poster.

## Core values

1. **The bevel is the entire system.** Light on the top-left, dark on the
   bottom-right, inverted while pressed. Every raised thing uses it; every
   sunken thing (inputs, the content well) uses it reversed. Get this wrong
   and nothing else matters.
2. **Zero radius, everywhere.** `--radius: 0`. There were no rounded
   corners.
3. **A strictly limited palette.** Grey `#c0c0c0`, navy `#000080`, teal
   `#008080`, plus the 16-colour VGA set. No intermediate tints.
4. **Text is black on grey.** Filled controls use white on navy — never the
   page background as a foreground, which is what `--on-*` exists to
   prevent here.
5. **Focus is a dotted rectangle.** Marching-ants, not a glow. Era-accurate
   *and* accessible.

## Signature details

- Modal headers take the navy→blue title-bar gradient with white bold text.
- The content well is *sunken* (`#808080 #ffffff #ffffff #808080` plus an
  inner black line); the status strip is *raised*. The shell itself obeys
  the 3D language, not just the controls.
- Tables draw a full 1px grid — Explorer's details view, not a modern
  borderless list.

## Icons

`themes/windows95/icons.svg` redraws the whole core set (178/178, 182
`<symbol>`s) in the chunky, low-detail pixel-art style of the real 95
icon set. Style rules:

- 24×24 grid, outline only (no fills), stroke from the theme's heavy
  `--icon-stroke-width: 2.6`, so details stay at least ~3.5 units apart.
- Hard corners everywhere: `stroke-linecap: square` and
  `stroke-linejoin: miter` on every shape (per element, or on a wrapping
  `<g>` in the last batch), overriding the generic sprite's rounded
  default.
- Straight segments only. Circles become octagons (vertices at 22.5° +
  k·45°), ellipses become six-sided lozenges, curves (moon, clouds,
  rainbow, coins) become polylines through octagon vertices. The settings
  glyph is a plus of tabs around a square, not a gear: the same low-res
  simplification the real set used at 16×16/32×32.
- `currentColor` only, so icons follow text colour and every state.
- Shared geometry: from "Round 2" on, the shapes are the same as
  `winamp-classic`, `winxp-luna` and `wmp11`; only the rendering differs.
  The last 47 ids ("Round 3", core-set top-up) were drawn by a small
  generator that reproduces the Round 2 renderers exactly.
  `icon-player-play` copies this theme's `icon-play`.

## Layout

The app shell becomes a **desktop window**: the teal backdrop shows at the
edges, a 1.6rem gradient title bar sits on top, the content is a sunken
well, and the status bar is raised. Switching to this theme visibly boxes
the app up.

## Known compromise

MS Sans Serif is not a web font and is absent from modern systems, so the
stack falls back to Tahoma — its closest ubiquitous relative. No
openly-licensed pixel face is vendored yet.

## Tell-tales of an inauthentic result

- Uniform 1px borders instead of two-tone bevels → flat-design cosplay.
- Any rounded corner or drop shadow.
- Buttons that don't invert their bevel on `:active`.
- Anti-aliased, modern-weight type in the title bar.

## Don'ts

- **No radius.** `--radius: 0`, `--badge-radius: 0`, `--progress-radius: 0`. Not "just 2px".
- **No drop shadow, no blur, no glow.** Depth is the two-tone bevel only.
- **No tints or in-between greys.** Stay on `#c0c0c0` / `#dfdfdf` / `#808080` / white / black plus navy and teal.
- **No flat 1px border in place of the bevel**, and no bevel that fails to invert on `:active`.
- **No transitions or fades.** Windows 95 repainted instantly.
- **No modern-weight, anti-aliased title-bar type**, and no Segoe UI in place of Tahoma/MS Sans Serif when a system copy is available.

## Typography

`--font` is `Tahoma, "MS Sans Serif", "Segoe UI", sans-serif`; `--font-mono` is `"Courier New", Consolas, monospace`. **Nothing is vendored** — all system fonts. The authentic face (MS Sans Serif, a bitmap font) is not a web font, so on most machines Tahoma is what renders, a close relative rather than the real thing. No capture in `references/windows95/` was measured for face; the claim rests on RESEARCH-level knowledge. No pixel face is vendored yet.

## Contrast honesty

- **`--bg` teal is lifted from the reference.** `references/windows95/RESEARCH.md` records the desktop as `#008080`. Shipped is `#008282` (2/255 more green and blue). Black text on `#008080` is 4.40:1; on `#008282` it is 4.52:1, just over the 4.5:1 floor. The desktop never carried body text on the real system, so the shift is invisible in practice, but it is a deviation.
- **AAA is not met on the teal pair, on purpose.** `--text` on `--bg` is ~4.5:1, below the 7:1 AAA target. Every readable surface in the real OS was the grey dialog (`--surface` `#c0c0c0`, black text 11.54:1), so the teal pair is decorative by construction. Brightening the teal further would be the inauthentic fix.
- Navy `#000080` under white is 16.01:1; navy on the teal desktop is 3.44:1 (chrome only, no text).
- `--muted` `#3a3a3a` is 6.2:1 on grey and 4.9:1 on the planner/notification tints, but fails on teal: text straight on the desktop (marketing hero, untinted bands) takes black for muted, link and trend text.
- `--success` `#008000` and `--warning` `#808000` are lamp/fill colours only; text uses `--success-text` `#004d00` and `--warning-text` `#4d4d00`.

## Reference status

`references/windows95/` has 9 captures plus `RESEARCH.md`: desktop/Notepad, My Computer/Paint/WordPad/Calc windows, a German Explorer/Media Player shot, a DLL icon grid, an icon/cursor sheet, FreeCell (`freecell_windows_95.avif`), a Start-menu shot (`htg_windows_95.avif`), the Internet icon close-up (`win95_the_internet_icon.avif`) and the splash screen (`windows_95_splash_screen.avif`) — per the audit in `RESEARCH.md`. They back the grey/navy/teal palette, the two-tone bevel and the dotted focus rectangle. `RESEARCH.md` notes the hexes as `#c0c0c0`, `#000080`, `#008080`.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

## Window chrome and the newer components (2026-09 pass)

- **Title bar:** navy with a bold white caption and the three bevelled
  caption buttons (minimize and maximize together, close set apart), one
  inline SVG; the active nav item is a grey raised block.
- **Panels are child windows:** every `.panel-header` is a navy caption
  bar (with light tints for muted and state text on it).
- **Tabs** are raised 95 tabs; the selected one lifts and joins its page.
- **Progress** is the segmented navy block bar in a sunken well.
- **Status bar** items sit in sunken fields.
- **Mixing console:** sunken bay, raised strips, keys that sink and light
  when on, a sunken trackbar groove with a raised grey thumb, and sunken
  white scribble and EQ fields.
- Icon buttons are square bevels, not circles.

## v5 layout

- **Tiers.** Desktop (901–1800px) is the v4 window unchanged. Tablet
  (481–900px) keeps the navy title bar; the bar wraps to two lines (brand
  and actions, then the scrolling nav) and the three caption buttons pin
  to the first line's right end instead of floating over both. Mobile
  (≤480px) drops the decorative caption buttons, so the brand gets their
  52px. No rail on any tier.
- **Nesting.** Only the outermost surface is a window with a navy caption.
  A panel inside a panel, card, dialog or drawer becomes a group box: a
  plain bold label over an etched grey/white rule. Controls in a caption
  bar (search field, select) keep the dialog's own colours, and
  `.btn-min`/`.btn-max`/`.btn-close` on a title bar are grey bevelled
  squares with black glyphs (min and max touch, close 2px apart).
- **XL gutter art.** The teal desktop carries on beside the window, with a
  column of desktop icons (My Computer, a folder, the Recycle Bin) at the
  left and Network Neighborhood at the right, drawn in teal one step off
  `--bg` (about 1.2:1). Still.
