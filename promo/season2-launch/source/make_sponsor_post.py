"""Season 2 logo-launch post with the two title sponsors. Builds an HTML page from the
design-system tokens and screenshots it with Playwright (node) at 1080x1350.
Needs Montserrat + Montserrat Alternates installed (fontconfig)."""
import re, subprocess, pathlib
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
LOGO = (HERE / '../../../brand/logo/icl-season2-reverse-transparent.svg').resolve().read_text()
LOGO_INNER = re.sub(r'^.*?<svg[^>]*>', '', LOGO, flags=re.S).rsplit('</svg>', 1)[0]
LOGO_SVG = f'<svg viewBox="140 300 690 580" xmlns="http://www.w3.org/2000/svg">{LOGO_INNER}</svg>'

HTML = f'''<!doctype html><meta charset="utf-8"><style>
:root{{--night:#1c0f33;--purple:#452874;--lav:#b9a9d0;--green:#6fd08f;--green-b:#8fe3a8}}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:Montserrat,sans-serif;
 background:radial-gradient(75% 75% at 50% 28%,#452874 0%,#26114f 55%,#1c0f33 100%);color:#fff}}
.logo{{position:absolute;left:190px;top:70px;width:700px}}
.eyebrow{{position:absolute;left:0;right:0;text-align:center;font-weight:700;letter-spacing:.32em;text-transform:uppercase;padding-left:.32em}}
.h{{position:absolute;left:0;right:0;text-align:center;font-family:'Montserrat Alternates';font-weight:700;letter-spacing:-.02em}}
.rule{{position:absolute;left:80px;right:80px;height:2px;background:#35255a}}
.plate{{position:absolute;top:1005px;width:448px;height:240px;background:#fff;border-radius:12px;overflow:hidden;
 display:flex;align-items:center;justify-content:center}}
.plate img{{mix-blend-mode:multiply;filter:brightness(1.12) contrast(1.2)}}
.p1{{left:80px}}.p2{{left:552px}}
.streak{{position:absolute;height:14px;border-radius:7px}}
</style>
<div class="logo">{LOGO_SVG}</div>
<div class="eyebrow" style="top:705px;font-size:24px;color:var(--green-b)">The wait is almost over</div>
<div class="h" style="top:735px;font-size:118px;line-height:1.2">coming soon</div>
<div class="rule" style="top:925px"></div>
<div class="eyebrow" style="top:955px;font-size:22px;color:var(--lav)">Title sponsors</div>
<div class="plate p1"><img src="sponsors/vip-government-transactions-center.jpg" style="width:470px"></div>
<div class="plate p2"><img src="sponsors/easyway.jpg" style="width:272px;margin-top:-4px"></div>
<div class="eyebrow" style="top:1285px;font-size:18px;color:var(--lav)">UAE IMAMA &nbsp;·&nbsp; Season 2</div>
</style>'''
(HERE / 'ig-post-sponsors-launch.html').write_text(HTML)
js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:1350}}}});
await p.goto('file://{HERE}/ig-post-sponsors-launch.html');await p.evaluate(()=>document.fonts.ready);
await p.screenshot({{path:'{OUT}/ig-post-sponsors-launch.png'}});await b.close()}})()"""
(HERE / '_shot.js').write_text(js)
subprocess.run(['node', str(HERE / '_shot.js')], check=True, env={**__import__('os').environ, 'NODE_PATH': '/opt/node22/lib/node_modules:/usr/lib/node_modules:/usr/local/lib/node_modules'})
(HERE / '_shot.js').unlink()
