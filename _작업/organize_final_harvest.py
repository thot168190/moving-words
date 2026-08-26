# -*- coding: utf-8 -*-
import os, shutil, glob

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"
dl_dir = "/Users/mihyunlee/Downloads"

dir_set12 = os.path.join(veo_dir, "11차완성본_Set12_음악소리")
dir_set13 = os.path.join(veo_dir, "12차완성본_Set13_사회제도")
os.makedirs(dir_set12, exist_ok=True)
os.makedirs(dir_set13, exist_ok=True)

# 1. 루트 파일 검사
root_files = sorted([f for f in os.listdir(veo_dir) if f.endswith(".mp4")])
print(f"veo-folder-1 루트 발견 파일 수: {len(root_files)}개")

# 2. Downloads 폴더 검사
dl_files = sorted(glob.glob(os.path.join(dl_dir, "*.mp4")))
print(f"Downloads 폴더 발견 파일 수: {len(dl_files)}개")

# 파일명 또는 생성 순서에 따라 Set 12 / Set 13 이동
all_found = []
for f in root_files:
    all_found.append((os.path.join(veo_dir, f), f))
for f in dl_files:
    all_found.append((f, os.path.basename(f)))

for src, fname in all_found:
    low = fname.lower()
    # Set 13 관련 키워드 (cart, blotter, briefcase, seal, scale, ballot, passport, vault, gavel, postbox)
    if any(k in low for k in ['cart', 'blotter', 'briefcase', 'seal', 'scale', 'ballot', 'passport', 'vault', 'gavel', 'postbox']):
        dst = os.path.join(dir_set13, fname)
        shutil.move(src, dst)
        print(f"📦 [Set 13 사회제도 이동] {fname} -> 12차완성본_Set13_사회제도/")
    # Set 12 관련 키워드 (bow, triangle, tuning, harmonica, mouthpiece, baton, mallet, cymbal, opera, stand)
    elif any(k in low for k in ['bow', 'triangle', 'tuning', 'harmonica', 'mouthpiece', 'baton', 'mallet', 'cymbal', 'opera', 'stand']):
        dst = os.path.join(dir_set12, fname)
        shutil.move(src, dst)
        print(f"📦 [Set 12 음악소리 이동] {fname} -> 11차완성본_Set12_음악소리/")
    else:
        # 일반 번호인 경우 기본 12차완성본_Set13_사회제도로 이동
        dst = os.path.join(dir_set13, fname)
        shutil.move(src, dst)
        print(f"📦 [기타 이동] {fname} -> 12차완성본_Set13_사회제도/")

print("\n============================================================")
print("🏆 [보는 단어장 / 움직이는 그림사전] 최종 전체 수확 폴더 완결 현황")
print("============================================================")
grand_total = 0
for item in sorted(os.listdir(veo_dir)):
    p = os.path.join(veo_dir, item)
    if os.path.isdir(p):
        cnt = len([f for f in os.listdir(p) if f.endswith(".mp4")])
        grand_total += cnt
        print(f"📁 {item} : 총 {cnt}편 안전 보관 완료 ✅")

print("============================================================")
print(f"🎉 [대기록 완주 달성] 최종 총 보관 영상 수: {grand_total}편!!")
print("============================================================")

