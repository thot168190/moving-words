# -*- coding: utf-8 -*-
with open("_작업/verify_prompt.py", "r", encoding="utf-8") as f:
    code = f.read()

# hand-drawn은 지뢰어가 아니므로 마스킹
code = code.replace("low_for_mines = re.sub(r'no text.*?completely silent\.', '', low, flags=re.DOTALL)",
                    "low_for_mines = re.sub(r'no text.*?completely silent\.', '', low, flags=re.DOTALL)\n    low_for_mines = low_for_mines.replace('hand-drawn', 'fine-drawn')")

with open("_작업/verify_prompt.py", "w", encoding="utf-8") as f:
    f.write(code)

