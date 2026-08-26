# -*- coding: utf-8 -*-
with open("_작업/build_set11_calm_pure_2d.py", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("Progressive line-reveal animation", "Cinematic progressive line-reveal animation")

with open("_작업/build_set11_calm_pure_2d.py", "w", encoding="utf-8") as f:
    f.write(code)

