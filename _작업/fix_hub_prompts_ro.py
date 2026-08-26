# -*- coding: utf-8 -*-
"""
로부장 지시서 1번 실행: 제작허브 프롬프트 4곳 정본 교체
1. 선: graphite -> dark-charcoal
2. 스타일 꼬리: for thoughtful young learners 제거 -> museum-quality
3. never black or dark charcoal 문장 통째로 삭제
4. The subjects remain centered while both outer edges stay clear. 필수문 추가
"""

import json, re

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

def patch_prompt(p):
    # 1. 선 교체
    p = p.replace("ultra-fine pale warm-grey graphite linework appears progressively from the empty white field.", 
                  "hair-thin dark-charcoal linework appears progressively from the empty white field.")
    
    # 2. 스타일 꼬리 교체
    old_style = "Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."
    new_style = "Style: luminous transparent watercolor, restrained tonal contrast, sophisticated museum-quality editorial illustration, generous untouched white space."
    p = p.replace(old_style, new_style)
    
    # 3. 검은 선 금지 문장 삭제
    p = re.sub(r'Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks\.\s*', '', p)
    
    # 4. 필수문 추가
    old_margin = "with equal narrow breathing margins on the left and right."
    new_margin = "with equal narrow breathing margins on the left and right. The subjects remain centered while both outer edges stay clear."
    if old_margin in p and new_margin not in p:
        p = p.replace(old_margin, new_margin)
        
    return " ".join(p.split())

for s in complete_100:
    for p in s["prompts"]:
        p["prompt"] = patch_prompt(p["prompt"])

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_100, f, ensure_ascii=False, indent=2)

# bulk_sets 파일들도 갱신
for s in complete_100:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("complete_100_data.json 및 bulk_sets 4곳 수정 완료!")

