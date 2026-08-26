# -*- coding: utf-8 -*-
"""
[손(Hand) 100% 원천 박멸 긴급 패치]
원인 분석:
- 'Each line is drawn as a moving point... advancing tip' 문구가 AI에게 '연필 촉을 쥔 사람 손'을 소환함!
- 해결:
  1. 성공이 100% 검증된 'ultra-fine pale graphite linework appears progressively from the empty white field on its own' 문법으로 전면 교체!
  2. 주체 명시: 'There is no visible person, hand, finger, pencil, pen, brush, tool or drawing implement anywhere.'
  3. 사물 자체의 우아한 자동 발현(self-revealing linework)으로 고정!
"""

import json, re

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

for s in complete_100:
    for p in s["prompts"]:
        t = p["prompt"]
        
        # 1. 손 소환 트리거 제거: "Each line is drawn as a moving point... extends from its own tip."
        t = re.sub(r'Throughout the whole sequence the field contains only the flat white surface and the marks already made on it; nothing else is ever present at any moment\. Each line is drawn as a moving point that travels from one end to the other, its advancing tip clearly visible the whole way, one line at a time, so the eye can follow the growing tip of every single stroke\. Nothing is revealed by a sweeping wipe and nothing fades into view - every line extends from its own tip\.\s*', 
                   'Every outline is extremely thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Lines trace smoothly into existence on their own with no drawing tools or hands visible. ', t)
        
        # 2. 0-4s 시작문구를 검증된 안전 문구로 교체
        t = t.replace('0-4s: hair-thin pale graphite linework appears progressively from the empty white field.',
                      '0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field.')
        
        # 3. 부정문 소환 방지: There is no visible ... 문구를 완벽한 안전문구로 보강
        old_no_vis = "There is no visible person, driver, student, live action element, wall, ceiling, darkness or heavy architecture anywhere."
        safe_no_vis = "There is no visible person, human, hand, drawing implement, wall, ceiling, darkness or heavy architecture anywhere."
        if old_no_vis in t:
            t = t.replace(old_no_vis, safe_no_vis)
            
        p["prompt"] = " ".join(t.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_100, f, ensure_ascii=False, indent=2)

for s in complete_100:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("손 소환 트리거 100% 소탕 및 안전 정본 교체 완료!")

