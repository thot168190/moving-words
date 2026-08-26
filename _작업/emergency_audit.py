# -*- coding: utf-8 -*-
import os, glob, json, subprocess

print("=== 1. Git Status 및 기존 파일 변경 여부 확인 ===")
res = subprocess.run(["git", "status", "--short", "public/learning/"], capture_output=True, text=True)
print(res.stdout)

print("\n=== 2. 각 챕터 폴더별 실제 파일 전수 조사 ===")
base = "public/learning"
for ch in ["ch1", "ch2", "ch3", "ch4", "ch5", "ch6", "ch7", "ch8", "ch9", "ch10", "ch11", "ch12", "ch13", "ch14", "ch15"]:
    p = os.path.join(base, ch)
    if os.path.exists(p):
        mp4s = sorted([f for f in os.listdir(p) if f.endswith(".mp4")])
        jpgs = sorted([f for f in os.listdir(p) if f.endswith(".jpg") or f.endswith(".png")])
        print(f"📁 {ch} : mp4 {len(mp4s)}개 / 이미지 {len(jpgs)}개")
        print(f"   mp4 목록: {mp4s}")

print("\n=== 3. chapterData 내 기존 등록된 video 경로 분석 ===")
with open("public/learning/index.html", "r", encoding="utf-8") as f:
    html = f.read()

i = html.index("const chapterData = {"); st = html.index("{", i); d = 0
for j in range(st, len(html)):
    if html[j] == "{": d += 1
    elif html[j] == "}":
        d -= 1
        if d == 0: en = j + 1; break

cdata = json.loads(html[st:en])
for ch_id, ch_val in cdata.items():
    works = ch_val.get("works", [])
    print(f"chapterData ch{ch_id}: {len(works)}개 작품")
    for w in works:
        vpath = w.get("video", "")
        real_exists = os.path.exists(os.path.join("public/learning", vpath.split("?")[0]))
        if not real_exists:
            print(f"   ❌ [파일 없음 경고] ch{ch_id}-{w['n']}: {vpath}")

