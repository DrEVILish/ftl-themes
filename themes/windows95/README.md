# Windows 95

> Beveled 3D gray — classic system dialog chrome on teal.

**Requires: L1** — sets `--ftl-app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

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
2. **Zero radius, everywhere.** `--ftl-radius: 0`. There were no rounded
   corners.
3. **A strictly limited palette.** Grey `#c0c0c0`, navy `#000080`, teal
   `#008080`, plus the 16-colour VGA set. No intermediate tints.
4. **Text is black on grey.** Filled controls use white on navy — never the
   page background as a foreground, which is what `--ftl-on-*` exists to
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

### Icons

`themes/windows95/icons.svg` redraws six of the most-used icons (home,
settings, search, close, user, bell) in the chunky, low-detail pixel-art
style of the real 95 icon set: large flat rectangular shapes, hard
corners (`stroke-linecap: square` / `stroke-linejoin: miter` on every
path, overriding the generic sprite's rounded default), and no curves
where a straight edge will do — the settings glyph is a plus of tabs
around a square rather than a circular gear, the same low-res
simplification the real icon set used at 16×16/32×32. Every other icon
falls back to the generic outline set, thickened by
`--ftl-icon-stroke-width: 2.6` like the rest of the theme.

## Layout

The app shell becomes a **desktop window**: the teal backdrop shows at the
edges, a 1.6rem gradient title bar sits on top, the content is a sunken
well, and the status bar is raised. Switching to this theme visibly boxes
the app up.

## Known compromise

MS Sans Serif is not a web font and is absent from modern systems, so the
stack falls back to Tahoma — its closest ubiquitous relative. Vendoring an
openly-licensed pixel face is tracked in `docs/theme-backlog.md`.

## Tell-tales of an inauthentic result

- Uniform 1px borders instead of two-tone bevels → flat-design cosplay.
- Any rounded corner or drop shadow.
- Buttons that don't invert their bevel on `:active`.
- Anti-aliased, modern-weight type in the title bar.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
Contrast-exempt: --ftl-text on --ftl-bg (the teal desktop) sits at ~4.5:1,
below the 7:1 AAA target. Deliberate: the teal desktop never carried body
text in Windows 95 — every readable surface was the grey dialog
(--ftl-surface #c0c0c0, where black text is ~17:1) — so the desktop pair is
decorative by construction, and brightening teal would be the inauthentic
fix. (Closes the intent documented in the theme.css header comment.)
