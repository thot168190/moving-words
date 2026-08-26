# -*- coding: utf-8 -*-
import json
with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for s in data:
    if s["set_id"] == "set04":
        print("=== 현재 Set 04 (09번 오두막 씬) 프롬프트 원문 ===")
        print(s["prompts"][8]["prompt"])
        print("\n=== 현재 Set 04 전체 10편 벌크 ===")
        for idx, p in enumerate(s["prompts"]):
            print(f"[{idx+1}번] {p['title']}")
