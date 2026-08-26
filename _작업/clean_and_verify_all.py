# -*- coding: utf-8 -*-
import json, re

with open("_작업/build_complete_100_prompts.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. 템플릿의 지뢰어(hand, tool) 제거
code = code.replace("There is no visible person, human hand, drawing tool, wall, ceiling, darkness or heavy architecture anywhere.", "There is no visible person, driver, student, live action element, wall, ceiling, darkness or heavy architecture anywhere.")

# 2. 설명문 내 지뢰어/금지어 교체
replacements = {
    "canvas": "cotton fabric",
    "handheld": "compact",
    "hand-crank": "crank-driven",
    "hand-tension": "high-tension",
    "hand-plane": "block plane",
    "hand block plane": "block plane",
    "handloom": "tabletop loom",
    "finger": "optical",
    "arm cuff": "pressure sleeve",
    "arm ": "sleeve ",
    "underarm": "support",
    "desk": "counter",
    "paper": "document sheet",
    "parchment": "scroll document",
    "artist": "creator",
    "multi-tool": "multi-blade knife",
    "drawing tools": "drawing items",
    "tools": "accessories",
    "tool": "device",
    "hand": "manual"
}

for k, v in replacements.items():
    code = re.sub(r'\b' + re.escape(k) + r'\b', v, code, flags=re.IGNORECASE)

with open("_작업/build_complete_100_prompts.py", "w", encoding="utf-8") as f:
    f.write(code)

