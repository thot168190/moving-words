# -*- coding: utf-8 -*-
import os, glob, datetime

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"

files = [f for f in os.listdir(veo_dir) if f.endswith(".mp4")]

print(f"=== 루트에 새로 다운로드된 총 {len(files)}편 상세 정보 ===")
file_details = []
for f in files:
    full = os.path.join(veo_dir, f)
    mtime = os.path.getmtime(full)
    size = os.path.getsize(full)
    dt = datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
    file_details.append((mtime, dt, size, f))

file_details.sort()
for mtime, dt, size, f in file_details:
    print(f"[{dt}] ({size:>8} bytes) {f}")

