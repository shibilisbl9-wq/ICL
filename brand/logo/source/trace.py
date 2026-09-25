from PIL import Image, ImageFilter
import numpy as np, subprocess, re
S=8
X0,Y0,X1,Y1=150,305,825,815
src=Image.open('original-logo.jpg').convert('RGB').crop((X0,Y0,X1,Y1))
big=src.resize(((X1-X0)*S,(Y1-Y0)*S),Image.BICUBIC).filter(ImageFilter.GaussianBlur(S*0.45))
a=np.array(big).astype(float)
L=a.mean(2)
H,W=L.shape
yy=np.arange(H)[:,None]/S+Y0; xx=np.arange(W)[None,:]/S+X0
green=(a[:,:,1]>a[:,:,0]+8)&(a[:,:,1]>a[:,:,2]-5)
def layer(name,mask,thr=205):
    ink=(L<thr)&mask
    img=Image.fromarray(np.where(ink,0,255).astype(np.uint8))
    img.save(name+'.pbm')
    subprocess.run(['potrace','-s','-t','40','-a','1.0','-O','0.4','-u','10','--flat','-o',name+'.svg',name+'.pbm'],check=True)
    s=open(name+'.svg').read()
    g=re.search(r'<g transform="([^"]+)"[^>]*>(.*)</g>',s,re.S)
    return g.group(1),g.group(2)
Ymax=np.ones_like(L,bool)
layers={}
layers['uae']=layer('uae',(yy<380)&(xx>292))
layers['ball']=layer('ball',(yy<452)&(xx<292)&~green,thr=225)
layers['green']=layer('green',(yy>=380)&(yy<493)&(xx>=250)&~((xx<292)&~green))
layers['cricket']=layer('cricket',(yy>=493)&(yy<630))
layers['league']=layer('league',(yy>=630))
import json; json.dump(layers,open('layers.json','w'))
for k,(t,p) in layers.items(): print(k,t,len(p))
