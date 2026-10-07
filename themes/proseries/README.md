# ProSeries

> A Pro Series live-console touch screen: navy-violet desk, bright blue channel strips, bevelled grey keys, a black home bar with the scene name in yellow.

**Requires: L1** — sets `--app-*` layout properties (black home bar, no rail); recolours correctly at L0. Best seen on [`proseries.html`](../../proseries.html), a full console built for it.

## What this theme is trying to achieve

The GUI of a large-format digital live console from the 2010s, as seen
on its 15-inch touch screens: everything bold and small, saturated blue
strips on a dark violet desk, grey bevelled push keys with dark labels
that light in their own colour, black knobs inside rings of white ticks,
and a black title bar carrying the page name, the scene and tap tempo.
It is an engineering screen, not a consumer app: dense, square, legible
at arm's length in a dark room.

## Core values

1. **Bold everywhere.** Every label is in the bold face, small. A regular
   weight reads as a web page, not a console.
2. **Keys light in their own colour.** Mute orange-red, solo olive-gold,
   monitor and select yellow, on green; unlit keys are neutral grey bevels.
   Never tint an unlit key.
3. **Dark text on lit keys and tags.** Channel name tags and lit keys carry
   near-black text, as on the console.
4. **Blue strips, black inserts.** Strips are a vivid blue gradient; send
   blocks, scene and value fields are black wells.
5. **Knobs are black with a white tick ring.** The value arc lights in
   yellow over the ticks; role colours (purple dynamics, orange pan, grey
   trim) are page choices, not the default.

## How the tokens carry that

- `--strip-bg`, `--strip-border`, `--strip-rule`: the strip gradient and its dark dividers.
- `--key-*`: grey bevel unlit, each function key's own lit colour.
- `--knob-*`: black cap, white pointer, white tick ring, yellow arc.
- `--fader-cap-bg`: the black hourglass cap with its grey disc; `--fader-slot`: the black slot.
- `--meter-*`: green / yellow / red segments on black with dim unlit LEDs.
- `--presence-color-1..6`: the console's name-tag colours (yellow, magenta,
  orange, blue, green, grey) for `data-color` tags.
- `--btn-*`: grey bevelled buttons; `.btn-primary` is the navy preset key.
- `--app-*`: black home bar, no rail, a radial desk backdrop.

## Signature details

- Knob tick rings drawn with a repeating conic gradient behind the value arc; the console's other
  pointer styles (chicken heads, clock, lobed, sculpted, LED ring, LED dot) are `data-pointer` values.
- Brushed-metal and leather faceplates are drawn in CSS (`data-finish`), never copied from the console.
- The home bar: a two-tone "home" tab, a round back key, the page title,
  a black scene field in yellow, a status key with a red lamp, tap tempo.
- The splash: a deep-blue sky with a gold "ProSeries" wordmark (no logos).
- Badges are solid lit tiles with dark text, never tints.
- Leaves with a CRT-style power-off when you switch theme.

## Layout

Black home bar across the top, no rail, the content on a radial
navy-violet desk. Panels are lavender-blue with light headers.

## v5 layout

- **Tiers:** phone and tablet keep the bar (it wraps); the desk scrolls.
- **Gutter art:** a dark navy field with faint specks, within 1.5:1 of `--bg`.
- **Nesting:** nested panels keep the same lavender with no second bevel.

## Tell-tales of an inauthentic result

- Regular-weight or uppercase tracked labels (the console is bold, mixed case).
- Coloured keys when unlit, or white text on a lit orange key.
- Rounded pill buttons or soft shadows; the screen is square and bevelled.
- Pastel or flat-grey strips instead of saturated blue.

## Don'ts

- Don't vendor the console's own artwork, logos or splash images.
- Don't lighten the strip blue to "improve" contrast; darken text wells instead.

## References

`references/proseries/` (three owner-supplied captures and RESEARCH.md).
