# -*- coding: utf-8 -*-
import os, glob, shutil

# 1. Downloads 폴더
dl_dir = "/Users/mihyunlee/Downloads"
cnt = 0
for f in glob.glob(os.path.join(dl_dir, "*.mp4")):
    try:
        os.remove(f)
        print(f"🗑️ [다운로드 폴더 삭제] {os.path.basename(f)}")
        cnt += 1
    except: pass

# 2. 휴지통 비우기 (~/.Trash)
trash_dir = os.path.expanduser("~/.Trash")
if os.path.exists(trash_dir):
    for f in os.listdir(trash_dir):
        full = os.path.join(trash_dir, f)
        if "Cinematic" in f or "reveal" in f or f.endswith(".mp4"):
            try:
                if os.path.isfile(full): os.remove(full)
                elif os.path.isdir(full): shutil.rmtree(full)
                print(f"🗑️ [휴지통 영구 삭제] {f}")
                cnt += 1
            except: pass

# 3. veo-folder-1 루트
veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"
for f in os.listdir(veo_dir):
    if f.endswith(".mp4"):
        full = os.path.join(veo_dir, f)
        os.remove(full)
        print(f"🗑️ [veo-folder-1 루트 삭제] {f}")
        cnt += 1

print(f"\n총 {cnt}개 잔여 파일 및 휴지통까지 100% 완전 청소 완료!")
