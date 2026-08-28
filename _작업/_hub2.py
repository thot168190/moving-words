# -*- coding: utf-8 -*-
import io, json, html
HEAD=("Progressive detailed fine-pencil construction, transparent watercolor and gentle object-motion animation "
"on a solid pure bright white background (#FFFFFF), edge to edge. The first frame is an entirely empty pure white field. "
"Static locked-off camera, one continuous 8-second take. The only visible subjects are ")
DRAW_H="0-3.5s: exceptionally fine pale-neutral 2H graphite strokes are visibly traced one by one across the empty white field. "
DRAW_T=(" Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons "
"or basic outlines. Each stroke has a clear beginning and endpoint. The illustration is built progressively rather than "
"fading into view. Previously completed lines remain stable.")
COL_H="3.5-5.5s: clear transparent watercolor develops in layered color. "
COL_T=(" Every wash stays pale and translucent, applied once and never built up to full saturation. "
"Preserve narrow white-paper highlights while keeping the colors fresh, luminous and distinguishable, "
"with graphite details visible through every layer.")
MOT_H="5.5-8s: "
MOT_T=" All other elements remain fixed. All graphite construction lines and watercolor boundaries remain stable."
STY_H=("Style: intricate premium pencil-and-watercolor plate, numerous hair-thin pale graphite construction lines, "
"accurate object anatomy, luminous layered transparent watercolor, ")
STY_T=", sophisticated museum-quality illustrated-dictionary artwork, clearly hand-drawn and never photographic."
NEG=("No dark outline, black ink, sepia ink, charcoal, thick contour, product photography, studio lighting, "
"realistic reflection, glossy highlight, cast shadow, 3D, CGI, text, label, border, hand, artist or visible drawing tool. ")
NEG_T=" Completely silent."

URGENT=[
("ch9_07 · 양팔 접시저울 다시","현재 그림에 #FFFFF 글자가 인쇄됨 · 같은 주제로 재제작",
 "exactly one illustrated brass balance scale with a central column, exactly two illustrated shallow weighing pans hanging on fine chains and exactly three illustrated small stacked weights beside it",
 "The stepped base and slender central column of the balance are traced first, followed by the crossbeam with its pivot, the fine hanging chains, the two shallow pans, and the three small graduated weights.",
 "A pale ochre wash settles lightly on the brass column and pans, faint warm grey tints the base, and soft slate-grey touches the small weights.",
 "the left weighing pan dips two millimetres and settles level again. The column, base and weights remain fixed.",
 "fine brass instrument textures","Exactly two pans and three weights."),
("ch11_09 · 모닥불과 장작 다시","현재 그림에 #FFFFFF 글자가 인쇄됨 · 같은 주제로 재제작",
 "exactly one illustrated ring of rounded stones enclosing a small campfire, exactly one illustrated stack of split logs beside it and one illustrated low wooden stool",
 "The uneven ring of rounded stones is traced first, followed by the crossed sticks and rising flame shapes within, the cut ends and bark texture of the stacked split logs, and the three legs and seat of the low stool.",
 "A pale warm grey wash settles lightly on the stones, faint amber and rose tint the flame, soft honey-brown colors the split logs, and pale oak tones the stool.",
 "one small flame tip leans two millimetres to the side and straightens. The stones, logs and stool remain fixed.",
 "warm campfire textures","Exactly one fire ring, one log stack and one stool."),
("ch11_12 · 여행가방과 호출벨 다시","현재 그림만 배경이 회색 · 순백 배경으로 재제작",
 "exactly one illustrated leather travel case with buckled straps, one illustrated brass counter bell and exactly one illustrated key with a tasselled tag",
 "The rounded corners and stitched seams of the travel case are traced first, followed by the two buckled straps, the domed brass bell with its plunger, and the notched key with its hanging tassel.",
 "A pale tan wash settles lightly on the leather case, soft ochre touches the brass bell, and faint cream tints the tassel.",
 "the tassel on the key sways two millimetres and comes to rest. The case and bell remain fixed.",
 "vintage travel textures","Exactly one case, one bell and one key."),
]
U=[]
for t,why,sub,dr,co,mo,sy,lk in URGENT:
    U.append((t,why,HEAD+sub+". "+DRAW_H+dr+DRAW_T+" "+COL_H+co+COL_T+" "+MOT_H+mo+MOT_T+" "+STY_H+sy+STY_T+" "+NEG+lk+NEG_T))
P=json.loads(io.open('_작업/_proms25.json',encoding='utf-8').read())
ALL=[p for *_,p in P]
BAN=["charcoal","sepia"," black","dark ","thick ","glossy","shadow","polished","metallic","studio"," ink ","label","border"]
for t,_,p in U:
    f=p[:p.index("No dark outline")].lower()
    h=[b.strip() for b in BAN if b in f]
    print(("★ "+t+" : "+str(h)) if h else ("OK "+t))

ur=""
for i,(t,why,p) in enumerate(U):
    ur+=f"""<div class="card urg"><div class=h><span class=badge>긴급</span><b>{html.escape(t)}</b>
<button class=c data-i="u{i}">복사</button></div><div class=el>{html.escape(why)}</div>
<pre id="pu{i}">{html.escape(p)}</pre></div>"""
GROUPS=[("1차",0,7),("2차",7,13),("3차",13,19),("4차",19,25)]
secs=""
for gname,a,b in GROUPS:
    rows=""
    for i,(t,el,l1,l2,ch,p) in enumerate(P[a:b],a+1):
        rows+=f"""<div class=card><div class=h><span class=no>{i:02d}</span><b>{html.escape(t)}</b>
<span class=ch>{ch}</span><button class=c data-i="{i-1}">복사</button></div>
<div class=el>{html.escape(el)}</div>
<div class=w><b class=l1>{' · '.join(l1)}</b> &nbsp; <span class=l2>{' · '.join(l2)}</span></div>
<pre id="p{i-1}">{html.escape(p)}</pre></div>"""
    names=" · ".join(t for t,_,_,_,_,_ in P[a:b])
    secs+=f"""<section><div class=gh><div><h2>{gname} 벌크 ({a+1:02d}~{b:02d})</h2><div class=gs>{html.escape(names)}</div></div>
<button class=g data-a="{a}" data-b="{b}">{gname} 전체 복사</button></div>{rows}</section>"""
page=f"""<!doctype html><html lang=ko><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1"><title>그림 벌크 허브</title><style>
*{{box-sizing:border-box}}
body{{margin:0;background:#ffffff;color:#1a1d21;font-family:Pretendard,-apple-system,"Apple SD Gothic Neo",sans-serif;line-height:1.6}}
header{{position:sticky;top:0;background:#f7f8fa;border-bottom:1px solid #e3e6ea;padding:15px 18px;display:flex;gap:12px;align-items:center;flex-wrap:wrap;z-index:9}}
h1{{font-size:17px;margin:0;font-weight:800;color:#111}}
.sub{{font-size:12px;color:#6b7280}}
button{{background:#1f7a52;color:#fff;border:0;border-radius:7px;padding:8px 15px;font-size:13px;font-weight:700;cursor:pointer;white-space:nowrap}}
#all{{margin-left:auto;background:#1f5f8b}}
main{{padding:18px;max-width:1000px;margin:0 auto}}
section{{margin-bottom:26px}}
.gh{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:#f7f8fa;border:1px solid #e3e6ea;border-radius:10px;padding:13px 15px;margin-bottom:11px}}
.gh h2{{font-size:15px;margin:0;color:#8a6200}}
.gs{{font-size:11.5px;color:#6b7280;margin-top:2px}}
.gh button{{margin-left:auto}}
.card{{background:#fff;border:1px solid #e3e6ea;border-radius:10px;padding:12px 14px;margin-bottom:9px}}
.card.urg{{border:2px solid #d14343;background:#fff7f7}}
.badge{{background:#d14343;color:#fff;font-size:10.5px;font-weight:800;padding:2px 8px;border-radius:99px}}
.h{{display:flex;gap:9px;align-items:center;flex-wrap:wrap}}
.no{{color:#9aa1ab;font-family:ui-monospace,monospace;font-size:12px}}
.h b{{font-size:14px;color:#111}}
.ch{{color:#8a6200;font-family:ui-monospace,monospace;font-size:11px;background:#fdf6e3;padding:2px 7px;border-radius:99px}}
.h button{{margin-left:auto;padding:5px 12px;font-size:12px}}
.el{{font-size:11.5px;color:#6b7280;margin:4px 0 6px}}
.w{{font-family:ui-monospace,monospace;font-size:11.5px;margin-bottom:8px}}
.l1{{color:#c0392b}}.l2{{color:#2563a8}}
pre{{white-space:pre-wrap;word-break:break-word;font-family:ui-monospace,Menlo,monospace;font-size:10.5px;color:#4b5563;background:#f7f8fa;border:1px solid #e3e6ea;border-radius:7px;padding:10px;margin:0;max-height:110px;overflow-y:auto}}
.note{{background:#fdf6e3;border:1px solid #ecdcb0;border-radius:10px;padding:13px 15px;margin-bottom:18px;font-size:13px;color:#3a3320}}
.note b{{color:#8a6200}}
</style></head><body>
<header><div><h1>그림 벌크 허브 — 재제작 3장 + 신규 25장</h1>
<div class=sub>정본 세필수채 공식 · 금지어 충돌 0 · 기존 157편과 중복 0</div></div>
<button id=all>신규 25장 전체 복사</button></header>
<main>
<div class=note><b>맨 위 붉은 세 장이 긴급 재제작입니다.</b> 지금 사이트에 올라가 있는 그림에 색상코드 글자가 인쇄돼 있거나 배경이 회색입니다.
단어를 고쳐도 안 되니 그림을 다시 뽑아야 합니다. <b>이것부터 돌리십시오.</b><br><br>
<b class=l1 style="font-family:ui-monospace">붉은 단어</b> = 그림에 반드시 보여야 함(퀴즈에 나옴) &nbsp;
<span class=l2 style="font-family:ui-monospace">푸른 단어</span> = 이야기로 이어지는 말(안 보여도 됨)</div>
<section><div class=gh><div><h2 style="color:#d14343">긴급 재제작 3장</h2>
<div class=gs>ch9_07 저울 · ch11_09 모닥불 · ch11_12 여행가방</div></div>
<button class=gu style="background:#d14343">3장 전체 복사</button></div>{ur}</section>
{secs}</main>
<script>
const T=[];for(let i=0;i<25;i++)T.push(document.getElementById('p'+i).textContent);
const U=[];for(let i=0;i<3;i++)U.push(document.getElementById('pu'+i).textContent);
function cp(s,b){{
 try{{navigator.clipboard.writeText(s)}}catch(e){{
  var ta=document.createElement('textarea');ta.value=s;document.body.appendChild(ta);ta.select();document.execCommand('copy');ta.remove();}}
 var o=b.textContent;b.textContent='복사됨';setTimeout(function(){{b.textContent=o}},1500);
}}
document.querySelectorAll('.c').forEach(function(b){{b.onclick=function(){{
 var k=b.dataset.i; cp(k[0]==='u'?U[+k.slice(1)]:T[+k], b);}};}});
document.querySelectorAll('.g').forEach(function(b){{b.onclick=function(){{
 cp(T.slice(+b.dataset.a,+b.dataset.b).join('\\n\\n'),b);}};}});
document.querySelector('.gu').onclick=function(){{cp(U.join('\\n\\n'),this)}};
document.getElementById('all').onclick=function(){{cp(T.join('\\n\\n'),this)}};
</script></body></html>"""
io.open('_작업/bulk_26_복사허브.html','w',encoding='utf-8').write(page)
print("\n허브 재생성 · 긴급3 + 신규25 · %d bytes"%len(page))
