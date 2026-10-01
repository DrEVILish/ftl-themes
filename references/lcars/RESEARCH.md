# lcars — reference design notes

The design rules the `lcars` theme is built and reviewed against. Sources
are listed at the end; everything below is a summary with the specifics
kept, so the theme can be checked against it rule by rule.

## 1. What LCARS is (origin and spirit)

- LCARS (Library Computer Access/Retrieval System) was designed by
  **Michael Okuda** for *Star Trek: The Next Generation* (1987); screens
  built in it are nicknamed "okudagrams".
- Gene Roddenberry asked that panels **not have a great deal of activity**
  on them; the minimalist look was meant to read as *more* advanced than
  the original series. The flashing/scrolling-number activity seen later
  is drama, not the design's intent.
- Bold, curved lines, soft rounded buttons, **no mechanical elements**,
  black background, flat touch panels in place of physical buttons and
  switches.
- **"The LCARS swept IS LCARS."** The single most characteristic element
  is the *swept* (the elbow: a bar curving round into a perpendicular
  bar). An interface that can be expressed in one shape. Do not disfigure
  it.
- Its known flaw is space efficiency; accept it rather than cramping.

## 2. Visual nature

- A clean **vector look**: solid flat shapes, **no gradients, no emboss,
  no bevels, no outlines/strokes**. (The frames are drawn as filled pen
  shapes; only the main *data displays* inside frames may be richer —
  waveforms, schematics, gauges.)
- Frames bend "here or there" to frame whatever content they hold.

## 3. Frames

- Common frame structures: an elbow opening one way (┌, └), a bracket
  (┌ … └ closed on one side, "C"), and pairs of elbows facing each other
  across a gap (the classic TNG split frame: an upper frame whose elbow
  opens down, a lower frame whose elbow opens up). Frames can continue
  "on and on" into further elbows.
- Draw frames continuous; how many **segments** a frame is cut into
  depends on how many options it offers up front.
- **Thickness rule ("this is OMEGA"): a frame NEVER keeps the same
  thickness round the next turn.** It always goes thick → thin or thin →
  thick at an elbow. In practice the vertical side (the rail/leg) is
  thick and the horizontal bar thin.
- Frames group related controls ("localised frames"). A frame that does
  nothing but frame a category is "already a 20% sin"; a mostly empty frame
  whose frame is itself fully useful is beautiful.
- **Prefer breaking the frame itself into buttons** (segments carrying
  labels/codes) over floating separate buttons inside an empty frame —
  unless the frame is too thin to press.

### Elbow and corner geometry (from the guideline diagrams)

- **The swept**: the outer curve is a long, flat ellipse running from
  the outside of the leg into the outside of the bar; the inner curve is
  a small, true quarter circle. Both are tangent to the straight edges
  they meet — no kinks, no flat spots, no step where leg meets bar.
- One consistent inner radius `r` per frame family. Outer radius =
  `(leg width + r)` across × `(bar thickness + r)` down, which is exactly
  what keeps the inner curve circular.
- Wrong sweeps (the ✗ examples): a square notch where the curve should
  be, a cap or button glued onto the sweep, an outer curve that ends
  before the bar starts.
- **Every other corner is square.** Bar ends, leg ends, segment ends and
  blocks are cut flat; the only other round thing is the **cap**, which
  is a full semicircle (radius = half the bar's thickness), separated
  from the bar by the in-frame gap.

## 4. The cap

- The rounded **cap** is LCARS's full stop: it marks the **termination**
  of a bar. Caps appear only at a bar's free ends, facing outward.
- Its unconnected nature makes it a natural **button**.
- "Nonsense" caps (the amateur tell): caps in the middle of a run, caps
  facing into each other or into a joint, half-caps on segments that
  continue.

## 5. Buttons

- The canonical button is the **round rectangle (pill) at about a 3:1
  ratio** (reference sample 126 × 42 px). Label set in black, **in the
  bottom-right corner**.
- If the label is too long for 3:1, the pill must not be stretched; it
  changes to a variation that suits its surroundings: a **flat-ended
  block** (square on the side that meets the frame, cap on the free
  end), or **label on black followed by a cap**.
- **Conformity:** buttons inside one frame look alike. Buttons in
  different frames may use different variations.
- Labels are codes or short words; long descriptions go beside the
  control, not on it.

## 6. Spacing and grid

- Align everything to an **invisible grid**; misaligned blocks are the
  amateur's "disjointed look".
- There are exactly **two spacing constants**:
  1. **Main frame spacing** — the gap between frames (e.g. between the
     upper and lower frame's bars).
  2. **Spacing of the frame itself** — the gap between the segments
     inside one frame (smaller).
  Every other gap should use one of the two. Only the four main buttons on
  top of the frame and the text's own letter spacing are exempt.

## 7. Typography

- Use the LCARS face (Swiss 911 Ultra Compressed on screen; Antonio is
  the free stand-in here) — **one face, consistently**.
- **Only three font sizes:**
  1. **Main title** — the application's title or what it is doing now.
  2. **Sub header** — the main buttons on top of the frame and any sub
     header in the content area.
  3. **Normal data** — scrolling numbers and content details.
- **Text uses two colours:** one for normal display, one for highlight
  (the data currently being processed/selected). Anything more needs a
  reason.
- Upper case throughout; condensed; numbers are tabular codes
  (`02-654598`, `4768`).

## 8. Colour

- The easiest crime is colour "with a vengeance" — multi-colour LCARS
  from "a horrific colour vortex". A monotone LCARS beats that.
- Rules of thumb (count every hue, tint and shade):
  - **1 colour** — never wrong; up to **5 tints/shades** of it.
  - **2 colours** — fine; total hue/tint combinations **≤ 5**.
  - **3 colours** — good; stop here (maybe two more tints if needed).
  - **4 colours** — danger zone: each must **mean** something, e.g. idle,
    normal operation, real-time operation, text.
  - **5 colours** — only with a reason; what does the fifth mean, and
    what does a button flashing in it mean?
  - **6+** — "I have not seen any LCARS interface with more than five
    colours and looked right."
- Choose colours by colour theory (complementary … tetradic), not from a
  fixed "LCARS palette".
- Documented TNG hues (Okuda palette, via trekcolors): atomic tangerine
  `#ff9900`, lilac `#cc99cc`, periwinkle `#9999ff`, peach `#ff9966`, tan
  `#ffcc99`, mariner `#3366cc`, red `#cc6666`.
- Era palettes seen in the references: **TNG** orange/lilac/peach/tan on
  black; **Voyager/DS9** gold-tan and blue-violet; **Picard (2399)** grey-
  blue and ice-blue frames, pale blue text, orange-red highlight;
  **Lower Decks** cyan/teal/blue family with red alert values.

## 9. Animation and behaviour

- If a new task is needed, show a **new screen**; new controls appearing
  on a screen must **never shift existing buttons**.
- Transitions: simple **fade in / fade out** (not cross-fade), **under
  1 s** ("1 second being way too long"). Animation is not core to LCARS.
- Decorative scrolling numbers: split them into independent timelines
  with different lengths, generate numbers in code, so nothing loops
  visibly as one unit.
- Sound: optional, never annoying.

## 10. Data displays seen in the references

- **Audio / signal waveforms** (Picard *Communications*): a dark field
  with a faint grid and numbered axis ticks, the waveform in bright blue
  with a soft glow, magenta-pink peaks, and circular lock-on rings; set
  inside a bracket frame, captioned in small caps above.
- **ECG trace** (Lower Decks *Sickbay*): a single glowing line inside a
  `[ ]` bracket frame whose uprights are thick and caps thin.
- **Vertical gauges** (TNG MSD panel, left side): tall black tubes with a
  tick ruler on both sides numbered 1–5, filled from the bottom in one
  frame colour fading upward, a colour-coded code block under each
  (`318`, `195`, `458`); beside them columns of orange/white codes.
- **Data rows** (TNG MSD centre, Study "Appearance"): `[half-cap][label
  block, label bottom-right][BIG number in the frame colour][pill]` — the
  big condensed number is the value; labels are initials/codes.
- **Readout values** (Lower Decks): value in large condensed type beside
  a small coloured label pill (`O2 SAT 89.6 %`), red for alarm values.
- **Keypads/dials** (Picard, Study): circular direction pads built from
  arcs and wedges, still flat fills.

## 11. Patterns across the lcars.org.uk panel collection

512 screen-used LCARS panels captured and tagged in `lcars-org-uk/INDEX.md` (#1–#512); the same index also holds 446 non-LCARS Trek screens (alien species, Enterprise NX-01, TOS, Star Trek 2009) as #513–#958, which the patterns below do not draw on.
What recurs, and therefore belongs in the theme:

- **Elbow + segmented bars** frame almost every full screen (≈70%); the
  header is an elbow with a title at the right end of a bar, a second
  elbow opens up beneath it (split frame).
- **Columns of small numeric codes** sit in the upper frame of most
  screens (≈60%) — decoration that reads as data.
- The **content well** usually holds one data display: a schematic or
  cutaway (MSD), a map/star chart on a grid, or a waveform/graph, very
  often inside a `[ ]` bracket.
- **Pill buttons** cluster at the top-right of the header in 2–3 rows.
- Era palettes: TNG orange/lavender/peach; DS9 more blue/tan with grey
  elbows; alert screens switch the whole frame to red.
- PADD and wall-console captures show LCARS inside physical bezels —
  not relevant to the theme beyond colour.

## Sources

- Bracer Jack, *Creating a Coherent LCARS Interface* (LCARS GuideLine),
  republished at http://www.lcars-terminal.de/tutorial/guideline.htm —
  sections 2–8 above.
- Bracer Jack, *The LCARS Manifesto*,
  http://www.lcars-terminal.de/tutorial/manifesto.htm — sections 1, 3, 5,
  9 above (its "LCARS programming language" part is out of scope here).
- *LCARS Design Evolution and Principles* (study, Scribd 907412350) —
  "Appearance" page captured as `lcars-study-appearance.webp`; the full
  document is behind Scribd's wall and was not read.
- Captures in this folder: `picard-communications-tourangeau.jpg`
  (waveforms, Picard palette), `tng-msd-panel-meters.jpg` (frames,
  pills, data rows, vertical gauges), `lower-decks-sickbay-biobed.webp`
  (Lower Decks palette, ECG bracket, readout pills),
  `lcars-study-appearance.webp` (TNG panels 1987–2000), plus the earlier
  captures (`Lcars_wallpaper.svg.webp` — the TNG split frame;
  `Starship_LCARS_Interface_E_900_for_Site.webp` — Sovereign-class
  bracket frames and titles in bar breaks).
- lcars.org.uk panel galleries (TNG, TNG films, DS9, plus the Alien,
  Enterprise, TOS and Star Trek 2009 galleries) and lcars.htm, captured
  into `lcars-org-uk/` with a component index.
- Other working examples: https://www.thelcars.com/ ,
  https://github.com/MichalSvatos/pi-hole-lcars-next-gen
