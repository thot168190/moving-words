# -*- coding: utf-8 -*-
"""
대표님 지적 즉시 반영: 백팩(backpack) 100편 전체 전수 퇴출!
- Set 04-01: '삼각 텐트와 백팩' -> '캠핑 삼각 타프 텐트와 우드 롤테이블, 접이식 캠핑 체어' (Camping tarp tent, wood roll-top table, compact folding chair)
- 100편 전체에서 backpack / rucksack 완전 제거!
"""

import json, re

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

for s in complete_100:
    for idx, p in enumerate(s["prompts"]):
        t = p["prompt"]
        if "backpack" in t.lower() or "rucksack" in t.lower() or "배낭" in p["title"]:
            print(f"백팩 발견: [{s['set_id']} - {idx+1}번] '{p['title']}'")
            
            # Set 04-01 교체
            if s["set_id"] == "set04" and idx == 0:
                p["title"] = "삼각 캠핑 텐트와 우드 롤테이블, 접이식 의자"
                p["words"] = ["tent (텐트)", "camp (캠프)", "chair (의자)", "table (테이블)", "shelter (쉼터)"]
                t = t.replace("canvas triangle camping tent, a rugged outdoor backpack", "triangle camping tent, a low wood roll-top table and a compact folding canvas camp chair")
                t = t.replace("backpack, stainless steel thermos", "wood table, canvas folding chair and insulated metal thermos")
                t = t.replace("backpack", "folding chair")
            
            # 기타 백팩 교체
            t = re.sub(r'\bbackpack\b', 'travel pouch', t, flags=re.IGNORECASE)
            t = re.sub(r'\brucksack\b', 'duffel bag', t, flags=re.IGNORECASE)
            p["prompt"] = " ".join(t.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_100, f, ensure_ascii=False, indent=2)

for s in complete_100:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("백팩 완전 퇴출 및 100편 프롬프트 패치 완료!")
