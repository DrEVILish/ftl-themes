# iOS (Skeuomorphic)

> iPhone OS 1 to iOS 6 (2007-2012), with iOS 6 Settings as the peak:
> glossy blue bars, pinstripes and rounded white cells.

**Requires: L1.** The theme sets `--app-*` layout properties. At L0 (tokens only) it recolors correctly, but you only get the iPhone layout (status strip, nav bar, tab bar) once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The iPhone before iOS 7: every control is a physical object with a light
source above it. Bars are glossy blue plastic, cells are white cards
pressed into a pinstriped table, switches are slides with ON and OFF
printed on them, and Apple's own apps are dressed in linen, legal-pad
paper, felt and leather. This is the skeuomorphic entry. The flat iOS 7-18
look (thin type, white, frosted blur) is the separate `ios-flat` theme,
and the two must never converge.

## Core values

1. **Gloss has a split.** Every colored fill (bars, buttons, badges,
   selected cells) is a gradient with a hard highlight break near 50%. A
   flat fill is iOS 7, not this.
2. **Every label is embossed.** White 1px below the text on light grounds,
   dark 1px above it on colored and dark grounds.
3. **Pinstripes behind, white cells in front.** The page is the Settings
   `groupTableViewBackgroundColor` stripe. Content sits in rounded
   `#f7f7f7` cells with a `#abb0b8` outline.
4. **Bold Helvetica, black labels, blue values.** Cell titles are bold
   black. Secondary values are the detail blue `#385487`.
5. **Textures are CSS, and only Apple's.** Linen, legal pad, felt and
   leather appear where Apple used them, never as general decoration.

## Signature details

- **The navigation bar** is a blue gloss with an inset white highlight
  line, a bold white embossed title and capsule bar buttons. The active
  one is the brighter "Done" blue. A black iPhone status strip sits above
  it in the app shell, with a drawn signal row and battery and no text.
- **The tab bar** is the black glossy `UITabBar`. It is used both for the
  app shell's status strip and for `.tabs`. The selected tab is a lit
  square whose label glows blue.
- **The switch** is a 4.1em pill: an "ON" in white on blue at the left, or
  an "OFF" in gray on white at the right, with a full-height white knob.
- **The selected cell** is the `#058cf5` to `#015fe6` gradient with white
  text, and status text inside it turns white too.
- **Section headers** (`.panel-header`, `.table th`) use the plain-table
  gray-blue gradient with white bold type.
- **The modal** is the UIAlertView: navy glass with a gloss band at the
  top, a white rim, centered white text and dark glossy capsule buttons
  that stretch to fill the row. The primary button is lighter, as OK was.
- **Textures:** `.drawer` is Notification Center linen. `.textarea` is the
  Notes legal pad (ruled, with a double red margin and a Noteworthy face
  where available). `.hero` is Game Center felt in a wood rim.
  `.band.is-tinted` is stitched Calendar leather.
- **Small things:** `.badge-danger` is the SpringBoard red badge with a
  white ring. `kbd` is an iOS keyboard key. A popover gets the iPad's thick
  navy frame. Toasts are the iOS 5 black notification banner. Tappable
  list rows get a disclosure chevron.

## Layout

An iPhone app at desktop width. The black status strip and blue nav bar
run edge to edge at the top, the pinstriped grouped table fills the
middle with wide side margins, and the black glossy tab bar holds the
status strip at the foot with its items centered. There is no rail,
because iOS apps had none, and no window frame, which is what sets this
apart from `aqua`.

## Deliberate deviations from the reference

- The real iOS 6 nav bar starts at `#bdcbdc`, where a white title is
  about 1.7:1. This theme starts it at `#5b779c`, so the title and bar
  buttons hold 4.5:1 across the whole gradient. The gloss comes from the
  inset highlight line, not from a pale top stop. Do not lighten the
  gradient: `scripts/check.py` measures every stop.
- The count badge (`#8795af` in the reference) and the plain section
  header gradient are darkened for the same reason.
- The pinstripe contrast is raised slightly, so it still reads on a
  desktop panel.

## Tell-tales of an inauthentic result

- Flat fills, thin type, or a white nav bar. That is iOS 7, and belongs in
  `ios-flat`.
- A switch with no ON/OFF lettering, or the iOS 7 green switch.
- Labels without an emboss, or an emboss in the wrong direction (a white
  shadow under white text on blue).
- Cells with no pinstripe behind them, or a pinstripe running *inside* the
  cells.
- Linen, felt or leather used as a page background. Each one belongs to
  its own component only.
- An uppercase, letter-spaced label anywhere. iOS never did that.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it is correctly
recolored (pinstripes, cells, glossy controls) but uses the shell's
*default* arrangement, with no status strip and no tab bar at the foot.
Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell (CONTRACT.md "The
app shell" / "Adoption levels") to get the iPhone layout at **L1**.

## Reference status

There are 15 reference images in `references/ios-skeuomorphic/`, mostly
real iOS 6 screenshots, plus one iOS 5 alert. Sources, sampled hex values
and a component mapping are in its `RESEARCH.md`. Three pieces have no
reference image and were drawn from memory: the blue ON switch, the iPad
popover frame and the leather band.
