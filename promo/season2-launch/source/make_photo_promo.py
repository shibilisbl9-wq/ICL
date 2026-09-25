"""Season 2 teaser v2: Higgsfield background photos + post-1 layout + 'round two.' headline."""
import subprocess, pathlib
from make_promo import logo, caps, display, body, DEFS, GREEN_B, LAV, NIGHT
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent

SHADE = f'''<linearGradient id="shade-top" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{NIGHT}" stop-opacity="0.75"/><stop offset="1" stop-color="{NIGHT}" stop-opacity="0"/></linearGradient>
<linearGradient id="shade-bot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{NIGHT}" stop-opacity="0"/><stop offset="0.45" stop-color="{NIGHT}" stop-opacity="0.8"/><stop offset="1" stop-color="{NIGHT}" stop-opacity="0.97"/></linearGradient>'''
DEFS2 = DEFS.replace('</defs>', SHADE + '</defs>')

def frame(w, h, photo, pw, ph, py, top_h, bot_y, content):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{DEFS2}'
            f'<rect width="{w}" height="{h}" fill="{NIGHT}"/>'
            f'<image xlink:href="photos/{photo}" x="0" y="{py}" width="{pw}" height="{ph}" preserveAspectRatio="none"/>'
            f'<rect width="{w}" height="{top_h}" fill="url(#shade-top)"/>'
            f'<rect y="{bot_y}" width="{w}" height="{h-bot_y}" fill="url(#shade-bot)"/>'
            f'{content}</svg>')

def text_block(cx, eyebrow_y, head_y, head_size, foot_y, foot_size=22):
    return ''.join([caps(cx, eyebrow_y, 'SEASON 2  ·  COMING SOON', 26),
                    display(cx, head_y, 'round two.', head_size),
                    caps(cx, foot_y, 'NEW SEASON. SAME RIVALRIES.', foot_size, LAV)])

jobs = {
  # 4:5 feed post, batsman under floodlights (photo raw1 is 1536x2752)
  'ig-post-round-two-batsman': frame(1080, 1350, 'raw1.png', 1080, 1935, -440, 520, 760,
        logo(300, 40, 480) + text_block(540, 1110, 1245, 150, 1310, 20)),
  # 4:5 feed post, white ball at the crease (photo raw2 is 1856x2304)
  'ig-post-round-two-ball': frame(1080, 1350, 'raw2.png', 1080, 1341, 0, 520, 760,
        logo(300, 40, 480) + text_block(540, 1110, 1245, 150, 1310, 20)),
  # 9:16 story, batsman (keeps top/bottom 250px mostly clear of text)
  'ig-story-round-two': frame(1080, 1920, 'raw1.png', 1080, 1935, -150, 760, 1120,
        logo(270, 190, 540) + text_block(540, 1450, 1610, 170, 1680, 24)),
}
for name, svg in jobs.items():
    p = HERE / f'{name}.svg'; p.write_text(svg)
    subprocess.run(['rsvg-convert', '-o', str(OUT / f'{name}.png'), str(p)], check=True)
print('\n'.join(jobs))
