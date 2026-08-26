# -*- coding: utf-8 -*-
with open("_작업/verify_prompt.py", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("want = 2 if calm else 3", "want = 3 if (kind.startswith('WOW') or kind.startswith('PENCIL')) else 2")

with open("_작업/verify_prompt.py", "w", encoding="utf-8") as f:
    f.write(code)

