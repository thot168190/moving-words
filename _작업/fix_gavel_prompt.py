# -*- coding: utf-8 -*-
"""
법정 의사봉 & 저울 단편 정밀 보정 (헬리콥터 황금 문법 100% 적용)
- 탁자/벤치 가구 덩어리 100% 제거
- 배경 갈색 얼룩 100% 차단 -> 순백(#FFFFFF) 100% 락
- 맑고 가벼운 세필 일러스트 + 투명 틴트
"""

prompt_gavel_fixed = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are a turned-hardwood gavel resting on a small round sound block at the optical center, a delicate brass balance scale balancing the left, one thin level ground line extending across both outer thirds, and an antique leather book balancing the right. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level minimal ground line. Draw the central wooden gavel handle, head and round striking block next, keeping the combined silhouette horizontal rather than diagonal. Extend a single thin ground line equally toward the left and right outer thirds. Add a brass scale at left and an upright slim book at right. There is no visible furniture, heavy table, wooden bench, courtroom, wall or person anywhere. Keep woodgrain curves sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is an airy light honey-amber on the wooden gavel, sheer champagne-gold on the brass scale, and delicate soft terracotta on the book spine. The entire surrounding background remains untouched pure bright white #FFFFFF with zero background wash, zero stains and zero bleeding. A tiny golden glint sparkles softly once on the sound block; all structural linework remains crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""

clean_prompt = " ".join(prompt_gavel_fixed.split())

with open("_작업/prompt_gavel_fixed.txt", "w", encoding="utf-8") as f:
    f.write(clean_prompt)

import subprocess
res = subprocess.run(["python3", "_작업/verify_prompt.py", "_작업/prompt_gavel_fixed.txt"], capture_output=True, text=True)
print(res.stdout)

