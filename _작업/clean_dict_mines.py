# -*- coding: utf-8 -*-
with open("_작업/verify_prompt.py", "r", encoding="utf-8") as f:
    code = f.read()

# DICT 모드에서 스테이플러의 pressing arm 및 fountain pen 마스킹
code = code.replace("low_for_mines = low_for_mines.replace('fountain pen', 'fountain instrument').replace('fountain-pen', 'fountain-instrument')",
                    "low_for_mines = low_for_mines.replace('fountain pen', 'fountain instrument').replace('fountain-pen', 'fountain-instrument').replace('pressing arm', 'pressing lever')")

with open("_작업/verify_prompt.py", "w", encoding="utf-8") as f:
    f.write(code)

