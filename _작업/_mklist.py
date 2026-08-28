# -*- coding: utf-8 -*-
import io, html, json
SCENES=[
("우체국 창구","우체국 직원·소포·우표·저울",["clerk","stamp","label"],["deliver","receive","transfer","reserve","offer"],"ch5"),
("응급실 앞","구급차·경광등·들것",["ambulance","alarm","accident"],["injure","hurt","medical","crisis","prevent","avoid"],"ch6"),
("법정","법봉·저울·경찰 모자",["cop","justice"],["crime","arrest","punish","innocent","moral","evil","claim"],"ch4"),
("기차역 승강장","증기기관차·철로·역사 시계",["station","rail","engine"],["transport","depart","proceed","schedule"],"ch5"),
("박물관 전시실","유리장·전시대·안내판",["museum","hall"],["tradition","represent","display","ancient"],"ch4"),
("호텔 로비","프런트 데스크·열쇠·짐",["hotel","guest"],["serve","reserve","rent","charge"],"ch5"),
("영화관","영사기·필름·스크린",["cinema","studio"],["version","popular","fashion","copy","photo"],"ch4"),
("옛 성","성벽·망루·왕관",["castle","palace","royal"],["cast","tradition","protect","empire"],"ch11"),
("감옥 창살","쇠창살·자물쇠·열쇠",["prison"],["crime","punish","escape","private","privacy"],"ch4"),
("실험실 작업대","플라스크·현미경·기록장",["lab","laboratory","engineer"],["investigate","method","prove","suppose","notice","recognize"],"ch11"),
("방직 공장","물레방아·직조기·실타래",["mill","industry"],["produce","labor","manufacture","establish","system"],"ch6"),
("구조 헬리콥터","프로펠러·착륙장",["helicopter"],["mission","rapid","succeed","lead","assist"],"ch5"),
("발사대의 로켓","로켓·발사탑·연기",["rocket"],["launch","mission","success","advance","forward"],"ch11"),
("거리 행진","깃발·악대차·승합차",["van","parade"],["crowd","citizen","public","social","excite"],"ch5"),
("가게 계산대","금전등록기·가격표·영수증",["price","fee"],["purchase","value","worth","charge","expense","budget"],"ch7"),
("은행 창구","금고·서류·도장",["loan","stock"],["finance","fund","loss","profit","tax","property"],"ch7"),
("식당 차림표","메뉴판·조리법 수첩·양념",["menu","recipe"],["bitter","supply","brand","guarantee"],"ch7"),
("사람의 머리와 목","뇌 단면도·목·무릎 해부도",["brain","throat","knee"],["blind","breath","tear","faint","suffer","exist"],"ch8"),
("기계 제어반","스위치·펌프·계기판·모니터",["switch","pump","monitor"],["automatic","technology","code","click","stamp"],"ch6"),
("석탄 광차","석탄·수레·삽",["coal"],["labor","industry","waste","pollute"],"ch10"),
("가족 사진틀","쌍둥이·부부 사진·반지",["twin","female","male"],["bond","relate","engage","divorce","respect","senior"],"ch9"),
("광장의 군중","깃발·현수막·모인 사람들",["crowd","citizen"],["protest","public","social","oppose","insist","standard"],"ch9"),
("군용 장비","철모·군화·망원경",["military","bomb"],["enemy","threat","victim","violent","resist","harm","spy","rob"],"ch4"),
("시인의 책상","펜·원고지·촛불",["poet"],["sentence","speech","quote","mention","emphasize","explain","refer"],"ch12"),
("골프 그린","골프채·공·깃대",["golf"],["champion","challenge","effort","react","risk","manage"],"ch8"),
("초원의 얼룩말","얼룩말·풀·먼 산",["zebra"],["motion","shake","bow","local"],"ch2"),
]
tot_l1=sum(len(a) for _,_,a,_,_ in SCENES); tot_l2=sum(len(b) for _,_,_,b,_ in SCENES)
rows=""
for n,(t,el,l1,l2,ch) in enumerate(SCENES,1):
    rows+=f"""<tr><td class=n>{n:02d}</td><td><b>{t}</b><div class=el>{el}</div></td>
<td class=w>{' · '.join(l1)}</td><td class=w2>{' · '.join(l2)}</td><td class=ch>{ch}</td></tr>"""
copy_txt="\n".join("%02d. %s — 요소: %s / 레벨1: %s / 레벨2: %s / 배정: %s"%(i,t,el,", ".join(a),", ".join(b),c)
                   for i,(t,el,a,b,c) in enumerate(SCENES,1))
page=f"""<!doctype html><html lang=ko><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1">
<title>새로 그릴 그림 목록</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#0f1115;color:#e6e8ec;font-family:Pretendard,-apple-system,"Apple SD Gothic Neo",sans-serif;line-height:1.6}}
header{{position:sticky;top:0;background:#161a21;border-bottom:1px solid #262b34;padding:14px 18px;display:flex;gap:14px;align-items:center;flex-wrap:wrap;z-index:9}}
h1{{font-size:16px;margin:0;font-weight:800}}.sub{{font-size:12px;color:#8b93a1}}
button{{margin-left:auto;background:#2b7a5b;color:#fff;border:0;border-radius:8px;padding:10px 18px;font-size:14px;font-weight:700;cursor:pointer}}
main{{padding:18px;max-width:1100px;margin:0 auto}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
th{{text-align:left;padding:10px 8px;border-bottom:2px solid #2b323d;color:#9aa3b2;font-size:11px;letter-spacing:.08em}}
td{{padding:11px 8px;border-bottom:1px solid #1e242d;vertical-align:top}}
.n{{color:#6b7484;font-variant-numeric:tabular-nums;width:34px}}
.el{{font-size:11px;color:#8b93a1;margin-top:3px}}
.w{{color:#ff9d8a;font-family:ui-monospace,monospace;font-size:12px;width:26%}}
.w2{{color:#8ab4f8;font-family:ui-monospace,monospace;font-size:12px;width:32%}}
.ch{{color:#c8b273;font-family:ui-monospace,monospace;width:52px}}
.box{{background:#151922;border:1px solid #232833;border-radius:10px;padding:14px 16px;margin-bottom:16px;font-size:13px}}
.box b{{color:#f0c674}}
@media(max-width:760px){{td,th{{font-size:11px;padding:8px 4px}}}}
</style></head><body>
<header><div><h1>새로 그릴 그림 {len(SCENES)}장</h1>
<div class=sub>레벨1 {tot_l1}개 · 레벨2 {tot_l2}개 = 단어 {tot_l1+tot_l2}개 소화</div></div>
<button id=b>전체 복사</button></header>
<main>
<div class=box><b>읽는 법</b><br>
<span style="color:#ff9d8a">레벨1</span> = 그림에 눈으로 보여야 하는 것. 퀴즈에 나옵니다.<br>
<span style="color:#8ab4f8">레벨2</span> = 그 장면에서 이야기로 이어지는 말. 그림에 안 보여도 됩니다.<br>
요소는 그림에 그려야 할 물건입니다. 사람 손(연필·붓)은 나와도 됩니다.</div>
<table><tr><th></th><th>그림</th><th>레벨1 · 보여야 함</th><th>레벨2 · 이야기로</th><th>챕터</th></tr>
{rows}</table>
<pre id=t style="display:none">{html.escape(copy_txt)}</pre>
</main><script>
const b=document.getElementById('b');
b.onclick=async()=>{{try{{await navigator.clipboard.writeText(document.getElementById('t').textContent)}}catch(e){{}}
b.textContent='복사됨 ✓';setTimeout(()=>b.textContent='전체 복사',1600)}};
</script></body></html>"""
io.open('_작업/새로그릴그림_목록.html','w',encoding='utf-8').write(page)
print("장면 %d · 레벨1 %d · 레벨2 %d · 합 %d" % (len(SCENES),tot_l1,tot_l2,tot_l1+tot_l2))
