# Death Star Terminal

> Absolute black with glowing solid-colour indicator blocks, zero borders or shadows.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The Imperial control terminal aesthetic: a void of true black
punctuated only by solid-colour glowing indicator blocks — red, green,
blue — with no frame, border or shadow drawn anywhere to soften it.

## Core values

1. **Zero borders, zero shadows, zero radius.** Every panel/input/button
   border width is `0`. Structure comes only from solid fill against black.
2. **Indicators glow; everything else doesn't.** Only lamps and the focus
   ring carry any glow — restraint is what makes the glow read as a signal.
3. **Colour blocks are solid, not gradients.** A filled surface is one flat
   colour, full stop.
4. **True black, not near-black.** `--bg: #000`. This is the one theme
   in the catalogue that means it literally.

## Signature details

- Lamps carry a `0 0 10px` glow matched to their own state color
  (`.is-on` glows success-green, `.is-error` glows danger-red) — the only
  `box-shadow` this theme sets anywhere.
- Selected table rows fill solid accent blue with black text, not a tint —
  a "selected" row is a solid block, same discipline as everything else.
- Badges are square (`border-radius: 0`), overriding core's default pill —
  even the smallest decorative curve is stripped out here.

## Layout

No bar rule, no status rule — the bar and status strip are the same black
as the page, distinguished only by the content sitting on them.

## v5 layout

- **Tiers.** No rail, and the bar is just its red rule, so phone (≤480px)
  and tablet (481–900px) use core's one-column shell as is.
- **Nesting.** A panel inside another surface is a plain dark block (a
  second lattice ran lines through labels and fields), and its header is a
  slim red block at the left edge instead of another full red bar. Fields
  sit one step above `--surface-2` so a borderless input still shows on a
  panel, and close buttons in red headers are white.
- **XL gutter art.** More bulkhead: the circuit-grid lattice, much fainter
  than inside the shell, with a few unlit red control blocks. Still, and
  within about 1.2:1 of black.

## Tell-tales of an inauthentic result

- Any visible border on a panel, button or input.
- A gradient fill anywhere.
- A near-black (`#0a0a0a`-ish) background instead of true `#000`.

## Don'ts

- **No borders or shadows** beyond the hairline lattice; panels are black on black.
- **No colour beyond the red indicator and the white segments,** other than state colours.
- **No decorative typefaces or "Star Wars" lettering** (see Typography).
- **No filled red panels**; red is a lamp, a rule or a brand word.
- **No red as body text** — `--accent` fails as text on black.

## Typography

`--font` is `"Eurostile", "Michroma", sans-serif`; `--font-mono` is `Consolas, monospace`. Neither Eurostile (commercial) nor Michroma is vendored, so on most machines the generic sans-serif renders. **The stance is deliberate: this theme has no signature face.** `references/death-star/` shows control-room panels, indicator lamps and console details, but no on-screen lettering that pins down a typeface, and the film UI type is not something to fake with a Star Wars display font. The identity is carried by black, hairline white segments and red lamps; type stays neutral and small.

## Contrast honesty

- **Accent red fails as text.** `--accent` `#c81e1e` is 3.66:1 on black; white on it is 5.74:1, so red is safe only as a fill/lamp/rule. The app-bar brand text is lifted to `#ff5a5a` (6.86:1 on black).
- **Muted lifted:** `#6a6a6a` (3.8:1) to `#777777` (4.69:1 on black, 4.55:1 on `--surface-2` `#050505`).
- **Nav items** `#8a8a8a` (6.08:1 on black) sit a step above `--muted`; the `theme.css` comment says muted measured 3.9:1 on the bar, which does not match the 4.69:1 I compute on pure black (the bar may not be pure black; unverified).
- `--text` `#e6e6e6` is 16.83:1. Semantic fills (`#ff3b3b`, `#2fff6f`, `#ffcf2f`) are 5.9–15.7:1 on black with black `--on-*` text.
- The reference red in the photo is a lamp; `RESEARCH.md` records no hex, so `#c81e1e` is the theme's.

## Reference status

`references/death-star/` has 4 captures plus `RESEARCH.md`: `death-star-superlaser-still.jpeg` and `death-star-station-still.jpeg` (film stills), `death-star-executor-still.jpeg` (a further still, not described in `RESEARCH.md`) and `il_fullxfull.7108820316_cpn8.webp` (a builder's isolated console diorama with red/black panels, indicator dots and a green readout, which `RESEARCH.md` credits as the console reference). No isolated Imperial console-screen capture exists; the outsider read ("no borders, sparse tiny lamps") is what the layout follows.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
