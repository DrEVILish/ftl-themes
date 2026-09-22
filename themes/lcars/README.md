# LCARS

> Star Trek TNG/DS9/Voyager on-screen computer — candy pills on black.

## What this theme is trying to achieve

The **Library Computer Access/Retrieval System** as it appeared on screen
from 1987 onward: a black field organised by fat, rounded, candy-coloured
blocks, set in a tall condensed face, with sweeping elbow corners joining
horizontal bars to vertical rails.

The target is *recognisable at a glance from across a room* — someone
should identify it before reading a single word. If a screenshot needs a
caption to say which theme it is, it has failed.

## Core values

1. **Black is the substrate, not a colour choice.** LCARS is colour blocks
   floating on true black. Any grey "card" background is wrong.
2. **The elbow is the signature.** A horizontal bar that curves down into a
   vertical rail is the single most identifying shape in the whole system.
   The app shell's bar does exactly this (`--ftl-app-bar-radius`).
3. **Candy bars code by colour, not by meaning.** The orange/lavender/sky/
   rose/tan palette is decorative structure. Resist making every lavender
   block mean one semantic thing — that's a modern dashboard habit.
4. **Rounded ends, flat joins.** A block is a pill where it terminates and
   square where it meets its neighbour. That asymmetry is why buttons here
   are `0 1.2rem 1.2rem 0`, not fully rounded.
5. **Chunky, never dense.** This is a wall panel operated by hand, so
   `--ftl-density: 1.15`. A cramped LCARS is a wrong LCARS.
6. **Type is tall, condensed, uppercase.** Antonio stands in for the
   original's Swiss 911/Helvetica Compressed.

## How the tokens carry that

| Token | Value | Why |
|---|---|---|
| `--ftl-bg` | `#000000` | True black. Not near-black — the blocks must float. |
| `--ftl-accent` | `#ff9900` | The canonical LCARS orange; the system's primary structural colour. Matches "atomic tangerine" in the documented Okuda reference palette exactly. |
| `--ftl-lcars-lavender` / `-sky` / `-rose` / `-tan` / `-peach` | `#cc99cc` `#6699ff` `#cc6699` `#ffcc99` `#ff9966` | The candy palette, namespaced so it can never collide with another theme's tokens. `-lavender` matches the reference palette's "lilac" exactly; `-sky` was corrected from an unsourced pastel periwinkle to sit close to the reference's saturated blue family ("mariner"/"bahama-blue") while still clearing the button-text contrast floor. |
| `--ftl-radius` | `1.4rem` | Large by default — everything wants to be a pill. |
| `--ftl-on-accent` | `#000000` | Black text on candy fills. LCARS never sets light text on a colour block. |
| `--ftl-density` | `1.15` | Deliberately loose. |

Source: the Okuda-designed LCARS palette (Michael and Denise Okuda,
conceived for TNG starting 1987) as documented by the `trekcolors`
reference project — not a single "official" style sheet, since LCARS
predates CSS by a decade, but the closest thing to a canonical hex list
this catalog could verify against.

## Signature details

- **Meters** band in the *candy* palette (sky → orange → rose) rather than
  green/amber/red. A traffic-light meter instantly reads as a modern audio
  app wearing an LCARS costume.
- **Readouts** set in Antonio, large and blocky — the on-screen numerals.
- **The transport** is a black bar with a thick orange edge, and GO is a
  solid orange elbow (`0 1.4rem 1.4rem 0`), not an outline. On this theme
  the primary action is a *block*, consistent with everything else.
- **Lamps** are rounded rectangles, not circles: LCARS has few true circles.

## Layout — this theme moves the furniture

Selecting LCARS re-arranges the app shell, it does not merely recolour it:

- a **6rem candy rail** appears down the left (`--ftl-app-columns`), drawn
  entirely in CSS as a hard-stopped gradient stack so no app ships
  LCARS-specific markup;
- the **top bar becomes a solid orange sweep** whose bottom-left corner
  elbows into that rail (`1rem 1rem 0 3rem`);
- content insets to the right of the rail, and the status strip rounds off
  the bottom of the frame.

On phones the rail becomes a horizontal colour strip under the bar rather
than disappearing — the colour coding is most of the identity.

`themes/lcars/chrome.css` additionally offers a richer, opt-in frame with
individually rounded rail bars and a real nav inside the rail, for apps
willing to add markup. Most apps should use the shell instead.

## Extending it

Do:
- Add new colours from the candy palette, namespaced `--ftl-lcars-*`.
- Keep black text on every coloured block.
- Let blocks touch with flat joins and terminate with pills.

Don't:
- Introduce grey surfaces, gradients, or drop shadows — LCARS is flat.
- Make it dense to "fit more".
- Circle-round the elbow corners uniformly; the asymmetry is the point.
- Use semantic red/green for meters or status blocks where a candy colour
  would do.

## Tell-tales of an inauthentic result

- Grey cards on a dark background → a generic dark theme with orange
  accents, not LCARS.
- Uniformly rounded pills everywhere → the elbow language is gone.
- Green/amber/red meters → an audio app in costume.
- Tight rows and small type → a spreadsheet wearing LCARS colours.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
