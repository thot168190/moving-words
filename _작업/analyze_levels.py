# -*- coding: utf-8 -*-
"""
1200단어 전체 조감도 분석기:
1. 전체 1202단어의 레벨별 / 갈래별 현황
2. 기존 66편 탑재 현황 vs 신규 세트 매핑
"""
import json, re

with open("public/learning/index.html", "r", encoding="utf-8") as f:
    html_text = f.read()

# chapterData 파싱
match = re.search(r'const chapterData = (\[.*?\]);', html_text, re.DOTALL)
if match:
    chapters = json.loads(match.group(1))
    existing_words = []
    for ch in chapters:
        for scene in ch.get("scenes", []):
            for w in scene.get("words", []):
                existing_words.append(w.get("word", "").lower())
    print(f"기존 탑재 단어 수: {len(existing_words)}개")

