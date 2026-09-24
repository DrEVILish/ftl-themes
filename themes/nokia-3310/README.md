# Nokia 3310

> The reflective yellow-green monochrome LCD of the 3310/3210 era: no backlight colour, no anti-aliasing, and selection reads as a hard colour invert rather than a highlight.

**Requires: L1** — sets `--ftl-app-*` layout properties (the inverted title strip); recolours correctly at L0 but the phone-screen composition needs the app shell.

## What this theme is trying to achieve

The 3310's screen was genuinely one colour: a reflective, non-backlit
yellow-green LCD with dark olive pixels, the same in every lighting
condition a backlight would otherwise vary. There is no second hue on the
real device — every visual distinction (selected menu item, header bar)
comes from inverting which of the two tones is foreground and which is
background, never from introducing a new colour.

## Core values

1. **Selection is inversion, not colour.** `--ftl-row-selected-bg` /
   `--ftl-row-selected-fg` swap the two LCD tones outright — light-on-dark
   instead of dark-on-light — the only way this hardware could highlight
   anything.
2. **Zero radius, zero gradient, zero shadow.** A reflective LCD segment
   display has none of these; every corner is square and every fill is
   flat.
3. **danger/success/warning are a documented compromise.** True hardware
   has no second colour at all; those three tokens use barely-different
   dark tones within the same LCD family specifically so the theme stays
   usable as a real design system without pretending the phone had a
   colour screen — see the comment beside them in `theme.css`.

## Signature details

- The signal-bars and battery-bars pseudo-elements in the corners of the
  app-bar — the one piece of chrome every candybar phone screen had.
- The inverted dark title strip across the top (`--ftl-app-bar-bg` set to
  the text colour, not the background) — the carrier-name bar convention.
- Bold, chunky text with no smoothing — this is a low-resolution segment
  display, not a modern hinted font.

### Icons

`themes/nokia-3310/icons.svg` redraws six icons (home, settings, search,
close, user, bell) as coarse, low-resolution monochrome LCD segment
shapes: big flat `currentColor` polygons and rects with minimal internal
detail, no anti-aliasing and almost no curves — the kind of menu glyph a
real feature-phone screen could actually render at its native
resolution. Every other icon falls back to the generic outline set.

## Tell-tales of an inauthentic result

- Any rounded corner or drop shadow.
- A saturated, clearly-differently-hued "accent" color — anything beyond
  the yellow-green/dark-olive family breaks the one-colour-screen premise.
- A soft/tinted selection highlight instead of a hard full invert.
