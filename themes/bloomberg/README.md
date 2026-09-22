# Bloomberg Terminal

> Black-and-amber data density — every pixel is monospace.

## What this theme is trying to achieve

**The financial data terminal look**: amber-on-black monospace text at
maximum density, function-key yellow, and a second cyan data category —
built for scanning a wall of numbers fast, not for looking friendly. This
is the catalog's extreme-density stress test as much as a period theme.

## Core values

1. **Everything is monospace.** `--ftl-font` and `--ftl-font-mono` are the
   same stack — headings, labels, buttons, body text, not just numeric
   readouts. A proportional-font heading next to monospace data is the
   single biggest tell this isn't authentic.
2. **Amber is the workhorse, yellow is the function key.** `--ftl-text` is
   amber; `--ftl-accent` is a brighter function-key yellow reserved for
   interactive elements. Losing that split makes everything read as one
   flat color.
3. **Cyan is the second data category.** `--ftl-accent-2` exists so a
   second kind of information (a different data feed, an idle state) can
   be color-coded distinctly from the primary amber — real terminals code
   meaning into color, never decoration.
4. **Density over chrome.** `--ftl-density: 0.7` — the tightest theme in
   the catalog on purpose. No decorative rail, minimal padding, a data
   wall rather than a spacious dashboard.
5. **Zero radius, zero gloss.** Every corner is square; every fill is
   flat. This is a data terminal, not a consumer app.

## Signature details

- Buttons are outlined amber-on-black at rest and invert to filled yellow
  with black text on hover — the terminal function-key press.
- Table cells get vertical rules between columns (`border-right`), a grid
  look real terminals use to keep dense columns readable.
- The status strip text is cyan, not amber — a second information channel,
  distinct at a glance from the primary data color.

## Layout

The shell becomes a **data wall**: a thin 1.8rem function-key bar, no
decorative rail at all (density wins over chrome), and a status strip that
reads as another data row rather than a conventional status bar.

## Tell-tales of an inauthentic result

- Any proportional (non-monospace) font anywhere on the page.
- Rounded corners or a gradient/gloss fill on any control.
- Generous padding or a spacious, low-density layout — this theme should
  feel cramped by this catalog's normal standards, deliberately.
- Cyan and amber used interchangeably instead of coding distinct meaning.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

Requires: L1 — the app shell (`.ftl-app-*`) markup is needed for the
intended layout; at L0 the bundle renders recolored only.
