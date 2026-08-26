# -*- coding: utf-8 -*-
with open("public/learning/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 기존에 대성공했던 스쿨버스, 딱정벌레 등 프롬프트가 보관된 파일들 확인
import glob
for f in sorted(glob.glob("_작업/*.txt") + glob.glob("_작업/*.json")):
    print(f)

