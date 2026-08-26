# -*- coding: utf-8 -*-
import glob

# 1,2,3차 성공했던 검증된 정본 프롬프트 확인
with open("_작업/google_flow_bulk_set2_10.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("=== 2차 성공본 프롬프트 헤더 및 0-4s ===")
lines = text.split("\n")
for l in lines[:10]:
    print(l)

