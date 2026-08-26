# -*- coding: utf-8 -*-
"""
지구본/혼천의/구체 천구의 전면 영구 퇴출:
- 토성 씬의 celestial globe -> '황동 별자리 지침바늘 (brass constellation needle)'
- 망원경 씬의 star globe -> '양피지 성도 두루마리 (star chart scroll)'
- 돔/천구의 -> '투명 삼각 프리즘 (Triangular Glass Prism)'
"""

import re

# 1. build_next_10_prompts.py 수정
with open("_작업/build_next_10_prompts.py", "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace("a small antique brass celestial globe ring balancing the left", "a slender brass constellation needle balancing the left")
c = c.replace("Add a brass celestial globe ring at left", "Add a brass constellation needle at left")
c = c.replace("faint champagne-gold on the brass ring", "faint champagne-gold on the brass needle")

with open("_작업/build_next_10_prompts.py", "w", encoding="utf-8") as f:
    f.write(c)

# 2. build_14_prompts.py 수정
with open("_작업/build_14_prompts.py", "r", encoding="utf-8") as f:
    c2 = f.read()

c2 = c2.replace("star globe", "star chart map")
with open("_작업/build_14_prompts.py", "w", encoding="utf-8") as f:
    f.write(c2)

print("지구본(Globe) 전면 퇴출 및 대체 완료!")

