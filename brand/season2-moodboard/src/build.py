"""Build the self-contained moodboard: inlines logos, Season 1 posters, reference images and fixture rows.

Usage: python3 build.py   ->  ../ICL-Season2-Moodboard.html
"""
import base64
import pathlib

HERE = pathlib.Path(__file__).parent
OUT = HERE.parent / "ICL-Season2-Moodboard.html"


def data_uri(path):
    mime = {"svg": "image/svg+xml", "jpg": "image/jpeg", "png": "image/png", "webp": "image/webp"}[path.suffix[1:]]
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


# Reference images R01–R20 grouped by the device they illustrate.
REFS = {
    "A": [5, 9, 12, 13],      # giant numerals / type behind the player
    "B": [18, 19, 20],        # script crossing caps
    "C": [6, 10, 11, 16],     # ribbons and streaks
    "D": [1, 3, 4],           # UI collage, walkout card
    "E": [2, 14, 15],         # grid, labels, circled dates, role circles
    "F": [7, 8],              # halftone, kit texture
    "G": [17],                # quiet register
}

TEAMS = {
    "BT": ("BLUE TITANS", "--t-bt"), "DD": ("DESERT DEVILS", "--t-dd"),
    "FL": ("FIRST LEGENDS", "--t-fl"), "ER": ("ENHANCE ROYALS", "--t-er"),
    "BS": ("BIZPOINT STRIKERS", "--t-bs"), "NSK": ("NAHDA SUPER KINGS", "--t-nsk"),
}
FIXTURES = [  # placeholders until the S2 schedule is confirmed
    ("09:00", "BT", "DD", "G01"), ("10:30", "FL", "ER", "G02"), ("12:00", "BS", "NSK", "G01"),
    ("13:30", "DD", "FL", "G02"), ("15:00", "ER", "BS", "G01"),
]


def fixture_rows():
    rows = []
    for time, a, b, ground in FIXTURES:
        (an, ac), (bn, bc) = TEAMS[a], TEAMS[b]
        sw = lambda c: f'<i style="display:inline-block;width:calc(18*var(--u));height:calc(18*var(--u));border-radius:2px;background:var({c})"></i>'
        rows.append(
            '<div class="flow" style="display:grid;grid-template-columns:calc(120*var(--u)) 1fr calc(60*var(--u)) 1fr calc(70*var(--u));'
            'align-items:center;gap:calc(14*var(--u));height:calc(100*var(--u));border-bottom:1px solid var(--line-strong)">'
            f'<span style="font-family:var(--f-mono);font-size:calc(20*var(--u));letter-spacing:.14em">{time}</span>'
            f'<span style="display:flex;align-items:center;gap:calc(12*var(--u));font-family:var(--f-display);font-weight:800;font-size:calc(38*var(--u));white-space:nowrap">{sw(ac)}{an}</span>'
            '<span style="font-family:var(--f-mono);font-size:calc(18*var(--u));text-align:center;color:var(--ink-mute)">VS</span>'
            f'<span style="display:flex;align-items:center;gap:calc(12*var(--u));font-family:var(--f-display);font-weight:800;font-size:calc(38*var(--u));white-space:nowrap">{sw(bc)}{bn}</span>'
            f'<span style="font-family:var(--f-mono);font-size:calc(18*var(--u));letter-spacing:.14em;text-align:right;color:var(--ink-mute)">{ground}</span>'
            "</div>"
        )
    return "\n".join(rows)


def refs(letter):
    out = []
    for n in REFS[letter]:
        uri = data_uri(HERE / "references" / f"r{n:02d}.jpg")
        out.append(f'<figure><img src="{uri}" alt="Reference R{n:02d}" loading="lazy"><figcaption>R{n:02d}</figcaption></figure>')
    return "".join(out)


html = (HERE / "moodboard.src.html").read_text()
for p in sorted((HERE / "assets").iterdir()) + sorted((HERE / "cutouts").iterdir()):
    html = html.replace("{{" + p.stem + "}}", data_uri(p))
for letter in REFS:
    html = html.replace("{{refs-" + letter + "}}", refs(letter))
html = html.replace("{{fixtures}}", fixture_rows())

FACES = [  # family, file, weight range (variable fonts)
    ("Big Shoulders Display", "BigShouldersDisplay-latin.woff2", "800 900"),
    ("Mrs Saint Delafield", "MrsSaintDelafield-latin.woff2", "400"),
    ("Outfit", "Outfit-latin.woff2", "300 700"),
    ("JetBrains Mono", "JetBrainsMono-latin.woff2", "400 700"),
]
html = html.replace("{{fontfaces}}", "\n".join(
    f"@font-face{{font-family:'{fam}';src:url(data:font/woff2;base64,"
    + base64.b64encode((HERE / "fonts" / f).read_bytes()).decode()
    + f") format('woff2');font-weight:{w};font-style:normal;font-display:block}}"
    for fam, f, w in FACES))
assert "{{" not in html, html[html.index("{{"):html.index("{{") + 40]
OUT.write_text(html)
print(OUT, f"{len(html) / 1e6:.2f} MB")
