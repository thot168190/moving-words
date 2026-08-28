# -*- coding: utf-8 -*-
import os
from build_26_prompts import scenes, build_prompt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BULK_DIR = os.path.join(ROOT, "_작업/bulk_26")
os.makedirs(BULK_DIR, exist_ok=True)

batches = [
    ("bulk_part1_01_07.txt", scenes[0:7]),
    ("bulk_part2_08_14.txt", scenes[7:14]),
    ("bulk_part3_15_20.txt", scenes[14:20]),
    ("bulk_part4_21_26.txt", scenes[20:26]),
]

for filename, batch_scenes in batches:
    filepath = os.path.join(BULK_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        # 순수 프롬프트만 엔터 2개로 구분 (주석/헤더/슬래시 일체 없음)
        prompts = [build_prompt(sc).strip() for sc in batch_scenes]
        f.write("\n\n".join(prompts) + "\n")
    print(f"순수 프롬프트 생성 완료: {filepath} ({len(batch_scenes)}개)")

print("\n주석·슬래시 100% 제거된 순수 벌크 프롬프트 생성 완료!")
