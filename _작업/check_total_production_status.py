# -*- coding: utf-8 -*-
import os, json

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"

print("=== 1. 다운로드 완료 및 안전 보관 세트 목록 ===")
folders = sorted([f for f in os.listdir(veo_dir) if os.path.isdir(os.path.join(veo_dir, f))])
total_downloaded = 0
for folder in folders:
    cnt = len([f for f in os.listdir(os.path.join(veo_dir, folder)) if f.endswith(".mp4")])
    total_downloaded += cnt
    print(f"📁 {folder} : {cnt}편")

print(f"\n현재 다운로드 완료 총계: {total_downloaded}편\n")

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=== 2. 마스터 100편 데이터 세트별 제작 현황 ===")
for idx, s in enumerate(data):
    sid = s["set_id"]
    sname = s["set_name"]
    prompt_cnt = len(s["prompts"])
    print(f"[{str(idx+1).zfill(2)}] {sid} ({sname}) : {prompt_cnt}편 프롬프트 정본화 완비")

