# -*- coding: utf-8 -*-
"""
대표님 명령: Set 07부터 Set 13까지 손(Hand)을 100% 영구 금지!
30편 무사고 성공작(3차 정본)의 검증된 문법으로 완벽 복원!
"""

import json

PROVEN_SAFE_TEMPLATE = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are {subjects}.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. {draw_steps} There is no visible person, driver, student, live action element, wall, ceiling, darkness or heavy architecture anywhere. Keep lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is {palette}. All surrounding space stays untouched pure white with no wash of any kind extending behind the subjects. {motion} All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

from rebuild_all_100_scenes_atlas import ALL_SETS_DATA

complete_100_final = []

for s in ALL_SETS_DATA:
    set_prompts = []
    
    # Set 07 ~ Set 13은 30편 무사고 검증 정본 문법 적용
    if s["set_id"] in ["set07", "set08", "set09", "set10", "set11", "set12", "set13"]:
        for idx, sc in enumerate(s["scenes"]):
            # draw_steps 정제 (Begin with / Draw 형태)
            d_step = f"Begin with the minimal base structure. Draw the main central forms next, keeping the combined silhouette horizontal rather than diagonal. Extend delicate contour lines equally toward both sides. Add the balancing accessory elements."
            
            prompt_text = PROVEN_SAFE_TEMPLATE.format(
                subjects=sc["subjects"],
                draw_steps=d_step,
                palette=sc["palette"],
                motion=sc["motion"]
            )
            clean_p = " ".join(prompt_text.split())
            
            # 지뢰어 완전 소탕
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
            
            set_prompts.append({
                "id": f"{s['set_id']}-{str(idx+1).zfill(2)}",
                "chapter": f"{s['set_id'].upper()} ({s['target_branches']})",
                "title": sc["title"],
                "words": sc["words"],
                "prompt": clean_p
            })
    else:
        # 기존 세트 유지
        for old_s in complete_100:
            if old_s["set_id"] == s["set_id"]:
                set_prompts = old_s["prompts"]
                break

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

print("Set 07 ~ Set 13 무사고 손 0% 검증 정본으로 100% 재건축 완료!")

