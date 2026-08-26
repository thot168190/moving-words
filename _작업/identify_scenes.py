# -*- coding: utf-8 -*-
# 프롬프트 목록과 대조
import json
with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Set 11 (주방) 목록:")
for idx, p in enumerate(data[7]["prompts"]):
    print(f"[{str(idx+1).zfill(3)}] {p['title']}")

print("\nSet 12 (악기) 목록:")
for idx, p in enumerate(data[8]["prompts"]):
    print(f"[{str(idx+1).zfill(3)}] {p['title']}")

print("\nSet 13 (사회) 목록:")
for idx, p in enumerate(data[9]["prompts"]):
    print(f"[{str(idx+1).zfill(3)}] {p['title']}")
