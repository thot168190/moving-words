# -*- coding: utf-8 -*-
"""허브 재생성 — 프롬프트 수정 후 이걸 돌리면 HTML이 갱신된다."""
import io, json, html
P=json.loads(io.open('_작업/_proms25.json',encoding='utf-8').read())
L=[p for *_,p in P]; G=[(0,6),(6,12),(12,18),(18,24),(24,25)]; SEP="\n\n"
tas="".join('<textarea class=hid id="g%d">%s</textarea>'%(gi,html.escape(SEP.join(L[a:b]))) for gi,(a,b) in enumerate(G,1))
tas+="".join('<textarea class=hid id="s%d">%s</textarea>'%(i,html.escape(p)) for i,p in enumerate(L))
tas+='<textarea class=hid id="gall">%s</textarea>'%html.escape(SEP.join(L))
secs=""
for gi,(a,b) in enumerate(G,1):
    n=b-a; rows=""
    for i,(t,el,l1,l2,ch,p) in enumerate(P[a:b],a+1):
        rows+=f"""<div class=card><div class=h><span class=no>{i:02d}</span><b>{html.escape(t)}</b>
<span class=ch>{ch}</span><button class=c data-t="s{i-1}">복사</button></div>
<div class=el>{html.escape(el)}</div>
<div class=w><b class=l1>{' · '.join(l1)}</b> &nbsp; <span class=l2>{' · '.join(l2)}</span></div></div>"""
    names=" · ".join(t for t,_,_,_,_,_ in P[a:b])
    secs+=f"""<section><div class=gh><div><h2>{gi}차 벌크 · {n}장 ({a+1:02d}~{b:02d})</h2>
<div class=gs>{html.escape(names)}</div></div><button class=c big data-t="g{gi}">이 {n}장 복사</button></div>{rows}</section>"""
page=f"""<!doctype html><html lang=ko><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1"><title>벌크 6개씩 · 25장</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#fff;color:#1a1d21;font-family:Pretendard,-apple-system,"Apple SD Gothic Neo",sans-serif;line-height:1.6}}
header{{position:sticky;top:0;background:#f7f8fa;border-bottom:1px solid #e3e6ea;padding:15px 18px;display:flex;gap:12px;align-items:center;flex-wrap:wrap;z-index:9}}
h1{{font-size:17px;margin:0;font-weight:800;color:#111}}.sub{{font-size:12px;color:#6b7280}}
button{{background:#1f7a52;color:#fff;border:0;border-radius:7px;padding:8px 15px;font-size:13px;font-weight:700;cursor:pointer;white-space:nowrap}}
button.big{{background:#14532d}}#allb{{margin-left:auto;background:#1f5f8b}}
main{{padding:18px;max-width:1000px;margin:0 auto}}section{{margin-bottom:22px}}
.gh{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:#eef7f1;border:1px solid #c9e3d4;border-radius:10px;padding:13px 15px;margin-bottom:9px}}
.gh h2{{font-size:15px;margin:0;color:#1f7a52}}.gs{{font-size:11.5px;color:#4b6b58;margin-top:2px}}
.gh button{{margin-left:auto}}
.card{{background:#fff;border:1px solid #e3e6ea;border-radius:10px;padding:10px 13px;margin-bottom:6px}}
.h{{display:flex;gap:9px;align-items:center;flex-wrap:wrap}}
.no{{color:#9aa1ab;font-family:ui-monospace,monospace;font-size:12px}}.h b{{font-size:14px;color:#111}}
.ch{{color:#8a6200;font-family:ui-monospace,monospace;font-size:11px;background:#fdf6e3;padding:2px 7px;border-radius:99px}}
.h button{{margin-left:auto;padding:5px 12px;font-size:12px}}
.el{{font-size:11.5px;color:#6b7280;margin:3px 0 4px}}
.w{{font-family:ui-monospace,monospace;font-size:11.5px}}.l1{{color:#c0392b}}.l2{{color:#2563a8}}
.hid{{position:fixed;left:-9999px;top:0;width:10px;height:10px;opacity:0}}
.note{{background:#fdf6e3;border:1px solid #ecdcb0;border-radius:10px;padding:13px 15px;margin-bottom:18px;font-size:13px;color:#3a3320}}
.note b{{color:#8a6200}}code{{background:#fff;padding:1px 5px;border-radius:4px;border:1px solid #eee;font-size:11.5px}}
</style></head><body>
{tas}
<header><div><h1>벌크 6개씩 · 25장</h1><div class=sub>line-reveal 정본 · 10항목 검증 통과</div></div>
<button id=allb class=c data-t="gall">25장 전체 복사</button></header>
<main>
<div class=note><b>정본을 바로잡았습니다</b><br>
대표님이 실제로 쓰시는 골격은 <b>line-reveal 계열</b>(MENSA·DOMUS 허브)인데,
제가 8/25에 잠근 <b>세필수채 계열</b>을 쓰고 있었습니다. 25장 전부 line-reveal 정본으로 다시 썼습니다.<br><br>
<b>그 골격에 제 고민이 이미 다 들어 있었습니다</b><br>
· 여백 — <code>occupies the central three-quarters of the frame with equal narrow white margins on both sides</code><br>
· 그려짐 — <code>Each line appears progressively from its own endpoint, one complete line at a time</code><br>
· 옅은 색 — <code>Use only ... Leave most interiors as untouched white space</code> · <code>No dark, dense or fully filled areas</code><br>
· 글자 — <code>Never: hex codes, color codes, #FFFFFF, printed text</code><br><br>
정본은 <code>_작업/01_지시서/정본_line-reveal_MENSA_20260827.md</code> 에 잠가 뒀습니다.<br><br><b>줄바꿈 주의</b> — 벌크는 <b>빈 줄로 프롬프트를 나눕니다.</b> 프롬프트 안에 빈 줄이 있으면 한 편이 여러 조각으로 쪼개집니다(6개가 54개로). 그래서 프롬프트 하나를 <b>한 줄</b>로 합쳤습니다. 내용은 정본 그대로입니다.<br><br>
<b class=l1 style="font-family:ui-monospace">붉은 단어</b> = 그림에 보여야 함 &nbsp;
<span class=l2 style="font-family:ui-monospace">푸른 단어</span> = 이야기로 이어지는 말</div>
{secs}</main>
<script>
document.querySelectorAll('.c').forEach(function(b){{
  b.onclick=function(){{
    var ta=document.getElementById(b.dataset.t);
    ta.style.position='static';ta.style.left='0';
    ta.focus();ta.select();ta.setSelectionRange(0,ta.value.length);
    var ok=false; try{{ok=document.execCommand('copy')}}catch(e){{}}
    if(!ok&&navigator.clipboard){{try{{navigator.clipboard.writeText(ta.value);ok=true}}catch(e){{}}}}
    ta.style.position='fixed';ta.style.left='-9999px';
    var n=ta.value.split(/\\n\\s*\\n/).filter(function(x){{return x.trim()}}).length;
    var o=b.textContent;b.textContent='복사됨 · '+n+'개';
    setTimeout(function(){{b.textContent=o}},1800);
  }};
}});
</script></body></html>"""
io.open('_작업/bulk_26_복사허브.html','w',encoding='utf-8').write(page)
print("허브 재생성 완료")
