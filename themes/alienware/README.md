# Alienware

> Matte black gaming chrome — angular cuts, AlienFX cyan glow.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

**Alienware's gaming-rig identity**: matte black chassis, cut/angular
edges instead of curves, and a single AlienFX accent color glowing along
one edge — the light strip every Alienware machine has. Aggressive but
controlled, not a rainbow of RGB.

## Core values

1. **Angles, never curves.** `--radius: 0.2rem` and every major
   surface has its corners cut with `clip-path`, not rounded. This is the
   catalog's deliberate contrast point against `aqua`/`barbie`'s gloss and
   curves — a rounded Alienware is a contradiction.
2. **One glow, not many.** The AlienFX cyan (`--accent`) is the only
   thing allowed to glow. A version of this theme with every element
   lit up in a different color has missed the "one light strip" idea.
3. **Matte black, not gloss.** Flat fills, no gradients on the base chrome
   — the shine belongs to `aqua`/`winxp-luna`, not here.
4. **Uppercase, tracked-out headings.** The gamer-hardware branding voice:
   wide letter-spacing, all caps, never soft title case.
5. **The rail is the light strip.** The app shell's decorative rail is a
   thin lit cyan strip (light cyan `#b6f5ff` fading through `--accent` to
   a deeper `#0090b3`, with a multi-layer cyan bloom) — the physical
   AlienFX edge light, not a navigation column. Purple (`--accent-2`)
   does not appear on the rail; it is limited to the active-row marker
   and `--flare`. (An earlier version of this README called the rail
   cyan-to-purple; the CSS never did that, and no capture attests it.)

## Signature details

- Buttons and panels have their corners angle-cut via `clip-path`, the
  same technique `tron` uses; focus indication uses a `drop-shadow`
  filter instead of the clipped standard outline, for the same reason
  tron's does — `clip-path` also clips `:focus-visible`'s outline.
- The app bar carries a 2px lit cyan rule, not a full gradient fill —
  restraint, not a wash of color.
- Selected table rows get a faint cyan tint; the active-row marker uses
  the secondary purple, so the two states stay visually distinct.

## Layout

The shell becomes a **matte black gaming chassis**: a thin lit-edge bar,
a narrow glowing AlienFX rail down the side, and a flush black content
well — hardware, not a HUD.

## Tell-tales of an inauthentic result

- Rounded corners anywhere on chrome.
- Multiple glow colors competing for attention.
- A gradient or gloss fill on the base button/panel chrome.
- Soft, title-case headings instead of tracked-out uppercase.

## Don'ts

- **No rounded chrome.** Corners are cut with `clip-path`; `--radius` is `0.2rem`.
- **No second glowing colour.** Cyan is the one light; purple is a quiet secondary (row marker), never a glow.
- **No gradient or gloss on base buttons/panels.**
- **No soft title-case headings**; uppercase, tracked out.
- **No purple on the rail** (see Core values).

## Typography

- **Headings:** Orbitron Bold (700/800), **vendored** (`assets/fonts/Orbitron-Bold.woff2`, SIL OFL, `assets/fonts/NOTICE.md`), uppercase and tracked. It is a stand-in for Alienware's angular brand lettering, not the actual logo face.
- **Body:** `--font` is `"Segoe UI", Arial, sans-serif` (system, **not vendored**); `--font-mono` is `Consolas, monospace`. Only headings get the display face, so body copy looks like generic Windows on purpose.
- The reference captures (`references/alienware/`) are mostly third-party icon/desktop skins, so no capture there confirms a face; the choice rests on brand knowledge.

## Contrast honesty

- **Cyan on black is safe:** `--accent` `#00d4ff` is 11.17:1 on `--bg`, 10.19:1 on `--surface`; `--on-accent` `#001318` is 10.72:1 on it. The hex itself is the theme's, not measured (`RESEARCH.md` records no value).
- **Purple is the weak one:** `--accent-2` `#7a5cff` is 4.52:1 on `--bg` but 4.13:1 on `--surface`, so it is used only for the active-row marker and `--flare` (non-text), never for copy.
- **Danger text lifted:** `--danger` `#ff3b5c` is 5.68:1 on `--bg`; `--danger-text` `#ff6b84` (6.61:1 on `--surface`) is the small-copy variant.
- **Muted:** `#8a8a92` is 5.27:1 on `--surface` and 4.79:1 on `--surface-2`.
- **The rail is unattested.** The cyan strip, its `#b6f5ff`-to-`#0090b3` fade and its bloom are decoration drawn from the RESEARCH text ("single AlienFX cyan glow per lighting zone"); no capture in the folder shows an app rail, and there is no purple in it.

## Reference status

`references/alienware/` has 8 captures plus `RESEARCH.md`. Per its audit, most are third-party icon-pack and desktop-skin images (Invader/XP-era), not the Dell AlienFX zone editor or Command Center in the capture targets: **this is the weakest-relevance set in the repo** and proper Dell captures remain a gap. They loosely back the matte black plus single cyan glow and the angular vent/cut language. The angle-cut corners, the corner brackets and the rail are the theme's interpretation of the RESEARCH text.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
