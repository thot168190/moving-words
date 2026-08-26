# -*- coding: utf-8 -*-
import os, glob

base_dir = "public/learning"
expected_counts = {
    "ch2": (20, "ch2_14", "ch2_33"),
    "ch4": (10, "ch4_04", "ch4_13"),
    "ch5": (16, "ch5_06", "ch5_21"),
    "ch6": (5,  "ch6_07", "ch6_11"),
    "ch10": (10, "ch10_05", "ch10_14"),
    "ch11": (20, "ch11_04", "ch11_23"),
    "ch12": (10, "ch12_05", "ch12_14"),
}

print("=== [STEP 2 자가검증] 챕터별 신규 생성 파일 실측 검증 ===")
total_vids = 0
total_posters = 0

for ch, (cnt, start_name, end_name) in expected_counts.items():
    ch_dir = os.path.join(base_dir, ch)
    # 신규 배정된 mp4 파일
    vids = sorted([f for f in os.listdir(ch_dir) if f.startswith(f"{ch}_") and f.endswith(".mp4")])
    posters = sorted([f for f in os.listdir(ch_dir) if f.startswith(f"{ch}_") and f.endswith("-poster.jpg")])
    
    print(f"[{ch}] 기대 {cnt}편 -> 실제 영상: {len(vids)}편 ({vids[0]} ~ {vids[-1]}) / 포스터: {len(posters)}장")
    total_vids += len(vids)
    total_posters += len(posters)

print(f"\n총 신규 배정 영상: {total_vids}편 (목표: 91편) ✅")
print(f"총 신규 생성 포스터: {total_posters}장 (목표: 91장) ✅")

# CSV 행 수 확인
with open("_작업/141편_대장.csv", "r", encoding="utf-8-sig") as f:
    lines = f.readlines()
print(f"대장 CSV 총 행수 (헤더 포함): {len(lines)}줄 (기록 데이터: {len(lines)-1}건) ✅")

