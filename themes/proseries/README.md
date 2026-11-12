# ProSeries

> A Pro Series live-console touch screen: navy-violet desk, bright blue channel strips, bevelled grey keys, a black home bar with the scene name in yellow.

**Requires: L1** — sets `--app-*` layout properties (black home bar, no rail); recolours correctly at L0. Best seen on [`proseries.html`](../../proseries.html), a full console built for it.

## What this theme is trying to achieve

The GUI of a large-format digital live console from the 2010s, as seen
on its 15-inch touch screens: everything bold and small, saturated blue
strips on a dark violet desk, grey bevelled soft keys with dark labels,
function keys that sit dark in their own colour and light up, black knobs inside rings of white ticks,
and a black title bar carrying the page name, the scene and tap tempo.
It is an engineering screen, not a consumer app: dense, square, legible
at arm's length in a dark room.

## Core values

1. **Bold everywhere.** Every label is in the bold face, small and mixed
   case: form labels, hints, table heads and stat labels included. A
   regular weight or an uppercase tracked label reads as a web page. The
   one exception is running text (`.prose`, textareas), which the console
   never shows: it is regular weight at 1.5 line height.
2. **Keys light in their own colour.** Mute orange-red, solo olive-gold,
   monitor and select yellow, on green. Unlit keys are dark faces tinted
   with their function colour and a dark LED, with white labels; lit keys
   brighten and the LED glows.
3. **Dark text on lit keys and tags.** Channel name tags and lit keys carry
   near-black text, as on the console.
4. **Blue strips, black inserts.** Strips are a vivid blue gradient; send
   blocks, scene and value fields are black wells.
5. **Knobs are black with a white tick ring.** The value arc lights in
   yellow over the ticks; role colours (purple dynamics, orange pan, grey
   trim) are page choices, not the default.

## How the tokens carry that

- `--strip-bg`, `--strip-border`, `--strip-rule`: the strip gradient and its dark dividers.
- `--key-*`: a dark face tinted with the key's colour unlit, the same colour bright and glowing when lit.
- `--knob-*`: black cap, white pointer, white tick ring, yellow arc.
- `--fader-cap-bg`: the black hourglass cap with its grey disc; `--fader-slot`: the black slot.
- `--meter-*`: green / yellow / red segments on black with dim unlit LEDs.
- `--presence-color-1..6`: the console's name-tag colours (yellow, magenta,
  orange, blue, green, grey) for `data-color` tags.
- `--btn-*`: grey bevelled buttons; `.btn-primary` is the navy preset key,
  `.btn-secondary` the grey copy/paste key, `.btn-tertiary` a flat grey key
  and `.btn-ghost` a key outline (never bare text on the desk).
- `--card-bg`: the strip blue (flat #3a62b4), so the console blue shows on
  every page; muted text in a card lifts to near-white. `--panel-bg` is the
  sidebar's royal-blue section, flat. Both are single fills with a hard
  1px drop, no blur, to keep scrolling cheap.
- `--slider-bg`: the black fader slot; `--slider-thumb-*`: the fader cap on
  its side (upright on `.slider.is-vertical`, which draws a 4px slot in its
  touch-sized box). `--badge-radius`/`--switch-radius`/`--btn-icon-radius`: square.
- `--btn-close-*`: a white round close disc with a dark glyph (dark red on `.is-danger`).
- `--app-*`: black home bar, no rail, a flat navy desk.

## Signature details

- Knob tick rings drawn with a repeating conic gradient behind the value arc; the console's other
  pointer styles (chicken heads, clock, lobed, sculpted, LED ring, LED dot) are `data-pointer` values.
- Brushed-metal and leather faceplates are drawn in CSS (`data-finish`), never copied from the console.
- The home bar: a two-tone "home" tab, a round back key, the page title,
  a black scene field in yellow, a status key with a red lamp, tap tempo.
  On every page the bar's current item is the two-tone tab, the brand gets
  the round back key and fields in the bar are the black yellow scene field.
- The splash: a deep-blue sky with a gold "ProSeries" wordmark (no logos).
- Badges and filter chips are square solid lit tiles with dark text, never tints or pills.
- Lit keys carry near-black text over their glowing face.
- Every slider thumb is the black hourglass fader cap with its grey disc,
  never the default accent dot.
- Icon buttons are square bevelled soft keys (ghost ones grey); the round
  back key and close disc are the only round controls.
- Leaves with a CRT-style power-off when you switch theme.

## Layout

Black home bar across the top, no rail, the content on a flat
navy-violet desk. Panels are royal blue with light headers; cards are strip blue.

## v5 layout

- **Tiers:** phone and tablet keep the bar. On a phone it is two rows at
  most: the brand beside a nav that scrolls on one line, then the scene
  field, search, bell and avatar. The desk scrolls.
- **Gutter art:** a dark navy field with faint specks, within 1.5:1 of `--bg`.
- **Nesting:** nested panels keep the same blue with no second bevel.

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
