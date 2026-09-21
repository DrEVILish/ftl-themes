# The Matrix

> Green phosphor on black — monospace terminal cascade.

## What this theme is trying to achieve

A **phosphor terminal** as filmed: monospace everything, black field,
green text with a faint bloom, and the sense that you are reading a machine
directly rather than an interface built for you.

## Core values

1. **Monospace is non-negotiable.** Every element, not just values.
2. **Green is the only colour with a job.** Semantic red exists for genuine
   errors and nothing else. Introducing a second decorative hue breaks the
   single-phosphor illusion.
3. **Bloom, not glow.** A 2px text-shadow across all text imitates
   phosphor persistence. It is deliberately subtle — a strong glow reads as
   neon, which is a different aesthetic entirely.
4. **Outline over fill.** Base controls are transparent with a green rule.
   Only semantic variants take a fill, so a delete button still reads as
   dangerous.
5. **Uppercase headings, tracked.** Terminal banner conventions.

## Signature details

- A heading flicker animation, gated behind
  `@media (prefers-reduced-motion: no-preference)` and never carrying state
  on its own.
- Panels glow faintly *inward* (`inset` shadow) as though lit from behind.
- Selected rows wash green at 12%; the active-row marker stays a hard bar.

## Layout

A **terminal**: black bar, one hairline rule, no rail, content filling the
frame. The least furniture of any theme in the catalogue — deliberately the
opposite extreme from LCARS.

## Extending it

Do: keep everything monospace; keep the bloom subtle; add new states as
brightness steps of green rather than as new hues.
Don't: add a second accent colour, use a sans-serif anywhere, or let the
flicker animation communicate anything.

## Tell-tales of an inauthentic result

- A proportional font anywhere → the illusion collapses immediately.
- Multiple accent hues → a "hacker" theme, not a phosphor terminal.
- Heavy neon glow → cyberpunk, not CRT.
