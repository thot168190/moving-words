# -*- coding: utf-8 -*-
import os, glob, re

base_dir = "public/learning"
chapters = ["ch2", "ch4", "ch5", "ch6", "ch10", "ch11", "ch12"]

print("=== 기존 챕터별 동영상 현황 및 마지막 번호 조사 ===")
for ch in chapters:
    ch_dir = os.path.join(base_dir, ch)
    if not os.path.exists(ch_dir):
        os.makedirs(ch_dir, exist_ok=True)
    files = [f for f in os.listdir(ch_dir) if f.endswith(".mp4") and not f.startswith(".")]
    # 번호 추출
    nums = []
    for f in files:
        m = re.search(rf"{ch}_(\d+)\.mp4", f)
        if m:
            nums.append(int(m.group(1)))
    max_num = max(nums) if nums else 0
    print(f"📁 {ch} : 현재 {len(files)}편 존재 (마지막 번호: {max_num}) -> 신규 배정 시작 번호: {max_num + 1}")

