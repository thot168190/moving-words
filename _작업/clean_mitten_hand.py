# -*- coding: utf-8 -*-
import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for s in data:
    for p in s["prompts"]:
        p["prompt"] = p["prompt"].replace("hand pockets", "mitten pockets")
        p["prompt"] = p["prompt"].replace("hand fan", "cooling fan")
        p["prompt"] = p["prompt"].replace("hand ", "manual ")

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

for s in data:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

