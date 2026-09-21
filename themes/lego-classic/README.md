# LEGO Classic

> Primary colour blocks, thick borders, and circular studs.

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
5. **Studs are decoration on panel headers only** — a nod to the brick's
   top, not applied everywhere.

## Layout

A solid blue bar and status strip with a thick black rule — a base plate
in a specific colour, with the white content area as the build surface on
top of it.

## Tell-tales of an inauthentic result

- Thin or no borders — the moulding line is the entire identity.
- A button with no press-shadow interaction.
- Pastel or muted colours instead of flat primaries.
