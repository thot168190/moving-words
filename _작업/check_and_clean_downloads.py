# -*- coding: utf-8 -*-
import os, glob

dl_dir = "/Users/mihyunlee/Downloads"

mp4_files = glob.glob(os.path.join(dl_dir, "*.mp4"))
cinematic_mp4s = [f for f in mp4_files if "Cinematic" in f or "reveal" in f or "animation" in f]

print(f"=== {dl_dir} 내 비디오 다운로드 파일 현황 ===")
print(f"발견된 임시 mp4 영상: {len(cinematic_mp4s)}개")

for f in cinematic_mp4s:
    print(" - 삭제 대상:", os.path.basename(f))
    os.remove(f)

print(f"\n총 {len(cinematic_mp4s)}개 다운로드 임시 영상 파일 삭제 완료!")
