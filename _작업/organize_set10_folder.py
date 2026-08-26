# -*- coding: utf-8 -*-
import os, shutil, glob

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"
dl_dir = "/Users/mihyunlee/Downloads"

dir_set10 = os.path.join(veo_dir, "9차완성본_Set10_서재도구")
os.makedirs(dir_set10, exist_ok=True)

# 1. veo-folder-1 루트에 있는 mp4 이동
root_files = sorted([f for f in os.listdir(veo_dir) if f.endswith(".mp4")])
print(f"veo-folder-1 루트 발견 파일 수: {len(root_files)}개")

for idx, f in enumerate(root_files):
    src = os.path.join(veo_dir, f)
    dst = os.path.join(dir_set10, f)
    shutil.move(src, dst)
    print(f"📦 [Set 10 이동] {f} -> 9차완성본_Set10_서재도구/")

# 2. Downloads 폴더에 남아있는 신규 영상이 있다면 이동
dl_files = sorted(glob.glob(os.path.join(dl_dir, "*Cinematic*.mp4")) + glob.glob(os.path.join(dl_dir, "*Progressive*.mp4")) + glob.glob(os.path.join(dl_dir, "*animation*.mp4")))
for f in dl_files:
    fname = os.path.basename(f)
    dst = os.path.join(dir_set10, fname)
    shutil.move(f, dst)
    print(f"📦 [Downloads에서 이동] {fname} -> 9차완성본_Set10_서재도구/")

print("\n=== 전체 수확 보관 폴더 현황 ===")
total_videos = 0
for item in sorted(os.listdir(veo_dir)):
    p = os.path.join(veo_dir, item)
    if os.path.isdir(p):
        cnt = len([f for f in os.listdir(p) if f.endswith(".mp4")])
        total_videos += cnt
        print(f"📁 {item} : 총 {cnt}편 안전 보관 중")

print(f"\n🏆 [대기록 달성] 현재까지 안전하게 수확 및 보관 완료된 총 영상 수: {total_videos}편!!")

