# Windows XP (Luna)

> The default Luna Blue desktop — glossy blue chrome, green go, rounded windows.

## What this theme is trying to achieve

The **Windows XP desktop as it shipped**, before anyone changed a setting:
the royal-blue glossy title bar with rounded corners, the tan/silver
"Luna" content background, Tahoma set everywhere, and the confident green
of the Start button. This is the theme most people picture the instant
someone says "Windows XP."

## Core values

1. **Gloss is the whole personality.** A light highlight band over every
   filled surface — the title bar, buttons, the nav bar — is what separates
   Luna from the flat Windows 95 look it replaced. Losing the highlight
   line at the top of the title bar is the single biggest tell.
2. **Round, never sharp.** `--ftl-radius: 8px`, and windows themselves get
   rounded top corners. XP retired square dialogs on purpose.
3. **Blue chrome, tan content.** The title bar and taskbar are the vivid
   royal blue (`#0054e3`); the actual working area is the calmer
   `#ece9d8` tan, with white cards for real content. Don't paint the
   content area blue — that's the chrome's color, not the page's.
4. **Green means go, blue means select.** The Start-button green is
   reserved for primary/affirmative actions; the selection blue
   (`#316ac5`) is for "this row is chosen," not "click me."
5. **Tahoma, not a modern system font.** Segoe UI is the *next* Windows —
   swapping it in undoes the one typographic signal that says "XP."

## Signature details

- Modal headers repeat the title bar's exact three-stop gloss gradient.
- Buttons carry a 1px `#7f9db9` border and an inset top highlight — the
  "is this actually pressable" cue XP relied on before flat design existed.
- The primary button variant brightens toward `#3f9eff` at the top of its
  gradient, distinguishing it from a plain gloss button at a glance.

## Layout

The app shell becomes an **XP window**: a glossy round-cornered blue title
bar on top, a darker-blue taskbar-style strip on the bottom, and the tan
Luna background filling the well between them.

## Tell-tales of an inauthentic result

- A flat, single-color title bar with no gloss highlight.
- Square corners anywhere on the window frame.
- Segoe UI or a modern system font in place of Tahoma.
- Blue used for the content background instead of the tan/white pairing.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

Requires: L1 — the app shell (`.ftl-app-*`) markup is needed for the
intended layout; at L0 the bundle renders recolored only.
