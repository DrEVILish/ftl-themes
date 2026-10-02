#!/usr/bin/env python3
"""Themed transactional emails (PLAN.md §22) -> dist/email/<slug>/<name>.html|.txt

Email clients don't support custom properties, @layer, web fonts or most
layout CSS, so each theme's tokens are resolved here to literal colours and
written into table-based, inline-styled HTML (600px wide) plus a plain-text
version. Each email keeps the theme's palette, its title-bar colour and
radius; effects (blur, glow, gradients) don't survive email clients, so
gradients collapse to their first colour.

Usage: python3 scripts/build_emails.py [slug ...]   (default: every theme)
"""
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_manifest import root_tokens, resolve_color  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dist" / "email"
WEB_SAFE = {"arial", "helvetica", "verdana", "tahoma", "trebuchet ms", "georgia",
            "times new roman", "courier new", "segoe ui", "-apple-system", "system-ui"}

EMAILS = {
    "welcome": dict(subject="Welcome to {app}", heading="Welcome aboard",
        paras=["Your {app} account is ready. Sign in any time to pick up where you left off."],
        cta=("Open {app}", "{url}")),
    "verify-email": dict(subject="Confirm your email address", heading="Confirm your email",
        paras=["Tap the button below to confirm this is your address. The link expires in 24 hours.",
               "If you didn't create an account, you can ignore this message."],
        cta=("Confirm email", "{url}/verify")),
    "reset-password": dict(subject="Reset your password", heading="Reset your password",
        paras=["Someone asked to reset the password for your account. If it was you, choose a new one below.",
               "The link expires in 1 hour. If it wasn't you, your password stays the same."],
        cta=("Choose a new password", "{url}/reset")),
    "receipt": dict(subject="Your receipt from {app}", heading="Thanks for your payment",
        paras=["Here's your receipt. Keep it for your records."],
        rows=[("Company plan, monthly", "$49.00"), ("Extra seats x 2", "$18.00"), ("Tax", "$13.40"), ("Total paid", "$80.40")],
        cta=("View invoice", "{url}/billing")),
    "alert": dict(subject="Action needed: payment failed", heading="Your payment didn't go through", tone="danger",
        paras=["We couldn't charge the card ending 4242 for your Company plan. Update it within 7 days to keep your workspace active."],
        cta=("Update payment method", "{url}/billing")),
    "weekly-digest": dict(subject="Your week in {app}", heading="Your week at a glance",
        paras=["Here's what happened in your workspace this week."],
        rows=[("New playlists", "12"), ("Tracks added", "148"), ("Shared with you", "5")],
        cta=("See all activity", "{url}/activity")),
}


def solid(tokens, value, base=(255, 255, 255, 1.0)):
    """A literal #rrggbb for a token value: first colour of a gradient,
    translucent colours composited over base."""
    if value is None:
        return None
    m = re.search(r"(#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|var\(--[a-z0-9-]+[^)]*\))", value)
    c = resolve_color(tokens, m.group(1) if m else value)
    if c is None:
        return None
    r, g, b, a = c
    r, g, b = (round(x * a + y * (1 - a)) for x, y in zip((r, g, b), base[:3]))
    return "#%02x%02x%02x" % (r, g, b)


def lum(hexc):
    r, g, b = (int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True)
    return (x + 0.05) / (y + 0.05)


def ink_on(bg, *cands):
    """The first candidate that reads at 4.5:1 on bg, else black/white."""
    for c in cands:
        if c and contrast(c, bg) >= 4.5:
            return c
    return "#000000" if contrast("#000000", bg) >= contrast("#ffffff", bg) else "#ffffff"


def font_stack(tokens):
    fams = [f.strip().strip("'\"") for f in tokens.get("--font", "Arial").split(",")]
    safe = [f for f in fams if f.lower() in WEB_SAFE]
    mono = "mono" in tokens.get("--font", "").lower() or "courier" in tokens.get("--font", "").lower()
    tail = "'Courier New', Courier, monospace" if mono else "Arial, Helvetica, sans-serif"
    return ", ".join([f"'{f}'" if " " in f else f for f in safe] + [tail])


def palette(slug):
    t = root_tokens((ROOT / "themes" / slug / "theme.css").read_text(), slug)
    bg = solid(t, t.get("--bg")) or "#ffffff"
    base = tuple(int(bg[i:i + 2], 16) for i in (1, 3, 5)) + (1.0,)
    surface = solid(t, t.get("--surface"), base) or bg
    text = ink_on(surface, solid(t, t.get("--text"), base))
    muted = ink_on(surface, solid(t, t.get("--muted"), base), text)
    accent = solid(t, t.get("--accent"), base) or "#2563eb"
    bar = solid(t, t.get("--app-bar-bg") or t.get("--modal-header-bg"), base) or accent
    danger = solid(t, t.get("--danger"), base) or "#c0392b"
    radius = re.sub(r"[^\d.a-z%]", "", (t.get("--radius") or "4px").split()[0]) or "4px"
    if "var(" in (t.get("--radius") or ""):
        radius = "4px"
    return dict(bg=bg, surface=surface, text=text, muted=muted, accent=accent,
                on_accent=ink_on(accent, solid(t, t.get("--on-accent"), base)),
                bar=bar, on_bar=ink_on(bar, solid(t, t.get("--app-bar-fg"), base), solid(t, t.get("--modal-header-fg"), base)),
                border=solid(t, t.get("--border"), base) or muted, danger=danger,
                on_danger=ink_on(danger, solid(t, t.get("--on-danger"), base)),
                font=font_stack(t), radius=radius)


def render(slug, name, spec, app="Playlist Lab", url="https://app.example.com"):
    p = palette(slug)
    fill = lambda s: s.format(app=app, url=url)
    esc = lambda s: html.escape(fill(s))
    tone_bg, tone_fg = (p["danger"], p["on_danger"]) if spec.get("tone") == "danger" else (p["accent"], p["on_accent"])
    rows = ""
    for i, (k, v) in enumerate(spec.get("rows", [])):
        last = i == len(spec["rows"]) - 1
        w = "font-weight:bold;" if last and name == "receipt" else ""
        rows += (f'<tr><td style="padding:8px 0;border-top:1px solid {p["border"]};color:{p["text"]};{w}">{esc(k)}</td>'
                 f'<td align="right" style="padding:8px 0;border-top:1px solid {p["border"]};color:{p["text"]};{w}">{esc(v)}</td></tr>')
    table = (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:16px 0;font-size:15px;">{rows}</table>') if rows else ""
    paras = "".join(f'<p style="margin:0 0 16px;font-size:16px;line-height:24px;color:{p["text"]};">{esc(x)}</p>' for x in spec["paras"])
    label, href = spec["cta"]
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark"><title>{esc(spec["subject"])}</title></head>
<body style="margin:0;padding:0;background:{p["bg"]};">
<span style="display:none;max-height:0;overflow:hidden;">{esc(spec["paras"][0])}</span>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{p["bg"]};"><tr><td align="center" style="padding:24px 12px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="width:100%;max-width:600px;background:{p["surface"]};border:1px solid {p["border"]};border-radius:{p["radius"]};font-family:{p["font"]};">
<tr><td style="padding:14px 24px;background:{p["bar"]};color:{p["on_bar"]};font-size:15px;font-weight:bold;border-radius:{p["radius"]} {p["radius"]} 0 0;">{esc(app)}</td></tr>
<tr><td style="padding:28px 24px 8px;">
<h1 style="margin:0 0 16px;font-size:22px;line-height:28px;color:{p["text"]};">{esc(spec["heading"])}</h1>
{paras}{table}
<table role="presentation" cellpadding="0" cellspacing="0" style="margin:8px 0 24px;"><tr><td style="background:{tone_bg};border-radius:{p["radius"]};">
<a href="{html.escape(fill(href))}" style="display:inline-block;padding:12px 22px;color:{tone_fg};font-size:16px;font-weight:bold;text-decoration:none;">{esc(label)}</a>
</td></tr></table>
</td></tr>
<tr><td style="padding:16px 24px;border-top:1px solid {p["border"]};font-size:12px;line-height:18px;color:{p["muted"]};">
You're getting this because you have a {esc(app)} account. <a href="{html.escape(url)}/settings/email" style="color:{p["muted"]};">Email settings</a></td></tr>
</table></td></tr></table></body></html>
"""
    txt = "\n\n".join([fill(spec["heading"]), *[fill(x) for x in spec["paras"]],
                       *("{}: {}".format(fill(k), fill(v)) for k, v in spec.get("rows", [])),
                       f"{fill(label)}: {fill(href)}", f"-- \n{app} · Email settings: {url}/settings/email"]) + "\n"
    return doc, txt


def main(slugs):
    for slug in slugs:
        d = OUT / slug
        d.mkdir(parents=True, exist_ok=True)
        for name, spec in EMAILS.items():
            doc, txt = render(slug, name, spec)
            (d / f"{name}.html").write_text(doc)
            (d / f"{name}.txt").write_text(txt)
    print(f"built dist/email for {len(slugs)} theme(s), {len(EMAILS)} templates each")


if __name__ == "__main__":
    if sys.argv[1:] == ["--test"]:
        assert contrast("#000000", "#ffffff") > 20 and ink_on("#000000") == "#ffffff"
        p = palette("blue-future")
        assert all(v.startswith("#") for k, v in p.items() if k not in ("font", "radius")), p
        assert contrast(p["text"], p["surface"]) >= 4.5 and contrast(p["on_accent"], p["accent"]) >= 4.5
        print("ok"); sys.exit()
    slugs = sys.argv[1:] or sorted(p.parent.name for p in (ROOT / "themes").glob("*/theme.css"))
    main(slugs)
