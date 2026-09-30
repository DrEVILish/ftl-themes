# Windows Media Player 11

> Black glass with a cool blue glow — WMP11's signature skin.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

**Windows Media Player 11's black-glass skin**: a dark translucent chassis,
cool blue illumination from beneath the controls, and softly rounded glass
panels. The Vista-era "glass" idiom done in its most restrained form.

## Core values

1. **Glass, not solid.** Surfaces are translucent gradients with a blur
   behind them. A fully opaque panel loses the idiom.
2. **Light comes from below.** Blue glow sits under controls and behind the
   bar — the player is lit from inside.
3. **Cool blue only.** `#3fa9f5`/`#7fd1ff`. Warmth anywhere reads as a
   different era.
4. **Generously rounded.** `--radius: 0.8rem` — glass panes have soft
   edges, unlike WinAmp's hard chassis.
5. **Restraint.** Vista glass is easy to overdo; the bloom should be
   noticeable only in motion and on hover.

## Signature details

- **The tab strip.** The app bar is WMP11's black glossy strip (a hard
  gloss break at 50%): nav items become evenly spaced tabs split by
  hairline dividers, the current one a blue glossy box with the small ▼
  under it, and the round back/forward orbs sit at its left end (inline
  SVG, no markup).
- **The transport bar.** The status strip is the black glossy player bar
  with a blue seek line along its top edge and, centred, the transport
  capsule — stop, prev | round blue play orb | next, volume — drawn as one
  inline SVG. Decorative only; it is dropped under 1000px so it never
  covers the app's own status text.
- **Blue silk** — WMP11's default visualization — fills the content well
  (and the bare page, for apps without the shell) as bright light ribbons
  over deep navy; the black-glass panels float on it.
- **Panel headers** are the player's list-pane header bars: dark gloss
  split at the middle, white text, a hairline highlight.
- **One "selected" look:** the blue glossy capsule of the active tab
  (`--wmp-capsule`) marks every selection — page tabs, segmented
  controls, pagination, selected rows and list items.
- **Seek bar:** progress is a thin glowing blue line in a black groove;
  slider thumbs are small glossy blue orbs.
- Panels and the modal carry a genuine specular highlight band across
  their upper half (a bright-to-transparent gradient layer), the actual
  glossy-glass reflection, not just a faint ambient shadow — that band is
  what makes the idiom read as glass at a glance instead of as a plain
  dark panel with a blue border.
- Buttons are a dark top-lit gradient that gains a strong blue halo on
  hover.
- The round GO button carries the same idea at its most concentrated: a
  bright convex highlight cap over its top half plus a wide blue bloom —
  WMP11's single most recognizable lit element.
- Semantic variants keep gradient fills so danger/success still read
  against the neutral glass base button.
- The slider thumb glows — the volume/seek control is the lit part.

## Layout

The shell becomes **one player window**: tab strip on top, blue-silk
content well, transport bar along the bottom, joined with no gaps and
6px outer corners.

## Tell-tales of an inauthentic result

- Opaque panels → the glass is gone.
- Warm or saturated accent colours.
- Sharp corners.
- Glow on everything rather than on hover and the active control.

## Don'ts

- **No light or white fields.** Inputs are recessed dark panes.
- **No flat blue discs for the play button**; it needs the glass cap highlight and glow.
- **No warm accent**; the glow is cool blue.
- **No opaque grey chrome**; it is black glass with a cool backlit seam.
- **No square, hard-edged controls**; radius is `0.4rem`.

## Typography

`--font` is `"Segoe UI", Tahoma, sans-serif`; `--font-mono` is `Consolas, monospace`. **System fonts, nothing vendored.** `RESEARCH.md` does not name a face; WMP 11 on Vista used Segoe UI and on XP used Tahoma, which is what the stack encodes (unverified against the MiniMode XP/Vista capture). On non-Windows systems the generic sans renders.

## Contrast honesty

No AA lift is recorded in `theme.css` for this theme, and none is needed: the colours are dark-on-light-accent by design.

- `--accent` `#3fa9f5` is 7.73:1 on `--bg` and 7.17:1 on `--surface`; `--on-accent` `#05050a` is 7.95:1 on it. `--accent-2` `#7fd1ff` (headings) is 10.89:1 on `--surface`.
- **The blue glow is decoration, not contrast.** The focus ring, slider-thumb bloom and heading `text-shadow` use `rgba(63,169,245,…)` halos; text always sits on its own solid colour, so nothing depends on the glow for legibility.
- `--muted` `#8888a0` is 5.31:1 on `--surface` and 4.79:1 on `--surface-2`.
- `RESEARCH.md` records no hex, so `#3fa9f5` and the black-glass greys are the theme's own numbers.

## Reference status

`references/wmp11/` has 4 captures plus `RESEARCH.md`: `Windows_Media_Player_11_in_MiniMode_-_XP,_Vista.png` and `images.jpg` (MiniMode chrome), a Now-Playing visualization webp and `wmp11.jpg` (blue-silk visualization). They back the black glass, the blue glow and the round play button. `RESEARCH.md` names the gap: no clean Library-view capture remains, so the tab strip and breadcrumbs are not evidenced by a file.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
