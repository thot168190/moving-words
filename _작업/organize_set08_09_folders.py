# -*- coding: utf-8 -*-
import os, shutil

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"

dir_set08 = os.path.join(veo_dir, "7차완성본_Set08_사계절날씨")
dir_set09 = os.path.join(veo_dir, "8차완성본_Set09_조류곤충생태")

os.makedirs(dir_set08, exist_ok=True)
os.makedirs(dir_set09, exist_ok=True)

# Set 08: 001 ~ 010
for i in range(1, 11):
    fname = f"{str(i).zfill(3)}_Cinematic-progressive-line-reveal-animation-on-a-s.mp4"
    src = os.path.join(veo_dir, fname)
    if os.path.exists(src):
        dst = os.path.join(dir_set08, fname)
        shutil.move(src, dst)
        print(f"[Set 08] {fname} -> 7차완성본_Set08_사계절날씨/")

# Set 09: 001(1) ~ 010(1)
for i in range(1, 11):
    fname = f"{str(i).zfill(3)}_Cinematic-progressive-line-reveal-animation-on-a-s (1).mp4"
    src = os.path.join(veo_dir, fname)
    if os.path.exists(src):
        dst_name = f"{str(i).zfill(3)}_Cinematic-progressive-line-reveal-animation-on-a-s.mp4"
        dst = os.path.join(dir_set09, dst_name)
        shutil.move(src, dst)
        print(f"[Set 09] {fname} -> 8차완성본_Set09_조류곤충생태/{dst_name}")

print("\n=== 전체 수확 보관 폴더 현황 ===")
for item in sorted(os.listdir(veo_dir)):
    p = os.path.join(veo_dir, item)
    if os.path.isdir(p):
        cnt = len([f for f in os.listdir(p) if f.endswith(".mp4")])
        print(f"📁 {item} : 총 {cnt}편 안전 보관 중")

