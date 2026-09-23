#!/usr/bin/env python3
"""Builds examples/<theme>.html — one showcase page per theme.

Hard rule for every page: markup uses ONLY ftl-themes' own classes plus
plain semantic HTML. No <style> block, no style="" attribute, no class that
isn't part of the library. If a page can't express something without custom
CSS, that is a gap in the library, not a reason to add CSS here (see
examples/README.md "Gaps found while building these pages").

Each page links the self-contained bundle dist/<theme>.css, so it renders
from a static file server with nothing else loaded.

Usage: python3 scripts/build_examples.py
"""
import re
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "examples"


# --- Component builders ---------------------------------------------------
# Each returns an HTML string using only .ftl-* classes.

def bar(brand, items, active=0):
    links = "\n".join(
        f'  <a class="ftl-nav-item{" is-active" if i == active else ""}" href="#">{e(t)}</a>'
        for i, t in enumerate(items)
    )
    return f"""<header class="ftl-app-bar">
  <span class="ftl-nav-brand">{e(brand)}</span>
{links}
</header>"""


def status_bar(parts):
    out = []
    for p in parts:
        kind = p[0]
        if kind == "lamp":
            out.append(f'  <span class="ftl-lamp {p[1]}" role="img" aria-label="{e(p[2])}"></span>')
        elif kind == "status":
            out.append(f'  <span class="ftl-status ftl-status-{p[1]}">{e(p[2])}</span>')
        elif kind == "mono":
            out.append(f'  <span class="ftl-mono">{e(p[1])}</span>')
        elif kind == "kbd":
            out.append("  <span>" + " ".join(f"<kbd>{e(k)}</kbd> {e(v)}" for k, v in p[1]) + "</span>")
        else:
            out.append(f"  <span>{e(p[1])}</span>")
    return '<footer class="ftl-app-status">\n' + "\n".join(out) + "\n</footer>"


def crumbs(items):
    parts = [f'  <a class="ftl-breadcrumb-item" href="#">{e(t)}</a>' for t in items[:-1]]
    parts.append(f'  <span class="ftl-breadcrumb-item is-current" aria-current="page">{e(items[-1])}</span>')
    return '<nav class="ftl-breadcrumbs" aria-label="Breadcrumb">\n' + "\n".join(parts) + "\n</nav>"


def heading(title, lede=None, level=1):
    out = f"<h{level}>{e(title)}</h{level}>"
    if lede:
        out += f"\n<p>{e(lede)}</p>"
    return out


def btn(label, variant="", tooltip=None, icon=False, aria=None):
    cls = "ftl-btn"
    if variant:
        cls += " " + " ".join(f"ftl-btn-{v}" for v in variant.split())
    if icon:
        cls += " ftl-btn-icon"
    attrs = ""
    if tooltip:
        attrs += f' data-tooltip="{e(tooltip)}"'
    if aria:
        attrs += f' aria-label="{e(aria)}"'
    return f'<button class="{cls}" type="button"{attrs}>{e(label)}</button>'


def toolbar(*items):
    """A wrapping row of controls (layout only; not the .ftl-toolbar bar)."""
    return '<div class="ftl-cluster">\n  ' + "\n  ".join(items) + "\n</div>"


def meter(label, value, low=70, high=90, optimum=0, unit="%"):
    fid = _fid()
    return f"""<div class="ftl-field">
    <label class="ftl-label" for="{fid}">{e(label)}</label>
    <meter class="ftl-meter" id="{fid}" min="0" max="100" low="{low}" high="{high}" optimum="{optimum}" value="{value}">{value}{e(unit)}</meter>
  </div>"""


def progress(label, value):
    fid = _fid()
    return f"""<div class="ftl-field">
    <label class="ftl-label" for="{fid}">{e(label)}</label>
    <progress class="ftl-progress" id="{fid}" max="100" value="{value}">{value}%</progress>
  </div>"""


def radios(legend, options, checked=0, inline=False):
    name = _fid()
    rows = "\n  ".join(
        f'<label class="ftl-check"><input class="ftl-radio" type="radio" name="{name}"{" checked" if i == checked else ""}> {e(o)}</label>'
        for i, o in enumerate(options)
    )
    cls = "ftl-radio-group is-inline" if inline else "ftl-radio-group"
    return f'<fieldset class="{cls}">\n  <legend>{e(legend)}</legend>\n  {rows}\n</fieldset>'


def anchored_menu(trigger, items, danger=None):
    out = [f'<button class="ftl-context-menu-item" type="button" role="menuitem">{e(i)}</button>' for i in items]
    if danger:
        out.append('<div class="ftl-context-menu-divider" role="separator"></div>')
        out.append(f'<button class="ftl-context-menu-item is-danger" type="button" role="menuitem">{e(danger)}</button>')
    menu = '<div class="ftl-context-menu is-below" role="menu">\n    ' + "\n    ".join(out) + "\n  </div>"
    return f'<span class="ftl-anchor">\n  {btn(trigger, aria=trigger)}\n  {menu}\n</span>'


def transport(state, go, readout=None, lamps=(), status=None, extra=()):
    parts = [f'<button class="ftl-btn ftl-btn-go" type="button">{e(go)}</button>']
    for lamp_state, label in lamps:
        parts.append(f'<span class="ftl-lamp {lamp_state}" role="img" aria-label="{e(label)}"></span>')
    if readout:
        value, unit = readout
        u = f'<span class="ftl-readout-unit">{e(unit)}</span>' if unit else ""
        parts.append(f'<span class="ftl-readout ftl-readout-lg">{e(value)}{u}</span>')
    if status:
        parts.append(f'<span class="ftl-status ftl-status-{status[0]}">{e(status[1])}</span>')
    parts.extend(extra)
    cls = "ftl-transport" + (f" {state}" if state else "")
    return f'<div class="{cls}">\n  ' + "\n  ".join(parts) + "\n</div>"




def stat(value, label, trend=None):
    t = ""
    if trend:
        direction, text = trend
        t = f'\n    <span class="ftl-stat-trend is-{direction}">{e(text)}</span>'
    return f"""<div class="ftl-stat">
    <span class="ftl-stat-value">{e(value)}</span>
    <span class="ftl-stat-label">{e(label)}</span>{t}
  </div>"""


def stats(*items):
    return '<div class="ftl-grid ftl-grid-sm">\n  ' + "\n  ".join(
        f'<div class="ftl-card">{stat(*i)}</div>' for i in items) + "\n</div>"


def cell(c):
    if isinstance(c, tuple):
        kind = c[0]
        if kind == "status":
            return f'<span class="ftl-status ftl-status-{c[1]}">{e(c[2])}</span>'
        if kind == "badge":
            mod = f" ftl-badge-{c[1]}" if c[1] else ""
            return f'<span class="ftl-badge{mod}">{e(c[2])}</span>'
        if kind == "lamp":
            return f'<span class="ftl-lamp {c[1]}" role="img" aria-label="{e(c[2])}"></span>'
        if kind == "mono":
            return f'<span class="ftl-mono">{e(c[1])}</span>'
        if kind == "trend":
            return f'<span class="ftl-stat-trend is-{c[1]}">{e(c[2])}</span>'
        if kind == "avatar":
            return f'<span class="ftl-avatar ftl-avatar-sm">{e(c[1])}</span> {e(c[2])}'
    return e(str(c))


def table(headers, rows, sort=0, sort_dir="ascending", sticky=True, caption=None):
    th = []
    for i, h in enumerate(headers):
        a = f' aria-sort="{sort_dir}"' if sort is not None and i == sort else ""
        th.append(f'<th scope="col"{a}>{e(h)}</th>')
    body = []
    for r in rows:
        state = ""
        if isinstance(r, dict):
            state = r.get("state", "")
            r = r["cells"]
        cls = f' class="{state}"' if state else ""
        body.append(f"    <tr{cls}>" + "".join(f"<td>{cell(c)}</td>" for c in r) + "</tr>")
    cap = f"\n  <caption>{e(caption)}</caption>" if caption else ""
    tcls = "ftl-table is-sticky" if sticky else "ftl-table"
    return (
        f'<table class="{tcls}">{cap}\n  <thead><tr>' + "".join(th) + "</tr></thead>\n  <tbody>\n"
        + "\n".join(body) + "\n  </tbody>\n</table>"
    )


_field_id = [0]


def _fid():
    _field_id[0] += 1
    return f"f{_field_id[0]}"


def field(kind, label, *args):
    fid = _fid()
    if kind == "text":
        value, hint = (list(args) + [None, None])[:2]
        h = f'\n    <span class="ftl-field-hint" id="{fid}-hint">{e(hint)}</span>' if hint else ""
        d = f' aria-describedby="{fid}-hint"' if hint else ""
        return f"""<div class="ftl-field">
    <label class="ftl-label" for="{fid}">{e(label)}</label>
    <input class="ftl-input" id="{fid}" type="text" value="{e(value or '')}"{d}>{h}
  </div>"""
    if kind == "search":
        placeholder = args[0]
        return f"""<div class="ftl-field">
    <label class="ftl-label" for="{fid}">{e(label)}</label>
    <input class="ftl-input" id="{fid}" type="search" placeholder="{e(placeholder)}">
  </div>"""
    if kind == "select":
        opts = "".join(f"<option>{e(o)}</option>" for o in args[0])
        return f"""<div class="ftl-field">
    <label class="ftl-label" for="{fid}">{e(label)}</label>
    <select class="ftl-select" id="{fid}">{opts}</select>
  </div>"""
    if kind == "textarea":
        return f"""<div class="ftl-field">
    <label class="ftl-label" for="{fid}">{e(label)}</label>
    <textarea class="ftl-textarea" id="{fid}">{e(args[0])}</textarea>
  </div>"""
    if kind == "slider":
        lo, hi, val = args
        return f"""<div class="ftl-field">
    <label class="ftl-label" for="{fid}">{e(label)}</label>
    <input class="ftl-slider" id="{fid}" type="range" min="{lo}" max="{hi}" value="{val}">
  </div>"""
    if kind == "switch":
        checked = " checked" if args and args[0] else ""
        hint = args[1] if len(args) > 1 else None
        h = f'\n    <span class="ftl-field-hint">{e(hint)}</span>' if hint else ""
        return f"""<div class="ftl-field-row">
    <label class="ftl-label" for="{fid}">{e(label)}</label>{h}
    <label class="ftl-switch"><input id="{fid}" type="checkbox"{checked}><span class="ftl-switch-track"><span class="ftl-switch-thumb"></span></span></label>
  </div>"""
    if kind == "check":
        checked = " checked" if args and args[0] else ""
        return f"""<div class="ftl-field-row">
    <label class="ftl-label" for="{fid}">{e(label)}</label>
    <input class="ftl-checkbox" id="{fid}" type="checkbox"{checked}>
  </div>"""
    raise ValueError(kind)


def form(title, *fields):
    return (
        '<div class="ftl-field-group">\n  <div class="ftl-field-group-title">'
        + e(title) + "</div>\n  " + "\n  ".join(field(*f) for f in fields) + "\n</div>"
    )


def panel(header, *inner):
    h = f'\n  <div class="ftl-panel-header">{e(header)}</div>' if header else ""
    return ('<section class="ftl-panel">' + h + '\n  <div class="ftl-stack ftl-stack-sm">\n  '
            + "\n  ".join(inner) + "\n  </div>\n</section>")


def card(*inner):
    return '<div class="ftl-card ftl-stack ftl-stack-sm">\n  ' + "\n  ".join(inner) + "\n</div>"


def alert(kind, text):
    return f'<div class="ftl-alert ftl-alert-{kind}" role="status">{e(text)}</div>'


def toast(kind, text):
    return f"""<div class="ftl-toast-region" aria-live="polite">
  <div class="ftl-toast ftl-toast-{kind}">{e(text)}</div>
</div>"""


def modal(title, body, buttons):
    return f"""<div class="ftl-modal" role="dialog" aria-label="{e(title)}">
  <div class="ftl-modal-header">{e(title)}</div>
  <p>{e(body)}</p>
  <div class="ftl-modal-footer">
    {" ".join(buttons)}
  </div>
</div>"""


def tabs(items, active=0):
    t = "\n  ".join(
        f'<button class="ftl-tab{" is-active" if i == active else ""}" type="button" role="tab" aria-selected="{"true" if i == active else "false"}">{e(x)}</button>'
        for i, x in enumerate(items)
    )
    return f'<div class="ftl-tabs" role="tablist">\n  {t}\n</div>'


def segmented(items, active=0, label="View"):
    t = "\n  ".join(
        f'<button class="ftl-segmented-item{" is-active" if i == active else ""}" type="button" aria-pressed="{"true" if i == active else "false"}">{e(x)}</button>'
        for i, x in enumerate(items)
    )
    return f'<div class="ftl-segmented" role="group" aria-label="{e(label)}">\n  {t}\n</div>'


def accordion(*items):
    out = []
    for title, body, is_open in items:
        o = " open" if is_open else ""
        out.append(
            f'<details class="ftl-accordion-item"{o}>\n  <summary class="ftl-accordion-trigger">{e(title)}</summary>\n'
            f'  <div class="ftl-accordion-panel">{e(body)}</div>\n</details>'
        )
    return "\n".join(out)


def empty(icon, title, hint):
    return f"""<div class="ftl-empty-state">
  <span class="ftl-empty-state-icon" aria-hidden="true">{e(icon)}</span>
  <span class="ftl-empty-state-title">{e(title)}</span>
  <span class="ftl-empty-state-hint">{e(hint)}</span>
</div>"""


def dropzone(text):
    return f'<div class="ftl-dropzone">{e(text)}</div>'


def pagination(n, active, label="Pages"):
    items = ['<a class="ftl-pagination-item is-disabled" aria-disabled="true">&lsaquo;</a>' if active == 1
             else '<a class="ftl-pagination-item" href="#">&lsaquo;</a>']
    for i in range(1, n + 1):
        if i == active:
            items.append(f'<a class="ftl-pagination-item is-active" aria-current="page">{i}</a>')
        else:
            items.append(f'<a class="ftl-pagination-item" href="#">{i}</a>')
    items.append('<a class="ftl-pagination-item" href="#">&rsaquo;</a>')
    return f'<nav class="ftl-pagination" aria-label="{e(label)}">\n  ' + "\n  ".join(items) + "\n</nav>"








def badges(*items):
    out = []
    for kind, text in items:
        mod = f" ftl-badge-{kind}" if kind else ""
        out.append(f'<span class="ftl-badge{mod}">{e(text)}</span>')
    return " ".join(out)


def chips(items, active=0):
    return toolbar(*[
        f'<button class="ftl-badge ftl-badge-accent ftl-badge-button{" is-active" if i == active else ""}" type="button" aria-pressed="{"true" if i == active else "false"}">{e(t)}</button>'
        for i, t in enumerate(items)
    ])


def avatars(*initials, size=""):
    cls = "ftl-avatar" + (f" ftl-avatar-{size}" if size else "")
    return " ".join(f'<span class="{cls}">{e(i)}</span>' for i in initials)


def keys(*pairs):
    return "<p>" + " &nbsp; ".join(f"<kbd>{e(k)}</kbd> {e(v)}" for k, v in pairs) + "</p>"


def code(text):
    return f"<pre><code>{e(text)}</code></pre>"


def skeleton():
    return (
        '<div class="ftl-skeleton ftl-skeleton-text" aria-hidden="true"></div>\n'
        '<div class="ftl-skeleton ftl-skeleton-text" aria-hidden="true"></div>\n'
        '<div class="ftl-skeleton ftl-skeleton-block" aria-hidden="true"></div>'
    )


def spinner(label):
    return f'<p><span class="ftl-spinner" role="status" aria-label="{e(label)}"></span> {e(label)}</p>'




def page(theme, title, bar_html, main_parts, status_html):
    main = '<div class="ftl-stack">\n\n' + "\n\n".join(main_parts) + "\n\n</div>"
    return f"""<!DOCTYPE html>
<!-- Generated by scripts/build_examples.py — edit the script, not this file.
     Only ftl-themes classes and semantic HTML: no <style>, no style="". -->
<html lang="en" data-theme="{theme}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} — ftl-themes / {theme}</title>
<link rel="stylesheet" href="../dist/{theme}.css">
</head>
<body class="ftl-app">

{bar_html}

<aside class="ftl-app-rail" aria-hidden="true"></aside>

<main class="ftl-app-main">

{main}

</main>

{status_html}

</body>
</html>
"""


# --- Per-theme pages ------------------------------------------------------
# Content is written for each theme's own world, so each page shows what
# the theme is FOR rather than the same demo in a different paint.

PAGES = {}


def theme(name):
    def reg(fn):
        PAGES[name] = fn
        return fn
    return reg


@theme("windows95")
def _():
    return page(
        "windows95", "Exploring - C:\\My Documents",
        bar("Exploring - C:\\My Documents", ["File", "Edit", "View", "Tools", "Help"], active=-1),
        [
            toolbar(btn("Back", aria="Back"), btn("Up", tooltip="Up One Level"), btn("Cut"), btn("Copy"), btn("Paste"),
                    btn("Delete", "danger"), btn("Properties", "primary"),
                    anchored_menu("File", ["Open", "Print", "Quick View", "Send To", "Rename"], danger="Delete")),
            crumbs(["My Computer", "(C:)", "My Documents"]),
            table(["Name", "Size", "Type", "Modified"], [
                ["Budget 1995.xls", "24KB", "Microsoft Excel Worksheet", "8/24/95 9:14 AM"],
                {"state": "is-selected", "cells": ["Letter to Mom.doc", "11KB", "Microsoft Word Document", "8/22/95 6:02 PM"]},
                ["Setup.log", "3KB", "Text Document", "8/24/95 8:55 AM"],
                ["Clouds.bmp", "301KB", "Bitmap Image", "7/11/95 12:00 AM"],
                ["Readme.txt", "6KB", "Text Document", "7/11/95 12:00 AM"],
            ]),
            modal("Confirm File Delete", "Are you sure you want to send 'Letter to Mom.doc' to the Recycle Bin?",
                  [btn("Yes", "primary"), btn("No")]),
            panel("Display Properties",
                  tabs(["Background", "Screen Saver", "Appearance", "Settings"], active=3),
                  form("Settings",
                       ("select", "Color palette", ["High Color (16 bit)", "256 Color", "True Color (24 bit)"]),
                       ("slider", "Desktop area", 0, 3, 1),
                       ("check", "Show settings icon on task bar", True)),
                  radios("Font size", ["Small Fonts", "Large Fonts", "Custom"], inline=True),
                  toolbar(btn("OK", "primary"), btn("Cancel"), btn("Apply"))),
        ],
        status_bar([("text", "5 object(s)"), ("mono", "345KB"), ("text", "(Disk free space: 212MB)")]),
    )


@theme("winxp-luna")
def _():
    return page(
        "winxp-luna", "My Documents",
        bar("My Documents", ["File", "Edit", "View", "Favorites", "Tools", "Help"], active=-1),
        [
            transport(None, "start", status=("ok", "Connected to the Internet"),
                      extra=[btn("Search", "ghost"), btn("Folders", "ghost")]),
            alert("info", "Updates are ready for your computer. Click here to review and install them."),
            panel("File and Folder Tasks",
                  toolbar(btn("Make a new folder"), btn("Publish this folder to the Web"), btn("Share this folder")),
                  segmented(["Thumbnails", "Tiles", "Icons", "List", "Details"], active=4, label="View as")),
            table(["Name", "Size", "Type", "Date Modified"], [
                ["My Music", "", "File Folder", "10/25/2001 2:10 PM"],
                ["My Pictures", "", "File Folder", "10/25/2001 2:10 PM"],
                {"state": "is-selected", "cells": ["Bliss.jpg", "1,440 KB", "JPEG Image", "8/23/2001 12:00 PM"]},
                ["Resume.doc", "34 KB", "Microsoft Word Document", "11/2/2001 9:41 AM"],
            ]),
            modal("Log Off Windows", "Are you sure you want to log off?",
                  [btn("Log Off", "primary"), btn("Switch User"), btn("Cancel", "secondary")]),
            panel("User Accounts",
                  avatars("JD", "AS", size="lg"),
                  form("Change your account",
                       ("text", "Account name", "John", "This name appears on the Welcome screen."),
                       ("select", "Account type", ["Computer administrator", "Limited"]),
                       ("switch", "Use the Welcome screen", True))),
        ],
        status_bar([("text", "4 objects"), ("text", "1.44 MB"), ("status", "ok", "My Computer")]),
    )


@theme("win7-aero")
def _():
    return page(
        "win7-aero", "Pictures Library",
        bar("Libraries", ["Organize", "Share with", "Slide show", "Burn", "New folder"], active=-1),
        [
            crumbs(["Libraries", "Pictures", "Vacation 2009"]),
            toolbar(field("search", "Search Pictures", "Search Pictures"),
                    segmented(["Extra large", "Large", "Medium", "Details"], active=3, label="Change your view")),
            table(["Name", "Date taken", "Tags", "Size", "Rating"], [
                ["Beach.jpg", "7/14/2009 3:22 PM", ("badge", "accent", "Family"), "3.1 MB", "★★★★☆"],
                {"state": "is-selected", "cells": ["Sunset.jpg", "7/14/2009 8:47 PM", ("badge", "accent", "Favorite"), "2.8 MB", "★★★★★"]},
                ["Harbor.jpg", "7/15/2009 10:05 AM", ("badge", "", "Untagged"), "2.2 MB", "★★★☆☆"],
                ["Lighthouse.jpg", "7/16/2009 1:30 PM", ("badge", "success", "Shared"), "4.0 MB", "★★★★☆"],
            ], sort=1, sort_dir="descending"),
            panel("Details pane",
                  stats(("47", "Items"), ("312 MB", "Total size"), ("4", "Shared", ("up", "+2 today")))),
            toast("success", "Burned 47 items to disc."),
            panel("Personalization",
                  form("Window Color and Appearance",
                       ("select", "Color", ["Sky", "Twilight", "Sea", "Leaf", "Lime", "Frost"]),
                       ("switch", "Enable transparency", True),
                       ("slider", "Color intensity", 0, 100, 60)),
                  toolbar(btn("Save changes", "primary"), btn("Cancel", "secondary"))),
        ],
        status_bar([("text", "47 items"), ("text", "1 item selected"), ("mono", "2.8 MB")]),
    )


@theme("aqua")
def _():
    return page(
        "aqua", "iTunes",
        bar("iTunes", ["Library", "Radio", "Music Store", "Playlists"]),
        [
            transport("is-play", "▶", readout=("2:47", "of 4:12"), status=("ok", "Playing"),
                      extra=[btn("◀◀", aria="Previous"), btn("▶▶", aria="Next")]),
            toolbar(segmented(["Songs", "Albums", "Artists"], label="Browse"),
                    field("search", "Search", "Search Library")),
            table(["Song", "Time", "Artist", "Album", "My Rating"], [
                {"state": "is-active", "cells": ["Clocks", ("mono", "5:07"), "Coldplay", "A Rush of Blood to the Head", "★★★★★"]},
                ["Hey Ya!", ("mono", "3:55"), "OutKast", "Speakerboxxx/The Love Below", "★★★★☆"],
                {"state": "is-selected", "cells": ["Seven Nation Army", ("mono", "3:52"), "The White Stripes", "Elephant", "★★★★☆"]},
                ["Crazy in Love", ("mono", "3:56"), "Beyoncé", "Dangerously in Love", "★★★☆☆"],
            ]),
            modal("Do you want to save changes to this playlist before closing?",
                  "If you don't save, your changes will be lost.",
                  [btn("Don't Save", "ghost"), btn("Cancel", "secondary"), btn("Save", "primary")]),
            panel("Preferences",
                  tabs(["General", "Sharing", "Importing", "Burning"]),
                  form("General",
                       ("text", "Library name", "Jane's Music"),
                       ("select", "Source text", ["Small", "Large"]),
                       ("switch", "Show genre when browsing", True),
                       ("switch", "Automatically update songs on iPod", False))),
        ],
        status_bar([("text", "1,284 songs"), ("text", "3.6 days"), ("mono", "5.82 GB")]),
    )


@theme("imac-g3")
def _():
    return page(
        "imac-g3", "Mac OS Setup Assistant",
        bar("Setup Assistant", ["Introduction", "Name", "Location", "Internet", "Conclusion"], active=1),
        [
            heading("Think different.", "Welcome to your new iMac. Let's get you on the Internet in three easy steps."),
            card(heading("Step 2 of 5: Name and Organization", level=2),
                 form("About you",
                      ("text", "What is your name?", "Jony", "This is used to identify your computer on a network."),
                      ("text", "Organization", "Apple Computer, Inc."),
                      ("select", "Your iMac's color", ["Bondi Blue", "Blueberry", "Grape", "Tangerine", "Lime", "Strawberry"])),
                 toolbar(btn("Go Back", "secondary"), btn("Continue", "primary"))),
            panel("Choose a flavor",
                  chips(["Bondi Blue", "Blueberry", "Grape", "Tangerine", "Lime", "Strawberry"]),
                  avatars("B", "G", "T", "L", size="lg")),
            stats(("233 MHz", "PowerPC G3"), ("32 MB", "Memory"), ("4 GB", "Hard disk")),
            alert("success", "You're connected. There's no step 3."),
            dropzone("Drag a picture here to use it as your desktop pattern."),
        ],
        status_bar([("lamp", "is-on", "Power"), ("text", "Mac OS 8.1"), ("mono", "12:00 PM")]),
    )


@theme("winamp-classic")
def _():
    return page(
        "winamp-classic", "Winamp",
        bar("WINAMP", ["Main", "Equalizer", "Playlist Editor", "Media Library"]),
        [
            transport("is-play", "▶", readout=("01:23", None), lamps=[("is-on", "Stereo"), ("", "Mono")],
                      status=("ok", "128 kbps · 44 kHz"),
                      extra=[btn("⏮", aria="Previous"), btn("⏸", aria="Pause"), btn("⏹", aria="Stop"), btn("⏭", aria="Next")]),
            panel("1. DJ Mike Llama - Llama Whippin' Intro (0:05) ***",
                  form("Main", ("slider", "Volume", 0, 100, 80), ("slider", "Balance", -50, 50, 0), ("slider", "Seek", 0, 100, 30)),
                  toolbar(btn("EQ", "secondary"), btn("PL", "secondary"), btn("Shuffle", "ghost"), btn("Repeat", "ghost"))),
            panel("Equalizer",
                  toolbar(btn("ON", "primary"), btn("AUTO"), btn("PRESETS")),
                  form("Bands",
                       ("slider", "Preamp", -12, 12, 0),
                       ("slider", "60 Hz", -12, 12, 6),
                       ("slider", "310 Hz", -12, 12, 3),
                       ("slider", "1 kHz", -12, 12, 0),
                       ("slider", "6 kHz", -12, 12, 2),
                       ("slider", "16 kHz", -12, 12, 4))),
            table(["#", "Title", "Length"], [
                {"state": "is-active", "cells": ["1.", "DJ Mike Llama - Llama Whippin' Intro", ("mono", "0:05")]},
                ["2.", "Daft Punk - Around the World", ("mono", "7:09")],
                {"state": "is-selected", "cells": ["3.", "Fatboy Slim - Right Here, Right Now", ("mono", "6:27")]},
                ["4.", "The Prodigy - Firestarter", ("mono", "4:40")],
            ], sort=None),
            toolbar(btn("+ ADD"), btn("- REM"), btn("SEL"), btn("MISC"), btn("LIST", "primary")),
        ],
        status_bar([("mono", "0:05/18:21"), ("text", "It really whips the llama's ass.")]),
    )


@theme("wmp11")
def _():
    return page(
        "wmp11", "Windows Media Player",
        bar("Windows Media Player", ["Now Playing", "Library", "Rip", "Burn", "Sync", "Media Guide"], active=1),
        [
            crumbs(["Music", "Library", "Album Artist", "Daft Punk"]),
            toolbar(segmented(["Artist", "Album", "Songs", "Genre"], active=1, label="Library view"),
                    field("search", "Search", "Search")),
            table(["Title", "Length", "Rating", "Contributing Artist"], [
                {"state": "is-active", "cells": ["One More Time", ("mono", "5:20"), "★★★★★", "Daft Punk"]},
                ["Aerodynamic", ("mono", "3:27"), "★★★★☆", "Daft Punk"],
                {"state": "is-selected", "cells": ["Digital Love", ("mono", "4:58"), "★★★★★", "Daft Punk"]},
                ["Harder, Better, Faster, Stronger", ("mono", "3:44"), "★★★★☆", "Daft Punk"],
            ]),
            transport("is-play", "▶", readout=("02:11", None), status=("ok", "Playing: One More Time"),
                      extra=[btn("⏹", aria="Stop"), btn("⏮", aria="Previous"), btn("⏭", aria="Next"),
                             btn("🔀", "ghost", aria="Shuffle"), btn("🔁", "ghost", aria="Repeat")]),
            panel("Rip settings",
                  form("Rip",
                       ("select", "Format", ["Windows Media Audio", "Windows Media Audio Pro", "MP3", "WAV (Lossless)"]),
                       ("slider", "Audio quality", 48, 192, 128),
                       ("switch", "Rip CD when inserted", True),
                       ("switch", "Eject CD after ripping", False))),
            toast("success", "Ripped 14 tracks to your library."),
        ],
        status_bar([("text", "14 items, 1 hour 1 minute"), ("status", "ok", "Online store: URGE")]),
    )


@theme("msdos")
def _():
    return page(
        "msdos", "The Norton Commander",
        bar("The Norton Commander", ["Left", "Files", "Commands", "Options", "Right"], active=-1),
        [
            table(["Name", "Size", "Date", "Time"], [
                ["..", "►UP--DIR◄", "03-15-91", "4:12p"],
                ["DOS", "►SUB-DIR◄", "03-15-91", "4:12p"],
                {"state": "is-active", "cells": ["NC", "►SUB-DIR◄", "03-15-91", "4:14p"]},
                ["AUTOEXEC.BAT", "184", "03-15-91", "4:30p"],
                {"state": "is-selected", "cells": ["CONFIG.SYS", "112", "03-15-91", "4:30p"]},
                ["COMMAND.COM", "47845", "04-09-91", "5:00a"],
            ], sort=None, caption="C:\\"),
            code("C:\\>DIR /W\n\n Volume in drive C has no label\n Directory of C:\\\n\n[DOS]      [NC]       AUTOEXEC.BAT  CONFIG.SYS   COMMAND.COM\n        5 file(s)      48141 bytes\n                    20512768 bytes free"),
            modal("Copy", "Copy \"CONFIG.SYS\" to C:\\BACKUP\\", [btn("Copy", "primary"), btn("Tree"), btn("Cancel")]),
            panel("Configuration",
                  form("Screen options",
                       ("check", "Show hidden files", False),
                       ("check", "Clock", True),
                       ("check", "Key bar", True),
                       ("select", "Screen colors", ["Color", "Black & White", "Laptop"]))),
            alert("danger", "Abort, Retry, Fail?"),
        ],
        status_bar([("kbd", [("1", "Help"), ("2", "Menu"), ("3", "View"), ("4", "Edit"), ("5", "Copy"),
                             ("6", "RenMov"), ("7", "Mkdir"), ("8", "Delete"), ("10", "Quit")])]),
    )


@theme("lcars")
def _():
    return page(
        "lcars", "USS Enterprise — Operations",
        bar("LCARS 47", ["Ops", "Engineering", "Tactical", "Science", "Medical"]),
        [
            transport("is-play", "Engage", readout=("47634.44", "stardate"),
                      lamps=[("is-on", "Warp core online"), ("is-on", "Shields up"), ("is-warn", "Impulse reserve")],
                      status=("ok", "All decks report ready")),
            alert("danger", "Red alert. All hands to battle stations."),
            stats(("Warp 6", "Cruising velocity", ("up", "+1 factor")), ("98%", "Shield strength"), ("1,014", "Crew complement")),
            panel("Power allocation", meter("Shields", 98, low=20, high=40, optimum=100), meter("Warp core", 76, low=20, high=40, optimum=100)),
            tabs(["Decks", "Subspace", "Sensors", "Transporters"]),
            table(["Deck", "System", "Status", "Personnel"], [
                {"state": "is-active", "cells": ["01", "Main Bridge", ("status", "ok", "Nominal"), "14"]},
                ["08", "Sickbay", ("status", "ok", "Nominal"), "22"],
                {"state": "is-selected", "cells": ["10", "Ten Forward", ("status", "warn", "Reduced power"), "61"]},
                ["36", "Main Engineering", ("status", "error", "Plasma leak"), "38"],
            ]),
            panel("Transporter Room 3",
                  segmented(["Energize", "Hold pattern", "Abort"], label="Transporter mode"),
                  form("Lock",
                       ("text", "Coordinates", "Grid 4, bearing 127 mark 4"),
                       ("slider", "Phase transition coils", 0, 100, 72),
                       ("switch", "Pattern enhancers", True))),
            toast("success", "Away team beamed aboard."),
        ],
        status_bar([("lamp", "is-on", "Main computer"), ("mono", "LCARS ACCESS 47"), ("text", "NCC-1701-D")]),
    )


@theme("matrix")
def _():
    return page(
        "matrix", "Construct",
        bar("NEBUCHADNEZZAR", ["Operator", "Construct", "Broadcast", "Sentinels"]),
        [
            code("Wake up, Neo...\nThe Matrix has you...\nFollow the white rabbit.\n\nKnock, knock, Neo."),
            alert("danger", "Agent detected in sector 12. Jack out immediately."),
            transport("is-rec", "Jack in", readout=("00:04:17", None), lamps=[("is-on", "Carrier signal"), ("is-error", "Sentinels")],
                      status=("warn", "Trace program running")),
            table(["Process", "Host", "Signal", "State"], [
                {"state": "is-active", "cells": ["neo.exe", "Room 101", ("mono", "-42 dB"), ("status", "ok", "Connected")]},
                ["trinity.exe", "Heart O' the City Hotel", ("mono", "-51 dB"), ("status", "ok", "Connected")],
                {"state": "is-selected", "cells": ["morpheus.exe", "Adams St. Bridge", ("mono", "-60 dB"), ("status", "warn", "Unstable")]},
                ["smith.agent", "Unknown", ("mono", "—"), ("status", "error", "Hostile")],
            ]),
            panel("Operator console",
                  form("Load program",
                       ("select", "Program", ["Combat training", "Jump", "Woman in the red dress", "Pilot: B-212 helicopter"]),
                       ("slider", "Download speed", 1, 10, 9),
                       ("switch", "Show code view", True)),
                  toolbar(btn("Upload", "primary"), btn("Hard line", "secondary"), btn("Pull plug", "danger"))),
            keys(("Ctrl", "Break — emergency exit"), ("Esc", "Leave construct")),
            spinner("Searching for the exit"),
        ],
        status_bar([("lamp", "is-on", "Carrier"), ("mono", "CALL TRANS OPT: RECEIVED. 9-18-99 14:32:21 REC:Log>"), ("mono", "WARNING: CARRIER ANOMALY")]),
    )


@theme("tron")
def _():
    return page(
        "tron", "ENCOM — The Grid",
        bar("ENCOM OS-12", ["Programs", "Games", "I/O Tower", "MCP"]),
        [
            transport("is-play", "Derez", readout=("1982", "cycle"), lamps=[("is-on", "Grid link"), ("is-warn", "Recognizers inbound")],
                      status=("warn", "User on the Grid")),
            stats(("256", "Active programs"), ("12", "Light cycles", ("down", "-3 this cycle")), ("99.7%", "Grid stability")),
            table(["Program", "User", "Sector", "Status"], [
                {"state": "is-active", "cells": ["TRON", "Alan Bradley", "I/O Tower", ("status", "ok", "Online")]},
                ["CLU", "Kevin Flynn", "Sector 7G", ("status", "error", "Rogue")],
                {"state": "is-selected", "cells": ["QUORRA", "—", "Outlands", ("status", "warn", "Isomorphic")]},
                ["RINZLER", "—", "Arena", ("status", "idle", "Standby")],
            ]),
            panel("Identity disc",
                  segmented(["Light cycle", "Disc wars", "Light jet"], label="Game"),
                  form("Configure",
                       ("text", "Program designation", "TRON"),
                       ("select", "Jet wall color", ["Cyan", "Orange", "White"]),
                       ("switch", "Friendly-fire lock", True))),
            toolbar(anchored_menu("Program actions", ["Rectify", "Repurpose", "Archive"], danger="Derez")),
            alert("warning", "End of line."),
        ],
        status_bar([("lamp", "is-on", "Grid"), ("mono", "ENCOM 511"), ("text", "Greetings, Program.")]),
    )


@theme("nerv")
def _():
    return page(
        "nerv", "NERV HQ — MAGI",
        bar("NERV", ["Command", "MAGI", "Evangelion", "Pattern Analysis"], active=1),
        [
            alert("danger", "Pattern blue. Angel confirmed. Level 1 battle stations."),
            stats(("MELCHIOR-1", "Approve", ("up", "Scientist")), ("BALTHASAR-2", "Approve", ("up", "Mother")),
                  ("CASPER-3", "Reject", ("down", "Woman"))),
            transport("is-rec", "Launch", readout=("41.3", "% sync"), lamps=[("is-on", "Umbilical"), ("is-warn", "Internal battery")],
                      status=("warn", "Activation limit 4:59")),
            table(["Unit", "Pilot", "Sync ratio", "Status"], [
                {"state": "is-active", "cells": ["EVA-01", "Ikari Shinji", ("mono", "41.3%"), ("status", "ok", "Active")]},
                ["EVA-00", "Ayanami Rei", ("mono", "32.7%"), ("status", "idle", "Standby")],
                {"state": "is-selected", "cells": ["EVA-02", "Sohryu Asuka Langley", ("mono", "78.4%"), ("status", "warn", "Deploying")]},
            ], sort=2, sort_dir="descending"),
            panel("Operation Yashima",
                  form("Positron rifle",
                       ("slider", "Power draw (Japan grid)", 0, 100, 100),
                       ("select", "Firing position", ["Futagoyama", "Mt. Kami", "Tokyo-3 central"]),
                       ("switch", "Shield deployed", True)),
                  toolbar(btn("Fire", "danger"), btn("Abort", "secondary"))),
            code("MAGI SYSTEM: 2-1 MAJORITY — RESOLUTION CARRIED\nA.T. FIELD: NEUTRALIZED"),
        ],
        status_bar([("lamp", "is-error", "Emergency"), ("mono", "TOKYO-3 / GEOFRONT"), ("text", "God's in his heaven. All's right with the world.")]),
    )


@theme("pipboy")
def _():
    return page(
        "pipboy", "Pip-Boy 3000",
        bar("PIP-BOY 3000", ["STAT", "INV", "DATA", "MAP", "RADIO"], active=1),
        [
            tabs(["Weapons", "Apparel", "Aid", "Misc", "Ammo"]),
            table(["Item", "DAM", "WG", "VAL"], [
                {"state": "is-active", "cells": ["10mm Pistol", "18", "3.5", "53"]},
                ["Hunting Rifle", "30", "10", "150"],
                {"state": "is-selected", "cells": ["Stimpak (4)", "—", "0", "75"]},
                ["Nuka-Cola", "—", "1", "20"],
                ["Bobby pin (12)", "—", "0", "1"],
            ], sort=2),
            stats(("290/290", "HP"), ("78/80", "AP"), ("184/210", "Weight", ("down", "Overencumbered soon"))),
            panel("S.P.E.C.I.A.L.",
                  table(["Attribute", "Rank"], [
                      ["Strength", "5"], ["Perception", "6"], ["Endurance", "4"], ["Charisma", "3"],
                      ["Intelligence", "8"], ["Agility", "7"], ["Luck", "5"],
                  ], sort=None, sticky=False)),
            progress("XP to level 13", 97),
            alert("warning", "Radiation levels rising: 212 RADS."),
            panel("Radio",
                  radios("Station", ["Diamond City Radio", "Classical Radio", "Distress Signal"]),
                  form("Tuner", ("slider", "Frequency", 88, 108, 96))),
        ],
        status_bar([("mono", "LVL 12"), ("mono", "HP 290/290"), ("mono", "AP 78/80"), ("mono", "XP 1450/1500")]),
    )


@theme("blue-future")
def _():
    return page(
        "blue-future", "Telemetry Recorder",
        bar("VECTOR-7", ["Record", "Channels", "Storage", "Network"]),
        [
            transport("is-rec", "Rec", readout=("01:24:07:12", "TC"), lamps=[("is-on", "Sync"), ("is-on", "Link")],
                      status=("ok", "Writing to NVMe-0"), extra=[btn("Mark", "secondary"), btn("Stop", "danger")]),
            stats(("128", "Channels armed"), ("48 kHz", "Sample rate"), ("2.1 TB", "Free", ("down", "-18 GB/h"))),
            panel("Input levels",
                  '<div class="ftl-grid ftl-grid-sm">',
                  meter("01 Main L", 64), meter("02 Main R", 62), meter("17 Ambience", 97), meter("64 Talkback", 8),
                  '</div>',
                  progress("Disk used", 58)),
            table(["Channel", "Source", "Peak", "State"], [
                {"state": "is-active", "cells": ["01", "Main L", ("mono", "-6.2 dBFS"), ("status", "ok", "Armed")]},
                ["02", "Main R", ("mono", "-6.4 dBFS"), ("status", "ok", "Armed")],
                {"state": "is-selected", "cells": ["17", "Ambience", ("mono", "-0.3 dBFS"), ("status", "warn", "Near clip")]},
                ["64", "Talkback", ("mono", "—"), ("status", "idle", "Idle")],
            ]),
            panel("Session",
                  form("Recording",
                       ("text", "Session name", "Run 47 — ascent"),
                       ("select", "File format", ["Broadcast WAV (BWF)", "RF64", "CAF"]),
                       ("switch", "Auto-split at 2 GB", True, "Avoids FAT32 limits"),
                       ("switch", "Mirror to secondary disk", False))),
            alert("warning", "Channel 17 has clipped 3 times this take."),
            spinner("Verifying checksum"),
        ],
        status_bar([("lamp", "is-on", "Clock locked"), ("mono", "DANTE 128×128"), ("mono", "CPU 23%")]),
    )


@theme("cue-lab")
def _():
    return page(
        "cue-lab", "Cue Lab — Hamlet, Act III",
        bar("Cue Lab", ["Cues", "Audio", "Video", "Lighting", "Network"]),
        [
            transport("is-play", "GO", readout=("00:42:17", None), lamps=[("is-on", "Show mode")],
                      status=("ok", "Standing by: 14 — Ghost appears"),
                      extra=[btn("Panic", "danger"), btn("Pause", "secondary")]),
            table(["#", "Name", "Type", "Pre", "Duration"], [
                ["12", "House to half", ("badge", "", "Light"), ("mono", "0.0"), ("mono", "5.0")],
                ["13", "Storm SFX loop", ("badge", "accent", "Audio"), ("mono", "0.0"), ("mono", "∞")],
                {"state": "is-active", "cells": ["14", "Ghost appears", ("badge", "warning", "Group"), ("mono", "0.5"), ("mono", "8.0")]},
                {"state": "is-selected", "cells": ["15", "Projection: battlements", ("badge", "success", "Video"), ("mono", "0.0"), ("mono", "12.0")]},
                ["16", "Blackout", ("badge", "", "Light"), ("mono", "0.0"), ("mono", "0.0")],
            ], sort=0),
            keys(("Space", "GO"), ("Esc", "Panic"), ("[", "Pause"), ("]", "Resume")),
            panel("Inspector — Cue 14",
                  tabs(["Basics", "Triggers", "Levels", "Fades"]),
                  form("Basics",
                       ("text", "Name", "Ghost appears"),
                       ("select", "Continue", ["Do not continue", "Auto-continue", "Auto-follow"]),
                       ("slider", "Master level", -60, 12, 0),
                       ("switch", "Armed", True))),
            alert("info", "Workspace saved 2 minutes ago."),
        ],
        status_bar([("lamp", "is-on", "Show mode"), ("mono", "84 cues"), ("text", "Operator: SM")]),
    )


@theme("bloomberg")
def _():
    return page(
        "bloomberg", "Bloomberg — Monitor",
        bar("<GO>", ["WEI", "MOST", "TOP", "ECO", "FXC"]),
        [
            field("text", "Command", "AAPL US Equity GP", "Type a mnemonic and press GO"),
            stats(("5,648.40", "S&P 500", ("up", "+0.42%")), ("41,563.08", "DJIA", ("up", "+0.18%")),
                  ("17,713.53", "NASDAQ", ("down", "-0.21%"))),
            table(["Ticker", "Last", "Chg", "%Chg", "Volume"], [
                {"state": "is-active", "cells": ["AAPL", ("mono", "229.87"), ("trend", "up", "+1.34"), ("trend", "up", "+0.59%"), ("mono", "44.2M")]},
                ["MSFT", ("mono", "417.14"), ("trend", "down", "-2.01"), ("trend", "down", "-0.48%"), ("mono", "18.9M")],
                {"state": "is-selected", "cells": ["NVDA", ("mono", "119.37"), ("trend", "up", "+3.12"), ("trend", "up", "+2.68%"), ("mono", "302.5M")]},
                ["TSLA", ("mono", "214.11"), ("trend", "down", "-5.40"), ("trend", "down", "-2.46%"), ("mono", "88.1M")],
            ], sort=3, sort_dir="descending"),
            tabs(["1) News", "2) Filings", "3) Estimates", "4) Holders"]),
            accordion(("FED HOLDS RATES STEADY, SIGNALS PATIENCE", "Policy makers left the benchmark range unchanged…", True),
                      ("OIL RISES AS SUPPLY CONCERNS MOUNT", "Brent crude rose for a third session…", False)),
            keys(("F8", "Equity"), ("F9", "Corp"), ("F10", "Mtge"), ("F11", "Index"), ("F12", "Curncy")),
        ],
        status_bar([("lamp", "is-on", "Realtime"), ("mono", "NY 16:00:00"), ("text", "Delayed data not shown")]),
    )


@theme("alienware")
def _():
    return page(
        "alienware", "Alienware Command Center",
        bar("ALIENWARE", ["Home", "Library", "FX", "Fusion"], active=2),
        [
            transport("is-play", "Apply", lamps=[("is-on", "AlienFX")], status=("ok", "Profile: Overdrive"),
                      extra=[segmented(["Quiet", "Balanced", "Performance", "Overdrive"], active=3, label="Thermal profile")]),
            stats(("144 fps", "Average", ("up", "+18%")), ("71 °C", "GPU temp"), ("2,850 rpm", "CPU fan")),
            table(["Zone", "Effect", "Color", "State"], [
                {"state": "is-active", "cells": ["Alien head", "Breathing", ("badge", "accent", "Cyan"), ("status", "ok", "On")]},
                ["Keyboard", "Spectrum", ("badge", "", "Multi"), ("status", "ok", "On")],
                {"state": "is-selected", "cells": ["Tron lights", "Static", ("badge", "accent", "Cyan"), ("status", "ok", "On")]},
                ["Power button", "Morph", ("badge", "danger", "Red"), ("status", "idle", "Off")],
            ], sort=None),
            panel("Lighting",
                  form("AlienFX",
                       ("select", "Effect", ["Static", "Breathing", "Spectrum", "Morph", "Pulse"]),
                       ("slider", "Brightness", 0, 100, 85),
                       ("switch", "Dim when idle", True),
                       ("switch", "Sync with game events", True))),
            toast("success", "Overdrive applied."),
        ],
        status_bar([("lamp", "is-on", "AlienFX"), ("mono", "Aurora R16"), ("text", "Driver 552.44")]),
    )


@theme("aperture")
def _():
    return page(
        "aperture", "Aperture Science Enrichment Center",
        bar("APERTURE SCIENCE", ["Test Chambers", "Subjects", "Cores", "Cake"]),
        [
            heading("Test Chamber 19", "The Enrichment Center reminds you that the Weighted Companion Cube will never threaten to stab you."),
            stats(("19", "Chamber"), ("99%", "Subject compliance"), ("1", "Cakes promised", ("down", "0 delivered"))),
            transport(None, "Place portal", lamps=[("is-on", "Blue portal"), ("is-warn", "Orange portal")],
                      status=("ok", "Test in progress")),
            table(["Subject", "Chambers", "Status"], [
                {"state": "is-active", "cells": ["Chell", "19", ("status", "ok", "Testing")]},
                ["Doug Rattmann", "—", ("status", "warn", "Unaccounted for")],
                {"state": "is-selected", "cells": ["Weighted Companion Cube", "17", ("status", "idle", "Incinerated")]},
            ], sort=1, sort_dir="descending"),
            panel("Chamber configuration",
                  form("Hazards",
                       ("switch", "Aerial Faith Plate", True),
                       ("switch", "High-energy pellet", True),
                       ("switch", "Deadly neurotoxin", False, "Requires GLaDOS override"),
                       ("slider", "Test difficulty", 1, 10, 8))),
            alert("warning", "Please assume the party escort submission position."),
            modal("Emergency intelligence incinerator", "Please dispose of the Weighted Companion Cube.",
                  [btn("Dispose", "danger"), btn("Refuse", "secondary")]),
        ],
        status_bar([("lamp", "is-on", "GLaDOS"), ("mono", "APERTURE SCIENCE"), ("text", "We do what we must because we can.")]),
    )


@theme("cyber-goth")
def _():
    return page(
        "cyber-goth", "Club Nocturne — Tonight",
        bar("NOCTURNE", ["Lineup", "Tickets", "Guestlist", "Merch"]),
        [
            transport("is-play", "Drop", readout=("138", "BPM"), lamps=[("is-on", "UV"), ("is-on", "Fog")],
                      status=("ok", "Floor at capacity")),
            table(["Time", "Artist", "Genre", "Room"], [
                ["22:00", ("avatar", "VX", "Vexx"), ("badge", "accent", "EBM"), "Main"],
                {"state": "is-active", "cells": ["23:30", ("avatar", "NR", "Neon Ritual"), ("badge", "success", "Aggrotech"), "Main"]},
                {"state": "is-selected", "cells": ["01:00", ("avatar", "SH", "Sinthetik Heart"), ("badge", "warning", "Futurepop"), "Crypt"]},
                ["02:30", ("avatar", "DV", "Dead Voltage"), ("badge", "danger", "Industrial"), "Crypt"],
            ], sort=0),
            chips(["All", "EBM", "Aggrotech", "Futurepop", "Industrial"]),
            panel("Guestlist",
                  form("Add a name",
                       ("text", "Name", "Lux Obscura"),
                       ("select", "Door", ["Main door", "Back door", "VIP"]),
                       ("switch", "Plus one", True)),
                  toolbar(btn("Add", "primary"), btn("Clear", "ghost"))),
            toast("success", "Lux Obscura added to the guestlist."),
            empty("☾", "No afterparty yet", "Check back after 04:00."),
        ],
        status_bar([("lamp", "is-on", "Doors open"), ("mono", "CAP 412/450"), ("text", "No flash photography")]),
    )


@theme("death-star")
def _():
    return page(
        "death-star", "DS-1 Orbital Battle Station",
        bar("IMPERIAL NAVY", ["Command", "Superlaser", "Detention", "Hangar"], active=1),
        [
            alert("danger", "Rebel fighters detected in the Trench. Stay on target."),
            transport("is-rec", "Fire", readout=("0:30", "to target"), lamps=[("is-on", "Main reactor"), ("is-warn", "Thermal exhaust port")],
                      status=("warn", "Commence primary ignition")),
            stats(("98.2%", "Reactor output"), ("1", "Planets destroyed", ("up", "Alderaan")), ("0", "Exhaust ports shielded", ("down", "Oversight"))),
            table(["Sector", "Function", "Commander", "Status"], [
                {"state": "is-active", "cells": ["Overbridge", "Command", "Grand Moff Tarkin", ("status", "ok", "Operational")]},
                ["AA-23", "Detention block", "Lt. Shann Childsen", ("status", "error", "Breach")],
                {"state": "is-selected", "cells": ["Bay 327", "Docking", "TK-421", ("status", "warn", "Not at post")]},
                ["Trench", "Exhaust", "—", ("status", "ok", "Operational")],
            ]),
            panel("Superlaser",
                  form("Targeting",
                       ("select", "Target", ["Alderaan", "Yavin 4", "Scarif"]),
                       ("slider", "Tributary beam power", 0, 100, 100),
                       ("switch", "Stand by", True))),
            modal("Grand Moff Tarkin", "You may fire when ready.", [btn("Fire", "danger"), btn("Stand down", "secondary")]),
        ],
        status_bar([("lamp", "is-on", "Operational"), ("mono", "DS-1"), ("text", "Fully armed and operational")]),
    )


@theme("steampunk")
def _():
    return page(
        "steampunk", "The Babbage Boiler Room",
        bar("BABBAGE & SONS", ["Boilers", "Difference Engine", "Aether", "Telegraph"]),
        [
            transport("is-play", "Engage", readout=("142", "psi"), lamps=[("is-on", "Pilot flame"), ("is-warn", "Safety valve")],
                      status=("ok", "Full steam ahead")),
            stats(("412 °F", "Boiler temperature"), ("88 rpm", "Flywheel", ("up", "+6")), ("3 tons", "Coal remaining", ("down", "-1 per hour"))),
            table(["Gear", "Teeth", "Ratio", "Condition"], [
                {"state": "is-active", "cells": ["Main drive", "96", "1 : 1", ("status", "ok", "Oiled")]},
                ["Escapement", "30", "3.2 : 1", ("status", "ok", "Oiled")],
                {"state": "is-selected", "cells": ["Governor", "48", "2 : 1", ("status", "warn", "Squeaking")]},
                ["Analytical cam", "120", "0.8 : 1", ("status", "error", "Seized")],
            ]),
            panel("Valve controls",
                  form("Steam distribution",
                       ("slider", "Throttle", 0, 100, 65),
                       ("slider", "Condenser flow", 0, 100, 40),
                       ("select", "Route steam to", ["Loom", "Difference Engine", "Airship dock"]),
                       ("switch", "Automatic stoker", True))),
            accordion(("Maintenance log, 14th inst.", "Governor bearing replaced; cam shaft to be inspected Tuesday next.", True),
                      ("Standing orders", "No naked flames within six yards of the aether reservoir.", False)),
        ],
        status_bar([("lamp", "is-on", "Pilot flame"), ("mono", "No. 7 BOILER"), ("text", "Est. 1837")]),
    )


@theme("vaporwave")
def _():
    return page(
        "vaporwave", "ＶＡＰＯＲ ＭＡＬＬ",
        bar("ＶＡＰＯＲ ＭＡＬＬ", ["Ｆｏｏｄ Ｃｏｕｒｔ", "Ｍｕｓｉｃ", "Ｆｏｕｎｔａｉｎ", "Ｅｘｉｔ"], active=1),
        [
            heading("リサフランク420 / 現代のコンピュー", "Now playing in the atrium. Please enjoy your stay."),
            transport("is-play", "▶", readout=("7:21", None), status=("ok", "Smooth jazz · 67% speed")),
            table(["Track", "Artist", "Year", "Mood"], [
                {"state": "is-active", "cells": ["リサフランク420 / 現代のコンピュー", "Macintosh Plus", "2011", ("badge", "accent", "Nostalgic")]},
                ["Palm Mall", "Palm Mall", "2014", ("badge", "", "Ambient")],
                {"state": "is-selected", "cells": ["Enjoy Your Stay", "Various", "1995", ("badge", "success", "Hopeful")]},
                ["Fountain Plaza", "Windows 96", "2015", ("badge", "warning", "Liminal")],
            ], sort=2),
            pagination(4, 2, label="Tracks"),
            toolbar(avatars("♒", "☯", "✿", size="lg"), badges(("accent", "Ａｅｓｔｈｅｔｉｃ"), ("success", "Ｃｈｉｌｌ"))),
            card(heading("Ｆｏｏｄ Ｃｏｕｒｔ", "Open until 9pm. Try the orange julius.", level=2),
                 toolbar(btn("Visit", "primary"), btn("Later", "ghost"))),
            empty("◬", "The mall is closed", "It has been closed since 1998."),
        ],
        status_bar([("lamp", "is-on", "Fountain"), ("mono", "EST. 1987"), ("text", "Ｐｌｅａｓｅ ｅｎｊｏｙ ｙｏｕｒ ｓｔａｙ")]),
    )


@theme("material")
def _():
    return page(
        "material", "Inbox",
        bar("Mail", ["Inbox", "Starred", "Sent", "Drafts"]),
        [
            toolbar(field("search", "Search mail", "Search mail"),
                    btn("⟳", "ghost", tooltip="Refresh", icon=True, aria="Refresh"),
                    btn("⋮", "ghost", tooltip="More", icon=True, aria="More")),
            chips(["Primary", "Social", "Promotions", "Updates"]),
            table(["From", "Subject", "Received"], [
                {"state": "is-active", "cells": [("avatar", "AK", "Ana K."), "Design review moved to Thursday", "10:42"]},
                [("avatar", "GH", "GitHub"), "[ftl-themes] CI passed on main", "09:15"],
                {"state": "is-selected", "cells": [("avatar", "MR", "Marco R."), "Q3 roadmap draft — comments welcome", "Yesterday"]},
                [("avatar", "LP", "Lena P."), "Lunch?", "Mon"],
            ], sort=2, sort_dir="descending"),
            pagination(3, 1, label="Mail pages"),
            card(heading("Compose", level=2),
                 form("New message",
                      ("text", "To", "team@example.com"),
                      ("text", "Subject", "Weekly update"),
                      ("textarea", "Message", "Hi all — here's what shipped this week…")),
                 toolbar(btn("Send", "primary"), btn("Discard", "ghost"))),
            toast("success", "Message sent. Undo"),
            skeleton(),
        ],
        status_bar([("text", "3.2 GB of 15 GB used"), ("status", "ok", "Synced")]),
    )


@theme("barbie")
def _():
    return page(
        "barbie", "Dreamhouse Planner",
        bar("Dreamhouse", ["Rooms", "Closet", "Friends", "Garage"]),
        [
            heading("Hi Barbie!", "Planning the pool party for Saturday."),
            stats(("12", "Guests confirmed", ("up", "+4 today")), ("3", "Outfit changes"), ("1", "Pink convertible")),
            panel("Guest list",
                  toolbar(avatars("K", "S", "T", "M", "R", size="lg")),
                  table(["Friend", "RSVP", "Bringing"], [
                      {"state": "is-active", "cells": [("avatar", "K", "Ken"), ("status", "ok", "Yes"), "Surfboard"]},
                      [("avatar", "S", "Skipper"), ("status", "ok", "Yes"), "Playlist"],
                      {"state": "is-selected", "cells": [("avatar", "T", "Teresa"), ("status", "warn", "Maybe"), "Cupcakes"]},
                      [("avatar", "M", "Midge"), ("status", "ok", "Yes"), "Lemonade"],
                  ], sort=None, sticky=False)),
            segmented(["Pool", "Rooftop", "Garden"], label="Party location"),
            card(form("Outfit",
                      ("select", "Look", ["Poolside glam", "Disco", "Western", "Astronaut"]),
                      ("switch", "Matching sunglasses", True),
                      ("textarea", "Notes", "Pink, obviously.")),
                 toolbar(btn("Save look", "primary"), btn("Shuffle", "secondary"))),
            toast("success", "Invitations sent!"),
        ],
        status_bar([("lamp", "is-on", "Dreamhouse"), ("text", "Malibu"), ("mono", "Sat 2:00 PM")]),
    )


@theme("hot-wheels")
def _():
    return page(
        "hot-wheels", "Hot Wheels — Race Day",
        bar("HOT WHEELS", ["Race", "Garage", "Tracks", "Leaderboard"]),
        [
            transport("is-play", "Race!", readout=("00:03.41", "lap"), lamps=[("is-on", "Booster"), ("is-warn", "Loop")],
                      status=("ok", "Lap 2 of 3")),
            stats(("312 mph", "Top speed", ("up", "New record")), ("4", "Loops cleared"), ("1st", "Position")),
            table(["Pos", "Car", "Driver", "Best lap"], [
                {"state": "is-active", "cells": ["1", "Twin Mill", "You", ("mono", "3.41")]},
                ["2", "Bone Shaker", "Rival", ("mono", "3.58")],
                {"state": "is-selected", "cells": ["3", "Deora II", "Cousin", ("mono", "3.77")]},
                ["4", "Rodger Dodger", "Dad", ("mono", "4.02")],
            ], sort=3),
            panel("Build a track",
                  form("Track pieces",
                       ("select", "Launcher", ["Super charger", "Rubber band", "Gravity drop"]),
                       ("slider", "Loops", 0, 6, 2),
                       ("switch", "Shark jump", True))),
            toolbar(badges(("danger", "Red Line"), ("warning", "Treasure Hunt"), ("success", "Mainline")),
                    btn("Open garage", "primary")),
        ],
        status_bar([("lamp", "is-on", "Track powered"), ("mono", "SINCE 1968"), ("text", "Challenge accepted.")]),
    )


@theme("lego-classic")
def _():
    return page(
        "lego-classic", "Galaxy Explorer — Build Instructions",
        bar("LEGO", ["Build", "Inventory", "Minifigures", "Sets"]),
        [
            crumbs(["Sets", "Classic Space", "928 Galaxy Explorer"]),
            stats(("338", "Pieces"), ("4", "Minifigures"), ("Step 24", "of 60", ("up", "40% complete"))),
            pagination(6, 3, label="Instruction pages"),
            table(["Part", "Color", "Qty", "Found"], [
                {"state": "is-active", "cells": ["Brick 2×4", ("badge", "danger", "Red"), "12", ("status", "ok", "12/12")]},
                ["Plate 1×6", ("badge", "", "Gray"), "8", ("status", "ok", "8/8")],
                {"state": "is-selected", "cells": ["Slope 45° 2×2", ("badge", "warning", "Yellow"), "6", ("status", "warn", "4/6")]},
                ["Space logo tile", ("badge", "", "Blue"), "2", ("status", "error", "0/2")],
            ], sort=0),
            panel("Minifigures",
                  toolbar(avatars("R", "W", "Y", "B", size="lg")),
                  segmented(["Red", "White", "Yellow", "Blue"], label="Suit color")),
            alert("warning", "2 pieces missing — check under the sofa."),
            toolbar(btn("Previous step", "secondary"), btn("Next step", "primary")),
        ],
        status_bar([("lamp", "is-on", "Build mode"), ("mono", "SET 928"), ("text", "Ages 7–12")]),
    )


# --- Index ----------------------------------------------------------------

def index(names):
    links = "\n".join(
        f'  <a class="ftl-dropdown-item" href="{n}.html">{e(n)}</a>' for n in names
    )
    return f"""<!DOCTYPE html>
<!-- Generated by scripts/build_examples.py -->
<html lang="en" data-theme="material">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ftl-themes — examples</title>
<link rel="stylesheet" href="../dist/material.css">
</head>
<body class="ftl-app">
<header class="ftl-app-bar"><span class="ftl-nav-brand">ftl-themes examples</span></header>
<main class="ftl-app-main">
<h1>One page per theme</h1>
<p>Every page is built only from ftl-themes classes and semantic HTML — no custom CSS, no inline styles.</p>
<nav class="ftl-dropdown" aria-label="Themes">
{links}
</nav>
</main>
</body>
</html>
"""


def library_classes():
    css = [p.read_text() for p in (ROOT / "core").glob("*.css")]
    css += [p.read_text() for p in (ROOT / "themes").glob("*/*.css")]
    return {c for text in css for c in re.findall(r"\.((?:ftl|is)-[\w-]+)", text)}


def violations(html, defined):
    """The page rule: library classes and semantic HTML only."""
    body = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    problems = []
    if re.search(r"<style\b|\sstyle=", body):
        problems.append("contains a <style> block or style attribute")
    used = {c for attr in re.findall(r'class="([^"]+)"', body) for c in attr.split()}
    if used - defined:
        problems.append("uses classes the library doesn't define: " + ", ".join(sorted(used - defined)))
    return problems


def main():
    OUT.mkdir(exist_ok=True)
    themes = sorted(p.name for p in (ROOT / "themes").iterdir() if (p / "theme.css").exists())
    missing = [t for t in themes if t not in PAGES]
    if missing:
        raise SystemExit(f"no example page defined for: {', '.join(missing)}")
    defined = library_classes()
    pages = {f"{name}.html": PAGES[name] for name in themes}
    pages["index.html"] = lambda: index(themes)
    for filename, build in pages.items():
        _field_id[0] = 0
        html = build()
        problems = violations(html, defined)
        if problems:
            raise SystemExit(f"examples/{filename}: " + "; ".join(problems))
        (OUT / filename).write_text(html)
        print(f"built examples/{filename}")


if __name__ == "__main__":
    main()
