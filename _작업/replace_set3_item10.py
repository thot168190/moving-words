# -*- coding: utf-8 -*-
"""
10번 씬 교체: 실사/어두운 돔 위험 100% 제거 -> 맑고 투명한 '유리 프리즘과 무지개 스펙트럼(Prism & Rainbow Optics)'
- lens, degree, chart, observe, beam
"""

new_prompt_10 = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are a triangular optical glass prism dispersing a soft rainbow light beam at the optical center, a slender brass circular degree protractor balancing the left, one delicate level workbench line extending across both outer thirds, and a color spectrum chart strip balancing the right. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level minimal baseline. Draw the geometric triangular glass prism facet and refractive light path next, keeping the combined silhouette balanced. Extend a single thin baseline equally toward the left and right outer thirds. Add a brass degree angle protractor at left and a small spectrum scale strip at right. There is no visible room, wall, scientist, dark night or heavy telescope anywhere. Keep glass reflection lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a sheer translucent whisper of pastel rainbow red, yellow, cyan and violet across the dispersed light beam, airy watery-aqua on the glass prism, pale champagne-gold on the brass protractor, and delicate ivory on the scale strip. A tiny luminous glint sparkles softly once along the prism apex; all structural linework remains crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""

import json

# SET3_PROMPTS의 10번째 항목 수정
from build_set3_prompts import SET3_PROMPTS
SET3_PROMPTS[9] = {
    "id": "set3-10",
    "chapter": "New Chapter (OPTICA)",
    "title": "투명 삼각 프리즘과 무지개 분광 스펙트럼",
    "words": ["lens (렌즈·광학)", "degree (각도·도)", "chart (도표·스펙트럼)", "observe (관측하다)", "beam (빛줄기)"],
    "prompt": new_prompt_10
}

# 1. 텍스트 파일 갱신
with open("_작업/google_flow_bulk_next10.txt", "w", encoding="utf-8") as f:
    for p in SET3_PROMPTS:
        clean_line = " ".join(p["prompt"].split())
        f.write(clean_line + "\n\n")

# 2. 통합 허브 재빌드
import build_master_hub

print("10번 씬 프리즘 광학 씬으로 교체 및 허브 갱신 완료!")
