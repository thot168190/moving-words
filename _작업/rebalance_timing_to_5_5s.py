# -*- coding: utf-8 -*-
"""
시간 배분 황금 비율 전면 적용:
- 0-5.5s (70%): 선화가 뼈대부터 세부 디테일까지 끝까지 여유롭고 완벽하게 그려짐!
- 5.5-8s (30%): 마지막 2.5초 동안만 맑은 수채화 틴트 번짐 + 잔잔한 1회 미세 모션으로 3D 실사화 원천 차단!
"""

import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for s in data:
    for p in s["prompts"]:
        t = p["prompt"]
        t = t.replace("0-4s:", "0-5.5s:")
        t = t.replace("4-8s:", "5.5-8s:")
        p["prompt"] = " ".join(t.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

for s in data:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("시간 배분 0-5.5s / 5.5-8s 황금 비율 전면 적용 완료!")

