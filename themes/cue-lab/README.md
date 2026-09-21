# Cue Lab

> Flat live-show console — hairline grids, amber accent, no glow.

## What this theme is trying to achieve

A **show-control console** of the kind an operator sits behind during a
live performance: a dense cue list, a flat neutral chrome that never
competes with it, and exactly one control that shouts — **GO**.

The design target is the moment before a cue fires. The operator is
half-watching the stage, glancing down. They must find the current cue,
the next cue, and the GO button in under a second, in a dark room, under
stress. Everything in this theme serves that moment.

## Core values

1. **One loud thing.** GO is the only element allowed a glow. If a second
   element competes with it, the theme has failed at its one job.
2. **Flat everywhere else.** No gradients, no elevation, no decorative
   shadow. Depth cues cost scanning time and add nothing to a list.
3. **Density is a feature.** `--ftl-density: 0.85`. Fitting more of the cue
   list on screen is worth more than breathing room.
4. **Amber is state, not decoration.** `#ff8c1a` marks the active cue, the
   armed transport, the thing that is about to happen.
5. **Neutral greys carry the chrome.** `#141414`/`#1d1d1d`/`#262626` — a
   console body, not a brand colour.
6. **Numbers are tabular.** Cue numbers and times must not reflow as they
   change.

## How the tokens carry that

| Token | Value | Why |
|---|---|---|
| `--ftl-bg` / `--ftl-surface` / `-2` | `#141414` / `#1d1d1d` / `#262626` | A near-neutral grey ladder. Warm-free so amber stays the only colour with a job. |
| `--ftl-accent` | `#ff8c1a` | Amber: active, armed, current. |
| `--ftl-danger` | `#d63a3f` | Darkened from a brighter red so white text on a destructive button clears 4.5:1. |
| `--ftl-radius` | `0.2rem` | Nearly square — hardware, not app. |
| `--ftl-density` | `0.85` | Tight rows. The single most consequential token here. |
| `--ftl-font` | System sans | A console is read, not admired; the platform UI face is the most legible option at small sizes. |

## Instruments

- **The transport is the theme.** A flat strip with a 0.3rem amber left
  edge, carrying GO. GO is a 2px amber outline that fills faintly and
  blooms on hover — a deliberate, and the *only*, exception to the
  no-glow rule.
- **Meters** use conventional green/amber/red banding, squared off
  (`--ftl-meter-radius: 0`).
- **Lamps** are square and unlit-dark with no bloom: panel LEDs, not
  indicators on a web page.
- **Readouts** are plain, heavy, amber — a cue number, not a spectacle.

## Layout

Minimal chrome: a 2.6rem bar with a 2px amber rule under it, **no rail**,
0.6rem content padding, and a status strip. Every spare pixel goes to the
list. Compared with LCARS, switching to this theme visibly *tightens* the
whole shell.

## Extending it

Do:
- Keep new surfaces flat and neutral.
- Use amber only for "this is current / this is armed".
- Prefer tighter spacing when in doubt.

Don't:
- Add a second glowing element. If something else needs emphasis, give it
  amber, not light.
- Introduce a gradient or a shadow anywhere.
- Round corners to soften the look.
- Use a universal `!important` reset to enforce flatness — that erases
  state indicators like the active-row marker. Express flatness by leaving
  the `--ftl-*-shadow` properties unset.

## Tell-tales of an inauthentic result

- Two or more things glowing → GO no longer wins the eye.
- Comfortable, airy rows → fewer cues visible, slower to scan.
- A shadowed card holding the cue list → a web dashboard, not a console.
- Amber used as a brand accent on ordinary chrome → the state signal is
  diluted and "current cue" stops standing out.
