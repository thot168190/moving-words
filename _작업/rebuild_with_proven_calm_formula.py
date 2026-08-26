# -*- coding: utf-8 -*-
"""
1~3차 대성공작(prompt_calm_ch11.txt)의 정본 공식 100% 이식:
1. "Draw the/Extend/Add" 인위적 그리기 동사 전면 제거 -> "...are revealed first through many clean short line segments... then appear one by one"
2. "pale 15% grey" 흐리멍텅한 선 -> "hair-thin dark-charcoal linework appears progressively from the empty white field" (선명하고 또렷한 선화 그려짐 복원)
3. 4-8s: 맑은 수채화 틴트 + 잔잔한 1회 미세 모션
4. 손 0% 원천 봉쇄 (human hand/artist 소환 원인 동사 100% 제거)
"""

import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    sets_data = json.load(f)

# 검증된 CALM 정본 템플릿
CALM_TEMPLATE = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame with equal narrow breathing margins on the left and right. The subjects remain centered while both outer edges stay clear. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are {subjects}.

0-4s: hair-thin dark-charcoal linework appears progressively from the empty white field. {reveal_steps} Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. The restrained palette is {palette}. All surrounding space stays untouched pure white with no wash of any kind extending behind the subjects. {motion} All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: delicate fine-line engraving, luminous transparent watercolor, restrained tonal contrast, generous white space, sophisticated museum-quality editorial illustration."""

# Set 08 리빌 단계 재작성 (사물 중심 출현 문법)
reveal_dict_set08 = {
    "set08-01": "The central straight shaft and wooden J-handle are revealed first through clean line segments. The symmetrical arched canopy ribs and fabric panels then appear one by one, followed by the pointed top ferrule and three tiny water droplets on the rim.",
    "set08-02": "The ribbed base cuffs of both mittens are revealed first through clean short line segments. The curved thumb pieces and rounded hand pockets then appear one by one, followed by the slender connecting yarn cord and delicate knit texture lines.",
    "set08-03": "The central leaf stem and radiating lobed leaf edges are revealed first through clean line segments. The layered geometric scales of the pinecone then appear one by one, followed by the fine branching leaf veins and delicate stem base.",
    "set08-04": "The vertical slender flower stem is revealed first through clean vertical line segments. The smooth overlapping tulip cup petals then appear one by one, followed by the broad pointed green leaf and delicate flower base.",
    "set08-05": "The turned wooden handle and base pivot are revealed first through clean line segments. The radial curved bamboo structural ribs then appear one by one, followed by the clean perimeter sheet binding and fine lattice lines.",
    "set08-06": "The circular glass flask outline and flared lip are revealed first through clean curved line segments. The three round surface dew droplets then appear one by one, followed by the delicate light reflection arcs and level base.",
    "set08-07": "The cross spar spar of the diamond kite is revealed first through clean geometric line segments. The stretched fabric face and tail ribbon bows then appear one by one, followed by the wooden string winder spool and fine tether cord.",
    "set08-08": "The vertical mounting rod and circular cardinal letter hub are revealed first through clean line segments. The horizontal arrow pointer and rooster silhouette then appear one by one, followed by the feathered rooster tail and comb.",
    "set08-09": "The horizontal base ledge is revealed first through clean horizontal line segments. The three tapering pointed icicle cones then appear one by one, followed by the vertical crystalline facet lines and sharp tips.",
    "set08-10": "The wide curved crescent brim contour is revealed first through clean curved line segments. The spiral woven straw texture lines then appear one by one, followed by the soft fabric headband and neat rear bow tie."
}

# 적용
for s in sets_data:
    if s["set_id"] == "set08":
        for p in s["prompts"]:
            pid = p["id"]
            if pid in reveal_dict_set08:
                # 파레트 및 모션 추출
                # 기존 프롬프트에서 subjects, palette, motion 파싱
                text = p["prompt"]
                sub_part = text.split("The only visible subjects throughout the sequence are ")[1].split(". 0-4s:")[0].split(".\n\n0-4s:")[0]
                pal_part = text.split("The restrained palette is ")[1].split(". All surrounding space stays")[0]
                mot_part = text.split("All surrounding space stays untouched pure white with no wash of any kind extending behind the subjects. ")[1].split(" All other elements remain still.")[0]
                
                new_prompt = CALM_TEMPLATE.format(
                    subjects=sub_part,
                    reveal_steps=reveal_dict_set08[pid],
                    palette=pal_part,
                    motion=mot_part
                )
                p["prompt"] = " ".join(new_prompt.split())

# Set 09 ~ 13도 동일하게 'are revealed first through... then appear one by one'으로 정밀 교체
for s in sets_data:
    if s["set_id"] in ["set09", "set10", "set11", "set12", "set13"]:
        for p in s["prompts"]:
            text = p["prompt"]
            # Draw / Begin with 변환
            text = text.replace("ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks.",
                                "hair-thin dark-charcoal linework appears progressively from the empty white field.")
            text = text.replace("Begin with ", "")
            text = text.replace("Draw the ", "Then ")
            text = text.replace(" next. Extend the ", ", followed by ")
            text = text.replace(" next. Add the ", ", followed by ")
            text = text.replace("There is strictly zero person, driver, student, live action element, asphalt darkness, city buildings or moving train anywhere. Keep all outline contours sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs.",
                                "")
            text = text.replace("There is no visible person, driver, student, live action element, wall, ceiling, darkness or heavy architecture anywhere. Keep lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs.",
                                "")
            p["prompt"] = " ".join(text.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(sets_data, f, ensure_ascii=False, indent=2)

for s in sets_data:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("성공작(prompt_calm_ch11.txt) 공식 100% 이식 완료!")

