# -*- coding: utf-8 -*-
"""
대표님이 작성해주신 [돋보기(Magnifier) 착란·기형 차단 정본] 100% 장착:
- 손잡이 2개(기형) 방지: exactly one single wooden handle at 5 o'clock
- 렌즈 안 기괴한 형상 방지: visually empty and transparent, nothing inside
"""

import json

new_magnifier_prompt = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is evenly balanced around the optical center. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subject throughout the sequence is exactly one classic round reading magnifying glass resting flat at the optical center. It has exactly one circular lens, exactly one thin brass-colored rim and exactly one short wooden handle. The single handle is permanently attached at the lower-right edge of the rim and points toward the five-o’clock direction. No duplicated handle, secondary handle, detached part or motion trail may appear.

0-4s: ultra-fine pale warm-grey graphite linework is actively traced stroke by stroke progressively from the empty white field. Each new stroke begins at one visible point and travels forward to its endpoint, leaving the finished graphite line behind. The drawing is constructed progressively through clearly visible moving strokes, never by fading in, dissolving, materializing or revealing a completed image. Only the lines already traced may be visible; every unfinished part remains completely blank white.

Begin by tracing one continuous circular outer rim. Trace one smaller concentric circle inside it to define the lens. Next, actively trace the single wooden handle from its attachment point at the lower-right rim to its rounded endpoint. Add only two short, simple contour lines at the handle connection last.

Every detail becomes visible sequentially, never all at once. The magnifying glass must not exist before its individual strokes are traced. Previously completed lines remain delicate, completely stable and unchanged.

Every outline is very thin, soft and light, never black or dark charcoal. There are no bold contours, heavy edge lines, dense hatch marks, realistic reflections, glossy highlights, cast shadows, photographic textures or visible objects inside the lens. Keep the graphite lines pale but clearly readable, never darker than 25% grey.

4-8s: an extremely pale, water-heavy watercolor wash develops gently inside the completed graphite outlines. The watercolor appears gradually in small transparent painted areas rather than covering the object all at once. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled.

Apply a very pale warm walnut-tan wash to small parts of the single wooden handle. Apply a sheer muted champagne-beige wash to small parts of the circular rim. Apply only one extremely pale, flat cool-blue wash inside the lens.

The lens remains visually empty and transparent. Nothing is reflected, magnified, distorted or depicted inside it. No person, animal, face, eye, symbol, scenery, liquid, bubble or second object appears inside the lens.

All surrounding space stays untouched pure white, with no background wash extending behind the subject. During the final second, one small pale-blue watercolor patch inside the lens spreads slightly and then stops. The rim and single handle remain completely fixed.

The final composition remains centered, clearly readable and surrounded by generous untouched white space.

Style: master-level hand-drawn fine-line illustration with exceptionally thin pale warm-grey graphite strokes, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, visible stroke-by-stroke drawing process, generous white space. Flat 2D illustration only, never photorealistic, never live action, never 3D or CGI.

No text, labels, borders, panels, extra subjects, duplicated parts, second handle, hands, fingers, arms, pencils, pens, brushes, separate drawing tools or visible artist. Completely silent."""

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for s in data:
    if s["set_id"] == "set10":
        s["prompts"][1]["prompt"] = " ".join(new_magnifier_prompt.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("_작업/bulk_sets/set10_10.txt", "w", encoding="utf-8") as f:
    for p in data[6]["prompts"]:
        f.write(p["prompt"] + "\n\n")

print("대표님의 돋보기 완벽 교정 프롬프트 적용 완료!")

