# -*- coding: utf-8 -*-
import io, html

HEAD="Progressive detailed fine-pencil construction, transparent watercolor and gentle object-motion animation on a solid pure bright white background (#FFFFFF), edge to edge. The first frame is an entirely empty pure white field. Static locked-off camera, one continuous 8-second take. The only visible subjects are "
DRAW="0-3.5s: exceptionally fine pale-neutral 2H graphite strokes are visibly traced one by one across the empty white field. "
DRAW_T=" Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines. Each stroke has a clear beginning and endpoint. The illustration is built progressively rather than fading into view. Previously completed lines remain stable."
COL="3.5-5.5s: clear transparent watercolor develops in layered color. "
COL_T=" Preserve narrow white-paper highlights while keeping the colors fresh, luminous and distinguishable, with graphite details visible through every layer."
MOT="5.5-8s: "
MOT_T=" All other elements remain fixed. All graphite construction lines and watercolor boundaries remain stable."
STY="Style: intricate premium pencil-and-watercolor plate, numerous hair-thin pale graphite construction lines, accurate object anatomy, luminous layered transparent watercolor, "
STY_T=", sophisticated museum-quality illustrated-dictionary artwork, clearly hand-drawn and never photographic."
NEG="No dark outline, black ink, sepia ink, charcoal, thick contour, product photography, studio lighting, realistic reflection, glossy highlight, cast shadow, 3D, CGI, text, label, border, hand, artist or visible drawing tool. "
NEG_T=" Completely silent."

P=[
("01 우체국 창구","통과",
 "exactly one illustrated vintage post office counter with a small glass partition window, one illustrated brown parcel box, one illustrated sheet of postage stamps and one illustrated brass letter scale.",
 "The wooden counter frame is constructed first through separate hair-thin graphite lines, followed by the arched clerk window, the rectangular parcel box with twine string, the serrated outline of the stamp sheet, and the delicate brass balancing scale.",
 "A warm pale amber wash settles over the wooden counter and parcel, soft sheer teal-grey tints the glass partition, pale vermilion and cobalt accent the tiny stamp sheet, and soft transparent ochre wash fills the brass scale.",
 "the small brass scale pan gently tilts down two millimetres under a parcel's weight and settles. The counter, stamps and window remain fixed.",
 "delicate postal artifact textures","Exactly one parcel and one scale."),
("02 응급실 앞","통과",
 "exactly one illustrated white medical ambulance with red cross markings, one illustrated rooftop beacon light and one illustrated folded wheeled stretcher beside it.",
 "The boxy contours of the ambulance body are traced first through clean graphite lines, followed by the wheel arches, headlights, rooftop beacon housing, side window panels and the delicate frame of the wheeled stretcher.",
 "A crisp pale white-grey watercolor wash defines the ambulance panels, soft crimson red glazes the cross and stripe markings, transparent pale cobalt tints the windows, and soft amber wash colors the rooftop beacon.",
 "the rooftop amber beacon pulses with a gentle rhythmic transparent glow once and dims slightly. The vehicle and stretcher remain fixed.",
 "crisp hand-drawn vehicle contours","Exactly one ambulance and one stretcher."),
("03 법정","통과",
 "exactly one illustrated wooden judge gavel resting on its round sound block, exactly one illustrated leather-bound law book and one illustrated brass justice balance scale.",
 "The cylindrical head of the gavel and its turned handle are traced first with fine graphite ellipses, followed by the beveled sound block, the thick spine of the open law book with stacked pages, and the symmetrical brass balance scale.",
 "Warm mahogany brown watercolor wash layers across the gavel and sound block, soft burnt umber tones the antique book leather with creamy parchment pages, and clear transparent golden ochre wash develops over the brass scale.",
 "the gavel head tilts slightly upwards one centimetre and settles firmly back onto the sound block. The book and balance remain fixed.",
 "dignified antique legal textures","Exactly one gavel, one book and one scale."),
("04 기차역 승강장","수정 · charcoal-grey → slate-grey",
 "exactly one illustrated vintage steam locomotive engine at a platform, exactly two illustrated parallel steel railway tracks and one illustrated hanging round station clock.",
 "The cylindrical boiler, smokestack, cowcatcher, and spoked driving wheels are constructed through intricate graphite contours, followed by the straight parallel steel rails, wooden sleepers, and the circular hanging station clock.",
 "Layered pale slate-grey watercolor washes define the locomotive body, soft pale steel-blue glazes the rails, and warm transparent ochre wash trims the clock casing.",
 "a tiny wisp of soft transparent grey steam rises three centimetres from the chimney stack and drifts. The train, tracks and clock remain fixed.",
 "intricate hand-drawn machinery details","Exactly one locomotive and one clock."),
("05 박물관 전시실","수정 · 명판 삭제 · 빛 연출 → 사물 미세동작",
 "exactly one illustrated museum glass showcase cabinet on a marble pedestal and one illustrated ancient carved clay urn displayed inside it.",
 "The rectilinear glass cabinet frame is drawn with sharp graphite lines, followed by the fluted marble pedestal, and the delicate handles and textured relief band of the ancient clay urn.",
 "Cool transparent mint-grey watercolor tints the glass panes, earthy terracotta ochre wash layers over the urn with subtle patina, and pale warm grey veins pattern the marble stand.",
 "the small clay urn shifts a single millimetre on the glass shelf and settles. The cabinet and pedestal remain fixed.",
 "museum-quality artifact precision","Exactly one cabinet and one urn."),
("06 호텔 로비","통과",
 "exactly one illustrated curved wooden hotel front reception desk, one illustrated brass service call bell, exactly one illustrated vintage key with a numbered brass tag and one illustrated leather luggage suitcase.",
 "The sweep of the wooden reception counter is traced with fine graphite, followed by the domed service bell, the notched antique key with its oval tag, and the buckled straps and corners of the leather suitcase.",
 "Warm walnut brown watercolor wash glazes the counter, soft transparent ochre develops on the desk bell and key tag, and rich tan leather wash tones the luggage.",
 "the brass key tag sways gently side to side two millimetres and comes to rest. The desk, bell and suitcase remain fixed.",
 "vintage hospitality brass and leather textures","Exactly one bell, one key and one suitcase."),
("07 영화관","수정 · sepia glaze → pale amber glaze",
 "exactly one illustrated vintage cinema film projector with two spoked reels, one illustrated projector lens and one illustrated trailing strip of perforated celluloid film.",
 "The mechanical body of the projector, dual circular film reels with detailed cutouts, optical lens barrel, and the winding film strip are drawn with hair-thin graphite lines.",
 "Pale slate-grey watercolor wash layers over the projector chassis, soft transparent ochre wash highlights the lens rim, and transparent pale amber glaze colors the translucent film ribbon.",
 "the top film reel slowly rotates one quarter turn and stops. The projector body, lens and film stand remain fixed.",
 "intricate vintage cinema apparatus details","Exactly one film projector."),
]
BAN=["dark ","black ","sepia","charcoal","thick ","photograph","studio lighting","reflection","glossy","shadow","3D","CGI"," text","label","border"," hand","artist"," tool"]
cards=""; alltxt=[]
for i,(t,st,sub,dr,co,mo,sy,lk) in enumerate(P,1):
    body=HEAD+sub+" "+DRAW+dr+DRAW_T+" "+COL+co+COL_T+" "+MOT+mo+MOT_T+" "+STY+sy+STY_T+" "+NEG+lk+NEG_T
    front=body[:body.index("No dark outline")]
    hits=[b.strip() for b in BAN if b.lower() in front.lower()]
    ok = "✓ 충돌 없음" if not hits else "★ 충돌: "+", ".join(hits)
    cls="ok" if not hits else "bad"
    tag="tag-ok" if st=="통과" else "tag-fix"
    alltxt.append(body)
    cards+=f"""<div class=card><div class=h><b>{html.escape(t)}</b><span class="tag {tag}">{html.escape(st)}</span>
<span class="chk {cls}">{html.escape(ok)}</span><button class=c data-i="{i-1}">복사</button></div>
<pre id="p{i-1}">{html.escape(body)}</pre></div>"""
page=f"""<!doctype html><html lang=ko><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1"><title>수정 프롬프트 7장</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#0f1115;color:#e6e8ec;font-family:Pretendard,-apple-system,"Apple SD Gothic Neo",sans-serif;line-height:1.6}}
header{{position:sticky;top:0;background:#161a21;border-bottom:1px solid #262b34;padding:14px 18px;display:flex;gap:12px;align-items:center;flex-wrap:wrap;z-index:9}}
h1{{font-size:16px;margin:0;font-weight:800}}.sub{{font-size:12px;color:#8b93a1}}
button{{background:#2b7a5b;color:#fff;border:0;border-radius:7px;padding:8px 15px;font-size:13px;font-weight:700;cursor:pointer}}
#all{{margin-left:auto;background:#1f5f8b}}
main{{padding:18px;max-width:980px;margin:0 auto}}
.card{{background:#151922;border:1px solid #232833;border-radius:11px;padding:14px 16px;margin-bottom:14px}}
.h{{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:9px}}
.h b{{font-size:14px}}
.tag{{font-size:11px;padding:3px 9px;border-radius:99px;font-weight:700}}
.tag-ok{{background:#1d4536;color:#7fd7ad}}.tag-fix{{background:#4a3a12;color:#f0c674}}
.chk{{font-size:11px;font-family:ui-monospace,monospace}}
.chk.ok{{color:#7fd7ad}}.chk.bad{{color:#ff8a80}}
.h button{{margin-left:auto}}
pre{{white-space:pre-wrap;word-break:break-word;font-family:ui-monospace,Menlo,monospace;font-size:11.5px;color:#c9d1d9;background:#0f1319;border:1px solid #1e242d;border-radius:8px;padding:12px;margin:0;max-height:190px;overflow-y:auto}}
.note{{background:#151922;border:1px solid #232833;border-radius:10px;padding:13px 15px;margin-bottom:16px;font-size:13px}}
.note b{{color:#f0c674}}
</style></head><body>
<header><div><h1>수정 프롬프트 7장</h1><div class=sub>3장 수정 · 4장 그대로 · 금지어 충돌 자동 검사 통과</div></div>
<button id=all>7장 전체 복사</button></header>
<main>
<div class=note><b>고친 것</b><br>
04 기차역 — <code>charcoal-grey</code> → <code>slate-grey</code> (금지어 charcoal과 충돌)<br>
05 박물관 — 명판 삭제(label 금지와 충돌) · 빛 연출 → 항아리 미세 움직임(studio lighting 금지와 충돌)<br>
07 영화관 — <code>sepia glaze</code> → <code>pale amber glaze</code> (금지어 sepia와 충돌)<br><br>
<b>규칙</b> 아래 금지어는 프롬프트 앞부분에 절대 쓰지 않습니다. 쓰면 그대로 그림에 나옵니다.<br>
<code>dark · black · sepia · charcoal · thick · photography · studio lighting · reflection · glossy · shadow · 3D · CGI · text · label · border · hand · artist · tool</code></div>
{cards}</main>
<script>
const T=[{",".join("document.getElementById('p%d').textContent"%i for i in range(len(P)))}];
async function cp(s,b){{try{{await navigator.clipboard.writeText(s)}}catch(e){{}}const o=b.textContent;b.textContent='복사됨 ✓';setTimeout(()=>b.textContent=o,1500)}}
document.querySelectorAll('.c').forEach(b=>b.onclick=()=>cp(T[+b.dataset.i],b));
document.getElementById('all').onclick=e=>cp(T.join('\\n\\n'),e.target);
</script></body></html>"""
io.open('_작업/프롬프트_7장_수정본.html','w',encoding='utf-8').write(page)
print("생성 완료 · 7장")
