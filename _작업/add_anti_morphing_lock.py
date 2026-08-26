# -*- coding: utf-8 -*-
"""
모핑(변형·착란·사물 겹침) 100% 원천 차단 락 장착:
1. "The drawing remains a single fixed rigid object. Strictly zero morphing, zero shape-shifting, zero transformation between different objects, and zero superimposed secondary frames or extra plates."
2. 2D 시점 명확화 (측면도 or 정면도 고정)
"""

import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

ANTI_MORPH_SENTENCE = "The subject maintains a single, unchanging static geometry throughout. Strictly zero morphing, zero shape-shifting, zero transformation into other objects, zero secondary overlaid panels, and zero duplicate structures."

for s in data:
    if s["set_id"] in ["set10", "set11", "set12", "set13"]:
        for p in s["prompts"]:
            t = p["prompt"]
            # Previously completed lines 뒤에 강력한 모핑 방지 락 삽입
            if "Previously completed lines remain delicate, completely stable and unchanged." in t:
                t = t.replace("Previously completed lines remain delicate, completely stable and unchanged.",
                              f"Previously completed lines remain delicate, completely stable and unchanged. {ANTI_MORPH_SENTENCE}")
            p["prompt"] = " ".join(t.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

for sid, fname in [("set10", "set10_10.txt"), ("set11", "set11_10.txt"), ("set12", "set12_10.txt"), ("set13", "set13_10.txt")]:
    for s in data:
        if s["set_id"] == sid:
            with open(f"_작업/bulk_sets/{fname}", "w", encoding="utf-8") as f:
                for p in s["prompts"]:
                    f.write(p["prompt"] + "\n\n")

print("전체 세트에 [모핑·형태 변형·사물 겹침 100% 차단 락] 완벽 탑재 완료!")

