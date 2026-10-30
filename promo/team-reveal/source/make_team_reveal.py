"""Season 2 team reveal set: one poster per team (icon / owner / manager in three square
frames) plus one poster with all six. Real photos only; missing photos get a placeholder.
Edit teams.json (names, photo file, square crop) and re-run. Renders SVG -> PNG with rsvg-convert.
Needs Montserrat + Montserrat Alternates installed (fontconfig)."""
import json, re, subprocess, pathlib
from PIL import Image, ImageOps, ImageEnhance

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
RAW, CROPS = HERE / 'photos/raw', HERE / 'photos'
LOGO = (HERE / '../../../brand/logo/icl-season2-reverse-transparent.svg').resolve().read_text()
LOGO_INNER = re.sub(r'^.*?<svg[^>]*>', '', LOGO, flags=re.S).rsplit('</svg>', 1)[0]
TEAMS = json.loads((HERE / 'teams.json').read_text())['teams']

NIGHT, RAISED, HAIR = '#140a26', '#1f1238', '#35255a'
LAV, GREEN_B = '#b9a9d0', '#8fe3a8'
W, H = 1080, 1350


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;')


def prep_photo(p):
    """Square crop, black and white, light contrast lift; saved next to the raw photos."""
    if not p.get('photo'):
        return None
    x, y, s = p['crop']
    im = Image.open(RAW / p['photo'])
    im = ImageOps.exif_transpose(im).convert('L').crop((x, y, x + s, y + s)).resize((800, 800), Image.LANCZOS)
    im = ImageEnhance.Contrast(ImageOps.autocontrast(im, cutoff=1)).enhance(1.08)
    out = CROPS / f"{pathlib.Path(p['photo']).stem}-sq.jpg"
    im.convert('RGB').save(out, quality=90)
    return f'photos/{out.name}'


def logo(x, y, w):
    h = w * 580 / 690
    return f'<svg x="{x}" y="{y}" width="{w}" height="{h:.0f}" viewBox="140 300 690 580">{LOGO_INNER}</svg>'


def caps(x, y, text, size=22, fill=GREEN_B, anchor='middle', track=0.32):
    return (f'<text x="{x}" y="{y}" font-family="Montserrat" font-weight="700" font-size="{size}" '
            f'letter-spacing="{size*track:.1f}" fill="{fill}" text-anchor="{anchor}">{esc(text)}</text>')


def name_text(x, y, text, max_w, size, fill='#ffffff', anchor='middle'):
    # Montserrat Bold caps average ~0.72em per glyph; shrink long names to fit their frame
    size = min(size, max_w / (len(text) * 0.72))
    return (f'<text x="{x}" y="{y}" font-family="Montserrat" font-weight="800" font-size="{size:.1f}" '
            f'letter-spacing="{size*0.04:.1f}" fill="{fill}" text-anchor="{anchor}">{esc(text.upper())}</text>')


def team_title(x, y, t, max_w, size, anchor='middle'):
    a, b = t['name']
    label = f'{a} {b}'.strip()
    size = min(size, max_w / (len(label) * 0.62))
    tail = f'<tspan dx="{size*0.26:.1f}" fill="{t["colors"][1]}">{esc(b)}</tspan>' if b else ''
    return (f'<text x="{x}" y="{y}" font-family="Montserrat Alternates" font-weight="700" font-size="{size:.1f}" '
            f'letter-spacing="{-size*0.02:.1f}" fill="{t["colors"][0]}" text-anchor="{anchor}">{esc(a)}{tail}</text>')


def streaks(cx, cy, color, scale=1.0, opacity=1.0):
    # the ball's speed-line trail: rounded streaks at 45 deg, running up-right
    bars = [(0, 0, 420), (40, 34, 520), (10, 68, 360), (70, 102, 300), (110, 136, 180)]
    r = ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="14" rx="7" fill="{color}"/>' for x, y, w in bars)
    return f'<g opacity="{opacity}" transform="translate({cx} {cy}) rotate(-45) scale({scale}) translate(-300 -80)">{r}</g>'


def frame_sq(uid, x, y, s, href, accent, stroke):
    """One square photo frame with a soft corner; placeholder silhouette when there is no photo."""
    r = max(8, s * 0.04)
    clip = f'<clipPath id="c{uid}"><rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{r:.0f}"/></clipPath>'
    if href:
        inner = (f'<image xlink:href="{href}" x="{x}" y="{y}" width="{s}" height="{s}" clip-path="url(#c{uid})" '
                 f'preserveAspectRatio="xMidYMid slice"/>'
                 f'<rect x="{x}" y="{y+s*0.62:.0f}" width="{s}" height="{s*0.38:.0f}" fill="url(#fade)" clip-path="url(#c{uid})"/>')
    else:
        cx = x + s / 2
        inner = (f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{r:.0f}" fill="{RAISED}"/>'
                 f'<g clip-path="url(#c{uid})" fill="{HAIR}">'
                 f'<circle cx="{cx}" cy="{y+s*0.40:.0f}" r="{s*0.16:.0f}"/>'
                 f'<ellipse cx="{cx}" cy="{y+s*0.95:.0f}" rx="{s*0.32:.0f}" ry="{s*0.30:.0f}"/></g>'
                 + caps(cx, y + s * 0.14, 'PHOTO SOON', max(9, s * 0.045), LAV, track=0.25))
    return (clip + inner +
            f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{r:.0f}" fill="none" stroke="{accent}" stroke-width="{stroke}"/>')


def defs(t=None):
    glow = (f'<radialGradient id="glow" cx="0.5" cy="0.1" r="0.85"><stop offset="0" stop-color="{t["colors"][0]}" stop-opacity="0.42"/>'
            f'<stop offset="0.6" stop-color="{NIGHT}" stop-opacity="0"/></radialGradient>') if t else (
            '<radialGradient id="glow" cx="0.5" cy="0.05" r="0.9"><stop offset="0" stop-color="#452874"/>'
            f'<stop offset="0.7" stop-color="{NIGHT}" stop-opacity="0"/></radialGradient>')
    return (f'<defs>{glow}<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{NIGHT}" stop-opacity="0"/>'
            f'<stop offset="1" stop-color="{NIGHT}" stop-opacity="0.55"/></linearGradient></defs>')


def svg(content, d):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">{d}<rect width="{W}" height="{H}" fill="{NIGHT}"/><rect width="{W}" height="{H}" fill="url(#glow)"/>{content}</svg>')


def team_poster(t, hrefs):
    c1, c2 = t['colors']
    parts = [logo(56, 48, 210),
             caps(1024, 92, f'TEAM {t["no"]}', 22, c1, 'end'),
             caps(1024, 126, 'OF 6', 16, LAV, 'end'),
             caps(540, 372, 'SEASON 2  ·  TEAM REVEAL'),
             team_title(540, 492, t, 960, 128)]
    s, gap, y = 300, 30, 560
    for i, (p, href) in enumerate(zip(t['people'], hrefs)):
        x = 60 + i * (s + gap)
        owner = p['role'] == 'OWNER'
        parts.append(frame_sq(f'{t["slug"]}{i}', x, y, s, href, c1 if owner else HAIR, 5 if owner else 2))
        parts.append(caps(x + s / 2, y + s + 52, p['role'], 18, c1 if owner else c2 if t['name'][1] else c1))
        parts.append(name_text(x + s / 2, y + s + 96, p['name'], s - 40, 30))
    parts += [streaks(950, 1150, c1, 0.42, 0.55),
              f'<text x="540" y="1105" font-family="Montserrat Alternates" font-weight="600" font-size="40" fill="#ffffff" text-anchor="middle">the battle for the best begins.</text>',
              f'<rect x="60" y="1246" width="960" height="1" fill="{HAIR}"/>',
              caps(540, 1298, 'UAE IMAMA CRICKET LEAGUE  ·  SEASON 2', 18, LAV)]
    return svg(''.join(parts), defs(t))


def group_poster(all_hrefs):
    parts = [logo(56, 40, 180),
             caps(1024, 130, 'SEASON 2  ·  TEAM REVEAL', 18, GREEN_B, 'end'),
             f'<text x="1024" y="222" font-family="Montserrat Alternates" font-weight="700" font-size="84" letter-spacing="-1.7" fill="#ffffff" text-anchor="end">meet the six.</text>']
    cw, ch, gx = 470, 300, 20
    for k, (t, hrefs) in enumerate(zip(TEAMS, all_hrefs)):
        cx, cy = 60 + (k % 2) * (cw + gx), 290 + (k // 2) * (ch + 22)
        c1 = t['colors'][0]
        parts += [f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="14" fill="{RAISED}" stroke="{HAIR}"/>',
                  f'<rect x="{cx}" y="{cy}" width="6" height="{ch}" rx="3" fill="{c1}"/>',
                  caps(cx + cw - 20, cy + 44, t['no'], 16, c1, 'end'),
                  team_title(cx + 24, cy + 50, t, 370, 36, 'start')]
        s, g = 136, 13
        for i, (p, href) in enumerate(zip(t['people'], hrefs)):
            x, y = cx + 24 + i * (s + g), cy + 76
            owner = p['role'] == 'OWNER'
            parts.append(frame_sq(f'g{k}{i}', x, y, s, href, c1 if owner else HAIR, 3 if owner else 1.5))
            parts.append(caps(x + s / 2, y + s + 26, p['role'], 11, c1 if owner else LAV, track=0.25))
            parts.append(name_text(x + s / 2, y + s + 52, p['name'], s - 4, 17))
    parts.append(caps(540, 1312, 'UAE IMAMA CRICKET LEAGUE  ·  THE BATTLE FOR THE BEST BEGINS', 16, LAV))
    return svg(''.join(parts), defs())


def render(name, s):
    p = HERE / f'{name}.svg'
    p.write_text(s)
    subprocess.run(['rsvg-convert', '-o', str(OUT / f'{name}.png'), str(p)], check=True)


all_hrefs = []
for t in TEAMS:
    hrefs = [prep_photo(p) for p in t['people']]
    all_hrefs.append(hrefs)
    render(f'team-{t["no"]}-{t["slug"]}', team_poster(t, hrefs))
render('teams-all-six', group_poster(all_hrefs))
print('done')
