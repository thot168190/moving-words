# -*- coding: utf-8 -*-
"""
대표님의 최고 정본 [성인 자연사 도감 (Beetle Atlas)] 헌법을 허브 전체 100편(Set 04 ~ Set 13)에 일괄 적용!
"""

import json, re

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

for s in complete_100:
    for idx, p in enumerate(s["prompts"]):
        t = p["prompt"]
        
        # 1. 헤더: 순백 패널 금지 문구
        if "The background is one single continuous field of pure white" not in t:
            t = re.sub(r'^(Cinematic|Delicate).*?The main illustration',
                       'Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. The background is one single continuous field of pure white reaching every outer edge, and the subjects sit directly on that white with nothing underneath them - no board, no panel, no card, no mat, no textured surface and no visible edge of any kind. High-key lighting. The main illustration', t)
            
        # 2. 0-4s 선단 진행 문구
        if "advancing tip clearly visible" not in t:
            t = re.sub(r'0-4s:.*?(Begin with|Draw the|The clean|The low|The outer|The slender|The circular|The twin|The round|The segmented|The simple)',
                       '0-4s: hair-thin pale graphite linework appears progressively from the empty white field. Throughout the whole sequence the field contains only the flat white surface and the marks already made on it; nothing else is ever present at any moment. Each line is drawn as a moving point that travels from one end to the other, its advancing tip clearly visible the whole way, one line at a time, so the eye can follow the growing tip of every single stroke. Nothing is revealed by a sweeping wipe and nothing fades into view - every line extends from its own tip. \\1', t)
            
        # 3. 0-4s 마무리: 내부 비움 락
        if "strictly zero cross-hatching and zero line shading" not in t:
            t = t.replace("Every detail becomes visible sequentially", 
                          "Most of each form stays deliberately economical and free of internal lines, with strictly zero cross-hatching and zero line shading. Every detail becomes visible sequentially")
            
        # 4. 스타일 꼬리: 성인 자연사 도감 박물관급
        atlas_tail = "The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, precise pale graphite strokes and sophisticated control, maximum line value 20% grey, luminous transparent watercolor, restrained tonal contrast, generous untouched white space, sophisticated museum-quality editorial illustration for an adult natural-history atlas, mature and understated, with hairline strokes and no heavy outlines anywhere."
        
        t = re.sub(r'The final composition remains centered.*$', atlas_tail, t)
        if "natural-history atlas" not in t:
            t = re.sub(r'Style:.*$', atlas_tail, t)
            
        # 5. 금지어/지뢰어 최종 소탕
        t = t.replace("reaching every edge of the frame", "reaching every outer edge")
        t = t.replace("the canvas contains only", "the field contains only")
        t = t.replace("the frame contains only", "the field contains only")
        t = t.replace("spreading", "extending")
        t = t.replace("canvas", "cotton fabric")
        t = t.replace("cream", "warm-white")
        
        p["prompt"] = " ".join(t.split())

# 저장
with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_100, f, ensure_ascii=False, indent=2)

for s in complete_100:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("허브 100편 전체 [자연사 도감] 헌법 일괄 업그레이드 완료!")

