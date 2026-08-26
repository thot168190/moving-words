# -*- coding: utf-8 -*-
"""
실사/3D 렌더링 느낌 100% 제거 -> '따뜻하고 우아한 2D 그림책 세필 수채화 (Delicate 2D Storybook Watercolor)'로 전면 복원:
1. 'Cinematic' 단어 전면 제거 -> 'Delicate progressive line-reveal animation of a charming 2D picture-book illustration'
2. 실사/3D 금속 반사광 차단: 'strictly 2D flat hand-drawn illustration aesthetic, no 3D rendering, no photorealism, no CGI, no realistic metallic sheen'
3. 선화: 'soft delicate storybook graphite contour lines'
4. 채색: 'soft luminous transparent watercolor washes like a classic children's picture book'
"""

import json, re

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

for s in complete_100:
    for idx, p in enumerate(s["prompts"]):
        t = p["prompt"]
        
        # 1. Cinematic -> Delicate 2D picture-book
        t = t.replace("Cinematic progressive line-reveal animation", "Delicate progressive line-reveal animation of a 2D storybook illustration")
        
        # 2. 스타일 꼬리에 2D 그림책 감성 보강
        old_style = "Style: luminous transparent watercolor, restrained tonal contrast, sophisticated museum-quality editorial illustration, generous untouched white space."
        new_style = "Style: delicate 2D storybook fine-line illustration, luminous transparent watercolor washes, warm picture-book charm, strictly non-photorealistic, elegant hand-drawn 2D feel, generous untouched white space."
        t = t.replace(old_style, new_style)
        
        # 3. 실사 3D 방지 가드레일 추가
        t = t.replace("All other elements remain still.", "All other elements remain still. The image maintains a pure 2D hand-drawn picture-book aesthetic with zero 3D CGI and zero photorealism.")
        
        p["prompt"] = " ".join(t.split())

# 저장
with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_100, f, ensure_ascii=False, indent=2)

for s in complete_100:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("실사 느낌 100% 제거 및 2D 그림책 감성 복원 완료!")

