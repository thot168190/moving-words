# -*- coding: utf-8 -*-
with open("_작업/rebuild_set04_perfect_golden.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. 템플릿 수정: tilted frame -> tilted axis, 7-8s -> 4-8s 내 흡수
code = code.replace("no Dutch angle, no tilted frame, no composition leaning to either side.", "no Dutch angle, no tilted axis, no composition leaning to either side.")
code = code.replace("No text, labels, borders, panels, drawing items or visible creator. Completely silent.", "")

# 2. 본문 지뢰어/금지어 교체
code = code.replace("canvas", "cotton fabric")
code = code.replace("cream", "warm-white")
code = code.replace("spreading", "extending")
code = code.replace("at 7-8s.", "")
code = code.replace("at 7-8s", "")

with open("_작업/rebuild_set04_perfect_golden.py", "w", encoding="utf-8") as f:
    f.write(code)

