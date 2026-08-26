# -*- coding: utf-8 -*-
import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

for s in complete_100:
    for p in s["prompts"]:
        t = p["prompt"]
        
        # 지뢰어 hand, hands, tools 완전 제거
        t = t.replace("with no drawing tools or hands visible. ", "")
        t = t.replace("There is no visible person, human, hand, drawing implement, wall, ceiling, darkness or heavy architecture anywhere.",
                      "There is no visible person, driver, student, live action element, wall, ceiling, darkness or heavy architecture anywhere.")
        t = t.replace("hand", "manual")
        t = t.replace("hands", "manuals")
        t = t.replace("tools", "implements")
        
        p["prompt"] = " ".join(t.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_100, f, ensure_ascii=False, indent=2)

for s in complete_100:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

