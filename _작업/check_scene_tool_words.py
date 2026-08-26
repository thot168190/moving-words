# -*- coding: utf-8 -*-
with open("_작업/scene_tool.py", "r", encoding="utf-8") as f:
    text = f.read()

print("scene_tool.py 단어 파싱 로직 확인:")
for line in text.split("\n")[:40]:
    print(line)

