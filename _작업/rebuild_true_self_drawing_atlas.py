# -*- coding: utf-8 -*-
"""
대표님 명령:
1. 허브 100편 전체(Set 04 ~ Set 13)를 [손 0% + 선이 끝점에서부터 자라나는 진짜 자가 드로잉 정본]으로 전면 수정!
2. 대표님이 지금 뽑으실 차례인 Set 06 (정원·원예 10편) 최우선 복사!
"""

import json

PERFECT_TRUE_DRAWING_TEMPLATE = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. The background is one single continuous field of pure white reaching every outer edge, and the subjects sit directly on that white with nothing underneath them - no board, no panel, no card, no mat, no textured surface and no visible edge of any kind. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The subjects remain centered while both outer edges stay clear. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are {subjects}. There is no visible person, driver, student, live action element, wall, ceiling, darkness or heavy architecture anywhere.

0-4s: ultra-fine pale graphite linework appears progressively from the empty white field by an invisible moving point. Each line extends continuously from an advancing tip that travels along the contour, growing line by line on its own with zero human presence and zero physical instruments visible. Nothing fades into view and nothing is revealed by a sweeping wipe transition - every individual outline physically lengthens from its moving point until each form is complete. {draw_steps} Most of each form stays deliberately economical and free of internal lines, with strictly zero cross-hatching and zero line shading. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is {palette}. All surrounding space stays untouched pure white with no wash of any kind extending behind the subjects. {motion} All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, precise pale graphite lines and aesthetic precision, maximum line value 20% grey, luminous transparent watercolor, restrained tonal contrast, generous untouched white space, sophisticated museum-quality editorial illustration for an adult natural-history atlas, mature and understated, with hairline lines and no heavy outlines anywhere."""

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

# complete_100_data.json 내부의 100편 전체 프롬프트 재구성
from rebuild_all_100_scenes_atlas import ALL_SETS_DATA

complete_100_final = []

for s in ALL_SETS_DATA:
    set_prompts = []
    for idx, sc in enumerate(s["scenes"]):
        prompt_text = PERFECT_TRUE_DRAWING_TEMPLATE.format(
            subjects=sc["subjects"],
            draw_steps=sc["draw_steps"],
            palette=sc["palette"],
            motion=sc["motion"]
        )
        clean_p = " ".join(prompt_text.split())
        
        # 지뢰어 2차 정제
        clean_p = clean_p.replace("drawing tools", "implements")
        clean_p = clean_p.replace("drawing tool", "implement")
        clean_p = clean_p.replace("tool", "implement")
        clean_p = clean_p.replace("tools", "implements")
        clean_p = clean_p.replace("hand-drawn", "fine-line")
        clean_p = clean_p.replace("handmade", "crafted")
        clean_p = clean_p.replace("hand", "manual")
        clean_p = clean_p.replace("hands", "manuals")
        clean_p = clean_p.replace("paper", "sheet")
        clean_p = clean_p.replace("parchment", "vellum sheet")
        clean_p = clean_p.replace("canvas", "cotton fabric")
        clean_p = clean_p.replace("cream", "warm-white")
        clean_p = clean_p.replace("finger", "ring")
        clean_p = clean_p.replace("arm", "lever")
        clean_p = clean_p.replace("3D", "spatial")
        clean_p = clean_p.replace("strokes", "lines")
        clean_p = clean_p.replace("stroke", "line")
        
        # first frame / of the frame 복원
        clean_p = clean_p.replace("first structure", "first frame")
        clean_p = clean_p.replace("three-quarters of the structure", "three-quarters of the frame")
        
        set_prompts.append({
            "id": f"{s['set_id']}-{str(idx+1).zfill(2)}",
            "chapter": f"{s['set_id'].upper()} ({s['target_branches']})",
            "title": sc["title"],
            "words": sc["words"],
            "prompt": clean_p
        })
    
    filename = f"_작업/bulk_sets/{s['set_id']}_10.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for p in set_prompts:
            f.write(p["prompt"] + "\n\n")
            
    complete_100_final.append({
        "set_id": s["set_id"],
        "set_name": s["set_name"],
        "target_chapter": s["target_chapter"],
        "target_branches": s["target_branches"],
        "filename": filename,
        "prompts": set_prompts
    })

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_100_final, f, ensure_ascii=False, indent=2)

print("10개 세트 100편 전체 [진짜 자가 드로잉 정본] 재건축 완료!")

