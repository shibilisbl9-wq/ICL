"""Season 2 'coming soon' Instagram set. Renders SVG -> PNG with rsvg-convert.
Needs Montserrat + Montserrat Alternates installed (fontconfig)."""
import re, subprocess, pathlib
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
LOGO = (HERE / '../../../brand/logo/icl-season2-reverse-transparent.svg').resolve().read_text()
LOGO_INNER = re.sub(r'^.*?<svg[^>]*>', '', LOGO, flags=re.S).rsplit('</svg>', 1)[0]

NIGHT = '#1c0f33'; PURPLE = '#452874'; LAV = '#b9a9d0'
GREEN_B, GREEN_D = '#8fe3a8', '#4fb872'
PURP_B, PURP_M = '#f1c9ff', '#b27ae0'

DEFS = f'''<defs>
<radialGradient id="glow" cx="0.5" cy="0.28" r="0.75"><stop offset="0" stop-color="{PURPLE}"/><stop offset="0.55" stop-color="#26114f"/><stop offset="1" stop-color="{NIGHT}"/></radialGradient>
<linearGradient id="tg-green" x1="0" y1="0" x2="0.9" y2="1"><stop offset="0" stop-color="{GREEN_B}"/><stop offset="1" stop-color="{GREEN_D}"/></linearGradient>
<linearGradient id="tg-purple" x1="0" y1="0" x2="0.9" y2="1"><stop offset="0" stop-color="{PURP_B}"/><stop offset="1" stop-color="{PURP_M}"/></linearGradient>
<linearGradient id="st-p" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#d880fb" stop-opacity="0"/><stop offset="1" stop-color="#d880fb"/></linearGradient>
<linearGradient id="st-g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{GREEN_B}" stop-opacity="0"/><stop offset="1" stop-color="{GREEN_B}"/></linearGradient>
</defs>'''

def logo(x, y, w):
    h = w * 580 / 690
    return f'<svg x="{x}" y="{y}" width="{w}" height="{h:.0f}" viewBox="140 300 690 580">{LOGO_INNER}</svg>'

def streaks(cx, cy, scale=1.0, opacity=1.0):
    # the ball's speed-line trail: rounded streaks at 45 deg, running up-right
    bars = [(0, 0, 420, 'p'), (40, 34, 520, 'p'), (10, 68, 360, 'g'), (70, 102, 300, 'p'), (60, 136, 220, 'g'), (110, 170, 140, 'p')]
    r = ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="14" rx="7" fill="url(#st-{c})"/>' for x, y, w, c in bars)
    return f'<g opacity="{opacity}" transform="translate({cx} {cy}) rotate(-45) scale({scale}) translate(-300 -90)">{r}</g>'

def caps(x, y, text, size=26, fill=GREEN_B, anchor='middle', track=0.32):
    return f'<text x="{x}" y="{y}" font-family="Montserrat" font-weight="700" font-size="{size}" letter-spacing="{size*track:.1f}" fill="{fill}" text-anchor="{anchor}">{text}</text>'

def display(x, y, text, size, fill='#ffffff', anchor='middle', weight=700):
    return f'<text x="{x}" y="{y}" font-family="Montserrat Alternates" font-weight="{weight}" font-size="{size}" letter-spacing="{-size*0.02:.1f}" fill="{fill}" text-anchor="{anchor}">{text}</text>'

def body(x, y, text, size=34, fill=LAV, anchor='start'):
    return f'<text x="{x}" y="{y}" font-family="Montserrat" font-weight="500" font-size="{size}" fill="{fill}" text-anchor="{anchor}">{text}</text>'

def frame(w, h, content):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{DEFS}<rect width="{w}" height="{h}" fill="url(#glow)"/>{content}</svg>'

W, H = 1080, 1350
posts = {}

# 1. Announcement: the logo, then "coming soon"
posts['01-announcement'] = frame(W, H, ''.join([
    logo(150, 120, 780),
    caps(540, 950, 'THE WAIT IS ALMOST OVER'),
    display(540, 1090, 'coming soon', 132),
    caps(540, 1250, 'UAE IMAMA  ·  SEASON 2', 22, LAV),
]))

# 2. Big "2": round two
posts['02-round-two'] = frame(W, H, ''.join([
    display(1150, 1260, '2', 1250, 'url(#tg-green)', 'end'),
    streaks(250, 790, 1.1, 0.9),
    caps(80, 170, 'IMAMA CRICKET LEAGUE', 24, GREEN_B, 'start'),
    display(74, 300, 'round two.', 118, anchor='start'),
    body(80, 370, 'New season. Same rivalries.'),
    body(80, 418, 'Bigger stage.'),
    logo(70, 1075, 300),
]))

# 3. Get ready: gear-up lines, follow CTA
posts['03-get-ready'] = frame(W, H, ''.join([
    streaks(900, 250, 0.9, 0.7),
    caps(80, 330, 'SEASON 2  ·  COMING SOON', 24, GREEN_B, 'start'),
    display(74, 470, 'pads on.', 128, anchor='start'),
    display(74, 610, 'gloves on.', 128, anchor='start'),
    display(74, 750, 'season 2', 128, 'url(#tg-purple)', 'start'),
    display(74, 890, 'is coming.', 128, 'url(#tg-purple)', 'start'),
    f'<rect x="80" y="990" width="920" height="2" fill="#35255a"/>',
    body(80, 1070, 'Follow for the teams, fixtures', 34),
    body(80, 1118, 'and registration drop.', 34),
    logo(770, 1030, 240),
]))

# Story 1080x1920 (top/bottom 250px kept clear for Instagram UI)
story = frame(1080, 1920, ''.join([
    streaks(950, 150, 0.8, 0.7),
    logo(110, 300, 860),
    caps(540, 1140, 'THE WAIT IS ALMOST OVER', 28),
    display(540, 1300, 'coming soon', 150),
    body(540, 1560, 'Tap follow. Turn on notifications.', 36, LAV, 'middle'),
    body(540, 1610, 'Be first to know when Season 2 drops.', 36, LAV, 'middle'),
]))

files = {f'ig-post-{k}.svg': v for k, v in posts.items()}
files['ig-story-coming-soon.svg'] = story
for name, svg in files.items():
    p = HERE / name
    p.write_text(svg)
    subprocess.run(['rsvg-convert', '-o', str(OUT / name.replace('.svg', '.png')), str(p)], check=True)
print('\n'.join(files))
