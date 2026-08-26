# -*- coding: utf-8 -*-
import os, glob

dl_dir = "/Users/mihyunlee/Downloads"
veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"

print("=== 1. Downloads 폴더 청소 ===")
for f in glob.glob(os.path.join(dl_dir, "*.mp4")):
    os.remove(f)
    print(f"🗑️ [Downloads 삭제] {os.path.basename(f)}")

print("\n=== 2. veo-folder-1 루트 청소 ===")
for f in os.listdir(veo_dir):
    full = os.path.join(veo_dir, f)
    if os.path.isfile(full) and f.endswith(".mp4"):
        os.remove(full)
        print(f"🗑️ [veo-folder-1 삭제] {f}")

print("\n청소 완료! 현재 veo-folder-1 보관 폴더 목록:")
for f in sorted(os.listdir(veo_dir)):
    p = os.path.join(veo_dir, f)
    if os.path.isdir(p):
        cnt = len([x for x in os.listdir(p) if x.endswith(".mp4")])
        print(f"📁 {f} : {cnt}편")

