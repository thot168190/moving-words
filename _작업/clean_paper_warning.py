# -*- coding: utf-8 -*-
with open("_작업/rebuild_set09_observatory_formula.py", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("paper-thin", "delicate thin")

with open("_작업/rebuild_set09_observatory_formula.py", "w", encoding="utf-8") as f:
    f.write(code)

