# iOS (Skeuomorphic)

> iPhone OS 1 to iOS 6 (2007-2012), with iOS 6 Settings as the peak:
> glossy blue bars, pinstripes and rounded white cells.

**Requires: L1.** The theme sets `--app-*` layout properties. At L0 (tokens only) it recolors correctly, but you only get the iPhone layout (status strip, nav bar, tab bar) once the app shell is adopted. See "Adoption" below.

**Family:** iOS, root theme.

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

- **The navigation bar** is the iOS 6 steel blue: a smooth fall from a
  pale sheen at the top to the reference's `#5d779c`, with an inset white
  highlight line, a bold white embossed
  title and capsule bar buttons. A menubar in the bar and filter chips
  (`.badge-button`) on a bar are capsule bar buttons too. The active
  one is the brighter "Done" blue. Every label on a blue bar, switch and
  check labels included, is white and embossed. A black iPhone status strip sits above
  it in the app shell, with a drawn signal row, a centred bold "9:41 AM"
  clock (generated content with empty alt text, so screen readers skip it)
  and a battery.
  The nav bar and the tab bar are pinned (sticky), as UINavigationBar and
  UITabBar were; on phones, where the demo bar wraps to three rows, only
  the tab bar stays pinned.
- **The tab bar** is the black glossy `UITabBar`. It is used both for the
  app shell's status strip and for `.tabs`. Tab items keep a fixed width and
  centre as a group, as on an iPad, and share the bar evenly on phones
  (icon over label when a tab has one; text-only labels are 0.8rem bold).
  The selected tab is a lit square
  whose label glows blue. Status text and ghost buttons on the black bars
  (status strip, `.transport`) take light inks.
- **The slider** is the `UISlider` groove: a blue minimum track and a
  white-to-grey maximum track, each with a rim and an inset shade along
  its top, round-capped, painted inside the padded 24/44px hit area, and
  a white pearl knob. Firefox draws the blue track with
  `::-moz-range-progress`; Chromium has no fill pseudo-element, so the
  knob paints it as a border-image reaching back from the knob's left
  edge (it paints above the knob's fill, so it stops there) to the groove's start,
  cut to the rounded end by a clip-path notch (left-to-right horizontal
  sliders; the two-thumb `.slider.is-range` draws its own). A vertical
  slider turns the rim and shade 90 degrees.
- **A side rail** (`.nav-rail`) is Mail's mailbox list: one rounded white
  cell group with bold black labels and single hairline separators; the current
  mailbox is the blue selected cell. Capsule bar buttons stay on bars.
- **The switch** is a 4.1em pill: an "ON" in white on blue at the left, or
  an "OFF" in gray on white at the right, with a full-height white knob.
  The track never shrinks; a squeezed row truncates its label instead.
- **The selected cell** is the `#058cf5` to `#015fe6` gradient with white
  text, and status text inside it turns white too (`.is-selected` and
  `aria-selected="true"` rows, stacked-table labels included).
- **Section headers:** a `.panel-header` is the grouped-table section
  title, bold `#4c566c` with a white emboss and no bar. `.table th` is the
  slim plain-table strip, a gray-blue gradient with white bold type.
- **Text on the pinstripe** (intro copy and breadcrumbs placed straight
  in `.app-main`, and every `h1`-`h3` in `.app-main` that is not inside a
  cell, card, panel, list, table, modal or other filled surface) is slate
  `#4c566c` with the white emboss of iOS 6 header and footer text, so a
  page title is the same colour on every page. Text inside cells has none.
- **Grouped cell titles** (`.field-row > .label`) are 17pt-sized
  (1.0625rem) bold black, as Settings' "Wi-Fi" and "Airplane Mode" are.
  Adjacent `.field-row`s join into one grouped section: no gap, a single
  `#cacaca` separator, and rounded corners only on the first and last row.
- **Checkboxes and radios** (iOS 6 had neither) are glossy white wells in
  the `#8e9299` bar-button rim; checked, they show the `#385487` checkmark
  of a selected table cell (a dot for a radio).
- **Content toolbar icons** (`.btn-ghost.btn-icon`) are plain `#385487`
  glyphs with a 44px hit area that show the bordered white bar-button
  capsule on hover and focus. Every button and badge label is bold (700).
- **The segmented control** splits into equal-width segments, as
  `UISegmentedControl` always did.
- **Avatars** are the Contacts photo well: pale `#e4e6ea` with slate
  `#4c566c` initials inside a white mat and a soft drop shadow.
- **Message bubbles** are the iOS 6 SMS bubbles (grey received, green
  sent) with a curved tail at the bottom corner toward the sender.
- **Window controls** (`.btn-min`, `.btn-max`) in a modal header are dark
  capsule bar buttons beside the "Done" capsule.
- **Badges and filter chips** (`.badge`, `.badge-button`) are glossy
  split pills with bold embossed labels; an active chip is the Done blue.
  A count badge inside a selected blue cell (rail item, list row, table
  row) inverts to white with a `#015fe6` figure, as Mail's counts did.
- **Pagination** is a row of bordered white bar buttons (the segmented
  control's split gradient, `#8e9299` rim, bold slate labels); the
  current page is the Done blue.
- **Fields in table cells** keep a 44px minimum width, so a narrow table
  scrolls instead of squeezing a touch target.
- **The modal** is the UIAlertView: navy glass with a gloss band at the
  top, a white rim, centered white text and dark glossy capsule buttons
  that stretch to fill the row. The primary button is lighter, as OK was.
- **Textures:** `.drawer` is Notification Center linen. `.textarea` is the
  Notes legal pad (ruled, with a double red margin and a Noteworthy face
  where available). `.hero` is Game Center felt in a wood rim.
  `.band.is-tinted` is stitched Calendar leather.
- **Small things:** `.badge-danger` is the SpringBoard red badge with a
  white ring. `kbd` is an iOS keyboard key. A popover gets the iPad's thick
  navy frame. Toasts are the iOS 5 black notification banner with a black
  rim; a status toast leads with a small glossy tile in its tone, where the
  banner showed the app icon. Inline alerts are grouped cells with a 1px
  tinted rim and no side stripe. Tappable
  list rows (links, buttons and radio-select rows) get a grey disclosure
  chevron; a row that draws its own trailing chevron icon shows it in
  the same `#7b7b7b`. An `.accordion-item` is a grouped cell whose grey
  chevron turns down when open; dropdown and context-menu rows are square
  table cells with straight hairline separators; `.scrollspy-nav` is a light bordered toolbar.

## Layout

An iPhone app at desktop width. The black status strip and blue nav bar
run edge to edge at the top, the pinstriped grouped table fills the
middle with wide side margins, and the black glossy tab bar holds the
status strip at the foot with its items centered. There is no rail,
because iOS apps had none, and no window frame, which is what sets this
apart from `aqua`.

## Deliberate deviations from the reference

- The real iOS 6 nav bar runs from `#b8c9de` to `#5d779c`; a white title
  on its top half is about 1.7:1. This theme's background gradient spans
  only `#5d779c` to `#5a7499`, so white holds 4.5:1 at every stop
  (`scripts/check.py` measures them). The paler steel of the upper bar
  is an inset sheen (two stacked shadows) over the upper half of the bar:
  a 1px `#eff2f7` line, then about `#afc0d4` falling to `#5d779c` a
  little above mid-bar (about 40%; any lower and small bar text drops
  under 4.5:1), and the bold 1.25rem title (large
  text) stays at 3:1 or more from its cap line down; bar buttons sit on their own
  capsules. The bar is smooth, with no 50%
  break, as the reference is. Do not lighten the stops.
- The count badge (`#8795af` in the reference) and the plain-table
  header strip are darkened for the same reason: their white labels are
  below WCAG's large-text size, so they need 4.5:1.
- Instrument readouts keep extra padding (`0.3em 0.5em`) inside their
  black gloss box, so the figures never touch the painted edge.
- The pinstripe contrast is raised slightly, so it still reads on a
  desktop panel. It is drawn as one 7px tile (not a repeating gradient)
  to keep scrolling cheap on phones.

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

## v5 layout

- **Tiers.** No rail. Phones and tablets: core puts the title and bar buttons on line 1 and the glossy nav buttons (or a menubar) on line 2, with their labels centred in the 44px buttons; phones tighten the button padding. Content padding is set per tier (`--app-main-padding-mobile|-tablet`).
- **Nesting.** A panel, card, list, field row or table inside the navy alert view (`.modal`) goes back to black-on-white without the emboss, so its text no longer inherits the alert's white embossed type onto a white cell. Stacked-table labels use `--muted`.
- **XL gutter art (1801px+).** The grey linen of the iOS 6 notification shade and lock screen, woven from two fine crossing stripe sets and a soft vignette.

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

## Icons

`icons.svg` redraws the whole core icon set (178/178) as iOS 6-era solid
glyphs, drawn for this project (not Apple artwork):

- **Grid:** 24×24 viewBox, glyphs kept inside roughly 2–22.
- **Fill vs line:** every closed body is a solid silhouette (bell, folder,
  envelope, camera, clock face…). Interior detail is knocked out of it as an
  evenodd cut-out (the clock's hands, the envelope flap, a document's text
  lines, the camera lens ring), never drawn on top in another colour.
- **Stroke:** bodies carry a 1px round-join outline that softens their
  corners; free lines (chevrons, arrows' shafts, rings such as search) are a
  chunky 2.4 with round caps; arrow heads are solid triangles.
- **Colour:** `currentColor` only. The emboss and gloss of the real tab bar
  come from the theme's CSS around the icon, so the same glyph works grey in
  an idle tab, white on the blue bars and blue in a selected item.

The file is generated from one geometry source shared with `ios-flat` and
`liquid-glass`, each rendered in its own language (here: filled with
cut-outs).
