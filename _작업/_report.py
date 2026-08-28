# -*- coding: utf-8 -*-
import io, json, html
s=io.open('public/learning/index.html',encoding='utf-8').read()
i=s.index('const chapterData = {'); st=s.index('{',i); d=0
for j in range(st,len(s)):
    if s[j]=='{': d+=1
    elif s[j]=='}':
        d-=1
        if d==0: en=j+1; break
data=json.loads(s[st:en])

# 로부장 전수 판정 (검수 이미지 육안 확인 결과)
FAIL={
"1":{"03":"좌표가 전부 빈 하늘·바다 · dolphin이 그림에 없음"},
"2":{"11":"단어가 bush·trace 둘뿐 (여우·자작나무·통나무·낙엽 있음)",
     "13":"잎벌레에 specific·seem·unit·demonstrate",
     "14":"도토리에 develop·separate·definite·defense",
     "15":"깃털에 swallow·mark·gentle",
     "16":"잠자리에 nerve·chest·muscle",
     "17":"단풍씨앗에 feature·balance·progress",
     "18":"새알에 pregnant·health·bury"},
"3":{"17":"나비에 amaze·odd·annual·gesture·vary·adapt",
     "19":"무당벌레에 cell·nail·poison",
     "20":"견과그릇에 source·district·approach",
     "21":"달팽이에 wound·toe (2개뿐)"},
"4":{"01":"서랍장에 chart·graph","02":"타자기에 drama·scene·comedy",
     "04":"이젤에 bit·benefit·belief·bet·billion·beyond ★b 알파벳순",
     "05":"만년필에 context·consider·conscious·contact·contract·contest ★con 알파벳순",
     "06":"돋보기에 correct·converse·contribute·convince·cough·cope ★co 알파벳순",
     "07":"종에 cruel·county·council·credit·crown·cure ★c 알파벳순",
     "08":"잉크병에 debate·dare·cute·darling·debt·deal ★d 알파벳순",
     "09":"독서대에 deny·delay·define·demand·dentist·depend ★de 알파벳순",
     "10":"클립에 economy·each·due·earn·effect·ease ★e 알파벳순",
     "11":"클립에 embarrass·elect·either·electric·emotion·else ★e 알파벳순"},
"7":{"05":"쌍안경에 amuse·announce·although·altogether·analysis·annual ★a 알파벳순",
     "06":"유리병에 assign·argue·appreciate·aside·assess ★a 알파벳순",
     "07":"나침반에 attention·assume·associate·attend·attack·attempt ★att 알파벳순",
     "08":"통나무집에 awkward·attract·attitude·average·aware·audience ★a 알파벳순"},
"8":{"05":"텐트에 escape·accent·access·absolute·able·accept ★a 알파벳순",
     "06":"랜턴에 admire·achieve·admit·account·accuse ★a 알파벳순",
     "07":"등산화에 advise·advantage·adopt·advertise·advice·affair ★ad 알파벳순",
     "08":"카누에 alcohol·allow·affect·afford·agent·aid ★a 알파벳순",
     "09":"주전자에 appoint·apart·appeal·appear·apply ★ap 알파벳순",
     "10":"밧줄에 seek·target·background·band·search·toward"},
"9":{"02":"바이올린 활에 glue·opinion","03":"법봉에 suspect·quit·tune·folk·fellow·mate",
     "04":"회중시계에 especial·express·opera·theater·master·without",
     "05":"여권에 mental·concentrate·loud·bang·influence·possible",
     "06":"나무상자에 shame·beat·exhaust·individual·evidence·respond",
     "07":"저울에 giraffe(기린)·insure·experiment·fortunate ★그림에 #FFFFF 글자 박힘",
     "08":"밀랍도장에 salary·plus·particular·humor·mood·pride",
     "09":"가방에 extreme·intense·secretary·nut·major·communicate",
     "10":"압지기에 immediate·quality·whistle·self·thief·satisfy",
     "11":"도마에 gun(총)·struggle·pronounce·govern·noise·prime"},
"10":{"04":"우산에 forth·refuse·moreover·except·replace·income",
     "05":"장갑에 propose·message·rainbow·general·sum·spoil",
     "06":"참나무잎에 native·which·prefer·possess·topic·extra",
     "07":"튤립에 rat(쥐)·physical·junior·pardon·league·provide",
     "08":"부채에 politics·sudden·polite·therefore·rude·report",
     "09":"플라스크에 forgive·sweep·detect·rule·title·retire",
     "10":"연에 serious·calculate·found·unless·yell·create",
     "11":"풍향계에 sew·support·invest·practice·century·reason",
     "12":"고드름에 slave·university·shoulder·stuff·count·potential",
     "13":"모자에 person·terrible·principle·hire·beer·hesitate"},
"11":{"04":"나무다리·시냇물에 prepare·research·theory·society",
     "05":"피아노·첼로에 grant·content·wage·matter·fault·main",
     "06":"조명·가면에 upon·select·frankly·regard·smash·rare",
     "07":"책상·깃펜에 suggest·planet·pub·paragraph·involve·imagine",
     "08":"시계탑에 employ·yet·minor·vote·calendar·previous",
     "09":"모닥불에 then·frustrate·overall·spend·guilt ★그림에 #FFFFFF 글자 박힘",
     "10":"배터리·회로에 shout·event·interrupt·steal·stomach·grade",
     "11":"헬리콥터에 similar·improve·neighbor·tongue·responsible",
     "12":"여행가방에 necessary·expert·real·forever·battle·treat ★배경만 회색",
     "13":"구급상자에 screen·display·license·till·pull·volunteer"},
"12":{"05":"판화롤러에 commerce·coin·coach·command·committee·comment ★com 알파벳순",
     "06":"베틀에 complicate·compare·community·complain·concept·complete ★com 알파벳순",
     "07":"핀셋에 conflict·concert·concern·confident·confuse·confirm ★con 알파벳순",
     "08":"스테이플러에 desperate·describe·depress·deserve·despite·desire ★des 알파벳순",
     "09":"연필깎이에 disc·determine·destroy·diet·disgust·disappoint ★dis 알파벳순"},
}
NAME={"1":"인벤티오 · 세상을 발견해요","2":"비타 · 숲과 생명","3":"도무스 · 우리 집","4":"스콜라 · 학교생활",
      "5":"우르브스 · 도시와 교통","6":"살루스 · 음식과 건강","7":"센수스 · 몸과 감정","8":"모투스 · 운동과 도전",
      "9":"문두스 · 여행과 세계","10":"테라 · 지구와 날씨","11":"코스모스 · 우주와 과학","12":"솜니움 · 밤과 꿈"}

rows=""; tot=0; bad=0
for ck in sorted(data,key=int):
    works=data[ck]['works']; f=FAIL.get(ck,{})
    tot+=len(works); bad+=len(f)
    ok=len(works)-len(f)
    pct=int(ok/len(works)*100)
    color="#7fd7ad" if pct==100 else ("#f0c674" if pct>=70 else "#ff8a80")
    rows+=f"""<tr class=chead><td class=ch>ch{ck}</td><td>{NAME[ck]}</td>
<td class=num>{len(works)}편</td><td class=num style="color:{color}">{ok} / {len(works)}</td>
<td class=bar><span style="width:{pct}%;background:{color}"></span></td></tr>"""
    for n in sorted(f):
        rows+=f"""<tr class=frow><td></td><td class=fno>ch{ck}_{n}</td><td colspan=3 class=fwhy>{html.escape(f[n])}</td></tr>"""

page=f"""<!doctype html><html lang=ko><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1"><title>157편 전수조사 결과</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#0f1115;color:#e6e8ec;font-family:Pretendard,-apple-system,"Apple SD Gothic Neo",sans-serif;line-height:1.6}}
header{{background:#161a21;border-bottom:1px solid #262b34;padding:18px}}
h1{{font-size:19px;margin:0 0 4px;font-weight:800}}.sub{{font-size:13px;color:#8b93a1}}
main{{padding:18px;max-width:1000px;margin:0 auto}}
.big{{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:20px}}
.stat{{flex:1;min-width:150px;background:#151922;border:1px solid #232833;border-radius:11px;padding:15px}}
.stat .v{{font-size:30px;font-weight:800;line-height:1.15}}
.stat .l{{font-size:12px;color:#8b93a1;margin-top:3px}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
td{{padding:8px 7px;vertical-align:middle}}
.chead td{{border-top:1px solid #2b323d;font-weight:700;padding-top:13px}}
.ch{{color:#c8b273;font-family:ui-monospace,monospace;width:44px}}
.num{{text-align:right;font-variant-numeric:tabular-nums;width:72px}}
.bar{{width:110px}}.bar span{{display:block;height:7px;border-radius:99px}}
.frow td{{padding:3px 7px;border:0}}
.fno{{color:#ff8a80;font-family:ui-monospace,monospace;font-size:11.5px;width:78px}}
.fwhy{{color:#9aa3b2;font-size:12px}}
.note{{background:#151922;border:1px solid #232833;border-radius:11px;padding:14px 16px;margin-bottom:18px;font-size:13px}}
.note b{{color:#f0c674}}
</style></head><body>
<header><h1>157편 그림·단어 전수조사</h1>
<div class=sub>2026-08-27 · 로부장이 챕터별 검수 이미지를 직접 열어 편마다 판정</div></header>
<main>
<div class=big>
<div class=stat><div class=v style="color:#7fd7ad">{tot-bad}</div><div class=l>합격 · 그림과 단어가 맞음</div></div>
<div class=stat><div class=v style="color:#ff8a80">{bad}</div><div class=l>불합격 · 고쳐야 함</div></div>
<div class=stat><div class=v>{int((tot-bad)/tot*100)}%</div><div class=l>합격률 (전체 {tot}편)</div></div>
</div>
<div class=note><b>가장 큰 원인 — 알파벳 사전순 밀어넣기</b><br>
불합격 {bad}편 중 절반 가까이가 <b>a·b·c·d 순서대로 단어를 그림에 붙인 것</b>입니다.
이젤에 <code>bit benefit belief bet billion beyond</code>, 만년필에 <code>context consider conscious contact contract contest</code>.
그림을 보지 않고 남은 단어를 사전 순으로 채운 흔적입니다.<br><br>
<b>그림 자체에 문제가 있는 3편</b><br>
ch9_07 저울 · ch11_09 모닥불 — 그림에 <code>#FFFFF</code> 색상코드 글자가 인쇄됨<br>
ch11_12 여행가방 — 혼자 배경이 회색 (나머지는 전부 흰 배경)<br><br>
<b>온전한 챕터</b> ch5(16편) · ch6(10편)은 전편 합격입니다. 코다리가 제대로 고친 곳입니다.</div>
<table>{rows}</table>
</main></body></html>"""
io.open('_작업/전수조사_20260827.html','w',encoding='utf-8').write(page)
print("합격 %d / 불합격 %d / 전체 %d (%d%%)" % (tot-bad,bad,tot,int((tot-bad)/tot*100)))
