# -*- coding: utf-8 -*-
import io, json, os, sys
from PIL import Image, ImageDraw, ImageFont
CH=sys.argv[1]
s=io.open('public/learning/index.html',encoding='utf-8').read()
i=s.index('const chapterData = {'); st=s.index('{',i); d=0
for j in range(st,len(s)):
    if s[j]=='{': d+=1
    elif s[j]=='}':
        d-=1
        if d==0: en=j+1; break
ch=json.loads(s[st:en])[CH]
try: F=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",24)
except: F=ImageFont.load_default()
out='_작업/_검수_ch%s'%CH; os.makedirs(out,exist_ok=True)
tiles=[]
for k,w in enumerate(ch["works"]):
    p=os.path.join('public/learning',w["img"])
    if not os.path.exists(p): continue
    im=Image.open(p).convert('RGB'); W,H=im.size
    dr=ImageDraw.Draw(im,'RGBA')
    def put(words,spots,col):
        for (wd,_),(x,y) in zip(words,spots):
            px,py=W*x/100.0,H*y/100.0
            dr.ellipse([px-8,py-8,px+8,py+8],fill=col+(230,),outline=(255,255,255,255),width=3)
            bb=dr.textbbox((0,0),wd,font=F); tw,th=bb[2]-bb[0],bb[3]-bb[1]
            bx,by=px+14,py-th/2-5
            if bx+tw+12>W: bx=px-tw-26
            dr.rounded_rectangle([bx,by,bx+tw+12,by+th+10],7,fill=col+(235,))
            dr.text((bx+6,by+3),wd,font=F,fill=(255,255,255))
    put(ch["levelOneWords"][k],ch["levelOneSpots"][k],(200,40,60))
    put(ch["levelTwoWords"][k],ch["sceneSpots"][k],(30,110,190))
    dr.rectangle([0,0,W,40],fill=(0,0,0,200))
    dr.text((10,7),"ch%s_%s  %s"%(CH,w["n"],w["title"]),font=F,fill=(255,255,255))
    o='%s/%s.jpg'%(out,w["n"]); im.save(o,quality=85); tiles.append(o)
ims=[Image.open(t) for t in tiles]
tw,th=620,349
cols=2; rows=(len(ims)+cols-1)//cols
sheet=Image.new('RGB',(tw*cols,th*rows),(255,255,255))
for n,im in enumerate(ims): sheet.paste(im.resize((tw,th)),((n%cols)*tw,(n//cols)*th))
sheet.save('%s/00_전체.jpg'%out,quality=84)
print("ch%s %d장"%(CH,len(tiles)))
