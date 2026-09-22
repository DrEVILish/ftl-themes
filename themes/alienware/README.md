# Alienware

> Matte black gaming chrome — angular cuts, AlienFX cyan glow.

## What this theme is trying to achieve

**Alienware's gaming-rig identity**: matte black chassis, cut/angular
edges instead of curves, and a single AlienFX accent color glowing along
one edge — the light strip every Alienware machine has. Aggressive but
controlled, not a rainbow of RGB.

## Core values

1. **Angles, never curves.** `--ftl-radius: 0.2rem` and every major
   surface has its corners cut with `clip-path`, not rounded. This is the
   catalog's deliberate contrast point against `aqua`/`barbie`'s gloss and
   curves — a rounded Alienware is a contradiction.
2. **One glow, not many.** The AlienFX cyan (`--ftl-accent`) is the only
   thing allowed to glow. A version of this theme with every element
   lit up in a different color has missed the "one light strip" idea.
3. **Matte black, not gloss.** Flat fills, no gradients on the base chrome
   — the shine belongs to `aqua`/`winxp-luna`, not here.
4. **Uppercase, tracked-out headings.** The gamer-hardware branding voice:
   wide letter-spacing, all caps, never soft title case.
5. **The rail is the light strip.** The app shell's decorative rail is a
   thin lit cyan-to-purple gradient — the physical AlienFX edge light,
   not a navigation column.

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

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
