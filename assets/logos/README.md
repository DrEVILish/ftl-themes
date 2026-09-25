# Logo pack (`assets/logos/`)

This directory is **explicitly separate** from `assets/icons/` and is not
part of ftl-themes' own icon library or its MIT-style licensing. Read
this before adding, using, or vendoring anything here.

## What this is

`assets/icons/` is a generic, original UI icon set (folders, arrows,
media controls, hardware glyphs, etc.) authored in house and covered by
this repo's own MIT-style license. Nothing in it depicts a real company
or product — that's a hard rule for that library (see
`docs/icon-library-roadmap.md`, "Sourcing & licensing policy").

`assets/logos/` is the opposite case on purpose: **real third-party
brand marks** (company logos, product wordmarks, service icons), plus a
consuming app's own product logo(s), included here only because some
consuming apps need to *display* those marks for legitimate
interoperability/UX reasons — e.g. a "Connect your Spotify account"
button that should show Spotify's actual logo, not a generic music-note
icon, so the user recognizes which service they're linking.

A company logo is a **trademark**, not just a copyrighted graphic. Being
freely downloadable somewhere (SVGRepo's company-logo collection, a press
kit, a search result) does not grant trademark rights, and it doesn't
make the mark "open source" the way an MIT-licensed icon set is. That is
the entire reason this lives in its own directory with its own rules,
instead of being folded into the generic icon pack's merge/fallback
system.

## Rules for anything added here

1. **Never fabricate or guess a brand's logo.** Path data for a real
   company's mark must come from that company's own official,
   currently-published brand/press-kit page — verified by actually
   fetching that page and confirming it's the real company's own domain,
   not a third-party mirror, icon aggregator, or search result that
   merely claims to host "the real" file. If that page can't be reached
   or verified, don't add the logo — flag it as a documented gap instead
   (see `manifest.json`'s `pending` entries for the pattern).
2. **Every entry needs its official brand-guidelines URL recorded** in
   `manifest.json`, not just the SVG. Most companies' guidelines require,
   at minimum: show the mark unmodified (no recoloring, no distortion,
   no adding effects), respect a minimum size, respect a minimum clear
   space around it, and never imply endorsement or partnership that
   doesn't exist. Consuming apps that use a logo from this directory are
   responsible for following that specific brand's actual current
   guidelines — this repo does not restate or guarantee them, since they
   change without notice and are the brand owner's to define.
3. **This directory is not covered by ftl-themes' own MIT-style
   license.** Each logo remains the property of its respective owner.
   The exception is a consuming app's *own* product logo (see below) —
   that's the app owner's own IP, included here purely as a convenience
   asset for that app's own theming, not something this repo licenses to
   anyone else.
4. **Never vendor a real third-party brand mark just because it's easy
   to fetch.** `playlist-lab`'s `static/service-logos/` folder (Spotify,
   Apple, Amazon, Deezer, Tidal, Qobuz, YouTube, Plex, Last.fm,
   ListenBrainz, AllMusic/Billboard, etc.) is a concrete example of real
   third-party trademarks that `playlist-lab` has some basis to display
   in its own app, but which **this shared library has no redistribution
   right to bundle** — none of those files were copied in here. Adding
   any of them (or any other real brand) requires either (a) fetching
   that brand's own official SVG from their own verified official
   domain, with the guidelines URL recorded, or (b) the project owner
   explicitly supplying a file they hold the rights to use, per item 1.

## What's actually here right now

- `cutepi/` — the project owner's own **cutepi** app logos (their own
  product IP, not a third party's mark). Two variants: the primary
  `cutepi-logo.svg` and the `cutepi-logo-80s-corporate.svg` alternate
  treatment, both copied from `cutepi`'s own repo
  (`public/img/cutepi-logo.svg`, `LOGOs/cutepi-logo-80s-corporate.svg`).
- `playlist-lab/` — the project owner's own **playlist-lab** app logo
  (`playlist-lab-logo.svg`, copied from `static/logo.svg`). Deliberately
  **excludes** that app's `static/service-logos/` folder — see rule 4.
- See `manifest.json` for the structured entries, including `pending`
  placeholders for real third-party brand marks that are not yet safe to
  vendor (no verified official source fetched yet).

## Usage

```html
<link rel="stylesheet" href="assets/logos/logos.css">
<img class="ftl-logo" src="assets/logos/cutepi/cutepi-logo.svg" alt="cutepi">
```

`logos.css` is a tiny, separate, opt-in stylesheet — it is **not**
included in any theme's `dist/` bundle and is **not** processed by
`scripts/build_icons.py` or `scripts/build.sh`. Logos are not part of
the per-theme icon merge/fallback mechanism (that mechanism exists
specifically for the generic MIT-style icon set in `assets/icons/`).
A consuming app that wants a logo imports `logos.css` and the specific
SVG file(s) it needs, directly and explicitly.

## Self-hosting a third-party mark (without waiting on this repo)

A `pending` entry in `manifest.json` means "documented gap, not a usable
asset." An integrator that needs the mark now self-hosts it in their own
repo — no change here required:

1. Fetch the brand's official SVG from the brand owner's own verified
   domain (same rule 1 as above — never an aggregator or search result),
   save it as `<app>/service-logos/<brand>.svg` beside your own static
   assets, and follow that brand's guidelines page for clear space,
   minimum size, and no-endorse-implication rules.
2. Reference it directly (`<img src="…/service-logos/youtube.svg">`);
   don't add it to `assets/icons/` (rule: no third-party marks in the
   generic pack) and don't add a `file` field to this repo's
   `manifest.json` until rule 1's verified-source condition is met here.
