# -*- coding: utf-8 -*-
"""
대표님이 주신 황금 정본(새벽 시골길 씬)의 색감/선화 문법을 100편 전체에 1:1 완벽 이식:
1. 선화:
   "ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks."
2. 채색:
   "4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues."
3. 꼬리:
   "Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration, generous untouched white space. No text, labels, borders, panels, drawing items or visible creator. Completely silent."
"""

import json, re

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

for s in complete_100:
    for idx, p in enumerate(s["prompts"]):
        t = p["prompt"]
        
        # 1. 헤더 복원
        t = re.sub(r'^(Delicate|Cinematic).*?High-key lighting\.', 
                   'Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting.', t)
        
        # 2. 0-4s 선화 문법을 정본 황금문구로 교체
        t = re.sub(r'0-4s:.*?(Begin with|Draw the)', 
                   '0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. \\1', t)
        
        # 3. 4-8s 채색 문법을 정본 황금문구로 교체
        # 기존 채색 문맥 유지하면서 황금 규칙 적용
        t = re.sub(r'4-8s:.*?(The restrained palette is|Use distinct)', 
                   '4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. \\1', t)
        
        # 4. 스타일 꼬리를 정본 황금문구로 교체
        golden_tail = "The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration, generous untouched white space. No text, labels, borders, panels, drawing items or visible creator. Completely silent."
        
        t = re.sub(r'The final composition remains centered.*$', golden_tail, t)
        if "Style:" not in t:
            t += " " + golden_tail
            
        p["prompt"] = " ".join(t.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_100, f, ensure_ascii=False, indent=2)

for s in complete_100:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("새벽 시골길 황금 정본 문법 100편 전체 100% 이식 완료!")
