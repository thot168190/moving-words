# -*- coding: utf-8 -*-
"""
대표님 지적 완벽 해결: '선화 내부의 빽빽한 해칭/명암(먹) 100% 박멸'
원인:
1. AI가 'vintage brass', 'timber log cabin', 'stone chimney' 등을 그릴 때 
   질감을 표현하려고 펜선으로 빗금(hatching)과 빽빽한 먹 명암을 칠함.
2. 해결책:
   - "pure clean outline contours ONLY, strictly zero cross-hatching, zero line shading, zero internal texture hatching, completely empty open interiors"
   - "Every line is a hair-thin single stroke, never shaded, never textured with repeated strokes."
   - 헬리콥터처럼 외곽선만 맑고 가늘게 남기고 안쪽은 100% 비워두는 순수 라인아트로 강제 고정!
"""

import json, re

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

for s in complete_100:
    for idx, p in enumerate(s["prompts"]):
        t = p["prompt"]
        
        # 1. 0-4s 구간에 '빗금/명암 0% 완전 금지' 문구 강력 삽입
        old_linework = "Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks."
        new_linework = "Every outline is an ultra-fine, single-stroke contour with strictly zero cross-hatching, zero line shading, zero dark textures and zero dense hatch marks. The interiors of all subjects remain completely open and unshaded, never darkened with ink."
        t = t.replace(old_linework, new_linework)
        
        # 2. 스타일 꼬리에 '순수 외곽선(pure minimalist outline)' 보강
        old_tail = "master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey"
        new_tail = "master-level minimalist fine-line contour illustration with pure single-stroke outlines, strictly zero hatching, strictly zero shading, exceptionally thin pale warm-grey strokes, maximum line value 20% grey"
        t = t.replace(old_tail, new_tail)
        
        p["prompt"] = " ".join(t.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_100, f, ensure_ascii=False, indent=2)

for s in complete_100:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("해칭/먹 명암 100% 박멸 프롬프트 패치 완료!")
