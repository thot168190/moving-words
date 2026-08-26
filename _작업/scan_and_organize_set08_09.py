# -*- coding: utf-8 -*-
import os, glob, shutil, datetime

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"

print(f"=== {veo_dir} 루트 내 신규 다운로드 파일 검사 ===")
files = [f for f in os.listdir(veo_dir) if f.endswith(".mp4")]

file_details = []
for f in files:
    full = os.path.join(veo_dir, f)
    mtime = os.path.getmtime(full)
    size = os.path.getsize(full)
    dt = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
    file_details.append((mtime, dt, size, f))

file_details.sort()
print(f"총 {len(file_details)}편 발견:")
for mtime, dt, size, f in file_details:
    print(f"[{dt}] ({size:>8} bytes) {f}")

