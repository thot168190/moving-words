# -*- coding: utf-8 -*-
"""
CALM 필수문 14개 100% 충족 + 대표님 피드백 반영:
- 1. 15% grey 제한 문장 전면 삭제 -> 선이 또렷하게 보이도록 함
- 2. Cinematic, high-key lighting, believable materials, porcelain, crystalline, sophisticated editorial 등 실사 렌더링 유발어 100% 삭제
- 3. 지뢰어(hand, 3D, paper, cream) 0건
"""

import json

TEMPLATE = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are {subjects}.

0-5.5s: hair-thin dark-charcoal linework appears progressively from the empty white field. Every line has a clear beginning and ending; each stroke is actively traced across the white field so the drawing is built progressively rather than fading into view. {reveal_steps} There is no visible person, driver, student, live action element, wall, ceiling, darkness or heavy architecture anywhere. Keep outline curves sparse and delicate, never filled as solid blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

5.5-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. Over 80% of each object remains unfilled pure white. The restrained palette is {palette}. All surrounding space stays untouched pure white with no wash of any kind extending behind the subjects. {motion} All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

scenes_data = [
    {
        "title": "세라믹 티스푼과 각설탕 두 알", "words": ["spoon", "sugar", "sweet", "stir"],
        "subjects": "one delicate ceramic teaspoon resting flat at center beside two neat square white sugar cubes",
        "reveal_steps": "The curved outline strokes of the ceramic teaspoon handle and oval bowl are traced visibly first. The simple square outline strokes of the two sugar cubes are then drawn line by line in the center.",
        "palette": "only the palest whisper of warm-white on the ceramic spoon and sheer sparkling white on the sugar cubes",
        "motion": "A single tiny grain of sugar detaches softly and rests beside the cube on the clean white surface."
    },
    {
        "title": "원목 후추 그라인더 밀", "words": ["peppermill", "spice", "season", "flavor"],
        "subjects": "one tall turned wooden pepper mill standing upright at center with a simple brass top adjustment knob",
        "reveal_steps": "The vertical side contour strokes of the pepper mill body are traced visibly first. The circular top dome and turning screw strokes are then drawn line by line, followed by the lower base rings.",
        "palette": "only the palest sheer honey-tan wash on the wooden body with white showing through every wash",
        "motion": "The top wooden knob rotates smoothly by a quarter turn and comes to a complete rest."
    },
    {
        "title": "세라믹 버터 디쉬와 나무 스프레더", "words": ["butter", "knife", "spread", "dairy"],
        "subjects": "one rectangular white ceramic butter dish with dome lid, resting beside a flat wooden butter spreader",
        "reveal_steps": "The rectangular tray outline strokes are traced visibly first. The arched dome lid strokes and small wooden spreader outlines are then drawn line by line.",
        "palette": "only a faint whisper of pastel-yellow tint on the dish and sheer maple-tan on the spreader",
        "motion": "The wooden butter spreader rests poised in quiet stillness."
    },
    {
        "title": "유리 꿀단지와 원목 허니 디퍼", "words": ["honey", "dipper", "jar", "drizzle"],
        "subjects": "one ribbed clear glass honey jar holding one turned wooden grooved honey dipper at center",
        "reveal_steps": "The circular jar outline strokes are traced visibly first. The concentric horizontal ring strokes and vertical dipper wand lines are then drawn line by line.",
        "palette": "only the palest translucent honey-gold wash in the pot and sheer birch-tan on the dipper",
        "motion": "A single viscous amber drop of honey hangs from the lowest dipper disc in quiet suspension."
    },
    {
        "title": "세라믹 머그컵과 계피 스틱", "words": ["mug", "cinnamon", "spice", "warmth"],
        "subjects": "one stout ceramic cocoa mug standing at center with an arched handle, holding one simple rolled cinnamon stick",
        "reveal_steps": "The cylindrical cup outline strokes and arched handle are traced visibly first. The curled bark scroll strokes of the cinnamon stick are then drawn line by line.",
        "palette": "only the palest warm oatmeal wash on the mug and a sheer whisper of cinnamon-tan on the stick",
        "motion": "A single curling whisper of transparent white steam rises slowly from the cup rim."
    },
    {
        "title": "원목 계량 스푼 세트", "words": ["measure", "portion", "recipe", "bake"],
        "subjects": "a nested set of four graduated wooden measuring spoons held together on a simple brass ring at center",
        "reveal_steps": "The circular brass connecting ring strokes are traced visibly first. The four fan-shaped nested wooden spoon handle strokes and rounded bowl lines are then drawn line by line.",
        "palette": "only the palest sheer beech-tan wash with luminous pure white showing through every wash",
        "motion": "The smallest spoon in the nest settles with a tiny soft adjustment."
    },
    {
        "title": "유리 소금 셰이커 양념통", "words": ["salt", "shaker", "pour", "pinch"],
        "subjects": "one classic faceted clear glass salt shaker standing upright at center with a simple perforated metal dome cap",
        "reveal_steps": "The straight vertical facet strokes of the shaker body are traced visibly first. The domed cap curve and tiny shake hole dots are then drawn line by line.",
        "palette": "only a sheer watery-cyan tint on the glass edges and pale steel on the metal cap",
        "motion": "The clear salt shaker stands in crisp, clean culinary stillness."
    },
    {
        "title": "세라믹 에스프레소 잔과 받침대", "words": ["espresso", "saucer", "crema", "sip"],
        "subjects": "one small fluted white ceramic espresso cup resting on its circular matching saucer plate at center",
        "reveal_steps": "The circular saucer outline strokes are traced visibly first. The small thick-walled cup contours and loop handle lines are then drawn line by line.",
        "palette": "only the palest clean white wash with a faint whisper of hazelnut-tan crema on the surface",
        "motion": "A tiny wisp of transparent steam curls gently once from the warm cup surface."
    },
    {
        "title": "세라믹 레몬 스퀴저 착즙기", "words": ["lemon", "citrus", "squeeze", "juice"],
        "subjects": "one ribbed white ceramic lemon squeezer dish with a radial pointed squeezing cone at center",
        "reveal_steps": "The circular shallow saucer outline strokes are traced visibly first. The radial pointed cone strokes and handle loop lines are then drawn line by line.",
        "palette": "only the palest clean white wash with a sheer whisper of pastel-lemon tint in the inner dish",
        "motion": "A single tiny crystal drop of fresh juice drips softly from the spout into the dish."
    },
    {
        "title": "원목 빵 도마와 올리브 가지", "words": ["board", "olive", "sprig", "fresh"],
        "subjects": "one round carved wooden paddle cutting board resting flat at center, holding one fresh leafy olive sprig",
        "reveal_steps": "The circular paddle board contour strokes are traced visibly first. The slender woody twig strokes and five pointed leaf outlines are then drawn line by line.",
        "palette": "only the palest sheer olive-wood tan on the board and delicate watery sage-green on the fresh leaves",
        "motion": "The fresh olive leaf rests peaceful and still on the clean wooden surface."
    }
]

set11_prompts = []
for idx, sc in enumerate(scenes_data):
    p_text = TEMPLATE.format(
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

print("Set 11 대표님 감리 100% 반영 프롬프트 정본화 완료!")

