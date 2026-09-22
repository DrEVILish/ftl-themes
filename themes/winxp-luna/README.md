# Windows XP Luna

> The default XP look — rounded glossy blue chrome, green Start button, Tahoma.

## What this theme is trying to achieve

The **Windows XP Luna Blue** desktop theme — the one nearly everyone who
used a computer between 2001 and 2007 saw by default. Rounded window
corners, a glossy blue title bar, a tan-grey dialog body, and the green
Start button. The target is that specific, extremely-recognisable default
skin — not the later Royale/Media Center refresh, and not the Olive/Silver
alternate palettes (those are cheap follow-ons once this one is right; see
`docs/theme-backlog.md`).

## Core values

1. **Gloss, not flat.** Every filled surface — buttons, the title bar, the
   table header — is a vertical gradient with a highlight near the top,
   not a flat fill. This is what separates Luna from Windows 95's matte
   bevels or a modern flat-design button.
2. **Rounded, not sharp.** `--ftl-radius: 0.4rem` as the baseline, and the
   primary/success buttons go fully pill-shaped (`border-radius: 999px`)
   in an explicit homage to the Start button specifically — that one
   button was rounder than the rest of the UI, and this theme keeps that
   asymmetry rather than rounding everything equally.
3. **Tan-grey dialog body, not white.** `#ece9d8` is the actual Luna
   dialog background color — a warm off-white, distinct from a modern
   theme's pure white or grey.
4. **Two accents doing two different jobs.** Blue (`--ftl-accent`) is the
   chrome/selection color — title bars, the nav bar, selected rows. Green
   (`--ftl-flare`, reused as `--ftl-success`) is specifically the Start
   button's color, so success/"go" actions read as an intentional callback
   to it rather than an arbitrary green.
5. **Tahoma is not optional.** It's as much a part of the era's identity as
   the blue gradient; the fallback stack only exists for systems that
   truly lack it.

## Signature details

- Modal headers take the same rounded-top blue gradient as the title bar,
  white bold text — a modal is a small window, styled like one.
- The page backdrop is an abstract sky-blue gradient evoking the classic
  desktop, not a reproduction of the Bliss wallpaper photograph — the
  content "window" (`.ftl-app`) floats on it with a drop shadow, the same
  way Aqua's Mac window floats on its desktop gradient.
- Selected table rows use `#316ac5`, the actual Luna Explorer
  selection-highlight blue, not a generic accent tint.

## Layout

The app shell becomes a **desktop window**: a 2.6rem glossy blue title bar
with rounded top corners, a tan content well, and a light-blue status strip
with rounded bottom corners — the whole shell reads as one XP window sitting
on the sky backdrop, the same "boxed" treatment Windows 95 and Aqua use for
their own eras.

## Tell-tales of an inauthentic result

- A flat (non-gradient) title bar or buttons — Luna is defined by its gloss.
- Sharp corners anywhere in the shell or on the primary button.
- White or grey dialog backgrounds instead of the warm `#ece9d8` tan-grey.
- A green that doesn't trace back to the Start button — an arbitrary
  "success green" instead of the specific Luna one.
- Any font stack that doesn't lead with Tahoma.
