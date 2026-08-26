# -*- coding: utf-8 -*-
with open("_작업/verify_prompt.py", "r", encoding="utf-8") as f:
    code = f.read()

# 'fountain pen' 또는 'fountain-pen'은 정당한 주인공 명사이므로 검사 시 마스킹
code = code.replace("low_for_mines = low_for_mines.replace('hand-drawn', 'fine-drawn')",
                    "low_for_mines = low_for_mines.replace('hand-drawn', 'fine-drawn')\n    low_for_mines = low_for_mines.replace('fountain pen', 'fountain instrument').replace('fountain-pen', 'fountain-instrument')")

with open("_작업/verify_prompt.py", "w", encoding="utf-8") as f:
    f.write(code)

