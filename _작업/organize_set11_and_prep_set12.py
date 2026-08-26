# -*- coding: utf-8 -*-
import os, shutil, glob

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"
dl_dir = "/Users/mihyunlee/Downloads"

dir_set11 = os.path.join(veo_dir, "10차완성본_Set11_주방식탁")
os.makedirs(dir_set11, exist_ok=True)

# 1. veo-folder-1 루트에 새로 들어온 영상 이동
root_files = sorted([f for f in os.listdir(veo_dir) if f.endswith(".mp4")])
print(f"veo-folder-1 루트 발견 파일 수: {len(root_files)}개")

for f in root_files:
    src = os.path.join(veo_dir, f)
    dst = os.path.join(dir_set11, f)
    shutil.move(src, dst)
    print(f"📦 [Set 11 이동] {f} -> 10차완성본_Set11_주방식탁/")

# 2. Downloads 폴더
dl_files = sorted(glob.glob(os.path.join(dl_dir, "*Progressive*.mp4")) + glob.glob(os.path.join(dl_dir, "*fine-pencil*.mp4")) + glob.glob(os.path.join(dl_dir, "*animation*.mp4")))
for f in dl_files:
    fname = os.path.basename(f)
    dst = os.path.join(dir_set11, fname)
    shutil.move(f, dst)
    print(f"📦 [Downloads에서 이동] {fname} -> 10차완성본_Set11_주방식탁/")

print("\n=== 전체 수확 보관 폴더 현황 ===")
total_videos = 0
for item in sorted(os.listdir(veo_dir)):
    p = os.path.join(veo_dir, item)
    if os.path.isdir(p):
        cnt = len([f for f in os.listdir(p) if f.endswith(".mp4")])
        total_videos += cnt
        print(f"📁 {item} : 총 {cnt}편 안전 보관 중")

print(f"\n🏆 현재까지 안전하게 수확 및 보관 완료된 총 영상 수: {total_videos}편!!")

