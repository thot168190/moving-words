# -*- coding: utf-8 -*-
"""
대표님 스크린샷 실측 분석 기반 [Visibly Traced 물리 궤적 정본] 전면 장착:
1. 선화: "fine dark-charcoal ink strokes are visibly traced from one endpoint to the other across the pure white field. Each stroke is actively drawn with visible moving stroke tips, built progressively rather than fading into view." (페이드인 100% 박멸, 획이 그어지는 애니메이션 강제)
2. 채색: "an extremely pale single-tone transparent watercolor glaze fills only 20% of the flat 2D line art. Strictly zero 3D texture, zero photorealistic wood grain, zero volume shading, and zero drop shadows. Preserving flat 2D editorial picture-book aesthetic throughout." (3D 실사 렌더링 100% 원천 차단)
3. 스타일: "Style: flat 2D picture-book line-art animation, luminous transparent watercolor tint, pure flat graphic illustration, generous untouched white space."
"""

import json

VISIBLY_TRACED_TEMPLATE = """Cinematic progressive line-tracing animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are {subjects}.

0-5.5s: fine dark-charcoal strokes are visibly traced from one endpoint to the other across the pure white field. Each stroke is actively drawn with a clear beginning and ending; the illustration is built progressively stroke by stroke rather than fading into view. {reveal_steps} All previously drawn lines remain crisp, stable and flat 2D.

5.5-8s: an extremely pale, water-heavy transparent watercolor wash develops gently as a flat 2D color tint. Over 80% of the interior remains unfilled pure white paper. Strictly zero 3D realistic rendering, zero photorealistic texture, zero drop shadow, and zero dark gradient. The restrained palette is {palette}. All surrounding space stays untouched pure white. {motion} All other elements remain still. The final composition remains strictly flat 2D picture-book editorial art surrounded by generous untouched white space.

Style: flat 2D editorial picture-book illustration, fine dark-charcoal line tracing, luminous transparent watercolor tint, strictly non-photorealistic, generous untouched white space."""

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Set 11 교체
set11_scenes_traced = [
    {
        "title": "도자기 티스푼과 각설탕 두 알", "words": ["spoon", "sugar", "sweet", "stir"],
        "subjects": "one flat 2D illustrated porcelain teaspoon and two simple 2D square sugar cubes at center",
        "reveal_steps": "The clean curved outline strokes of the teaspoon handle and oval bowl are traced visibly first. The simple square outline strokes of the two sugar cubes are then traced line by line in the center.",
        "palette": "only a faint whisper of pastel tea-amber wash and soft cream tint on the flat 2D spoon",
        "motion": "The flat teaspoon outline shifts slightly by one gentle millimeter."
    },
    {
        "title": "원목 후추 그라인더 밀", "words": ["peppermill", "spice", "season", "flavor"],
        "subjects": "one flat 2D illustrated wooden pepper mill standing upright at center with a simple brass top knob",
        "reveal_steps": "The vertical side contour strokes of the pepper mill body are traced visibly first. The circular top dome and turning screw strokes are then actively drawn stroke by stroke.",
        "palette": "only a sheer flat wash of pale honey-tan on the 2D wooden body with white paper showing through",
        "motion": "The top knob outline rotates smoothly by a quarter turn."
    },
    {
        "title": "도자기 버터 디쉬와 나무 스프레더", "words": ["butter", "knife", "spread", "dairy"],
        "subjects": "one flat 2D illustrated ceramic butter dish with dome lid, resting beside a flat wooden spreader",
        "reveal_steps": "The rectangular tray outline strokes are traced visibly first. The arched dome lid strokes and small wooden spreader outlines are then actively drawn line by line.",
        "palette": "only a faint whisper of flat pastel-yellow watercolor tint and sheer maple-tan on the spreader",
        "motion": "The flat spreader outline rests poised in quiet stillness."
    },
    {
        "title": "유리 꿀단지와 원목 허니 디퍼", "words": ["honey", "dipper", "jar", "drizzle"],
        "subjects": "one flat 2D illustrated glass honey jar with ribbed contours, holding one 2D grooved honey dipper",
        "reveal_steps": "The circular jar outline strokes are traced visibly first. The concentric horizontal ring strokes and vertical dipper wand lines are then drawn stroke by stroke.",
        "palette": "only a sheer flat wash of pale translucent honey-gold on the 2D jar with white showing through",
        "motion": "One small flat golden honey drop hangs quietly from the dipper disc."
    },
    {
        "title": "도자기 머그컵과 계피 스틱", "words": ["mug", "cinnamon", "spice", "warmth"],
        "subjects": "one flat 2D illustrated ceramic cocoa mug with ear handle, holding one simple cinnamon stick",
        "reveal_steps": "The cylindrical cup outline strokes and arched handle are traced visibly first. The curled bark scroll strokes of the cinnamon stick are then actively drawn line by line.",
        "palette": "only a faint flat wash of warm oatmeal on the cup and sheer cinnamon-tan on the stick",
        "motion": "A single transparent white steam wisp rises gently from the cup rim."
    },
    {
        "title": "원목 계량 스푼 세트", "words": ["measure", "portion", "recipe", "bake"],
        "subjects": "one flat 2D illustrated set of four nested wooden measuring spoons on a simple brass ring",
        "reveal_steps": "The circular ring loop strokes are traced visibly first. The four fan-shaped spoon handle strokes and rounded bowl contour lines are then actively drawn stroke by stroke across the empty white field.",
        "palette": "only a sheer flat watercolor wash of pale beech-tan across the 2D spoon outlines with white paper showing through",
        "motion": "The smallest spoon outline settles with a tiny soft alignment."
    },
    {
        "title": "유리 소금 셰이커 양념통", "words": ["salt", "shaker", "pour", "pinch"],
        "subjects": "one flat 2D illustrated faceted glass salt shaker with a simple perforated metal dome cap",
        "reveal_steps": "The straight vertical facet strokes of the shaker body are traced visibly first. The domed cap curve and tiny shake hole dots are then actively drawn line by line.",
        "palette": "only a sheer watery-cyan tint on the flat glass outlines and pale grey on the cap",
        "motion": "The flat shaker rests in crisp, clean graphic stillness."
    },
    {
        "title": "도자기 에스프레소 잔과 받침대", "words": ["espresso", "saucer", "crema", "sip"],
        "subjects": "one flat 2D illustrated porcelain espresso cup resting on its matching 2D saucer plate",
        "reveal_steps": "The circular saucer outline strokes are traced visibly first. The small thick-walled cup contours and loop handle lines are then drawn stroke by stroke.",
        "palette": "only a faint whisper of flat hazelnut-tan watercolor wash on the crema surface",
        "motion": "A single tiny wisp of transparent steam curls softly from the cup."
    },
    {
        "title": "도자기 레몬 스퀴저 착즙기", "words": ["lemon", "citrus", "squeeze", "juice"],
        "subjects": "one flat 2D illustrated ceramic lemon squeezer dish with a radial pointed squeezing cone",
        "reveal_steps": "The circular shallow saucer outline strokes are traced visibly first. The radial pointed cone strokes and handle loop lines are then actively drawn stroke by stroke.",
        "palette": "only a sheer flat wash of pale sunny pastel-lemon watercolor tint inside the 2D dish",
        "motion": "A single flat crystal drop of juice drips softly from the spout."
    },
    {
        "title": "원목 빵 도마와 올리브 가지", "words": ["board", "olive", "sprig", "fresh"],
        "subjects": "one flat 2D illustrated round wooden paddle cutting board holding one fresh 2D olive twig",
        "reveal_steps": "The circular paddle board contour strokes are traced visibly first. The slender woody twig strokes and five pointed leaf outlines are then actively drawn line by line.",
        "palette": "only a sheer flat wash of pale olive-tan on the board and watery sage-green on the leaves",
        "motion": "The flat olive leaf outline rests in quiet, fresh graphic peace."
    }
]

set11_prompts = []
for idx, sc in enumerate(set11_scenes_traced):
    p_text = VISIBLY_TRACED_TEMPLATE.format(
        subjects=sc["subjects"],
        reveal_steps=sc["reveal_steps"],
        palette=sc["palette"],
        motion=sc["motion"]
    )
    clean_p = " ".join(p_text.split())
    set11_prompts.append({
        "id": f"set11-{str(idx+1).zfill(2)}",
        "chapter": "SET11 (주방과 식탁)",
        "title": sc["title"],
        "words": sc["words"],
        "prompt": clean_p
    })

for s in data:
    if s["set_id"] == "set11":
        s["prompts"] = set11_prompts

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("_작업/bulk_sets/set11_10.txt", "w", encoding="utf-8") as f:
    for p in set11_prompts:
        f.write(p["prompt"] + "\n\n")

print("Set 11 [Visibly Traced 물리 획 그리기 + 2D 평면 수채화 락] 적용 완료!")

