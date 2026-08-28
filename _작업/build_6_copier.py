# -*- coding: utf-8 -*-
import os

p1 = """Progressive detailed fine-pencil construction, transparent watercolor and gentle object-motion animation on a solid pure bright white background (#FFFFFF), edge to edge. The first frame is an entirely empty pure white field. Static locked-off camera, one continuous 8-second take. The only visible subjects are exactly one illustrated wooden post office counter with an arched clerk window, one illustrated brown parcel box tied with twine and one illustrated canvas mail sack leaning beside it. All subjects are drawn small and centred at the optical center, together occupying no more than the middle half of the frame width and height, with generous empty white space on every side and clear white space between each object. 0-3.5s: exceptionally fine pale-neutral 2H graphite strokes are visibly traced one by one across the empty white field. The counter frame is constructed first through separate hair-thin graphite lines, followed by the arched window opening, the square parcel with its knotted twine, and the slumped folds of the canvas mail sack. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines. Each stroke has a clear beginning and endpoint. The illustration is built progressively rather than fading into view. Previously completed lines remain stable. 3.5-5.5s: clear transparent watercolor develops in layered color. A pale sand wash settles lightly along selected panel edges of the wooden counter, faint blue-grey tints only the upper half of the window glass, soft biscuit touches one face of the parcel, and pale oatmeal shades the lower folds of the sack, leaving most of the white paper bare. Every wash stays pale and translucent, applied once and never built up to full saturation. Preserve narrow white-paper highlights while keeping the colors fresh, luminous and distinguishable, with graphite details visible through every layer. 5.5-8s: the knotted twine bow on the parcel loosens two millimetres and settles. The counter, window and sack remain fixed. All other elements remain fixed. All graphite construction lines and watercolor boundaries remain stable. Style: intricate premium pencil-and-watercolor plate, numerous hair-thin pale graphite construction lines, accurate object anatomy, luminous layered transparent watercolor, delicate postal artifact textures, sophisticated museum-quality illustrated-dictionary artwork, clearly hand-drawn and never photographic. No dark outline, black ink, sepia ink, charcoal, thick contour, product photography, studio lighting, realistic reflection, glossy highlight, cast shadow, 3D, CGI, text, label, border, hand, artist or visible drawing tool. Exactly one parcel and one sack. Completely silent."""

p2 = """Progressive detailed fine-pencil construction, transparent watercolor and gentle object-motion animation on a solid pure bright white background (#FFFFFF), edge to edge. The first frame is an entirely empty pure white field. Static locked-off camera, one continuous 8-second take. The only visible subjects are exactly one illustrated white medical ambulance with cross markings, one illustrated rooftop beacon lamp and one illustrated folded wheeled stretcher beside it. All subjects are drawn small and centred at the optical center, together occupying no more than the middle half of the frame width and height, with generous empty white space on every side and clear white space between each object. 0-3.5s: exceptionally fine pale-neutral 2H graphite strokes are visibly traced one by one across the empty white field. The boxy contours of the ambulance body are traced first, followed by the wheel arches, headlamps, rooftop beacon housing, side window panels and the slender frame of the folded stretcher. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines. Each stroke has a clear beginning and endpoint. The illustration is built progressively rather than fading into view. Previously completed lines remain stable. 3.5-5.5s: clear transparent watercolor develops in layered color. A faint grey wash settles lightly along selected panel seams of the ambulance, soft rose tints only the cross markings, pale blue touches the upper edge of the windows, and faint straw shades one side of the beacon lamp, leaving most of the white paper bare. Every wash stays pale and translucent, applied once and never built up to full saturation. Preserve narrow white-paper highlights while keeping the colors fresh, luminous and distinguishable, with graphite details visible through every layer. 5.5-8s: the rooftop beacon lamp brightens faintly once and dims again. The vehicle and stretcher remain fixed. All other elements remain fixed. All graphite construction lines and watercolor boundaries remain stable. Style: intricate premium pencil-and-watercolor plate, numerous hair-thin pale graphite construction lines, accurate object anatomy, luminous layered transparent watercolor, crisp hand-drawn vehicle contours, sophisticated museum-quality illustrated-dictionary artwork, clearly hand-drawn and never photographic. No dark outline, black ink, sepia ink, charcoal, thick contour, product photography, studio lighting, realistic reflection, glossy highlight, cast shadow, 3D, CGI, text, label, border, hand, artist or visible drawing tool. Exactly one ambulance and one stretcher. Completely silent."""

p3 = """Progressive detailed fine-pencil construction, transparent watercolor and gentle object-motion animation on a solid pure bright white background (#FFFFFF), edge to edge. The first frame is an entirely empty pure white field. Static locked-off camera, one continuous 8-second take. The only visible subjects are exactly one illustrated leather document case standing open, one illustrated stack of folded legal papers and one illustrated brass desk seal beside them. All subjects are drawn small and centred at the optical center, together occupying no more than the middle half of the frame width and height, with generous empty white space on every side and clear white space between each object. 0-3.5s: exceptionally fine pale-neutral 2H graphite strokes are visibly traced one by one across the empty white field. The buckled flap and stitched seams of the leather case are traced first, followed by the fanned edges of the folded paper stack and the turned handle of the brass desk seal. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines. Each stroke has a clear beginning and endpoint. The illustration is built progressively rather than fading into view. Previously completed lines remain stable. 3.5-5.5s: clear transparent watercolor develops in layered color. A pale biscuit wash settles lightly along selected edges of the leather case, faint cream tints only the outer paper edges, and soft grey touches one side of the desk seal, leaving most of the white paper bare. Every wash stays pale and translucent, applied once and never built up to full saturation. Preserve narrow white-paper highlights while keeping the colors fresh, luminous and distinguishable, with graphite details visible through every layer. 5.5-8s: the topmost folded paper lifts one millimetre at its corner and settles back. The case and seal remain fixed. All other elements remain fixed. All graphite construction lines and watercolor boundaries remain stable. Style: intricate premium pencil-and-watercolor plate, numerous hair-thin pale graphite construction lines, accurate object anatomy, luminous layered transparent watercolor, quiet legal-office textures, sophisticated museum-quality illustrated-dictionary artwork, clearly hand-drawn and never photographic. No dark outline, black ink, sepia ink, charcoal, thick contour, product photography, studio lighting, realistic reflection, glossy highlight, cast shadow, 3D, CGI, text, label, border, hand, artist or visible drawing tool. Exactly one case, one paper stack and one seal. Completely silent."""

p4 = """Progressive detailed fine-pencil construction, transparent watercolor and gentle object-motion animation on a solid pure bright white background (#FFFFFF), edge to edge. The first frame is an entirely empty pure white field. Static locked-off camera, one continuous 8-second take. The only visible subjects are exactly one illustrated vintage steam locomotive at a platform, exactly two illustrated parallel steel rails and one illustrated round hanging station clock. All subjects are drawn small and centred at the optical center, together occupying no more than the middle half of the frame width and height, with generous empty white space on every side and clear white space between each object. 0-3.5s: exceptionally fine pale-neutral 2H graphite strokes are visibly traced one by one across the empty white field. The cylindrical boiler, chimney stack, cowcatcher and spoked driving wheels are constructed through fine graphite contours, followed by the straight parallel rails, the wooden sleepers, and the circular hanging clock. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines. Each stroke has a clear beginning and endpoint. The illustration is built progressively rather than fading into view. Previously completed lines remain stable. 3.5-5.5s: clear transparent watercolor develops in layered color. A pale slate wash settles lightly along selected plate seams of the locomotive, faint steel-blue tints only the inner rail faces, and soft biscuit touches the rim of the clock casing, leaving most of the white paper bare. Every wash stays pale and translucent, applied once and never built up to full saturation. Preserve narrow white-paper highlights while keeping the colors fresh, luminous and distinguishable, with graphite details visible through every layer. 5.5-8s: a small wisp of pale translucent steam rises three centimetres from the chimney and drifts. The train, rails and clock remain fixed. All other elements remain fixed. All graphite construction lines and watercolor boundaries remain stable. Style: intricate premium pencil-and-watercolor plate, numerous hair-thin pale graphite construction lines, accurate object anatomy, luminous layered transparent watercolor, intricate hand-drawn machinery details, sophisticated museum-quality illustrated-dictionary artwork, clearly hand-drawn and never photographic. No dark outline, black ink, sepia ink, charcoal, thick contour, product photography, studio lighting, realistic reflection, glossy highlight, cast shadow, 3D, CGI, text, label, border, hand, artist or visible drawing tool. Exactly one locomotive and one clock. Completely silent."""

p5 = """Progressive detailed fine-pencil construction, transparent watercolor and gentle object-motion animation on a solid pure bright white background (#FFFFFF), edge to edge. The first frame is an entirely empty pure white field. Static locked-off camera, one continuous 8-second take. The only visible subjects are exactly one illustrated museum glass showcase cabinet on a stone pedestal and one illustrated ancient carved clay urn displayed inside it. All subjects are drawn small and centred at the optical center, together occupying no more than the middle half of the frame width and height, with generous empty white space on every side and clear white space between each object. 0-3.5s: exceptionally fine pale-neutral 2H graphite strokes are visibly traced one by one across the empty white field. The rectilinear glass cabinet frame is drawn with clean graphite lines, followed by the fluted stone pedestal, and the delicate handles and textured relief band of the ancient urn. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines. Each stroke has a clear beginning and endpoint. The illustration is built progressively rather than fading into view. Previously completed lines remain stable. 3.5-5.5s: clear transparent watercolor develops in layered color. A faint mint tint runs lightly along selected glass edges of the cabinet, pale terracotta settles only on the shoulder of the urn, and soft grey veins one side of the stone stand, leaving most of the white paper bare. Every wash stays pale and translucent, applied once and never built up to full saturation. Preserve narrow white-paper highlights while keeping the colors fresh, luminous and distinguishable, with graphite details visible through every layer. 5.5-8s: the small clay urn shifts a single millimetre on the glass shelf and settles. The cabinet and pedestal remain fixed. All other elements remain fixed. All graphite construction lines and watercolor boundaries remain stable. Style: intricate premium pencil-and-watercolor plate, numerous hair-thin pale graphite construction lines, accurate object anatomy, luminous layered transparent watercolor, museum artifact precision, sophisticated museum-quality illustrated-dictionary artwork, clearly hand-drawn and never photographic. No dark outline, black ink, sepia ink, charcoal, thick contour, product photography, studio lighting, realistic reflection, glossy highlight, cast shadow, 3D, CGI, text, label, border, hand, artist or visible drawing tool. Exactly one cabinet and one urn. Completely silent."""

p6 = """Progressive detailed fine-pencil construction, transparent watercolor and gentle object-motion animation on a solid pure bright white background (#FFFFFF), edge to edge. The first frame is an entirely empty pure white field. Static locked-off camera, one continuous 8-second take. The only visible subjects are exactly one illustrated curved wooden hotel reception desk, one illustrated brass call bell, exactly one illustrated room key with a numbered tag and one illustrated leather travel case. All subjects are drawn small and centred at the optical center, together occupying no more than the middle half of the frame width and height, with generous empty white space on every side and clear white space between each object. 0-3.5s: exceptionally fine pale-neutral 2H graphite strokes are visibly traced one by one across the empty white field. The sweep of the reception counter is traced with fine graphite, followed by the domed call bell, the notched key with its oval tag, and the buckled straps of the leather travel case. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines. Each stroke has a clear beginning and endpoint. The illustration is built progressively rather than fading into view. Previously completed lines remain stable. 3.5-5.5s: clear transparent watercolor develops in layered color. A pale nut-brown wash settles lightly along selected panel edges of the counter, faint straw touches only the dome of the call bell, soft biscuit tints the key tag, and pale tan shades one strap of the travel case, leaving most of the white paper bare. Every wash stays pale and translucent, applied once and never built up to full saturation. Preserve narrow white-paper highlights while keeping the colors fresh, luminous and distinguishable, with graphite details visible through every layer. 5.5-8s: the numbered key tag sways gently two millimetres and comes to rest. The desk, bell and case remain fixed. All other elements remain fixed. All graphite construction lines and watercolor boundaries remain stable. Style: intricate premium pencil-and-watercolor plate, numerous hair-thin pale graphite construction lines, accurate object anatomy, luminous layered transparent watercolor, vintage hospitality textures, sophisticated museum-quality illustrated-dictionary artwork, clearly hand-drawn and never photographic. No dark outline, black ink, sepia ink, charcoal, thick contour, product photography, studio lighting, realistic reflection, glossy highlight, cast shadow, 3D, CGI, text, label, border, hand, artist or visible drawing tool. Exactly one bell, one key and one case. Completely silent."""

prompts = [p1, p2, p3, p4, p5, p6]
titles = [
    "01. 우체국 창구 (Post office counter)",
    "02. 응급실 앞 (Emergency ambulance)",
    "03. 법정 (Courtroom document case)",
    "04. 기차역 승강장 (Steam locomotive)",
    "05. 박물관 전시대 (Museum showcase & urn)",
    "06. 호텔 프런트 (Hotel reception desk)"
]

# 1) 빈 줄 구분 파일 (줄바꿈 2개 \n\n)
f1 = "/Users/mihyunlee/workspace/움직이는그림사전/_작업/bulk_26/bulk_6_double_enter.txt"
with open(f1, "w", encoding="utf-8") as f:
    f.write("\n\n".join(prompts) + "\n")

# 2) 홑 줄 구분 파일 (줄바꿈 1개 \n)
f2 = "/Users/mihyunlee/workspace/움직이는그림사전/_작업/bulk_26/bulk_6_single_enter.txt"
with open(f2, "w", encoding="utf-8") as f:
    f.write("\n".join(prompts) + "\n")

# 3) 개별 복사용 HTML 생성
html_items = []
for idx, (t, p) in enumerate(zip(titles, prompts)):
    html_items.append(f"""
    <div style="background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:18px; margin-bottom:16px; box-shadow:0 1px 3px rgba(0,0,0,0.04);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
        <b style="font-size:15px; color:#1e293b;">#{idx+1} {t}</b>
        <button onclick="copySingle('p_{idx+1}', this)" style="background:#059669; color:#fff; border:0; padding:8px 16px; border-radius:6px; font-weight:700; cursor:pointer;">이것만 복사</button>
      </div>
      <textarea id="p_{idx+1}" style="width:100%; height:90px; font-family:monospace; font-size:11px; padding:10px; border:1px solid #cbd5e1; border-radius:6px; box-sizing:border-box; resize:vertical; background:#f8fafc; color:#334155;">{p}</textarea>
    </div>
    """)

hub_html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>6개 프롬프트 벌크 및 개별 복사</title>
<style>
  body {{ margin:0; background:#f1f5f9; font-family:Pretendard,-apple-system,sans-serif; color:#1e293b; padding:24px; }}
  .container {{ max-width:1000px; margin:0 auto; }}
  .top-box {{ background:#fff; border:1px solid #cbd5e1; border-radius:14px; padding:20px; margin-bottom:24px; }}
  .bulk-btn {{ background:#2563eb; color:#fff; border:0; padding:12px 22px; border-radius:8px; font-size:14px; font-weight:800; cursor:pointer; margin-right:10px; margin-bottom:10px; }}
  .bulk-btn:hover {{ background:#1d4ed8; }}
</style>
</head>
<body>
<div class="container">
  <div class="top-box">
    <h2 style="margin-top:0; color:#0f172a;">⚡ 6개 프롬프트 벌크 분리 복사</h2>
    <p style="color:#64748b; font-size:13px;">생성기 프로그램에 따라 줄바꿈 인식 방식이 다를 수 있어 2가지 벌크 방식과 개별 복사 버튼을 모두 준비했습니다.</p>
    <button class="bulk-btn" onclick="copyRaw('bulk_double', this)">1. 빈 줄 2개 구분으로 6개 전체 복사</button>
    <button class="bulk-btn" style="background:#4f46e5;" onclick="copyRaw('bulk_single', this)">2. 엔터 1개 구분으로 6개 전체 복사</button>
    <textarea id="bulk_double" style="display:none;">{"\n\n".join(prompts)}</textarea>
    <textarea id="bulk_single" style="display:none;">{"\n".join(prompts)}</textarea>
  </div>

  <h3 style="color:#334155; margin-bottom:14px;">📌 개별 프롬프트 1개씩 복사 (6개)</h3>
  {''.join(html_items)}
</div>
<script>
async function copyRaw(id, btn) {{
  const t = document.getElementById(id).value;
  await navigator.clipboard.writeText(t);
  const orig = btn.textContent;
  btn.textContent = '6개 전체 복사 완료! ✓';
  setTimeout(() => {{ btn.textContent = orig; }}, 1800);
}}
async function copySingle(id, btn) {{
  const t = document.getElementById(id).value;
  await navigator.clipboard.writeText(t);
  const orig = btn.textContent;
  btn.textContent = '복사됨 ✓';
  btn.style.background = '#047857';
  setTimeout(() => {{ btn.textContent = orig; btn.style.background = '#059669'; }}, 1600);
}}
</script>
</body>
</html>"""

out_hub = "/Users/mihyunlee/workspace/움직이는그림사전/_작업/bulk_6_복사기.html"
with open(out_hub, "w", encoding="utf-8") as f:
    f.write(hub_html)

print("준비 완료:", out_hub)
