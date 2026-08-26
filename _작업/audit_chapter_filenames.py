# -*- coding: utf-8 -*-
import os, glob

base_dir = "public/learning"
for ch in ["ch2", "ch4", "ch5", "ch6", "ch10", "ch11", "ch12"]:
    ch_dir = os.path.join(base_dir, ch)
    if os.path.exists(ch_dir):
        files = sorted([f for f in os.listdir(ch_dir) if f.endswith(".mp4")])
        print(f"[{ch}] ({len(files)} files): {files}")

