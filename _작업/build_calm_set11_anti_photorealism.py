# -*- coding: utf-8 -*-
"""
CALM 정본 공식 기반 3D 실사화 원천 박멸 빌더:
- 0-5.5s: fine dark-charcoal linework appears progressively from the empty white field.
- 5.5-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Over 80% of each object's interior remains unfilled pure white.
- Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space.
"""

import json

CALM_ANTI_3D_TEMPLATE = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are {subjects}.

0-5.5s: delicate fine graphite pencil linework appears progressively from the empty white field. Every outline is soft and thin, drawn in pure pencil graphite. {reveal_steps} There is no visible person, driver, student, live action element, wall, ceiling, darkness or heavy architecture anywhere. Keep outline curves sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

5.5-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is {palette}. All surrounding space stays untouched pure white with no wash of any kind extending behind the subjects. {motion} All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

set11_scenes_calm = [
    {
        "title": "도자기 티스푼과 각설탕 두 알", "words": ["spoon", "sugar", "sweet", "stir"],
        "subjects": "one delicate porcelain teaspoon resting flat at center beside two neat square white sugar cubes",
        "reveal_steps": "The slender contoured handle and oval bowl of the ceramic spoon are revealed first through clean light pencil segments. The two square crystalline sugar cubes then appear one by one, followed by the fine edge highlights on the cubes.",
        "palette": "only the palest whisper of warm-white on the porcelain spoon and sheer sparkling white on the sugar cubes",
        "motion": "A single tiny grain of sugar detaches softly and rests beside the cube on the clean white surface."
    },
    {
        "title": "원목 후추 그라인더 밀", "words": ["peppermill", "spice", "season", "flavor"],
        "subjects": "one tall turned wooden pepper mill standing upright at center with top brass adjustment knob",
        "reveal_steps": "The cylindrical turned wooden body and curved waist are revealed first through clean pencil line segments. The rotating top dome and small brass screw knob then appear one by one, followed by the lower grinding base rings.",
        "palette": "only the palest sheer honey-tan wash on the wood and faint brass tint on the knob",
        "motion": "The top wooden knob rotates smoothly a quarter turn and comes to a complete rest."
    },
    {
        "title": "도자기 버터 디쉬와 나무 스프레더", "words": ["butter", "knife", "spread", "dairy"],
        "subjects": "one rectangular white ceramic butter dish with dome lid handle at center, and a small wooden butter spreader",
        "reveal_steps": "The rectangular flanged ceramic tray is revealed first through clean light line segments. The dome cover and top loop handle then appear one by one, followed by the flat wooden spreader lying beside it.",
        "palette": "only a faint whisper of pastel-yellow tint on the dish and sheer maple-tan on the spreader",
        "motion": "The butter dish and spreader rest in immaculate breakfast peace."
    },
    {
        "title": "유리 꿀단지와 원목 허니 디퍼", "words": ["honey", "dipper", "jar", "drizzle"],
        "subjects": "one ribbed clear glass honey jar at center with one turned wooden grooved honey dipper resting angled inside",
        "reveal_steps": "The rounded glass honey pot with ribbed rings is revealed first through clean curved pencil segments. The wooden honey wand with concentric discs then appears, followed by the liquid honey level line inside the pot.",
        "palette": "only the palest translucent honey-gold wash in the pot and sheer birch-tan on the dipper",
        "motion": "A single viscous amber drop of honey hangs from the lowest dipper disc in quiet suspension."
    },
    {
        "title": "도자기 머그컵과 계피 스틱", "words": ["mug", "cinnamon", "spice", "warmth"],
        "subjects": "one stout ceramic hot cocoa mug standing at center with an arched handle, holding one curled cinnamon stick",
        "reveal_steps": "The cylindrical ceramic mug body and sturdy ear handle are revealed first through clean pencil segments. The rolled bark scroll of the cinnamon stick peeking from the rim then appears, followed by the smooth rim circle.",
        "palette": "only the palest warm oatmeal wash on the mug and a sheer whisper of cinnamon-tan on the stick",
        "motion": "A single curling whisper of transparent white steam rises slowly from the mug."
    },
    {
        "title": "원목 계량 스푼 세트", "words": ["measure", "portion", "recipe", "bake"],
        "subjects": "a nested set of four graduated wooden measuring spoons held together on a brass ring at center",
        "reveal_steps": "The circular brass connecting loop ring is revealed first through clean pencil line segments. The four fan-shaped nested wooden spoon handles then appear one by one, followed by the graduated round spoon bowls.",
        "palette": "only the palest sheer beech-tan wash with luminous pure white showing through every wash",
        "motion": "The smallest spoon in the nest settles with a tiny soft adjustment and rests."
    },
    {
        "title": "유리 소금 셰이커 양념통", "words": ["salt", "shaker", "pour", "pinch"],
        "subjects": "one classic faceted glass salt shaker standing upright at center with perforated dome metal cap",
        "reveal_steps": "The faceted vertical glass body is revealed first through clean geometric pencil segments. The screw-on domed stainless steel cap and tiny shake holes then appear, followed by the fine crystalline salt level line inside.",
        "palette": "only a sheer watery-cyan tint on the glass edges and pale steel on the metal cap",
        "motion": "The clear salt shaker stands in crisp, clean culinary stillness."
    },
    {
        "title": "도자기 에스프레소 잔과 받침대", "words": ["espresso", "saucer", "crema", "sip"],
        "subjects": "one small fluted white porcelain espresso cup resting on its circular matching saucer at center",
        "reveal_steps": "The circular saucer plate and center depression are revealed first through clean circular pencil segments. The small thick-walled espresso cup and tiny loop handle then appear, followed by the rich crema surface level line.",
        "palette": "only the palest clean porcelain-white with a faint whisper of hazelnut-tan crema on the surface",
        "motion": "A tiny wisp of transparent steam curls gently once from the warm cup surface."
    },
    {
        "title": "도자기 레몬 스퀴저 착즙기", "words": ["lemon", "citrus", "squeeze", "juice"],
        "subjects": "one ribbed white porcelain lemon citrus squeezer saucer sitting at center with sharp fluted cone",
        "reveal_steps": "The circular shallow collecting dish and side pouring spout are revealed first through clean light pencil segments. The pointed radial squeezing cone then appears, followed by the small handle loop and seed catching slots.",
        "palette": "only the palest clean porcelain-white with a sheer whisper of pastel-lemon tint in the inner dish",
        "motion": "A single tiny crystal drop of fresh citrus juice drips softly from the spout into the dish."
    },
    {
        "title": "원목 빵 도마와 올리브 가지", "words": ["board", "olive", "sprig", "fresh"],
        "subjects": "one round carved wooden paddle cutting board resting flat at center, holding one fresh leafy olive sprig",
        "reveal_steps": "The circular paddle board and handle with hanging hole are revealed first through clean pencil segments. The slender woody olive twig and five slender leaves then appear, followed by the two smooth oval green olives.",
        "palette": "only the palest sheer olive-wood tan on the board and delicate watery sage-green on the fresh leaves",
        "motion": "The fresh olive leaf rests peaceful and still on the clean wooden surface."
    }
]

set11_prompts = []
for idx, sc in enumerate(set11_scenes_calm):
    p_text = CALM_ANTI_3D_TEMPLATE.format(
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

print("Set 11 CALM 정본 2D 수채화 락 완벽 이식 완료!")

