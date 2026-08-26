# -*- coding: utf-8 -*-
import os, glob

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"

print(f"=== {veo_dir} 폴더 구조 및 파일 현황 ===")
items = os.listdir(veo_dir)
for item in sorted(items):
    full_path = os.path.join(veo_dir, item)
    if os.path.isdir(full_path):
        sub_files = [f for f in os.listdir(full_path) if f.endswith(".mp4")]
        print(f"📁 [폴더] {item} ({len(sub_files)}편)")
    elif item.endswith(".mp4"):
        print(f"🎬 [다운로드된 파일] {item}")

