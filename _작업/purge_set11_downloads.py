# -*- coding: utf-8 -*-
import os, glob

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"

# 1. veo-folder-1 루트에 있는 Set 11 다운로드 파일들 삭제
root_files = [f for f in os.listdir(veo_dir) if f.endswith(".mp4")]
print(f"=== {veo_dir} 루트 내 파일 삭제 처리 ===")
deleted_cnt = 0
for f in root_files:
    full = os.path.join(veo_dir, f)
    os.remove(full)
    print(f"🗑️ [루트 폐기 삭제] {f}")
    deleted_cnt += 1

# 2. 혹시 기존 다운로드 폴더(Downloads)에 남아있는 mp4 삭제
dl_dir = "/Users/mihyunlee/Downloads"
for f in glob.glob(os.path.join(dl_dir, "*Cinematic*.mp4")) + glob.glob(os.path.join(dl_dir, "*animation*.mp4")):
    os.remove(f)
    print(f"🗑️ [다운로드 폴더 폐기 삭제] {os.path.basename(f)}")
    deleted_cnt += 1

print(f"\n총 {deleted_cnt}개 Set 11 실사 실패본 완전 폐기 완료!")
