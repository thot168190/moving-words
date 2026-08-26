# -*- coding: utf-8 -*-
import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

set04 = None
for s in data:
    if s["set_id"] == "set04":
        set04 = s
        break

# 화면에 안 나온 6개 씬: 01, 02, 03, 04, 06, 09 (인덱스 0, 1, 2, 3, 5, 8)
target_indices = [0, 1, 2, 3, 5, 8]
next_6_prompts = [set04["prompts"][i] for i in target_indices]

print(f"=== 미생성 6개 정본 프롬프트 목록 ===")
output_texts = []
for idx, p in enumerate(next_6_prompts):
    print(f"\n[{idx+1}/6] {p['title']}")
    print(f"ID: {p['id']} · 단어: {', '.join(p['words'])}")
    output_texts.append(p["prompt"])

# 6개 한 번에 벌크 복사용 텍스트 저장
with open("_작업/set04_remaining_6.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(output_texts))

print("\n_작업/set04_remaining_6.txt 저장 완료!")
