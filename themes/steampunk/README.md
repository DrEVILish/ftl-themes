# Steampunk

> Victorian brass, mahogany and copper, with gear-driven dials.

**Requires: L1** — sets `--ftl-app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

Victorian-era heavy industry as furniture: mahogany-dark wood panels,
polished brass fittings, and copper-toned readouts, as though the
interface were machined rather than rendered.

## Core values

1. **Brass is metal, not paint.** Buttons and accents are a light-to-dark
   gradient with a warm highlight — a cast, polished surface.
2. **Riveted plating.** Panels carry corner rivets (small brass dots) —
   the one recurring decorative motif, used consistently and nowhere else.
3. **Serif type, small-caps headings.** This is Victorian print, not a
   sans-serif dashboard.
4. **Warm and dark.** Mahogany brown surfaces, never grey or cool-toned.

## Signature details

- Rivets are two `::before`/`::after` pseudo-elements per panel — 6px
  radial-gradient circles at each top corner, zero markup, pure CSS.
- Headings use `font-variant: small-caps`, not `text-transform:
  uppercase` — genuine small capitals, the Victorian-print detail every
  uppercase-heading theme elsewhere in the catalog skips.
- Buttons carry a three-stop vertical gradient (`#d9ab4a` → `#a97a24` →
  `#7a5416`) — brass needs the extra middle stop other themes' two-stop
  gloss buttons don't bother with, or it reads as plastic, not metal.

## Layout

A gradient brass-edged bar and a matching wood-panel status strip — the
console reads as a cabinet fitted with brass hardware.

## Tell-tales of an inauthentic result

- Flat, ungraded brass — metal needs its highlight to read as metal.
- A sans-serif or a cool grey palette.
- Rivets missing from panels, or appearing somewhere they shouldn't
  (buttons, inputs) — they belong to panel corners only.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
