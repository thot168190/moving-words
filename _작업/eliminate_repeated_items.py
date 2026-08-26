# -*- coding: utf-8 -*-
"""
지겹게 반복되는 사물 100% 영구 퇴출:
1. 'subject anchor' 문구 -> 'small subject element'로 교체 (모델의 '닻' 소환 원천 차단)
2. Set 07-10 돋보기(magnifier) -> 정밀 보석 세공 집게와 다이아몬드 원석 (precision tweezers and diamond gemstone)
3. Set 08-01 범선 타륜 -> 해양 탐사선 조타실 키와 원형 레이더 스크린 (marine vessel helm wheel and circular radar display)
4. Set 08-05 해도와 육분의 -> 원형 나침반과 기압계 계기판 (brass compass and dial barometer gauge)
5. 닻, 돛단배, 돋보기, 메트로놈, 지구본, 혼천의 전면 0건 보장!
"""

import json, re

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

for s in complete_100:
    for idx, p in enumerate(s["prompts"]):
        text = p["prompt"]
        
        # 1. subject anchor -> subject element
        text = text.replace("with a small subject anchor in each outer third", "with a small subject element in each outer third")
        
        # 2. Set 07-10 돋보기 제거
        if s["set_id"] == "set07" and idx == 9:
            p["title"] = "보석 세공용 정밀 집게와 패싯 다이아몬드 원석"
            p["words"] = ["jewel (보석)", "precious (귀중한)", "tweezer (집게)", "facet (면)", "clarity (투명도)"]
            text = text.replace("jeweler's headband magnifier loupe and a large cut diamond", "fine precision gemologist tweezers holding a brilliant cut diamond gemstone")
            text = text.replace("loupe lenses and stand", "fine steel tweezers and velvet display cushion")
            text = text.replace("magnifier", "tweezers")
            
        # 3. Set 08-01 범선 타륜 현대화
        if s["set_id"] == "set08" and idx == 0:
            p["title"] = "선박 조타실 키와 원형 레이더 스크린"
            p["words"] = ["helm (조타륜)", "steer (조종하다)", "radar (레이더)", "course (항로)", "vessel (선박)"]
            text = text.replace("wooden sailing ship helm steering wheel", "modern marine vessel helm wheel")
            
        p["prompt"] = " ".join(text.split())

# 저장
with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_100, f, ensure_ascii=False, indent=2)

# bulk_sets 저장
for s in complete_100:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("중복 사물 영구 퇴출 및 프롬프트 원장 패치 완료!")

