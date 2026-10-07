#!/usr/bin/env python3
"""Writes the shared demo-page menu into every example page.

Each page's <nav aria-label="Demo pages"> block is replaced with one
ul.menubar built from SECTIONS below, so adding a page means one line here,
not an edit to every page. Pages that don't exist yet are left out. The
links keep data-demo-link, so theme-loader.js carries ?theme= across.

  python3 scripts/demo_nav.py          rewrite every page
  python3 scripts/demo_nav.py --test   self-check, writes nothing
"""
import html, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

SECTIONS = [
    ("Apps", [
        ("dashboard", "Analytics dashboard"), ("marketing", "Marketing site"),
        ("ticketsystem", "Support desk"), ("livechat", "Team chat"),
        ("powerstation", "Power station"), ("soundmixer", "Sound mixer"),
        ("mission-control", "Mission control"), ("smart-home", "Smart home"),
        ("trading", "Trading terminal"), ("inventory", "Inventory & assets"),
        ("fleet", "Fleet dispatch"), ("planner", "Planner"),
        ("player", "Media player"), ("hud", "Game HUD"), ("desktop", "Desktop"),
        ("signage", "Event displays"),
    ]),
    ("Vehicles", [
        ("cockpit-car", "Car"), ("cockpit-plane", "Airliner"),
        ("cockpit-jet", "Fighter jet"), ("cockpit-boat", "Boat"),
        ("cockpit-submarine", "Submarine"), ("cockpit-spaceship", "Spaceship"),
    ]),
    ("Sci-Fi", [
        ("scifi-engineering", "Engine room"), ("scifi-warp", "Warp drive"),
        ("scifi-transporter", "Transporter"), ("scifi-comms", "Subspace comms"),
        ("scifi-tactical", "Tactical & shields"), ("scifi-cartography", "Stellar cartography"),
        ("scifi-medbay", "Medical bay"), ("scifi-cryo", "Cryo deck"),
        ("scifi-replicator", "Replicator"), ("scifi-holodeck", "Holodeck"),
    ]),
    ("Templates", [
        ("auth", "Sign in"), ("settings", "Settings"), ("master-detail", "Master–detail"),
        ("inbox", "Inbox"), ("onboarding", "Onboarding"), ("pricing", "Pricing"),
        ("404", "Not found"),
    ]),
    ("Components", [
        ("gallery", "Theme gallery"), ("components", "Core components"),
        ("components-tables", "Tables"), ("components-instruments", "Instruments"),
        ("audio-components", "Audio components"), ("audio-blocks", "Audio blocks"),
        ("proseries", "ProSeries console"),
        ("metering", "Metering & EQ"),
        ("media-decks", "Media decks"),
        ("components-forms", "Buttons & forms"), ("components-navigation", "Navigation"),
        ("navigation-patterns", "Signature navigation patterns"),
        ("components-surfaces", "Surfaces"), ("components-experience", "Display settings"),
        ("components-social", "Collaboration"), ("components-prose", "Prose & code"),
        ("components-sections", "Page sections"), ("components-shop", "Shop"),
        ("nesting", "Nesting"),
    ]),
]

NAV = re.compile(r'<nav\b[^>]*aria-label="Demo pages"[^>]*>.*?</nav>', re.S)


def menu(current, exists):
    out = ['<nav class="demo-nav" aria-label="Demo pages">',
           '      <ul class="menubar" role="menubar">']
    sections = [(t, [p for p in pages if exists(p[0])]) for t, pages in SECTIONS]
    sections = [s for s in sections if s[1]]
    for i, (title, pages) in enumerate(sections):
        here = any(p == current for p, _ in pages)
        end = " is-end" if i >= len(sections) - 2 else ""
        out.append(f'        <li role="none" class="has-submenu{end}"><button role="menuitem" aria-haspopup="menu"'
                   + (' class="is-active"' if here else "") + f'>{title}</button>')
        out.append('          <ul role="menu">')
        for page, label in pages:
            cur = ' aria-current="page"' if page == current else ""
            out.append(f'            <li role="none"><a role="menuitem" href="{page}.html" data-demo-link{cur}>'
                       f'{html.escape(label)}</a></li>')
        out.append('          </ul></li>')
    out.append('      </ul>')
    out.append('    </nav>')
    return "\n".join(out)


def rewrite(text, current, exists):
    return NAV.sub(lambda m: menu(current, exists), text, count=1)


def main():
    exists = lambda p: (ROOT / f"{p}.html").exists()
    changed = 0
    for f in sorted(ROOT.glob("*.html")):
        text = f.read_text()
        new = rewrite(text, f.stem, exists)
        if new != text:
            f.write_text(new)
            changed += 1
    print(f"demo_nav: {changed} page(s) updated")


def test():
    page = '<header><nav class="nav" aria-label="Demo pages"><a href="x.html">X</a></nav></header>'
    out = rewrite(page, "dashboard", lambda p: p in {"dashboard", "auth"})
    assert out.count("<nav") == 1 and 'href="dashboard.html" data-demo-link aria-current="page"' in out
    assert "Vehicles" not in out and 'href="auth.html"' in out and "cockpit" not in out
    assert rewrite(out, "dashboard", lambda p: p in {"dashboard", "auth"}) == out  # idempotent
    print("demo_nav: ok")


if __name__ == "__main__":
    test() if "--test" in sys.argv else main()
