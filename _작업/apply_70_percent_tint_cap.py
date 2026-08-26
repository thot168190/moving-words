# -*- coding: utf-8 -*-
"""
대표님의 신의 한 수 감리 반영:
"색감이 70% 찼을 때까지면 딱이겠는데 100% 가면 실사가 나와"
-> 4-8s 채색을 60-70% 반투명 틴트(water-heavy tint)에서 멈추도록 엄격한 상한선(Cap) 장착!
"""

import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for s in data:
    for p in s["prompts"]:
        t = p["prompt"]
        
        # 4-8s 문장을 70% 틴트 캡으로 정밀 강화
        old_4_8 = "4-8s: an extremely pale, water-heavy watercolor wash develops gently."
        new_4_8 = "4-8s: an extremely pale, water-heavy watercolor wash develops gently, settling at a delicate 65% translucent tint where the pure white background remains luminous through every wash."
        
        if old_4_8 in t:
            t = t.replace(old_4_8, new_4_8)
            
        old_fill = "No area becomes dark, dense or fully filled."
        new_fill = "No area becomes dark, dense or fully filled; color never reaches 100% opaque saturation, preserving the delicate 2D picture-book line art aesthetic throughout."
        if old_fill in t:
            t = t.replace(old_fill, new_fill)
            
        p["prompt"] = " ".join(t.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

for s in data:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("허브 전체 [65~70% 투명 틴트 캡 락] 장착 완료!")

