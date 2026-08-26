# -*- coding: utf-8 -*-
import os, subprocess

folder = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1/10차완성본_Set11_주방식탁"
os.makedirs("_작업/temp_check/thumbs", exist_ok=True)

files = sorted([f for f in os.listdir(folder) if f.endswith(".mp4") and " (1)" in f])
for f in files:
    src = os.path.join(folder, f)
    dst_img = f"_작업/temp_check/thumbs/{f[:3]}.jpg"
    subprocess.run(["ffmpeg", "-y", "-ss", "00:00:06", "-i", src, "-vframes", "1", dst_img], capture_output=True)

print("썸네일 추출 완료:")
for item in sorted(os.listdir("_작업/temp_check/thumbs")):
    print(f"- {item}")

