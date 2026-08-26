# -*- coding: utf-8 -*-
# 1,2,3차에서 손이 전혀 안 나왔던 진짜 프롬프트 검사

with open("_작업/google_flow_bulk_set2_10.txt", "r", encoding="utf-8") as f:
    text2 = f.read()

with open("_작업/google_flow_bulk_set3_10.txt", "r", encoding="utf-8") as f:
    text3 = f.read()

p2 = text2.split("\n\n")[0]
p3 = text3.split("\n\n")[0]

print("=== 2차 성공 프롬프트 1번 (토성) ===")
print(p2)
print("\n" + "="*50 + "\n")
print("=== 3차 성공 프롬프트 1번 (교통표지판/스쿨버스) ===")
print(p3)

