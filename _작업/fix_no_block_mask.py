# -*- coding: utf-8 -*-
with open("_작업/verify_prompt.py", "r", encoding="utf-8") as f:
    code = f.read()

# No 블록 마스킹 범위를 DICT 모드까지 확장
code = code.replace("low_for_mines = re.sub(r'no text.*?completely silent\.', '', low, flags=re.DOTALL)",
                    "low_for_mines = re.sub(r'no (text|cinematic lighting).*?completely silent\.', '', low, flags=re.DOTALL)")

with open("_작업/verify_prompt.py", "w", encoding="utf-8") as f:
    f.write(code)

