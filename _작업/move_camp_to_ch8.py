# -*- coding: utf-8 -*-
import os, shutil

# ch12_05~09 -> ch8_05~09
for i in range(5, 10):
    src_mp4 = f"public/learning/ch12/ch12_{i:02d}.mp4"
    src_jpg = f"public/learning/ch12/ch12_{i:02d}-poster.jpg"
    dst_mp4 = f"public/learning/ch8/ch8_{i:02d}.mp4"
    dst_jpg = f"public/learning/ch8/ch8_{i:02d}-poster.jpg"
    if os.path.exists(src_mp4):
        shutil.move(src_mp4, dst_mp4)
    if os.path.exists(src_jpg):
        shutil.move(src_jpg, dst_jpg)

# ch6_07~11 -> ch8_10~14
for idx, i in enumerate(range(7, 12), start=10):
    src_mp4 = f"public/learning/ch6/ch6_{i:02d}.mp4"
    src_jpg = f"public/learning/ch6/ch6_{i:02d}-poster.jpg"
    dst_mp4 = f"public/learning/ch8/ch8_{idx:02d}.mp4"
    dst_jpg = f"public/learning/ch8/ch8_{idx:02d}-poster.jpg"
    if os.path.exists(src_mp4):
        shutil.move(src_mp4, dst_mp4)
    if os.path.exists(src_jpg):
        shutil.move(src_jpg, dst_jpg)

print("ch8 캠핑 10편 이동 완료!")
