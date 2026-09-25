import json, re
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
L=json.load(open('layers.json'))

SPACE_TRIM=0
def text_path(txt, font, size, x, baseline, tracking, anchor='start'):
    f=TTFont(font); gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm
    sc=size/upm
    # measure
    adv=[gs[cmap[ord(c)]].width*sc-(SPACE_TRIM if c==' ' else 0) for c in txt]
    total=sum(adv)+tracking*(len(txt)-1)
    # right-anchor uses ink right edge of last glyph
    last=gs[cmap[ord(txt[-1])]]
    from fontTools.pens.boundsPen import BoundsPen
    bp=BoundsPen(gs); last.draw(bp); lx0,_,lx1,_=bp.bounds
    bp=BoundsPen(gs); gs[cmap[ord(txt[0])]].draw(bp); fx0=bp.bounds[0]
    if anchor=='end': x = x - (total - adv[-1] + lx1*sc)
    else: x = x - fx0*sc
    out=[]; cx=x
    for c,a in zip(txt,adv):
        if c!=' ':
            pen=SVGPathPen(gs); tp=TransformPen(pen,(sc,0,0,-sc,cx,baseline))
            gs[cmap[ord(c)]].draw(tp); out.append((c,pen.getCommands(),cx))
        cx+=a+tracking
    return out

TRACE='<g transform="translate(150,305) scale(0.125)"><g transform="translate(0,4080) scale(0.1,-0.1)" fill="{fill}">{paths}</g></g>'
def trace(name,fill): return TRACE.format(fill=fill,paths=L[name][1].replace('\n',' '))

# Tagline geometry, matched to the UAE IMAMA line: cap height 31px, ~31px letter gaps
CAP=31; SIZE=CAP/0.7; BASE=853; RIGHT=808
MONT='Montserrat_wght_700.ttf'
SPACE_TRIM=9
tag=text_path('SEASON 2',MONT,SIZE,RIGHT,BASE,tracking=26.5,anchor='end')
tag_x0=tag[0][2]

PALETTES={
 'color':   dict(uae='#452874', green=('#50a66b','#264f36'), purple=('#d880fb','#26114f'), ball=('#4a2d7a','#b98ad6'), ballfill='#ffffff', season='#452874', two='url(#g-green-up)', rule='url(#g-rule)', bg=None),
 'reverse': dict(uae='#ffffff', green=('#8fe3a8','#4fb872'), purple=('#f1c9ff','#b27ae0'), ball=('#ffffff','#c9a4ea'), ballfill='none', season='#ffffff', two='url(#g-green-up)', rule='url(#g-rule)', bg='#1c0f33'),
 'mono-dark':dict(uae='#1c0f33', green=('#1c0f33','#1c0f33'), purple=('#1c0f33','#1c0f33'), ball=('#1c0f33','#1c0f33'), ballfill='#ffffff', season='#1c0f33', two='#1c0f33', rule='#1c0f33', bg=None),
 'mono-white':dict(uae='#ffffff', green=('#ffffff','#ffffff'), purple=('#ffffff','#ffffff'), ball=('#ffffff','#ffffff'), ballfill='none', season='#ffffff', two='#ffffff', rule='#ffffff', bg='#1c0f33'),
}

def svg(p, season=True, bg=False):
    VX,VY,VW,VH=140,300,690,(580 if season else 520)
    defs=f'''<defs>
<linearGradient id="g-green" x1="0" y1="1" x2="0.95" y2="-0.05"><stop offset="0" stop-color="{p['green'][0]}"/><stop offset="1" stop-color="{p['green'][1]}"/></linearGradient>
<linearGradient id="g-purple" x1="0" y1="1" x2="0.72" y2="-0.17"><stop offset="0" stop-color="{p['purple'][0]}"/><stop offset="1" stop-color="{p['purple'][1]}"/></linearGradient>
<linearGradient id="g-ball" x1="1" y1="1" x2="0" y2="0"><stop offset="0.3" stop-color="{p['ball'][0]}"/><stop offset="1" stop-color="{p['ball'][1]}"/></linearGradient>
<linearGradient id="g-rule" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{p['green'][0]}" stop-opacity="0"/><stop offset="1" stop-color="{p['green'][1]}"/></linearGradient>
<linearGradient id="g-green-up" x1="0" y1="0" x2="0.95" y2="1.05"><stop offset="0" stop-color="{p['green'][0]}"/><stop offset="1" stop-color="{p['green'][1]}"/></linearGradient>
</defs>'''
    body=[]
    if bg and p['bg']: body.append(f'<rect x="{VX}" y="{VY}" width="{VW}" height="{VH}" fill="{p["bg"]}"/>')
    if p['ballfill']!='none': body.append(f'<circle cx="253" cy="351" r="19" fill="{p["ballfill"]}"/>')
    body.append(trace('ball','url(#g-ball)'))
    body.append(trace('uae',p['uae']))
    body.append(trace('green','url(#g-green)'))
    body.append(trace('cricket','url(#g-purple)'))
    body.append(trace('league','url(#g-purple)'))
    if season:
        # speed-line rule echoing the ball's trail, running from the block's left edge to the tagline
        body.append(f'<rect x="262" y="{BASE-CAP/2-2.5:.1f}" width="{tag_x0-262-22:.1f}" height="5" rx="2.5" fill="{p["rule"]}"/>')
        for c,d,x in tag:
            body.append(f'<path d="{d}" fill="{p["two"] if c=="2" else p["season"]}"/>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VX} {VY} {VW} {VH}" width="{VW*2}" height="{VH*2}">\n{defs}\n'+'\n'.join(body)+'\n</svg>\n'

out='../'
for k,p in PALETTES.items():
    open(f'{out}icl-season2-{k}.svg','w').write(svg(p,True,bg=p['bg'] is not None and k!='x'))
    open(f'{out}icl-season2-{k}-transparent.svg','w').write(svg(p,True,bg=False)) if p['bg'] else None
open(f'{out}icl-master-no-tagline.svg','w').write(svg(PALETTES['color'],False))
print('tag starts at',tag_x0)
