# Event displays and signage (v5)

Source: `core/components/signage.css`. Example page: `signage.html`.

The pieces an event timer, a stage display or a room screen needs. A display is read from
3–10 m, has no operator chrome, and often runs on a device that reports reduced motion.

Shared conventions:

- Every look reads a `--countdown-*`, `--timeline-*`, `--stage-*`, `--lower-third-*`,
  `--qr-*`, `--word-cloud-*`, `--ranked-*` or `--count-*` token with a fallback to the
  base tokens, so every theme works with no theme edits.
- Motion runs under `prefers-reduced-motion: no-preference` and stops under
  `html[data-motion="reduced"]` / `"none"`, except on unattended screens (below).
- No state is colour alone: glyphs, signs, weight, outlines and text carry it too.

---

## Unattended screens `html[data-motion="always"]`

A TV stick or a Pi often reports reduced motion by default. On a screen nobody operates,
set `<html data-motion="always">`: every animation in the library (the connection lamp,
the loading hourglass, splash marks, countdown pulses, enter/exit) runs whatever the
device reports. The build (`scripts/motion_always.py`) copies each motion block for it,
so components keep one motion block each. **Never use it on an interactive page**: it
overrides the user's own setting.

## Signage surface `html[data-surface="signage"]`

```html
<html data-surface="signage" data-motion="always">
<body><main class="safe-area" data-fit="contain">…</main></body>
```

- **Root size:** `--signage-root` (default `1.5vh`; `--signage-root-portrait`, `1.5vw`,
  when rotated), so every `rem` scales with the output and 720p, 1080p and 4K look the
  same. Nothing scrolls. Operator pages keep the OS root size.
- **`.safe-area`** pads the content inside the TV's overscan: `--safe-inset-block` /
  `--safe-inset-inline` (4vh / 4vw), or the device's `env(safe-area-inset-*)` if larger.
  `data-fit="cover"` drops the inset; `data-fit="shadow"` vignettes the edge.

## Countdown states `.countdown[data-state]`

```html
<time class="countdown countdown-xl" data-state="overtime" aria-live="off">
  <span class="countdown-sign">+</span>0:12</time>
<p class="visually-hidden" role="status">Overtime</p>
```

Extends the instruments `.countdown`. States: `running` (default), `armed` (cued),
`paused` (a pause glyph), `held` (at zero), `alert1`, `alert2`, `overtime` (with the
"+" sign). `alert2` and `overtime` are heavier and pulse (`--countdown-pulse-period`, 1s,
to `--countdown-pulse-opacity`, .72). `.countdown-xl` sets `--countdown-size` (default
`clamp(3rem, 18vw, 14rem)`); `.countdown-tenths` and `.countdown-sign` ride smaller.
Per-item alert colours are inline `--countdown-alert1` / `--countdown-alert2`.

- **Accessibility:** the timer changes every frame, so it is **not** a live region.
  Announce state changes ("Overtime", "2 minutes left") in a sibling
  `.visually-hidden[role=status]`.

| Token | Default |
|---|---|
| `--countdown-armed-fg`, `--countdown-held-fg` | `var(--muted)` |
| `--countdown-paused-fg` | `var(--warning-text)` |
| `--countdown-alert1` / `--countdown-alert2` | `var(--warning-text)` / `var(--danger-text)` |
| `--countdown-overtime` | `var(--countdown-alert2)` |
| `--countdown-xl-size` | `clamp(3rem, 18vw, 14rem)` |

## Day bar `.timeline-bar`

```html
<div class="timeline-bar" role="img" aria-label="Day 09:00–17:30, now 10:12, in the keynote">
  <span class="timeline-seg is-done" style="--start:0%; --size:6%">Doors</span>
  <span class="timeline-seg is-active" style="--start:9%; --size:12%">Keynote</span>
  <span class="timeline-seg" data-kind="break" style="--start:21%; --size:6%">Coffee</span>
  <span class="timeline-now" style="--at:18%"></span>
</div>
<div class="timeline-scale"><time>09:00</time><time>13:00</time><time>17:30</time></div>
```

Segments sit at `--start` and are `--size` wide; `--seg-color` tints one. Breaks are
striped (`--timeline-break-pattern`), done segments dimmed (`--timeline-done-filter`), the
active one underlined. The needle moves by position only. Labels hide when the bar is
narrower than 30rem (a container query). The bar is one `role="img"` whose label the app
keeps current; segments that are links or buttons are focusable.

## Stage edge and attention

- **`.stage-edge[data-level="warn|danger"]`** rings the element inside its edge in `vmin`
  (`--stage-edge-warn-width` .45vmin, `--stage-edge-danger-width` .7vmin), coloured by
  `--stage-alert` (an operator's choice) or warning / danger. Seen in peripheral vision.
- **`.is-attention`** blinks at 1 Hz in steps (`--attention-period`; under 3 Hz, WCAG
  2.3.1); **`.is-urgent`** pulses. Without motion both show a steady outline.
- **Standby:** `.splash.is-standby` (experience.css) is the operator blackout.

## Message band `.lower-third`

```html
<div class="lower-third" role="status" style="--banner-edge: #ff8a00"><p>Wrap up</p></div>
```

Over the lower third of its positioned parent (`.is-center`: the middle; `.is-fixed`: the
viewport). The operator's colour is the leading edge (`--banner-edge`,
`--banner-edge-width`) only; the text carries the meaning. `--banner-size` defaults to
`clamp(1.7rem, 6vh, 6rem)`. Animate it in with `data-enter`.

## QR join card `.qr-card`

```html
<div class="qr-card">
  <img class="qr-card-code" src="join.svg" alt="QR code: join at timerpi.local/j">
  <span class="qr-card-label">Join the Q&amp;A</span>
  <span class="qr-card-url">timerpi.local/j</span>
</div>
```

The code always sits on a light quiet zone (`--qr-bg`, `--qr-quiet`) with crisp pixels
(`image-rendering: pixelated`), whatever a theme does to images; forced colours leave it
alone. `--qr-size` (7rem). `.is-corner` pins it bottom-end inside the safe area. Always
print the URL beside the code.

## Word cloud `.word-cloud`

```html
<ul class="word-cloud" aria-label="Audience words">
  <li class="word-cloud-word is-top" data-tone="1" style="--weight:.9; --x:0; --y:0">coffee
    <span class="visually-hidden">, 18 votes</span></li>
</ul>
```

The app places each word (`--x` / `--y` from -1 to 1 around the centre, `--rotate`) and
weights it (`--weight` 0–1 between `--word-cloud-min` and `--word-cloud-max`); ftl paints
it. `data-tone="1..6"` picks a chart colour, mixed toward the text colour
(`--word-cloud-tone-strength`, 35%) so every tone keeps 3:1 on any theme; `.is-top` glows. A physics layout is app
code; without motion, place the words statically (a spiral).

## Ranked wall `.ranked-list`

```html
<ol class="ranked-list is-positioned" style="--ranked-height: 30rem">
  <li class="ranked-item is-spotlight" aria-current="true" style="--slot-y: 0rem">
    When do the slides go up? <span class="ranked-votes">14</span></li>
</ol>
```

The DOM order is the rank order (screen readers hear the rank). With `.is-positioned` the
app also sets each item's `--slot-y` and the item slides there (`--ranked-move`), so a
reorder animates. `.is-spotlight` (a heavy accent border), `.is-answered` (success; say
so in text), `.is-leaving` (fades), `.is-new` (rises in). Without motion the order just
changes.

## Count-up `.count`, `.is-counting`

```html
<div class="meter is-solid is-counting" style="--stagger-index:1">
  <div class="meter-fill" style="--meter-level:35%"></div></div>
<data class="count" value="35" style="--count:35; --stagger-index:1"><span class="visually-hidden">35</span></data>
```

The number counts from `--count-from` (0) to `--count` (an integer, registered with
`@property`) and the bar grows from empty, over `--count-duration` (900ms), each
`--stagger-index` × `--stagger` (120ms) later. Put the final value inside as
visually-hidden text (that is what assistive tech reads); the digits you see are drawn, in
a box `--count-digits` (3) characters wide. Without motion the result shows at once.
Re-trigger by replacing the element.

## Enter and exit `[data-enter]`, `[data-exit]`

```html
<section class="widget is-entering" data-enter="pop" data-exit="slide">…</section>
```

`fade`, `slide` or `pop`. The app adds `.is-entering` when the element appears and
`.is-exiting` before removing it (after `--motion-exit-duration`). Durations:
`--motion-enter-duration` (450ms), `--motion-exit-duration` (400ms).
