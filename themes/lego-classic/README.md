# LEGO Classic

> Primary colour blocks, thick borders, and circular studs.

**Requires: L1** — sets `--ftl-app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The brick itself as a UI: primary colours, thick black outlines on
everything, and a chunky "pressable" 3D shadow that a button visibly loses
when clicked — a physical toy, not a flat icon of one.

## Core values

1. **Thick black outlines, always 3px.** Every control is outlined like a
   brick's moulding line.
2. **A button has a shadow it loses on press.** `--ftl-btn-shadow` is a
   hard offset shadow; `:active` drops it and nudges the button down —
   the brick physically depresses.
3. **Primary colours only** — red, yellow, blue, green — no intermediate
   tints. `--ftl-flare` (blue) carries structural chrome (nav, table
   heads) so red stays reserved for actions/danger.
4. **Bold, geometric type.** Heavy weight headings.
5. **Studs are big and everywhere a brick's top face would show one** —
   the app bar, every panel/card top, and every panel/modal header, all
   carrying large two-tone discs, not a thin accent line easy to miss.

## Signature details

- Studs are large (~18-20px) two-tone `radial-gradient` discs — a bright
  offset highlight inside a darker rim — tiled every 32-36px, not
  individual `<span>` elements: zero markup, purely decorative CSS. A
  faint pinprick-sized dot doesn't read as a brick stud at a glance; a
  disc this size does.
- The app bar carries its own stud row along its bottom edge, since it's
  the single largest, most-visible brick-top surface on the page.
- `.ftl-btn:active` drops the shadow to `0 1px 0` and nudges the button
  `translateY(2px)` — the brick visibly sinks into the plate, not just
  darkens.
- `--ftl-flare` (moulding blue, `#0055bf`) carries the app bar, status
  strip, and table headers — structural chrome is always blue regardless
  of which primary color a button uses.

## Layout

A solid blue bar and status strip with a thick black rule — a base plate
in a specific colour, with the white content area as the build surface on
top of it.

## Tell-tales of an inauthentic result

- Thin or no borders — the moulding line is the entire identity.
- A button with no press-shadow interaction.
- Pastel or muted colours instead of flat primaries.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
