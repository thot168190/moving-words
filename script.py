import re, json
from PIL import Image
import vtracer
scenes=[]
for name in ['whale','lighthouse','ship']:
    img=Image.open(f'public/line-{name}.png').convert('L')
    bw=img.point(lambda x: 0 if x<140 else 255,'1').convert('RGB')
    w,h=bw.size; tw=1100
    bw.resize((tw,int(h*tw/w))).save(f'/tmp/{name}.png')
    vtracer.convert_image_to_svg_py(f'/tmp/{name}.png',f'/tmp/{name}.svg',
        colormode='binary',mode='spline',filter_speckle=10,
        corner_threshold=80,length_threshold=6.0,splice_threshold=50)
    svg=open(f'/tmp/{name}.svg').read()
    vb=re.search(r'viewBox="([^"]+)"',svg)
    vbv=vb.group(1) if vb else '0 0 1100 800'
    paths=[]
    for m in re.finditer(r'<path([^>]*?)/?>',svg,re.S):
        a=m.group(1)
        f_=re.search(r'fill="([^"]+)"',a)
        if f_ and f_.group(1).upper() in ('#FFFFFF','#FFF','WHITE'): continue
        d=re.search(r'd="([^"]+)"',a); t=re.search(r'transform="([^"]+)"',a)
        if d: paths.append({'d':d.group(1),'t':t.group(1) if t else ''})
    scenes.append({'id':name,'vb':vbv,'lineart':paths,
                   'img':f'/metric-{name}.png',
                   'en':{'whale':'WHALE','lighthouse':'LIGHTHOUSE','ship':'SHIP'}[name],
                   'ko':{'whale':'고래','lighthouse':'등대','ship':'돛단배'}[name]})
open('public/metric-scenes.json','w').write(json.dumps({'scenes':scenes},ensure_ascii=False))
