# -*- coding: utf-8 -*-
import os

p = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1/3차완성본"
files = sorted([f for f in os.listdir(p) if f.endswith(".mp4")])
print(f"3차완성본 파일 수: {len(files)}")
for f in files:
    print(f"- {f}")

