# -*- coding: utf-8 -*-
with open("_작업/rebuild_all_100_scenes_atlas.py", "r", encoding="utf-8") as f:
    code = f.read()

# 템플릿 헤더 복원
code = code.replace("first structure is an entirely empty pure white field.", "first frame is an entirely empty pure white field.")
code = code.replace("The main illustration is centered and occupies the central three-quarters of the structure,", "The main illustration is centered and occupies the central three-quarters of the frame,")
code = code.replace("tubular metal frame", "tubular metal chassis")
code = code.replace("crutch frames", "crutch shafts")

with open("_작업/rebuild_all_100_scenes_atlas.py", "w", encoding="utf-8") as f:
    f.write(code)

