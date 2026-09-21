# Windows 95

> Beveled 3D gray — classic system dialog chrome on teal.

## What this theme is trying to achieve

The **Windows 95/98 desktop**: a teal backdrop, battleship-grey controls,
and the 3D bevel language that made every control look physically pressable
on a 256-colour display. The target is a system dialog, not a nostalgia
poster.

## Core values

1. **The bevel is the entire system.** Light on the top-left, dark on the
   bottom-right, inverted while pressed. Every raised thing uses it; every
   sunken thing (inputs, the content well) uses it reversed. Get this wrong
   and nothing else matters.
2. **Zero radius, everywhere.** `--ftl-radius: 0`. There were no rounded
   corners.
3. **A strictly limited palette.** Grey `#c0c0c0`, navy `#000080`, teal
   `#008080`, plus the 16-colour VGA set. No intermediate tints.
4. **Text is black on grey.** Filled controls use white on navy — never the
   page background as a foreground, which is what `--ftl-on-*` exists to
   prevent here.
5. **Focus is a dotted rectangle.** Marching-ants, not a glow. Era-accurate
   *and* accessible.

## Signature details

- Modal headers take the navy→blue title-bar gradient with white bold text.
- The content well is *sunken* (`#808080 #ffffff #ffffff #808080` plus an
  inner black line); the status strip is *raised*. The shell itself obeys
  the 3D language, not just the controls.
- Tables draw a full 1px grid — Explorer's details view, not a modern
  borderless list.

## Layout

The app shell becomes a **desktop window**: the teal backdrop shows at the
edges, a 1.6rem gradient title bar sits on top, the content is a sunken
well, and the status bar is raised. Switching to this theme visibly boxes
the app up.

## Known compromise

MS Sans Serif is not a web font and is absent from modern systems, so the
stack falls back to Tahoma — its closest ubiquitous relative. Vendoring an
openly-licensed pixel face is tracked in `docs/theme-backlog.md`.

## Tell-tales of an inauthentic result

- Uniform 1px borders instead of two-tone bevels → flat-design cosplay.
- Any rounded corner or drop shadow.
- Buttons that don't invert their bevel on `:active`.
- Anti-aliased, modern-weight type in the title bar.
