# -*- coding: utf-8 -*-
"""
STEP 2 완벽 실행 스크립트:
1) 세트별 프롬프트 번호(001~010) 그룹핑
2) 각 번호에서 파일 크기(bytes)가 가장 큰 Best Take 1편 선택
3) public/learning/ch{N}/ 로 복사 (파일명 규칙 ch{N}_{MM}.mp4)
4) ffmpeg로 포스터 ch{N}_{MM}-poster.jpg 생성
5) _작업/141편_대장.csv 대장 작성
"""

import os, glob, shutil, subprocess, csv

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"
out_base = "public/learning"

# 세트별 폴더 매핑 및 씬 목록 가져오기 함수
def get_best_takes(folder_name):
    fpath = os.path.join(veo_dir, folder_name)
    if not os.path.exists(fpath):
        print(f"[경고] 폴더 없음: {fpath}")
        return []
    
    files = sorted([f for f in os.listdir(fpath) if f.endswith(".mp4")])
    # 001~010 등으로 묶기
    groups = {}
    for f in files:
        prefix = f[:3] if f[:3].isdigit() else "001"
        if prefix not in groups:
            groups[prefix] = []
        full_p = os.path.join(fpath, f)
        groups[prefix].append({
            "filename": f,
            "path": full_p,
            "size": os.path.getsize(full_p)
        })
    
    results = []
    for prefix in sorted(groups.keys()):
        v_list = groups[prefix]
        # 크기 기준 내림차순 정렬 (가장 큰 것 1순위)
        best = sorted(v_list, key=lambda x: x["size"], reverse=True)[0]
        results.append({
            "set_folder": folder_name,
            "prefix": prefix,
            "version_count": len(v_list),
            "all_files": [x["filename"] for x in v_list],
            "best_file": best["filename"],
            "best_path": best["path"],
            "size_kb": best["size"] // 1024
        })
    return results

# 1. 91편 배정 정의
# ch11: 1,2차 우주구조 10편 (ch11_04 ~ ch11_13) + 9차 서재도구 10편 (ch11_14 ~ ch11_23)
# ch5 : 3차 교통 11편 (ch5_06 ~ ch5_16) + 11차 음악소리 5편 (ch5_17 ~ ch5_21)
# ch12: 4차 캠핑베이커리 5편 (ch12_05 ~ ch12_09) + 11차 음악소리 5편 (ch12_10 ~ ch12_14)
# ch2 : 5차 정원원예 10편 (ch2_14 ~ ch2_23) + 8차 조류곤충 10편 (ch2_24 ~ ch2_33)
# ch4 : 6차 미술공예 10편 (ch4_04 ~ ch4_13)
# ch6 : 4차 캠핑베이커리 5편 (ch6_07 ~ ch6_11)
# ch10: 7차 사계절날씨 10편 (ch10_05 ~ ch10_14)

plan = [
    # (세트폴더, 슬라이스/개수, 타겟챕터, 시작번호)
    ("1,2차완성본", slice(0, 10), 11, 4),
    ("9차완성본_Set10_서재도구", slice(0, 10), 11, 14),
    ("3차완성본", slice(0, 11), 5, 6),
    ("11차완성본_Set12_음악소리", slice(0, 5), 5, 17),
    ("4차완성본", slice(0, 5), 12, 5),
    ("11차완성본_Set12_음악소리", slice(5, 10), 12, 10),
    ("5차완성본_Set06_정원원예", slice(0, 10), 2, 14),
    ("8차완성본_Set09_조류곤충생태", slice(0, 10), 2, 24),
    ("6차완성본_Set07_미술공예", slice(0, 10), 4, 4),
    ("4차완성본", slice(5, 10), 6, 7),
    ("7차완성본_Set08_사계절날씨", slice(0, 10), 10, 5),
]

csv_rows = []
total_transferred = 0

print("=== STEP 2 배정 및 복사, 포스터 생성 시작 ===")

for folder_name, sl, ch_num, start_idx in plan:
    takes = get_best_takes(folder_name)[sl]
    target_ch_dir = os.path.join(out_base, f"ch{ch_num}")
    os.makedirs(target_ch_dir, exist_ok=True)
    
    current_idx = start_idx
    for t in takes:
        num_str = str(current_idx).zfill(2)
        new_video_name = f"ch{ch_num}_{num_str}.mp4"
        new_poster_name = f"ch{ch_num}_{num_str}-poster.jpg"
        
        dst_video = os.path.join(target_ch_dir, new_video_name)
        dst_poster = os.path.join(target_ch_dir, new_poster_name)
        
        # 1. 비디오 복사 (원본 유지)
        shutil.copy2(t["best_path"], dst_video)
        
        # 2. 포스터 생성 (ffmpeg 첫 프레임)
        subprocess.run([
            "ffmpeg", "-y", "-i", dst_video,
            "-vframes", "1", "-q:v", "2",
            dst_poster
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # 3. CSV 대장 행 기록
        # 원본파일,세트,프롬프트번호,버전수,선택한파일,배정챕터,새파일명,상태
        csv_rows.append([
            t["all_files"][0],
            t["set_folder"],
            t["prefix"],
            t["version_count"],
            t["best_file"],
            f"ch{ch_num}",
            new_video_name,
            "옮김완료"
        ])
        
        print(f"✅ [ch{ch_num}] {t['set_folder']} #{t['prefix']} -> {new_video_name} & poster ({t['size_kb']}KB, {t['version_count']}개 버전 중 Best)")
        current_idx += 1
        total_transferred += 1

# 대장 CSV 저장
csv_path = "_작업/141편_대장.csv"
with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["원본대표파일", "세트", "프롬프트번호", "버전수", "선택한BestTake", "배정챕터", "새파일명", "상태"])
    for r in csv_rows:
        writer.writerow(r)

print(f"\n============================================================")
print(f"🎉 STEP 2 완벽 완료! 총 {total_transferred}편 배정 및 포스터 생성 완결")
print(f"📄 대장 저장 완료: {csv_path}")
print(f"============================================================")

