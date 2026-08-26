# -*- coding: utf-8 -*-
import os, subprocess, json

folder_p = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1/10차완성본_Set11_주방식탁"
files = sorted([f for f in os.listdir(folder_p) if f.endswith(".mp4")])

print(f"=== {folder_p} 내부 파일 목록 (총 {len(files)}개) ===")
for f in files:
    print(f"- {f}")

# ffprobe로 첫 몇 개 파일의 메타데이터 확인 (가능하다면)
if files:
    sample = os.path.join(folder_p, files[0])
    print(f"\n샘플 파일 크기 및 정보: {sample}")

