# -*- coding: utf-8 -*-
with open("_작업/rebuild_set11_locked_wow_formula.py", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("There is no visible person, hands or kitchen background.", "There is no visible person, chef or room interior boundary.")
code = code.replace("cream", "warm-ivory")

with open("_작업/rebuild_set11_locked_wow_formula.py", "w", encoding="utf-8") as f:
    f.write(code)

