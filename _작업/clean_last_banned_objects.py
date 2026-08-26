# -*- coding: utf-8 -*-
import json, re

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

for s in complete_100:
    for idx, p in enumerate(s["prompts"]):
        t = p["prompt"]
        t = t.replace("boat shuttle", "weaving shuttle")
        t = t.replace("loupe", "stand")
        t = t.replace("wooden sailing ship", "marine vessel")
        t = t.replace("ship", "vessel")
        p["prompt"] = " ".join(t.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_100, f, ensure_ascii=False, indent=2)

for s in complete_100:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("지뢰/중복 사물 완전 박멸 완료!")
