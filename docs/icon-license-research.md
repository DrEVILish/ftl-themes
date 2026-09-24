# Icon source license research

Companion to `icon-library-roadmap.md`. That doc commits this project to
**original, in-house line drawings** as the default sourcing strategy, but
several existing icon families were evaluated as possible vendor-in
sources (either for the generic 2,000-icon set, or for theme-specific sets
like a Win95/WinXP/Win7 "folder" icon). This doc records what was actually
checked, so "we didn't use X" or "we could vendor Y" isn't just asserted
from memory.

The bar for "usable here" is stricter than "free to use in one app": this
library is vendored **verbatim, in bulk, as SVG source**, embedded into
**other people's bundled CSS/asset pipelines**, across **22 themes** and
however many consuming apps end up using `ftl-themes`. That means:

- A license that requires per-use or per-page attribution is a bad fit —
  there's no natural place to put a required attribution link inside a
  CSS icon sprite, and a consuming app has no reason to know it owes one.
- A license that's "free for the icons you already downloaded, but revocable
  or paid to keep using going forward" doesn't work for something meant to
  be redistributed indefinitely as part of an open component library.
- "Free with attribution" can be fine for a single app's about page or
  credits screen. It is a poor fit for a sprite sheet reused by other
  projects' bundles, where the requirement doesn't travel with the asset.

## Table

| Source | License | Attribution required? | Safe to bulk-vendor SVGs verbatim? | Notes |
|---|---|---|---|---|
| Bootstrap Icons | MIT | No (but customary/appreciated; MIT requires retaining the copyright/license notice, not per-use attribution) | Yes | Already used elsewhere by the project owner (`cutepi` vendors the compiled font+CSS). Only a compiled webfont was available in this environment — no raw SVG path data to extract. If upstream SVG source is supplied, MIT permits vendoring verbatim with the license notice retained. See `icon-library-roadmap.md`. |
| Font Awesome (Free tier) | Icons: CC BY 4.0. Code/CSS: MIT. Fonts: SIL OFL 1.1 | Yes, for the icons (CC BY 4.0 requires attribution) | No — attribution-per-icon-set doesn't scale to 2,000+ icons x 22 themes x N consuming apps | Explicitly rejected as a source in `icon-library-roadmap.md` for exactly this reason. No path data used. |
| Feather Icons | MIT | No | Yes | Simple stroke-outline style, same visual convention this library already follows. Not currently vendored; noted here as a candidate if the project owner wants a broader base set later. |
| Lucide (Feather fork) | ISC (functionally MIT-equivalent, permissive) | No | Yes | Actively maintained descendant of Feather with a much larger glyph count; same considerations as Feather. |
| Tabler Icons | MIT | No | Yes | Large (5,000+) outline icon set, same general visual convention (stroke-based, `currentColor`-friendly). Good permissive-license candidate for bulk vendoring if the project ever wants to short-circuit hand-drawing the 2,000-icon generic set. |
| Material Symbols / Icons (Google) | Apache License 2.0 | No | Yes | Permissive, no attribution required, but the visual style (filled/rounded, variable-weight system) is a bigger departure from this library's established stroke-outline convention than Feather/Tabler/Bootstrap Icons are. |
| **Icons8 — "folder" set** (`icons8.com/icons/set/folder`) | Two-tier: **Free plan** = a proprietary Icons8 license modeled on CC BY-ND (attribution required); **paid plan** ("Universal Multimedia Licensing Agreement", subscription or ~$199/icon one-off) = attribution-free, but revocable/subscription-gated per Icons8's own terms | **Yes, under the free plan** — Icons8's free license requires a visible hyperlink back to icons8.com wherever the asset is used (their help center describes needing to link on every page that uses the asset, or a sitewide footer link as a minimum). Not required under a paid Universal Multimedia Licensing Agreement, but that removes the "free" framing and is a commercial license the project owner would have to purchase and maintain, per icon downloaded. | **No, not practical for this project even on the free tier** | Checked against `icons8.com/license` and Icons8's own help-center licensing pages. Confirmed: attribution requirement is a property of Icons8's *account tier* (free vs. paid subscription), not of the icon's visual style — the "folder" set is offered in multiple styles (e.g. Windows 11/Fluency, Color, iOS, Filled) but all styles sit under the same sitewide licensing terms; there is no style that is separately public-domain or attribution-free by itself. **This is a hard mismatch for a component library**: an attribution-link requirement can be satisfied on a single app's page or credits screen, but there's no clean place to attach "link to icons8.com" inside a CSS icon sprite that other people's apps bundle and reuse — the obligation doesn't travel with the SVG the way an MIT notice-in-source does, and a downstream consuming app would have no way to know it owes that link. Paying per icon (or maintaining an Icons8 subscription indefinitely, with the "keep using after cancellation" carve-out only covering already-downloaded assets) is a real ongoing cost/process burden at 2,000+ icons x 22 themes, similar in kind to the Font Awesome rejection above but with an added revocability wrinkle the CC BY 4.0 case doesn't have. **Verdict: do not vendor Icons8 SVGs (any style, including the folder set) into this library**, free or paid tier, for the same "attribution/licensing doesn't scale to a redistributed sprite" reason Font Awesome was rejected — and additionally because the paid route is a per-asset purchase, not a one-time permissive grant. Keep it out of scope; the win95/winxp/win7 "folder" icons stay original, hand-drawn per `icon-library-roadmap.md`'s existing folder-icon worked example. |

## Bottom line

Nothing here changes the roadmap's default: **original, in-house line
drawings**, in the existing 24x24 stroke-outline convention. The
permissive-license families above (Bootstrap Icons, Feather, Lucide,
Tabler, Material Symbols) remain plausible future accelerants *if* the
project owner explicitly decides to vendor rather than hand-draw, since
none of them carry a redistribution-hostile attribution clause. Font
Awesome's Free tier and **all of Icons8 (including the folder set, in
every visual style it ships)** are excluded on the same underlying
reasoning: attribution obligations that make sense for one app's UI don't
have anywhere to attach once the asset is redistributed inside a shared,
themeable icon sprite consumed by other people's bundles.
