# -*- coding: utf-8 -*-
import os, re
from build_26_prompts import scenes, build_prompt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BULK_DIR = os.path.join(ROOT, "_작업/bulk_26")
os.makedirs(BULK_DIR, exist_ok=True)

def to_single_line_prompt(sc):
    raw = build_prompt(sc)
    # 모든 내부 줄바꿈을 공백 1개로 치환하여 "완전한 한 줄(Single Line)"로 변환
    single_line = re.sub(r'\s+', ' ', raw).strip()
    return single_line

batches = [
    ("bulk_part1_01_07.txt", scenes[0:7]),
    ("bulk_part2_08_14.txt", scenes[7:14]),
    ("bulk_part3_15_20.txt", scenes[14:20]),
    ("bulk_part4_21_26.txt", scenes[20:26]),
]

for filename, batch_scenes in batches:
    filepath = os.path.join(BULK_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        # 1개 프롬프트 = 1줄 (내부 줄바꿈 0개), 프롬프트 간 구분은 줄바꿈 2개
        single_line_prompts = [to_single_line_prompt(sc) for sc in batch_scenes]
        f.write("\n\n".join(single_line_prompts) + "\n")
    print(f"한 줄 벌크 프롬프트 생성 완료: {filepath} ({len(batch_scenes)}개)")

print("\n1프롬프트 = 1줄(내부 엔터 0개) 완전 단일 라인 변환 완료!")
