# -*- coding: utf-8 -*-
import os, glob

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"

print("============================================================")
print("📦 [보는 단어장] 현재 보관된 전체 영상 폴더 및 파일 전수 점검")
print("============================================================")

total_count = 0
for item in sorted(os.listdir(veo_dir)):
    full_p = os.path.join(veo_dir, item)
    if os.path.isdir(full_p):
        v_files = sorted([f for f in os.listdir(full_p) if f.endswith(".mp4")])
        cnt = len(v_files)
        total_count += cnt
        print(f"\n📁 [{item}] -> 총 {cnt}편")
        for vf in v_files[:3]:
            print(f"   - {vf}")
        if cnt > 3:
            print(f"   - ... 외 {cnt - 3}편")

print("\n============================================================")
print(f"🏆 총 보관 완료된 영상 파일 수: {total_count}편")
print("============================================================")

