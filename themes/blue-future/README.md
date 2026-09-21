# Blue Future

> A futuristic sci-fi HUD: deep-space navy with cyan neon glow.

## What this theme is trying to achieve

An **advanced spacecraft computer** — or a high-end industrial control
system. Precise, uncluttered, dark. The reading should be "this instrument
is telling me the truth about a machine," not "this website has a neon
aesthetic."

The reference look is a live recorder/telemetry dashboard: a dark navy
shell, monospaced readouts, thin cyan rules, and glow used to mark what is
*live* rather than to decorate what is merely present.

## Core values

1. **Glow is a signal, not a decoration.** A glow means energized, live,
   selected, or focused. If everything glows, nothing is live. This is the
   rule most often broken when extending the theme.
2. **Telemetry is monospaced.** Any raw machine value — timecode, counts,
   IDs, sample rates, file sizes — sets in `--ftl-font-mono` with tabular
   figures (`.ftl-mono`). Proportional digits that jitter as they count
   break the instrument illusion.
3. **Cyan means live data; blue means interactive.** `--ftl-accent` (cyan)
   carries live/active/telemetry. `--ftl-accent-2` (blue) carries
   interactive-but-not-live. If both land on the same element, that's a bug.
4. **Structure over ornament.** Headings are tracked, uppercase, *dim* —
   they are labels on a panel, not titles on a page. The content is the
   bright thing; the chrome recedes.
5. **No gradients on interactive surfaces.** A flat fill plus a glow reads
   as energized. A gradient reads as a web button from 2012.

## Provenance

The palette is not invented: it is reconciled against the reference
implementation this theme is named for — a 1U rack recorder's telemetry
dashboard. Those values (`#00d9ff` cyan, `#0a1526` panel, `#0f3a5c` rule,
`#cfeeff` text, Consolas) are copied from the device, so selecting this
theme on that device reproduces its own look rather than approximating it.
Changing them is a change to the reference, not a matter of taste.

## How the tokens carry that

| Token | Value | Why this value |
|---|---|---|
| `--ftl-bg` | `#020509` | Near-black, faintly blue: a panel in a dark rack room. |
| `--ftl-surface` / `-2` | `#0a1526` / `#08192b` | Two steps up, both still very dark. The surface ladder is shallow on purpose — depth comes from hairlines and glow, not from lightening slabs. |
| `--ftl-border` / `--ftl-hairline` | `#0f3a5c` / `#0a2942` | Visible rules are blue-cast, and the hairline is dimmer: dense data needs separators that don't add up to a cage. |
| `--ftl-accent` | `#00d9ff` | Electric cyan. The live/telemetry color. |
| `--ftl-accent-2` | `#4d7dff` | Electric blue. Interactive/selected. |
| `--ftl-text` / `--ftl-muted` | `#cfeeff` / `#5b8aa8` | Text is blue-white, never pure white — reserve pure white for a genuinely critical value. Muted is a real step down so labels recede below data. |
| `--ftl-font` | Consolas | Monospace as the *primary* UI font, not just for values. This single choice does more for the "spacecraft computer" feel than any color. |
| `--ftl-radius` | `0.25rem` | Almost square. Rounded corners read as consumer software. |
| `--ftl-flare` | `#d85cff` | Magenta, used almost nowhere. Held in reserve for a single rare emphasis so it keeps its force. |

## Instruments

This theme exists for surfaces that meter something, so the instrument
primitives carry its identity more than the buttons do:

- **Meters** use true VU banding — `#0aff9d` green, `#ffe400` amber,
  `#ff2a2a` red, white peak-hold. These are deliberately *not* the theme's
  semantic `--ftl-success`/`-warning`/`-danger`: a meter is reporting signal
  level, not application state, and the eye reads the classic broadcast
  ramp faster than a palette-matched one.
- **Readouts** glow cyan and track slightly wide. A counter is the thing
  you read across the room.
- **Lamps** are round, dark-navy when off, cyan and blooming when on.
- **The transport** repeats the panel's corner-bracket language, and GO
  blooms rather than filling — an energized outline, not a painted button.

## Layout

A flat instrument panel: a full-width dark bar, **no rail**, edge-to-edge
content, and a status strip along the bottom for telemetry. Screen area
belongs to data, so the chrome is as thin as it can be while still framing.
This is the deliberate opposite of LCARS's chunky rail — switching between
the two should visibly move the furniture.

## Signature details

- **Grid-lined backdrop.** A 2rem cyan grid at 4% opacity over a radial
  vignette — the panel sits in a space, rather than floating on flat color.
- **Corner brackets** on panels and modals (`::before`/`::after`, 14px, 55%
  opacity): a HUD reticle framing content. Purely decorative and
  `pointer-events: none`.
- **Focus glows.** `--ftl-focus-ring` adds a cyan bloom on top of the
  always-present outline — focus is a live state, so it glows.
- **Square slider thumbs** with a glow: a physical fader cap, not a dot.

## Extending it

Do:
- Reach for `--ftl-accent` only when the thing is genuinely live.
- Add glow via `--ftl-*-shadow` properties so it stays tunable.
- Keep new readouts monospaced and tabular.

Don't:
- Add a gradient to any control.
- Brighten `--ftl-muted` to "improve readability" — the contrast floor is
  already verified by `scripts/check.sh`; if a label seems too dim, it's
  probably a label that shouldn't be competing with data.
- Round the corners.
- Use `--ftl-flare` more than once on a screen.

## Tell-tales of an inauthentic result

- Everything glows → nothing reads as live.
- Proportional digits in a counter → the layout twitches as it counts.
- Bright white headings → the chrome shouts over the data.
- A rounded, gradient-filled primary button → consumer web, not instrument.

## Reference implementation & stays-app-side

This theme is the theme-form of a rack recorder's telemetry dashboard
(PI9696), which is the visual reference: palette, brackets, switch
readouts, and deck metalwork values are that device's actual numbers.
The dashboard consumes this theme opt-in; with no theme it renders its
own identical built-in look.

Deliberately NOT themed (app-owned, do not add hooks for these):

- OLED bezel and mirror — a hardware representation, not chrome.
- Reel-deck SVG geometry and tape animation — flat fills are exposed as
  `--ftl-deck-*` for reskinning, but the drawing itself is the device.
- The square HUD rail switch (`.sci-switch`) and its ONLINE/OFFLINE
  readout — device identity; core's round `.ftl-switch` is a different
  widget, do not force them together.
- Round icon buttons and transport geometry — state *colors* are covered
  by `.ftl-transport.is-rec/.is-play/.is-pause`, sizes stay app-side.
- uPlot chart internals — the app reads bridge tokens via
  `getComputedStyle` with identical fallbacks.
- Brand logo and modal sheet layout.
