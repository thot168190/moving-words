# -*- coding: utf-8 -*-
"""
다운로드된 영상들을 완벽하고 안전하게 세트별 폴더로 정리!
"""

import os, shutil, glob

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"

# 1. 5차완성본_Set06_정원원예 폴더 생성
dir_set06 = os.path.join(veo_dir, "5차완성본_Set06_정원원예")
os.makedirs(dir_set06, exist_ok=True)

# 2. 6차완성본_Set07_미술공예 폴더 생성
dir_set07 = os.path.join(veo_dir, "6차완성본_Set07_미술공예")
os.makedirs(dir_set07, exist_ok=True)

# 루트 파일 분류
# 15:51~15:57 (Set 06): 파일명에 (1)이 없는 순수 001~010
for i in range(1, 11):
    f_name = f"{str(i).zfill(3)}_Cinematic-progressive-line-reveal-animation-on-a-s.mp4"
    src = os.path.join(veo_dir, f_name)
    if os.path.exists(src):
        dst = os.path.join(dir_set06, f_name)
        shutil.move(src, dst)
        print(f"[Set 06 이동] {f_name} -> 5차완성본_Set06_정원원예/")

# 16:01~16:07 (Set 07): 파일명에 (1)이 붙은 001~010
for i in range(1, 11):
    f_name = f"{str(i).zfill(3)}_Cinematic-progressive-line-reveal-animation-on-a-s (1).mp4"
    src = os.path.join(veo_dir, f_name)
    if os.path.exists(src):
        dst_name = f"{str(i).zfill(3)}_Cinematic-progressive-line-reveal-animation-on-a-s.mp4"
        dst = os.path.join(dir_set07, dst_name)
        shutil.move(src, dst)
        print(f"[Set 07 이동] {f_name} -> 6차완성본_Set07_미술공예/{dst_name}")

print("\n=== 세트별 수확 폴더 정리 완료 ===")
for folder in sorted(os.listdir(veo_dir)):
    p = os.path.join(veo_dir, folder)
    if os.path.isdir(p):
        cnt = len([f for f in os.listdir(p) if f.endswith(".mp4")])
        print(f"📁 {folder} : 총 {cnt}편 보관 중")

