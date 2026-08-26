# -*- coding: utf-8 -*-
import re

with open("src/data/words.ts", "r", encoding="utf-8") as f:
    text = f.read()

# 챕터별 scene id 카운트
for ch_num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    scenes = set(re.findall(rf'id:\s*["\'](ch{ch_num}_\d+|scene-ch{ch_num}-\d+)["\']', text))
    print(f"ch{ch_num}: 기존 {len(scenes)}개 씬 등록됨 -> {sorted(list(scenes))}")

