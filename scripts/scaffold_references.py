#!/usr/bin/env python3
"""Scaffolds references/<slug>/SOURCES.md for every theme: three specific,
named things to screenshot/photograph, plus a search hint good enough to
find a source image once network access allows it.

This exists because pulling real reference images requires broader network
access than a sandboxed session gets by default (see references/README.md
"Getting the images" for the current state) — the targets are pinned down
now so fetching three files per theme later is mechanical, not a second
research pass.

Usage: python3 scripts/scaffold_references.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# slug: [(filename, what to capture, a search/source hint), x3]
TARGETS = {
"alienware": [
    ("01-alienfx-zones.png", "AlienFX lighting-zone editor: the per-zone color picker grid (Alien head, keyboard, power button, rails)", "Dell AlienFX / Alienware Command Center lighting zones screenshot"),
    ("02-chassis-angles.jpg", "The matte-black chassis itself: angular vents and cut edges, not the software", "Alienware Aurora or laptop chassis product photo, angular vents"),
    ("03-command-center-overview.png", "Alienware Command Center's full dashboard (FX / Performance tabs) for general chrome/layout", "Alienware Command Center dashboard screenshot"),
],
"aperture": [
    ("01-test-chamber.jpg", "An Aperture Science test chamber: off-white panels, the blue/orange portal pair visible", "Portal test chamber screenshot off-white orange blue"),
    ("02-signage.jpg", "Aperture Science wall signage/stencil typography (the Univers-style lettering)", "Aperture Science signage Portal wiki"),
    ("03-glados-panel.jpg", "A GLaDOS control panel or turret/personality-core interface screen", "Portal GLaDOS control panel screenshot"),
],
"aqua": [
    ("01-window-chrome.png", "A Mac OS X Snow Leopard window: brushed-metal titlebar, pinstripe, traffic-light buttons", "Mac OS X Snow Leopard window screenshot brushed metal"),
    ("02-gel-buttons.png", "Aqua's gel/candy buttons close up, including the pulsing blue default button", "Aqua interface gel button pulsing default screenshot"),
    ("03-dock.png", "The Aqua Dock with reflection, for the gloss/reflection language", "Mac OS X Aqua dock screenshot reflection"),
],
"barbie": [
    ("01-dreamhouse-box.jpg", "Barbie Dreamhouse packaging — the exact brand pink, gold accents", "Barbie Dreamhouse box packaging photo"),
    ("02-logo.png", "The Barbie wordmark/logo (rounded, hot pink, gold sparkle treatment)", "Barbie logo pink gold"),
    ("03-app-ui.jpg", "An official Barbie app or website UI screen, for pill-chrome/rounded-button reference", "Barbie official app screenshot UI"),
],
"bloomberg": [
    ("01-terminal-screen.jpg", "A real Bloomberg Terminal screen: amber/black data density, function-key row", "Bloomberg Terminal screen photo amber black"),
    ("02-keyboard.jpg", "The Bloomberg keyboard with its colored function keys (GO, HELP, MENU)", "Bloomberg terminal keyboard colored keys photo"),
    ("03-multi-monitor.jpg", "A trader's multi-monitor Bloomberg desk setup, for density/layout reference", "Bloomberg terminal trading desk multi monitor photo"),
],
"blue-future": [
    ("01-apollo-console.jpg", "An Apollo-era Mission Control console: pale-green metal, analog dials, physical switches", "NASA Apollo Mission Control restored console photo"),
    ("02-apollo-room-wide.jpg", "Wide shot of the restored Mission Control room for layout/density reference", "NASA Apollo Mission Control Center restoration wide shot"),
    ("03-crt-readout.jpg", "A period CRT readout/oscilloscope display, for the monospace-readout-glow language", "vintage CRT telemetry readout monochrome photo"),
],
"cue-lab": [
    ("01-cue-list.png", "QLab's cue list: colored cue-type rows, the standing-by playhead triangle", "QLab 5 cue list screenshot playhead"),
    ("02-go-button.png", "QLab's GO button and transport controls close up", "QLab GO button screenshot"),
    ("03-workspace-overview.png", "A full QLab workspace (sidebar + cue list + inspector) for chrome/density reference", "QLab workspace overview screenshot"),
],
"cyber-goth": [
    ("01-outfit.jpg", "A cybergoth outfit: black PVC/vinyl with a UV-reactive neon accent", "cybergoth fashion PVC neon photo"),
    ("02-uv-lighting.jpg", "A club/event under UV blacklight for the neon-on-black glow reference", "cybergoth club UV blacklight neon photo"),
    ("03-hair-falls.jpg", "Cybergoth accessories (neon dreadlock falls, goggles) for the accent-color pairing", "cybergoth neon dreadlocks goggles photo"),
],
"death-star": [
    ("01-control-room.jpg", "A Death Star control-room set/still: black panels, sparse blue/white indicator lights", "Death Star control room Star Wars still"),
    ("02-targeting-computer.jpg", "The Death Star superlaser targeting console", "Death Star targeting computer screen Star Wars"),
    ("03-imperial-console-detail.jpg", "A close-up Imperial console panel for the indicator-block scale/spacing", "Imperial console Star Wars close up indicator lights"),
],
"hot-wheels": [
    ("01-track-orange.jpg", "The orange Hot Wheels track itself, close up", "Hot Wheels orange track photo"),
    ("02-blister-pack.jpg", "A Hot Wheels blister-pack card, for the flame logo and card typography", "Hot Wheels blister pack card photo"),
    ("03-flame-logo.png", "The Hot Wheels flame logo on its own", "Hot Wheels logo flame"),
],
"imac-g3": [
    ("01-bondi-blue-unit.jpg", "An original Bondi Blue iMac G3, full unit, for the translucent shell color", "iMac G3 Bondi Blue photo"),
    ("02-fruit-colorways.jpg", "The multicolor iMac G3 lineup (Blueberry/Grape/Tangerine/Lime/Strawberry) together", "iMac G3 five flavors colorways photo"),
    ("03-setup-assistant.png", "The Mac OS 8/9 Setup Assistant screen the unit shipped with", "Mac OS 9 Setup Assistant screenshot"),
],
"lcars": [
    ("01-tng-bridge-panel.jpg", "A TNG/DS9-era LCARS console: pill blocks and the elbow-curve rail", "LCARS Star Trek TNG console screenshot"),
    ("02-elbow-sweep.jpg", "A close-up LCARS elbow/sweep corner for the curve geometry", "LCARS elbow sweep close up"),
    ("03-full-screen.jpg", "A full LCARS display screen for the overall color-block density", "LCARS display screen Star Trek full"),
],
"lego-classic": [
    ("01-classic-space-set.jpg", "A Classic Space LEGO set box or built model, for the primary palette", "LEGO Classic Space set photo"),
    ("02-brick-studs-macro.jpg", "A macro shot of brick studs on top of a brick, for the stud texture", "LEGO brick studs macro photo"),
    ("03-instruction-booklet.jpg", "A LEGO instruction-booklet page, for the step/parts-list layout language", "LEGO instruction booklet page photo"),
],
"material": [
    ("01-app-bar-elevation.png", "A Material Design app with a colored app bar and elevation shadow on a card", "Material Design app bar elevation card screenshot"),
    ("02-fab-and-snackbar.png", "A floating action button plus a snackbar, both signature Material components", "Material Design FAB snackbar screenshot"),
    ("03-color-system.png", "Google's own Material color/elevation system diagram", "Material Design elevation color system diagram m2.material.io"),
],
"matrix": [
    ("01-digital-rain.jpg", "The Matrix digital-rain effect itself: green glyphs cascading on black", "Matrix digital rain screenshot green"),
    ("02-operator-console.jpg", "An Operator's console from the films (Tank/Link at the monitors)", "Matrix operator console screenshot green terminal"),
    ("03-code-closeup.jpg", "A close crop of the falling code for the phosphor-glow color reference", "Matrix code close up green phosphor"),
],
"msdos": [
    ("01-norton-commander.png", "Norton Commander's two-panel blue file view, double-line borders", "Norton Commander 5.0 screenshot two panel"),
    ("02-fkey-bar.png", "The F-key bar at the bottom (F1 Help, F2 Menu, ...) close up", "Norton Commander function key bar screenshot"),
    ("03-dialog-box.png", "A Norton Commander dialog/confirmation box for the double-line window chrome", "Norton Commander dialog box screenshot"),
],
"nerv": [
    ("01-magi-vote.jpg", "The MAGI system's three-way vote screen (Melchior/Balthasar/Casper)", "Evangelion MAGI system screenshot vote"),
    ("02-nerv-logo-titling.jpg", "NERV's logo and the show's title-card typography (heavy serif + Helvetica)", "Evangelion NERV logo title card typography"),
    ("03-eva-sync-panel.jpg", "An Evangelion sync-ratio / pilot status panel", "Evangelion sync ratio panel screenshot orange"),
],
"pipboy": [
    ("01-pipboy-inventory.jpg", "The Pip-Boy 3000's inventory/STAT screen, green phosphor with scanlines", "Fallout Pip-Boy 3000 inventory screen screenshot"),
    ("02-pipboy-physical.jpg", "The physical wrist-mounted Pip-Boy prop/model", "Pip-Boy 3000 physical prop replica photo"),
    ("03-special-screen.jpg", "The S.P.E.C.I.A.L. attributes screen", "Fallout Pip-Boy SPECIAL screen screenshot"),
],
"steampunk": [
    ("01-brass-gauges-leather.jpg", "Polished brass pressure gauges set into leather/wood paneling — the exact material pairing this theme should read as", "steampunk brass pressure gauge leather panel photo"),
    ("02-sight-glass.jpg", "A brass-and-glass sight-glass / liquid-level gauge (visible internal fluid + rivets)", "steampunk sight glass gauge brass photo"),
    ("03-control-panel.jpg", "A full steampunk control panel/prop: multiple gauges, brass switches, exposed rivets", "steampunk control panel brass gauges rivets prop photo"),
],
"tron": [
    ("01-grid-cycle.jpg", "The Grid from TRON: Legacy — cyan line-work on black, an identity disc or light cycle", "TRON Legacy Grid cyan light cycle screenshot"),
    ("02-cut-corner-ui.jpg", "A TRON: Legacy interface panel with its angular cut corners", "TRON Legacy UI panel cut corner screenshot"),
    ("03-clu-orange.jpg", "A CLU/Rinzler orange-accent shot, for the villain-accent color pairing", "TRON Legacy CLU orange screenshot"),
],
"vaporwave": [
    ("01-grid-horizon.jpg", "A classic vaporwave grid-horizon/sunset composition (pink/cyan)", "vaporwave grid sunset aesthetic image"),
    ("02-statue-glitch.jpg", "A vaporwave Greek-statue-plus-glitch composition, a defining genre motif", "vaporwave greek statue glitch aesthetic"),
    ("03-mall-japanese-text.jpg", "A vaporwave mall/plaza scene with Japanese katakana text overlay", "vaporwave mall aesthetic Japanese text"),
],
"win7-aero": [
    ("01-aero-glass-window.png", "A Windows 7 window with visible Aero Glass blur/translucency", "Windows 7 Aero glass window screenshot"),
    ("02-aero-taskbar.png", "The Aero glass taskbar with Aero Peek", "Windows 7 Aero taskbar glass screenshot"),
    ("03-aero-flip3d.png", "Aero Flip 3D window switcher, for the glass-depth effect", "Windows 7 Aero Flip 3D screenshot"),
],
"winamp-classic": [
    ("01-main-window.png", "Winamp's classic main window: LCD green readout, bevelled buttons", "Winamp classic skin main window screenshot"),
    ("02-equalizer.png", "The Winamp Equalizer window with its slider bank", "Winamp classic equalizer window screenshot"),
    ("03-playlist-editor.png", "The Winamp Playlist Editor window", "Winamp classic playlist editor screenshot"),
],
"windows95": [
    ("01-desktop.png", "The Windows 95 desktop: teal background, taskbar, Start button", "Windows 95 desktop screenshot teal"),
    ("02-dialog-bevels.png", "A Windows 95 dialog box for the 3D bevel chrome close up", "Windows 95 dialog box bevel screenshot"),
    ("03-explorer-window.png", "A Windows 95 Explorer window with its navy titlebar", "Windows 95 Explorer window screenshot"),
],
"winxp-luna": [
    ("01-start-menu.png", "The Luna Start menu with the green Start button", "Windows XP Luna Start menu green screenshot"),
    ("02-bliss-desktop.jpg", "The default XP desktop with the Bliss wallpaper", "Windows XP Bliss wallpaper desktop screenshot"),
    ("03-window-chrome.png", "An XP window's glossy blue titlebar/chrome close up", "Windows XP Luna window titlebar screenshot"),
],
"wmp11": [
    ("01-library-view.png", "WMP11's Library view with breadcrumbs and the black-glass chrome", "Windows Media Player 11 library screenshot"),
    ("02-now-playing.png", "WMP11's Now Playing view with the round play button", "Windows Media Player 11 now playing round button screenshot"),
    ("03-visualization.png", "A WMP11 visualization for the blue-glow backdrop reference", "Windows Media Player 11 visualization screenshot"),
],
}

HEADER = """# {label} — reference targets

Three specific things to capture for this theme, listed in `SOURCES.md`
rather than fetched yet — this session's network policy blocks the actual
image hosts (Wikipedia, Wikimedia, Fandom wikis, NASA, etc.). See
`references/README.md` for how to finish this once access is available.

| # | File | Capture this | Search hint |
|---|------|--------------|-------------|
"""


def main():
    for slug, targets in TARGETS.items():
        theme_dir = os.path.join(ROOT, "references", slug)
        os.makedirs(theme_dir, exist_ok=True)
        readme_path = os.path.join(ROOT, "themes", slug, "README.md")
        label = slug
        if os.path.exists(readme_path):
            with open(readme_path) as f:
                first = f.readline().strip()
                if first.startswith("# "):
                    label = first[2:]
        lines = [HEADER.format(label=label)]
        for fname, desc, hint in targets:
            lines.append(f"| {targets.index((fname, desc, hint)) + 1} | `{fname}` | {desc} | {hint} |\n")
        out_path = os.path.join(theme_dir, "SOURCES.md")
        with open(out_path, "w") as f:
            f.writelines(lines)
        print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
