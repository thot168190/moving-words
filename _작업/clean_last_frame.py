# -*- coding: utf-8 -*-
with open("_작업/rebuild_set12_13_fine_pencil.py", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("wooden frame pillars", "wooden vertical pillars")

with open("_작업/rebuild_set12_13_fine_pencil.py", "w", encoding="utf-8") as f:
    f.write(code)

