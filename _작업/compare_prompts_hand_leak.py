# -*- coding: utf-8 -*-
"""
1,2,3차 손 0% 성공작 vs 현재 Set 04 프롬프트 정밀 diff 분석
"""

# 1. 2차 성공작 (손 0% 완벽 통과본)
with open("_작업/google_flow_bulk_set2_10.txt", "r", encoding="utf-8") as f:
    set2_text = f.read()

# 2. 현재 Set 04
with open("_작업/bulk_sets/set04_10.txt", "r", encoding="utf-8") as f:
    set4_text = f.read()

import json
print("=== 2차 성공작 (손 0%) 샘플 1편 ===")
print(set2_text.split("\n\n")[0])

print("\n" + "="*50 + "\n")

print("=== 현재 Set 04 샘플 1편 ===")
print(set4_text.split("\n\n")[0])

