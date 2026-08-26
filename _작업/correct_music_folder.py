# -*- coding: utf-8 -*-
import os, shutil

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"

dir_old = os.path.join(veo_dir, "10차완성본_Set11_주방식탁")
dir_set12 = os.path.join(veo_dir, "11차완성본_Set12_음악소리")
dir_set11 = os.path.join(veo_dir, "10차완성본_Set11_주방식탁")

# 1. 현재 들어있는 30개 파일은 Set 12(악기와 소리: 트라이앵글, 악보대 등)이므로 11차완성본_Set12_음악소리로 이동
if os.path.exists(dir_old):
    files = [f for f in os.listdir(dir_old) if f.endswith(".mp4")]
    os.makedirs(dir_set12, exist_ok=True)
    for f in files:
        src = os.path.join(dir_old, f)
        dst = os.path.join(dir_set12, f)
        shutil.move(src, dst)
        print(f"📦 [Set 12 음악소리로 정정 이동] {f}")
    shutil.rmtree(dir_old)

# 2. Set 11 (주방) 빈 폴더 재생성
os.makedirs(dir_set11, exist_ok=True)

print("\n=== 정정 후 전체 수확 보관 폴더 현황 ===")
total_videos = 0
for item in sorted(os.listdir(veo_dir)):
    p = os.path.join(veo_dir, item)
    if os.path.isdir(p):
        cnt = len([f for f in os.listdir(p) if f.endswith(".mp4")])
        total_videos += cnt
        print(f"📁 {item} : 총 {cnt}편 안전 보관 중")

print(f"\n🏆 현재까지 정확하게 분류 완료된 총 영상 수: {total_videos}편!!")

