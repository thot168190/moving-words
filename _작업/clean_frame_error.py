# -*- coding: utf-8 -*-
with open("_작업/perfect_beetle_atlas_clean.py", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("the canvas contains only", "the field contains only")

with open("_작업/perfect_beetle_atlas_clean.py", "w", encoding="utf-8") as f:
    f.write(code)

