# -*- coding: utf-8 -*-
"""
Set 10 (일상 도구와 서재 10편) 완벽 최종 점검 및 복사
"""

import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

set10 = None
for s in data:
    if s["set_id"] == "set10":
        set10 = s
        break

print(f"=== {set10['set_name']} 10편 최종 점검 ===")
for idx, p in enumerate(set10["prompts"]):
    print(f"[{idx+1}] {p['title']} - 단어: {p['words']}")

with open("_작업/bulk_sets/set10_10.txt", "w", encoding="utf-8") as f:
    for p in set10["prompts"]:
        f.write(p["prompt"] + "\n\n")

