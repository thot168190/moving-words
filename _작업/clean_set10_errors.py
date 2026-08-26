# -*- coding: utf-8 -*-
with open("_작업/rebuild_set10_telescope_pure.py", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("from an empty white field", "from the empty white field")
code = code.replace("finger grip grooves", "ridged grip grooves")

with open("_작업/rebuild_set10_telescope_pure.py", "w", encoding="utf-8") as f:
    f.write(code)

