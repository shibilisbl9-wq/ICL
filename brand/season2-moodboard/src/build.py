"""Build the self-contained Season 2 moodboard ("Powerplay", navy, green and blue).

Inlines fonts, the recoloured logo, Higgsfield frames, cut-outs and references.
Usage: python3 build.py [artifact.html]  ->  ../ICL-Season2-Moodboard.html (+ a skeleton-free copy for publishing)
"""
import base64
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parents[2]
OUT = HERE.parent / "ICL-Season2-Moodboard.html"
DEEP, WHITE = "#030916", "#FFFFFF"


def data_uri(path):
    mime = {"svg": "image/svg+xml", "jpg": "image/jpeg", "png": "image/png", "webp": "image/webp", "woff2": "font/woff2"}[path.suffix[1:]]
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def logo(colour):
    # Recolour the single-ink transparent lockup; the logo is never redrawn.
    svg = (ROOT / "brand/logo/icl-season2-mono-white-transparent.svg").read_text().replace("#ffffff", colour)
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


# Every image is embedded once, in ASSETS, and <img data-k="key"> tags pick it up at load.
ASSETS = {}


def asset(key, make):
    if key not in ASSETS:
        ASSETS[key] = make()
    return f'data-k="{key}"'


def gen(name):
    return asset(name, lambda: data_uri(HERE / "generated" / f"{name}.webp"))


def ref(n):
    return asset(f"r{n:02d}", lambda: data_uri(HERE / "references" / f"r{n:02d}.jpg"))


# Reference families. R21–R23 (added 2 Oct) bring the team sheet, signal and grain looks.
FAMILIES = {
    "Scale": [5, 9, 12, 13],
    "Motion": [10, 11, 16],
    "Depth": [1, 3, 4, 6],
    "Structure": [2, 14, 15, 21],
    "Signal": [22],
    "Texture": [7, 8, 23],
    "Register": [17, 18, 19, 20],
}
FAMILY_OF = {n: fam for fam, ns in FAMILIES.items() for n in ns}
PALETTE_REFS = [(21, "Team sheet"), (22, "Signal"), (23, "Grain")]  # shown large at the top of Sources

# The wall: Higgsfield frames in display order -> (title, references answered).
WALL = [
    ("numeral-02", "Giant numeral", "R09 R13"),
    ("glitch-helmet", "Signal duotone", "R22"),
    ("collage-walkout", "Collage + walkout card", "R03 R04"),
    ("swiss-teamsheet", "Team sheet", "R21"),
    ("speed-streak", "Speed streak", "R11"),
    ("loud-potm", "Loud register", "R18"),
    ("breakout-window", "Breakout window", "R06"),
    ("duotone-powerplay", "Duotone hero", "R22"),
    ("countdown-3", "Countdown numeral", "R05"),
    ("serif-captain", "Serif behind", "R12"),
    ("story-matchday", "Story · bowling arc", "R10 R11"),
    ("calendar-matchday", "Circled date", "R14"),
    ("quiet-matchday", "Quiet register", "R17"),
    ("diagonal-squad", "Diagonal band", "R02"),
    ("grain-collage", "Grain plate", "R23"),
    ("ribbon-keeper", "Ribbon", "R10 R16"),
    ("squad-grid", "Role circles", "R15"),
    ("gameday-split", "Game-day split", "R20"),
    ("texture-halftone", "Halftone kit", "R07"),
    ("texture-shards", "Shard plate", "R08"),
]
TITLE = {name: title for name, title, _ in WALL}

DEVICES = [
    ("Scale", "Giant numbers",
     "One numeral or word fills 60 to 70% of the poster and sits behind the player. Numbers in Display; names and words in the Serif.",
     ["One giant element per poster.", "The player's feet sit on or below its baseline.",
      "Green numerals on Navy; Deep or darker-green numerals on Green."],
     ["numeral-02", "countdown-3", "serif-captain"]),
    ("Motion", "Ribbons & streaks",
     "Motion is drawn, not implied. Ribbons trace the real action path and streaks trail a runner.",
     ["Ribbons follow the bat swing, the dive or the bowling arc.", "Stripes run blue, a thin chalk seam, then green, from the outside in.",
      "Streaks run horizontally, behind the direction of travel.", "One motion device per poster."],
     ["ribbon-keeper", "speed-streak", "story-matchday"]),
    ("Depth", "Break the frame",
     "Every post has a layer the player breaks through: a window, a stack of photo tiles, a UI card.",
     ["A window holds the place: the Dubai skyline, the floodlit ground.",
      "Collages use three tiles at most and one UI card: walkout song, scorecard or post.",
      "UI cards are frosted dark glass (Deep at 70%) with a 24px radius. Nothing else is rounded past 8px."],
     ["breakout-window", "collage-walkout"]),
    ("Structure", "Grids, circles, sheets",
     "The information posts. Squads, fixtures, match days and standings sit on a visible system.",
     ["Graph-paper grid at 54px on the 1080 canvas, electric blue at 25%.", "Role codes in outlined circles: BAT, BWL, WK, AR.",
      "One hand-drawn green circle per poster, on the date or stat that matters.",
      "Team sheets follow R21: electric blue ground, a green fade, the name set vertically, the squad in one column.",
      "Team posts get one green diagonal band with a tone-on-tone palm pattern."],
     ["swiss-teamsheet", "calendar-matchday", "squad-grid", "diagonal-squad"]),
    ("Signal", "Duotone & scanlines",
     "The cool one. The player rendered as a broadcast signal: green and blue duotone, scanlines, channel split and a motion smear on Deep.",
     ["Blue carries the shadows, green the highlights, Deep the ground.", "Horizontal scanlines, 4 to 6px on the canvas.",
      "Channel split of 12px or less: green left, blue right.",
      "For launches, finals and player reveals. One in every nine grid posts at most."],
     ["duotone-powerplay", "glitch-helmet"]),
    ("Texture", "Heat plates",
     "Plates fill the ground of countdowns, night posts and story backgrounds.",
     ["Halftone dots, shattered shards or spray grain, in green and blue only.",
      "Never behind a face; under type at 60% opacity or less.", "Grain is the one finish allowed on flat colour."],
     ["texture-halftone", "texture-shards", "grain-collage"]),
    ("Register", "Loud & quiet",
     "Two volumes. Loud for awards and milestones; quiet for nights, results and thank-yous.",
     ["Loud: black-and-white player, green blocks, stacked Display caps, one blue script word crossing them.",
      "Quiet: Deep ground, one light, one Serif word, no motion devices.", "Game day: Serif headline over a wide action band."],
     ["loud-potm", "quiet-matchday", "gameday-split"]),
]

# Speed streaks behind the bowler on template B: x, y, width, height (canvas px), colour.
STREAKS = [(150, 790, 520, 12, "#030916"), (260, 830, 430, 22, "#1234F9"), (80, 878, 610, 9, "#061433"),
           (330, 920, 370, 18, "#1234F9"), (190, 968, 500, 14, "#030916"), (400, 1012, 300, 22, "#1234F9"),
           (250, 1058, 440, 9, "#061433")]

TICKER = "".join(f"<span>{w}<i>+</i></span>" for w in
                 ["Powerplay", "Under the lights", "Season 02", "Imama Cricket League", "UAE 2026"] * 2)


def zoom_fig(name, cls, caption_html):
    title = TITLE[name]
    return (f'<figure class="{cls}"><button class="zoom" type="button" data-zoom="{title}" aria-label="View larger: {title}">'
            f'<img {gen(name)} alt="{title}, generated in Higgsfield"></button>{caption_html}</figure>')


def wall():
    out = []
    for i, (name, title, refs) in enumerate(WALL, 1):
        cap = f"<figcaption><span>HF·{i:02d} {title}</span><b>{refs}</b></figcaption>"
        out.append(zoom_fig(name, "tile", cap))
    return "\n".join(out)


def refs_grid():
    out = []
    for n in range(1, 21):
        out.append(f'<figure class="ref"><img {ref(n)} alt="Reference R{n:02d}">'
                   f'<figcaption><b>R{n:02d}</b><span>{FAMILY_OF[n]}</span></figcaption></figure>')
    return "".join(out)


def palette_refs():
    return "".join(f'<figure><img {ref(n)} alt="Reference R{n:02d}, {label}">'
                   f'<figcaption><span>R{n:02d} · {label}</span><b>Added 2 Oct</b></figcaption></figure>'
                   for n, label in PALETTE_REFS)


def legend():
    return " ".join(f"<span>{fam} · {' '.join(f'R{n:02d}' for n in ns)}</span>" for fam, ns in FAMILIES.items())


def devices():
    out = []
    for fam, title, lede, rules, imgs in DEVICES:
        thumbs = "".join(f'<figure><img {ref(n)} alt="Reference R{n:02d}"><figcaption>R{n:02d}</figcaption></figure>'
                         for n in FAMILIES[fam])
        figs = "".join(zoom_fig(i, "", f"<figcaption>{TITLE[i]}</figcaption>") for i in imgs)
        n = "n2" if len(imgs) in (2, 4) else "n3"
        rules_html = "".join(f"<li>{r}</li>" for r in rules)
        out.append(f'<article class="dev"><div class="dev-text"><p class="mono">{fam}</p><h3 class="disp">{title}</h3>'
                   f'<p>{lede}</p><ul class="dev-rules">{rules_html}</ul><div class="dev-refs">{thumbs}</div></div>'
                   f'<div class="dev-imgs {n}">{figs}</div></article>')
    return "\n".join(out)


def streaks():
    return "".join(f'<i class="pB-streak" style="--x:{x};--y:{y};--w:{w};--h:{h};--c:{c}"></i>'
                   for x, y, w, h, c in STREAKS)


FACES = [  # family, file, style, weight, stretch
    ("Archivo", "Archivo-normal-latin.woff2", "normal", "100 900", "62% 125%"),
    ("Archivo", "Archivo-italic-latin.woff2", "italic", "100 900", "62% 125%"),
    ("Instrument Serif", "InstrumentSerif-normal-latin.woff2", "normal", "400", "100%"),
    ("Instrument Serif", "InstrumentSerif-italic-latin.woff2", "italic", "400", "100%"),
    ("JetBrains Mono", "JetBrainsMono-normal-latin.woff2", "normal", "100 800", "100%"),
    ("Mr Dafoe", "MrDafoe-normal-latin.woff2", "normal", "400", "100%"),
]


def fontfaces():
    return "\n".join(f"@font-face{{font-family:'{fam}';src:url({data_uri(HERE / 'fonts' / f)}) format('woff2');"
                     f"font-style:{st};font-weight:{w};font-stretch:{sw};font-display:block}}"
                     for fam, f, st, w, sw in FACES)


html = (HERE / "moodboard.src.html").read_text()
subs = {
    "{{fontfaces}}": fontfaces(), "{{ticker}}": TICKER, "{{wall}}": wall(), "{{refs}}": refs_grid(),
    "{{palrefs}}": palette_refs(), "{{legend}}": legend(), "{{devices}}": devices(), "{{streaks}}": streaks(),
}
for k, v in subs.items():
    html = html.replace(k, v)
html = html.replace('src="{{logo:deep}}"', asset("logo-deep", lambda: logo(DEEP)))
html = html.replace('src="{{logo:white}}"', asset("logo-white", lambda: logo(WHITE)))
html = html.replace('src="{{img:key-visual}}"', gen("key-visual"))
for p in (HERE / "cutouts").glob("*.webp"):
    html = html.replace('src="{{cut:' + p.stem + '}}"', asset("cut-" + p.stem, lambda p=p: data_uri(p)))
loader = ("<script>(function(){var A=" + json.dumps(ASSETS, separators=(",", ":")) +
          ";document.querySelectorAll('img[data-k]').forEach(function(i){i.src=A[i.getAttribute('data-k')];});})();</script>")
html = html.replace("<!--assets-->", loader)
assert "{{" not in html, html[html.index("{{"):html.index("{{") + 40]
# The artifact host adds its own document skeleton; the repo copy gets one here so it opens in standards mode.
if len(sys.argv) > 1:
    pathlib.Path(sys.argv[1]).write_text(html)
OUT.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8">'
               '<meta name="viewport" content="width=device-width,initial-scale=1">'
               '<style>body{margin:0}</style></head><body>\n' + html + '\n</body></html>\n')
print(OUT, f"{len(html) / 1e6:.2f} MB")
