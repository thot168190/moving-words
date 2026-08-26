# -*- coding: utf-8 -*-
with open("_작업/build_pure_new_sets_08_13.py", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("cross spar frame", "cross spar spar")
code = code.replace("magazine arm", "magazine lever")
code = code.replace("top pressing arm", "top pressing lever")
code = code.replace("top arm", "top lever")

with open("_작업/build_pure_new_sets_08_13.py", "w", encoding="utf-8") as f:
    f.write(code)

