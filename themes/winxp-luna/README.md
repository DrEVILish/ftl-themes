# Windows XP (Luna)

> The default Luna Blue desktop — glossy blue chrome, green go, rounded windows.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

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
2. **Round, never sharp.** `--radius: 8px`, and windows themselves get
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

### Icons

`themes/winxp-luna/icons.svg` redraws six icons (home, settings, search,
close, user, bell) as glossy, two-tone glyphs: a `currentColor` fill for
the base shape, a soft white highlight band across the top for the gloss
line Luna put on every filled surface, and a thin `currentColor` outline
to keep edges crisp — the same three-layer recipe as the title bar and
buttons, just applied at icon scale. The sprite ships 135 `<symbol>`s in total (`grep -c '<symbol'`), and each differs from the generic outline sprite in `assets/icons/icons.svg`; only the six above are described here, and the rest were not audited one by one for style.

## Layout

The app shell becomes an **XP window**: a glossy round-cornered blue title
bar on top, a darker-blue taskbar-style strip on the bottom, and the tan
Luna background filling the well between them.

## Tell-tales of an inauthentic result

- A flat, single-color title bar with no gloss highlight.
- Square corners anywhere on the window frame.
- Segoe UI or a modern system font in place of Tahoma.
- Blue used for the content background instead of the tan/white pairing.

## Don'ts

- **No flat, single-colour title bar** — the gloss highlight line at the top is the theme.
- **No square window corners**, and no pill/stadium shapes either: XP is `8px` rounding, not Barbie.
- **No blue content area.** Blue is chrome; the well is tan `#ece9d8` and white.
- **No green on selection and no blue on "go".** Green is the affirmative action, `#316ac5` blue is selection.
- **No Segoe UI or system-ui swapped in for Tahoma** where Tahoma exists.

## Typography

`--font` is `Tahoma, "Segoe UI", Verdana, sans-serif`; `--font-mono` is `"Courier New", Consolas, monospace`. Tahoma is the authentic XP face (named in `references/winxp-luna/RESEARCH.md`) but it is a **system font, not vendored**: Windows and macOS ship it, most Linux installs do not, and there Segoe UI/Verdana or the generic sans render instead.

## Contrast honesty

Luna's greens and blues sit on tan/white, and several needed adjustment:

- **Start green lifted.** The community-recreation green `#3d9f1e` is 3.4:1 under white text; shipped `--success` is `#2e7a14` (5.37:1). No official hex exists (`luna.msstyles` is a compiled resource), so this is a documented departure from folk consensus, not from a published value.
- **Success text on tan:** `--success` itself is only 4.40:1 on the `#ece9d8` background, so text uses `--success-text` `#2c7613` (4.64:1 on tan, 5.66:1 on white).
- **Blue on tan:** `--accent` `#0054e3` is 5.10:1 on tan and 6.22:1 on white/under white text. The selection blue `--accent-2` `#316ac5` is 4.31:1 on tan, so use it as a fill with white text (5.25:1), not as text on the tan well.
- **Warning:** `--warning` `#ff8c00` is 1.91:1 on tan and is a lamp/fill only; text uses `--warning-text` `#9e5700` (4.51:1 on tan, a narrow pass).
- `--danger` `#cc0000` is 4.83:1 on tan, 5.89:1 under white text. `--muted` `#5a5a5a` is 5.65:1 on tan.
- The app-bar nav text uses pale tints because the black tokens tuned for the tan area measured 1.0:1 on the blue bar.

## Reference status

`references/winxp-luna/` has 5 captures plus `RESEARCH.md`: a Luna Start-button crop (`RESEARCH.md` does not map which filename is which), a March Mountain XP icon promo, a tall XP icon grid, a Luna Sample dialog and a Bliss desktop with a real Start menu. They back the royal-blue gloss title bar, the tan content colour, the green Start pill and the red-orange Close button. `RESEARCH.md` lists no hex values, so `#0054e3`, `#ece9d8`, `#316ac5` and `#7f9db9` are the theme's own numbers, not sampled from these files (unverified against them).

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
