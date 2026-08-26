# -*- coding: utf-8 -*-
with open("_작업/rebuild_all_100_scenes_atlas.py", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("String(idx+1).zfill(2) if hasattr(str, 'zfill') else str(idx+1).zfill(2)", "str(idx+1).zfill(2)")

with open("_작업/rebuild_all_100_scenes_atlas.py", "w", encoding="utf-8") as f:
    f.write(code)

