# -*- coding: utf-8 -*-
import os

folder_4cha = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1/4차완성본"
files = [f for f in os.listdir(folder_4cha) if f.endswith(".mp4")]

print(f"=== 4차완성본 폴더 내부 총 {len(files)}편 ===")
for f in sorted(files):
    print(" -", f)

