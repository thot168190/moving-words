# -*- coding: utf-8 -*-
"""
잉크(Ink/Engraving) 퇴출 -> 맑고 부드러운 [연필(Graphite pencil sketch)] 정본으로 100% 전면 교체!
"""

import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for s in data:
    for p in s["prompts"]:
        t = p["prompt"]
        
        # 1. 0-5.5s 선화 정의: 잉크/다크차콜 -> 맑은 연필(Graphite pencil)
        t = t.replace("hair-thin dark-charcoal linework appears progressively from the empty white field.",
                      "delicate fine graphite pencil linework appears progressively from the empty white field.")
        t = t.replace("fine dark-charcoal linework appears progressively from the empty white field.",
                      "delicate fine graphite pencil linework appears progressively from the empty white field.")
        t = t.replace("ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks.",
                      "delicate fine graphite pencil linework appears progressively from the empty white field. Every outline is soft and thin, drawn in pure pencil graphite.")

        # 2. 스타일 정의: 판화/잉크(engraving) -> 연필 스케치(delicate graphite pencil sketch)
        t = t.replace("Style: delicate fine-line engraving,", "Style: delicate graphite pencil sketch,")
        t = t.replace("fine-line engraving,", "delicate graphite pencil sketch,")
        
        p["prompt"] = " ".join(t.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

for s in data:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("잉크 전면 퇴출 -> [맑은 연필(Graphite Pencil) 스케치] 정본 교체 완료!")

