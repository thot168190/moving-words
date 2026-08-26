# -*- coding: utf-8 -*-
with open("_작업/rebuild_set12_13_fine_pencil.py", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("desk tray plate", "sheet music tray plate")
code = code.replace("desk tray surface", "sheet music tray surface")
code = code.replace("pointer arm", "pointer indicator")
code = code.replace("cast frame", "cast base")
code = code.replace("wooden cart frame", "wooden cart structure")

with open("_작업/rebuild_set12_13_fine_pencil.py", "w", encoding="utf-8") as f:
    f.write(code)

