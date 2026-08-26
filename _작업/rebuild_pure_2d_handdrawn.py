# -*- coding: utf-8 -*-
"""
대표님 피드백 100% 반영 — 제품 실사 렌더링 유발 표현 전면 영구 박멸:
1. 퇴출 대상 (실사 렌더링 3D 유발어):
   - 'Cinematic' -> 'Hand-drawn 2D animation'
   - 'High-key lighting' -> 'Flat uniform illumination'
   - 'believable materials' / 'distinct, believable colors for different materials' -> 제거
   - 'porcelain' -> 'ceramic', 'crystalline' -> 'clear'
   - 'sophisticated contemporary editorial illustration' -> 'clean 2D picture-book illustration'
2. 선화 가시성 극대화:
   - 15% grey 제한 문장 전면 삭제
   - 'clear distinct dark-charcoal pencil line art is visibly drawn stroke by stroke'
"""

import json

PURE_2D_FORMULA = """Hand-drawn 2D progressive line-drawing animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. Flat uniform illumination with zero shadows. The main illustration is centered and occupies the central three-quarters of the frame with equal breathing margins on the left and right. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are {subjects}.

0-5.5s: clear distinct dark-charcoal pencil line art is visibly drawn stroke by stroke from the empty white field. Every line has a defined beginning and ending; each stroke is actively traced across the white field so the drawing is built progressively rather than fading into view. {reveal_steps} There is no visible person, hands, table surface, wall, darkness or 3D shading anywhere. Previously drawn lines remain completely crisp, stable and flat 2D.

5.5-8s: an extremely pale, water-heavy watercolor wash gently tints the flat 2D line drawing. Over 80% of the interior area remains untouched pure white paper. All color remains low-saturation, flat and transparent with zero 3D volume shading, zero gloss, zero realistic texture, and zero drop shadows. The restrained palette is {palette}. All surrounding background stays untouched pure white. {motion} All other elements remain still. The final composition is a pure flat 2D picture-book drawing surrounded by generous untouched white space.

Style: classic 2D picture-book line illustration, visible graphite pencil stroke drawing, luminous flat watercolor wash, strictly non-photorealistic, generous untouched white space."""

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Set 11 데이터 정제
scenes_clean = [
    {
        "title": "세라믹 티스푼과 각설탕 두 알", "words": ["spoon", "sugar", "sweet", "stir"],
        "subjects": "one flat 2D illustrated ceramic teaspoon resting flat at center beside two simple 2D square sugar cubes",
        "reveal_steps": "The clean curved outline strokes of the teaspoon handle and oval bowl are traced visibly first. The simple square outline strokes of the two sugar cubes are then drawn stroke by stroke in the center.",
        "palette": "only a sheer whisper of pale tea-amber tint and soft light-tan on the flat 2D spoon",
        "motion": "The flat teaspoon outline shifts slightly by one gentle millimeter."
    },
    {
        "title": "원목 후추 그라인더 밀", "words": ["peppermill", "spice", "season", "flavor"],
        "subjects": "one flat 2D illustrated wooden pepper mill standing upright at center with a simple brass top knob",
        "reveal_steps": "The vertical side contour strokes of the pepper mill body are traced visibly first. The circular top dome and turning screw strokes are then drawn stroke by stroke.",
        "palette": "only a sheer flat wash of pale honey-tan on the 2D wooden body with white paper showing through",
        "motion": "The top knob outline rotates smoothly by a quarter turn."
    },
    {
        "title": "세라믹 버터 디쉬와 나무 스프레더", "words": ["butter", "knife", "spread", "dairy"],
        "subjects": "one flat 2D illustrated ceramic butter dish with dome lid, resting beside a flat wooden spreader",
        "reveal_steps": "The rectangular tray outline strokes are traced visibly first. The arched dome lid strokes and small wooden spreader outlines are then drawn line by line.",
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
        "title": "세라믹 머그컵과 계피 스틱", "words": ["mug", "cinnamon", "spice", "warmth"],
        "subjects": "one flat 2D illustrated ceramic cocoa mug with ear handle, holding one simple cinnamon stick",
        "reveal_steps": "The cylindrical cup outline strokes and arched handle are traced visibly first. The curled bark scroll strokes of the cinnamon stick are then drawn line by line.",
        "palette": "only a faint flat wash of warm oatmeal on the cup and sheer cinnamon-tan on the stick",
        "motion": "A single transparent white steam wisp rises gently from the cup rim."
    },
    {
        "title": "원목 계량 스푼 세트", "words": ["measure", "portion", "recipe", "bake"],
        "subjects": "one flat 2D illustrated set of four nested wooden measuring spoons on a simple brass ring",
        "reveal_steps": "The circular ring loop strokes are traced visibly first. The four fan-shaped spoon handle strokes and rounded bowl contour lines are then drawn stroke by stroke.",
        "palette": "only a sheer flat watercolor wash of pale beech-tan across the 2D spoon outlines with white paper showing through",
        "motion": "The smallest spoon outline settles with a tiny soft alignment."
    },
    {
        "title": "유리 소금 셰이커 양념통", "words": ["salt", "shaker", "pour", "pinch"],
        "subjects": "one flat 2D illustrated faceted glass salt shaker with a simple perforated metal dome cap",
        "reveal_steps": "The straight vertical facet strokes of the shaker body are traced visibly first. The domed cap curve and tiny shake hole dots are then drawn line by line.",
        "palette": "only a sheer watery-cyan tint on the flat glass outlines and pale grey on the cap",
        "motion": "The flat shaker rests in crisp, clean graphic stillness."
    },
    {
        "title": "세라믹 에스프레소 잔과 받침대", "words": ["espresso", "saucer", "crema", "sip"],
        "subjects": "one flat 2D illustrated ceramic espresso cup resting on its matching 2D saucer plate",
        "reveal_steps": "The circular saucer outline strokes are traced visibly first. The small thick-walled cup contours and loop handle lines are then drawn stroke by stroke.",
        "palette": "only a faint whisper of flat hazelnut-tan watercolor wash on the crema surface",
        "motion": "A single tiny wisp of transparent steam curls softly from the cup."
    },
    {
        "title": "세라믹 레몬 스퀴저 착즙기", "words": ["lemon", "citrus", "squeeze", "juice"],
        "subjects": "one flat 2D illustrated ceramic lemon squeezer dish with a radial pointed squeezing cone",
        "reveal_steps": "The circular shallow saucer outline strokes are traced visibly first. The radial pointed cone strokes and handle loop lines are then drawn stroke by stroke.",
        "palette": "only a sheer flat wash of pale sunny pastel-lemon watercolor tint inside the 2D dish",
        "motion": "A single flat drop of juice drips softly from the spout."
    },
    {
        "title": "원목 빵 도마와 올리브 가지", "words": ["board", "olive", "sprig", "fresh"],
        "subjects": "one flat 2D illustrated round wooden paddle cutting board holding one fresh 2D olive twig",
        "reveal_steps": "The circular paddle board contour strokes are traced visibly first. The slender woody twig strokes and five pointed leaf outlines are then drawn line by line.",
        "palette": "only a sheer flat wash of pale olive-tan on the board and watery sage-green on the leaves",
        "motion": "The flat olive leaf outline rests in quiet, fresh graphic peace."
    }
]

set11_prompts = []
for idx, sc in enumerate(scenes_clean):
    p_text = PURE_2D_FORMULA.format(
        subjects=sc["subjects"],
        reveal_steps=sc["reveal_steps"],
        palette=sc["palette"],
        motion=sc["motion"]
    )
    clean_p = " ".join(p_text.split())
    # 금지어 정제
    clean_p = clean_p.replace("paper", "white space")
    clean_p = clean_p.replace("3D", "volume")
    clean_p = clean_p.replace("hands", "fingers")
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

print("Set 11 대표님 감리 피드백 100% 반영 프롬프트 재작성 완료!")

