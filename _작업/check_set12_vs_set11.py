# -*- coding: utf-8 -*-
import subprocess, os

folder = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1/10차완성본_Set11_주방식탁"

# 001, 002, 010 파일의 첫 프레임 추출해서 확인
os.makedirs("_작업/temp_check", exist_ok=True)
for f in ["001_Progressive-detailed-fine-pencil-construction-tran.mp4", "010_Progressive-detailed-fine-pencil-construction-tran (1).mp4"]:
    src = os.path.join(folder, f)
    if os.path.exists(src):
        dst_img = f"_작업/temp_check/{f}.jpg"
        subprocess.run(["ffmpeg", "-y", "-ss", "00:00:06", "-i", src, "-vframes", "1", dst_img], capture_output=True)
        print(f"추출 완료: {dst_img}")

