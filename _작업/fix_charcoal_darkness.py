# -*- coding: utf-8 -*-
"""
대표님 헌법: '먹물/목탄 짙은 명암(dark charcoal) 100% 영구 퇴출'
1. hair-thin dark-charcoal -> hair-thin soft warm-grey
2. 배경 수채화 얼룩(background stain) 원천 금지: strictly zero background wash or stain
3. 짙은 흑색/금속 명암 방지: all lines remain soft pale warm-grey (max 20% grey), no dense black masses
"""

import json, re

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

for s in complete_100:
    for idx, p in enumerate(s["prompts"]):
        t = p["prompt"]
        
        # 1. dark-charcoal -> soft warm-grey
        t = t.replace("hair-thin dark-charcoal linework", "hair-thin soft warm-grey linework")
        t = t.replace("dark-charcoal", "soft warm-grey")
        
        # 2. 배경 얼룩 방지 및 맑은 화사함 보강
        if "strictly zero color wash" not in t and "strictly zero watercolor wash" not in t:
            t = t.replace("4-8s: an extremely pale, water-heavy watercolor wash develops gently.", 
                          "4-8s: an extremely pale, water-heavy watercolor wash develops gently. There is strictly zero watercolor wash or stain on the background; 90% of the frame remains untouched pure white #FFFFFF.")
        
        p["prompt"] = " ".join(t.split())

# 저장
with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_100, f, ensure_ascii=False, indent=2)

for s in complete_100:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("먹물 톤다운 전면 제거 및 맑은 소프트 웜그레이로 100편 전체 복원 완료!")

