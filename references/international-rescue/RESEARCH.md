# International Rescue (Thunderbirds, 1965) — research notes

Purpose: back the `international-rescue` theme's palette, shape language and
type choices. Palette, shape and type guidance only: no logo, insignia
artwork, character likenesses or screenshots are reproduced anywhere.

Method: WebSearch (result summaries). Direct WebFetch of Wikipedia, the
Thunderbirds Fandom wiki, gerryanderson.com, theasc.com, fontsinuse.com and
tvtropes.org was blocked by the egress proxy, so every claim below rests on
search-result summaries of those pages, not on my reading the pages in full.
Treat "verified" below as "stated consistently by search summaries of
independent pages", not as first-hand.

## Verified

| Claim | Source | Used for |
|---|---|---|
| IR uniform: a dark blue body suit with a coloured sash over the left shoulder, holstered belt, pointed hat, coloured-lined boots; sash carries the IR emblem; hat has an oval IR badge. Each Tracy brother has a distinctive colour on sash, hat and boots. | https://thunderbirds.fandom.com/wiki/International_Rescue_Uniforms ; https://gerryanderson.com/en-us/blogs/blog/thunderbirds-thursday-the-international-rescue-uniforms (via search summaries) | `--app-bar-bg` deep navy `#0a2f6e`; diagonal-band motif; coloured accents as per-craft codes |
| Thunderbird 1: blue and silver | Search summaries citing https://en.wikipedia.org/wiki/List_of_Thunderbirds_vehicles and https://tvtropes.org/pmwiki/pmwiki.php/Series/Thunderbirds | `--accent` (blue) and info/primary semantics |
| Thunderbird 2: green (carries the land-based machines) | same | `--success` / `--lamp-on` |
| Thunderbird 3: orange-red ("to stand out in both blue sky and black space") | same | `--danger` |
| Thunderbird 4: yellow ("for high visibility in murky depths") | same | `--warning` |
| Thunderbird 5: gold and silver ("all the other colours were already taken") | same | rail lamp 5 is silver with gold ring |
| Tracy Island: designed by Derek Meddings, interiors by art director Bob Bell with production designer Keith Wilson; interiors have "characteristically large banks of controls and monitors" scaled to puppets; lounge hides launch chutes behind walls and under furniture; wall portraits of the brothers flash their eyes for incoming calls | https://en.wikipedia.org/wiki/Tracy_Island ; https://gerryanderson.com/en-us/blogs/blog/thunderbirds-thursday-celebrating-tracy-island | Big-controls/chunky-console shape language; lamps as hero indicators |
| The swimming pool basin slides aside to reveal the TB1 launch aperture; palm trees fall away for TB2's runway | https://thunderbirds.fandom.com/wiki/Swimming_Pool_(Tracy_Island) ; https://www.gerryanderson.com/thunderbirds-all-about-tracy-island/ | Concept only: the `.transport` bar and `.btn-go` as "the thing that slides the pool away" |
| Countdown "5, 4, 3, 2, 1 - Thunderbirds Are Go!" (Peter Dyneley as Jeff Tracy) opens the title sequence | https://en.wikipedia.org/wiki/Thunderbirds_(TV_series) ; https://thunderbirds.fandom.com/wiki/Title_Sequence | `.btn-go` label voice: uppercase heavy italic; go button is the loudest object on the page |
| "F.A.B." = IR's radio acknowledgement ("message received and understood"); the writers meant it to sound "hip" (from "fabulous"); "Fully Advised and Briefed" is a later fan/expanded-universe backronym | https://thunderbirds.fandom.com/wiki/F.A.B. ; https://gerryanderson.fandom.com/wiki/F.A.B. | README/docs wording only (no UI use) |
| Series filmed in colour though UK TV was still black-and-white; the 1966 feature used Supermarionation, Technicolor and Techniscope | https://en.wikipedia.org/wiki/Thunderbirds_(TV_series) ; https://en.wikipedia.org/wiki/Thunderbirds_merchandise | Justification for saturated flat primaries |
| Title/logo lettering: Microgramma is reported as used in many Gerry Anderson shows including Thunderbirds; a fan face "Anderson Thunderbirds Are Go" (Steve Ferrera) is based on the logo; craft-side lettering is commonly attributed to Univers 59 Ultra Condensed (with the caveat it may have been hand-painted or Letraset) | https://en.wikipedia.org/wiki/Microgramma_(typeface) ; https://fontsinuse.com/uses/43328/thunderbirds-captain-scarlet-and-ufo-tv-serie ; https://office-watch.com/2021/thunderbirds-are-go-in-office/ (via search summaries) | Typography note: no font vendored |

## Corrections to the brief's assumptions

- **Thunderbird 5 is gold and silver, not silver-white.** Rail lamp 5 is silver
  with a gold ring; it is not used as a semantic colour.
- **Thunderbird 1 is blue AND silver.** Only the blue is used.
- **"Cobalt uniform with gold buttons" is not confirmed.** Sources say "dark
  blue" with coloured sashes. The navy `#0a2f6e` is a design choice from that
  ("dark blue"), and gold trim is a design choice tied to the IR/TB4/TB5
  gold-yellow family, not a documented uniform button colour.
- **The title-card type may not be a "chunky italic sans".** The evidence
  points to a Microgramma-like extended face. The theme's heavy italic
  heading is an interpretation of the brief's "Thunderbirds are GO" energy,
  not a reproduction of the logo.

## Could not verify

- Exact hex colours of any craft, the uniform or the sets (no source gave
  hexes; all hexes in the theme are designed and WCAG-checked, not sampled).
- Per-brother sash colours in the 1965 series. Summaries I saw were of the
  2015 series wiki pages (Virgil green, Gordon yellow, Alan red), which need
  not match 1965. The theme does not assign brothers to colours.
- Brains' lab and Jeff Tracy's desk interior colours (cream/grey console
  panels, toggle/rocker switches, punched tape) — the "large banks of
  controls" statement is sourced; the specific panel colours, switch types
  and cream/white finish are period-plausible (1960s atomic-age design) but
  unsourced here.
- The "IR" wall/sash emblem's exact geometry. Deliberately not reproduced;
  the theme uses a generic diagonal-hazard band instead.
- Licence status of any font. No font is vendored; system stacks only.
