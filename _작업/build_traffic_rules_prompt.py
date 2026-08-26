# -*- coding: utf-8 -*-
"""
대표님 디렉션 100% 반영: [교통 신호등과 횡단보도 정지선]
- 단어: rule (규칙), order (질서), law (법칙/원칙), stop (정지), signal (신호)
- 정본 헌법: 실사/군중/시커먼 도로 100% 배제, 순백(#FFFFFF) 위 맑은 2D 세필 수채화
"""

prompt_traffic_rules = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are a slender vertical traffic light post with signal hoods at the optical center, a small yellow school van outline balancing the left, one level crosswalk zebra marking line extending across both outer thirds, and an octagonal stop sign post balancing the right. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level road baseline. Draw the tall vertical signal pole, crossing bar and hooded lights next, keeping the combined silhouette balanced. Extend parallel zebra stripe markings equally toward the left and right outer thirds. Add a compact school van silhouette at left and a stop sign pole at right. There is no visible crowd, pedestrians, asphalt darkness, city buildings or heavy cars anywhere. Keep vehicle outline curves sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a luminous sheer emerald-green and ruby-red tint in the signal lamps, gentle sunshine-yellow on the school van, delicate soft crimson on the stop sign, and cool slate-grey on the pole. The green signal lamp gives one soft gentle glow; all zebra markings and structural lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""

clean_prompt = " ".join(prompt_traffic_rules.split())

with open("_작업/prompt_traffic_rules.txt", "w", encoding="utf-8") as f:
    f.write(clean_prompt)

import subprocess
res = subprocess.run(["python3", "_작업/verify_prompt.py", "_작업/prompt_traffic_rules.txt"], capture_output=True, text=True)
print(res.stdout)

