# -*- coding: utf-8 -*-
import io, json, html
P=json.loads(io.open('_작업/_proms25.json',encoding='utf-8').read())
GROUPS=[("1차 벌크",0,7),("2차 벌크",7,13),("3차 벌크",13,19),("4차 벌크",19,25)]
secs=""; alljs=[]
for gi,(gname,a,b) in enumerate(GROUPS):
    items=P[a:b]
    names=" · ".join(t for t,_,_,_,_,_ in items)
    rows=""
    for i,(t,el,l1,l2,ch,p) in enumerate(items,a+1):
        rows+=f"""<div class=card>
<div class=h><span class=no>{i:02d}</span><b>{html.escape(t)}</b><span class=ch>{ch}</span>
<button class=c data-i="{i-1}">복사</button></div>
<div class=el>{html.escape(el)}</div>
<div class=w><span class=l1>{' · '.join(l1)}</span> <span class=l2>{' · '.join(l2)}</span></div>
<pre id="p{i-1}">{html.escape(p)}</pre></div>"""
    secs+=f"""<section><div class=gh><div><h2>{gname} ({a+1:02d}~{b:02d}편)</h2><div class=gs>{html.escape(names)}</div></div>
<button class=g data-a="{a}" data-b="{b}">{gname} 전체 복사</button></div>{rows}</section>"""
    alljs.append((a,b))
page=f"""<!doctype html><html lang=ko><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1"><title>새로 그릴 그림 25장</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#0f1115;color:#e6e8ec;font-family:Pretendard,-apple-system,"Apple SD Gothic Neo",sans-serif;line-height:1.6}}
header{{position:sticky;top:0;background:#161a21;border-bottom:1px solid #262b34;padding:15px 18px;display:flex;gap:12px;align-items:center;flex-wrap:wrap;z-index:9}}
h1{{font-size:17px;margin:0;font-weight:800}}.sub{{font-size:12px;color:#8b93a1}}
button{{background:#2b7a5b;color:#fff;border:0;border-radius:7px;padding:8px 15px;font-size:13px;font-weight:700;cursor:pointer;white-space:nowrap}}
#all{{margin-left:auto;background:#1f5f8b}}
main{{padding:18px;max-width:1000px;margin:0 auto}}
section{{margin-bottom:26px}}
.gh{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:#151922;border:1px solid #232833;border-radius:10px;padding:13px 15px;margin-bottom:11px}}
.gh h2{{font-size:15px;margin:0;color:#f0c674}}.gs{{font-size:11.5px;color:#8b93a1;margin-top:2px}}
.gh button{{margin-left:auto}}
.card{{background:#151922;border:1px solid #232833;border-radius:10px;padding:12px 14px;margin-bottom:9px}}
.h{{display:flex;gap:9px;align-items:center;flex-wrap:wrap}}
.no{{color:#6b7484;font-family:ui-monospace,monospace;font-size:12px}}
.h b{{font-size:14px}}
.ch{{color:#c8b273;font-family:ui-monospace,monospace;font-size:11px;background:#241f14;padding:2px 7px;border-radius:99px}}
.h button{{margin-left:auto;padding:5px 12px;font-size:12px}}
.el{{font-size:11.5px;color:#8b93a1;margin:4px 0 6px}}
.w{{font-family:ui-monospace,monospace;font-size:11.5px;margin-bottom:8px}}
.l1{{color:#ff9d8a}}.l2{{color:#8ab4f8}}
pre{{white-space:pre-wrap;word-break:break-word;font-family:ui-monospace,Menlo,monospace;font-size:11px;color:#8b93a1;background:#0f1319;border:1px solid #1e242d;border-radius:7px;padding:10px;margin:0;max-height:120px;overflow-y:auto}}
.note{{background:#151922;border:1px solid #232833;border-radius:10px;padding:13px 15px;margin-bottom:18px;font-size:13px}}
.note b{{color:#f0c674}}
</style></head><body>
<header><div><h1>새로 그릴 그림 25장</h1><div class=sub>정본 세필수채 공식 · 금지어 충돌 0 · 기존 157편과 중복 0 · 단어 168개 소화</div></div>
<button id=all>25장 전체 복사</button></header>
<main>
<div class=note><b>고친 것 세 가지</b><br>
① <b>기존 그림과 겹치던 8장을 교체</b>했습니다 — 법정·실험실·베틀·헬리콥터·제어반·시인책상·얼룩말·저울은 이미 157편 안에 있습니다.<br>
② <b>색을 옅게</b> 낮췄습니다. <code>겹쳐 칠하기</code>를 빼고 <code>한 번만 얹기</code>로 바꿨습니다.<br>
③ <b>금지어 충돌 0</b>. 프롬프트 뒤쪽 금지 목록에 있는 말이 앞부분에 하나도 없습니다.<br><br>
<span class=l1 style="font-family:ui-monospace">붉은 단어</span> = 그림에 반드시 보여야 함(퀴즈에 나옴) ·
<span class=l2 style="font-family:ui-monospace">푸른 단어</span> = 이야기로 이어지는 말(안 보여도 됨)</div>
{secs}</main>
<script>
const N={len(P)};
const T=Array.from({{length:N}},(_,i)=>document.getElementById('p'+i).textContent);
async function cp(s,b){{try{{await navigator.clipboard.writeText(s)}}catch(e){{
const ta=document.createElement('textarea');ta.value=s;document.body.appendChild(ta);ta.select();document.execCommand('copy');ta.remove()}}
const o=b.textContent;b.textContent='복사됨 ✓';setTimeout(()=>b.textContent=o,1500)}}
document.querySelectorAll('.c').forEach(b=>b.onclick=()=>cp(T[+b.dataset.i],b));
document.querySelectorAll('.g').forEach(b=>b.onclick=()=>cp(T.slice(+b.dataset.a,+b.dataset.b).join('\\n\\n'),b));
document.getElementById('all').onclick=e=>cp(T.join('\\n\\n'),e.target);
</script></body></html>"""
io.open('_작업/bulk_26_복사허브.html','w',encoding='utf-8').write(page)
print("허브 재생성 · 25장 · %d bytes"%len(page))
