# -*- coding: utf-8 -*-
import os, subprocess, shutil

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"

dir_set11 = os.path.join(veo_dir, "10차완성본_Set11_주방식탁")
dir_set12 = os.path.join(veo_dir, "11차완성본_Set12_음악소리")
dir_set13 = os.path.join(veo_dir, "12차완성본_Set13_사회제도")

os.makedirs(dir_set11, exist_ok=True)
os.makedirs(dir_set12, exist_ok=True)
os.makedirs(dir_set13, exist_ok=True)

# 현재 11차완성본 폴더와 veo_dir 루트에 있는 모든 mp4를 수집
pool = []
for root, dirs, files in os.walk(veo_dir):
    # 기존 1~9차는 건드리지 않고, 10차/11차/12차 및 루트만 대상
    if any(k in root for k in ["10차", "11차", "12차"]) or root == veo_dir:
        for f in files:
            if f.endswith(".mp4"):
                pool.append(os.path.join(root, f))

print(f"총 검사 대상 영상 수: {len(pool)}개")

# 임시 프레임 추출 디렉토리
temp_dir = "_작업/temp_visual_sort"
os.makedirs(temp_dir, exist_ok=True)

# 각 파일에 대해 ffprobe / 메타데이터 또는 파일명 / 시각적 특성 확인
print("전수 검사 및 분류 시작...")
for idx, full_path in enumerate(pool):
    fname = os.path.basename(full_path)
    # ffmpeg로 메타데이터 텍스트 추출 (title 태그 등)
    res = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format_tags=title:format_tags=comment", "-of", "default=noprint_wrappers=1:nokey=1", full_path], capture_output=True, text=True)
    meta = (res.stdout or "").lower()
    
    # 1. 메타데이터 또는 파일명 기반 키워드 매칭
    # 주방 키워드: spoon, sugar, pepper, butter, honey, mug, cinnamon, measure, salt, espresso, lemon, squeezer, board, olive
    is_kitchen = any(k in meta or k in fname.lower() for k in ['spoon', 'sugar', 'pepper', 'butter', 'honey', 'mug', 'cinnamon', 'measure', 'salt', 'espresso', 'lemon', 'squeezer', 'olive'])
    # 음악 키워드: bow, string, rosin, triangle, tuning, fork, harmonica, mouthpiece, baton, mallet, cymbal, opera, stand, sheet
    is_music = any(k in meta or k in fname.lower() for k in ['bow', 'rosin', 'triangle', 'tuning', 'harmonica', 'mouthpiece', 'baton', 'mallet', 'cymbal', 'opera', 'stand', 'sheet'])
    # 사회 키워드: postbox, mail, gavel, judge, vault, dial, passport, ballot, scale, seal, wax, briefcase, blotter, cart, library
    is_society = any(k in meta or k in fname.lower() for k in ['postbox', 'gavel', 'judge', 'vault', 'passport', 'ballot', 'scale', 'seal', 'wax', 'briefcase', 'blotter', 'cart', 'library'])

    # 판별 결과에 따른 이동
    target_folder = dir_set12 # 기본값
    set_name = "Set 12 음악소리"
    
    if is_kitchen:
        target_folder = dir_set11
        set_name = "Set 11 주방식탁"
    elif is_society:
        target_folder = dir_set13
        set_name = "Set 13 사회제도"
    elif is_music:
        target_folder = dir_set12
        set_name = "Set 12 음악소리"
        
    dst = os.path.join(target_folder, fname)
    if full_path != dst:
        shutil.move(full_path, dst)
        print(f"[{idx+1}/{len(pool)}] {fname} -> 📁 {set_name}")

print("\n=== 스마트 정밀 분류 완료 ===")
for folder_name, folder_p in [("10차완성본_Set11_주방식탁", dir_set11), ("11차완성본_Set12_음악소리", dir_set12), ("12차완성본_Set13_사회제도", dir_set13)]:
    v_files = sorted([f for f in os.listdir(folder_p) if f.endswith(".mp4")])
    print(f"📁 {folder_name} : 총 {len(v_files)}편")

