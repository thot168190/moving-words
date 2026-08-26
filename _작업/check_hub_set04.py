# -*- coding: utf-8 -*-
with open("_작업/제작허브.html", "r", encoding="utf-8") as f:
    c = f.read()

import re
matches = re.findall(r'"title":\s*"([^"]+)"', c)
print(f"허브 내 등록된 타이틀 총 {len(matches)}개:")
for m in matches[:15]:
    print(" -", m)

