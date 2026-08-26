# -*- coding: utf-8 -*-
"""
Set 11 (주방과 식탁 10편) - 진한 펜 전면 퇴출 -> 부드럽고 연한 [순수 연필 흑연 스케치(Soft Pale Graphite Pencil)] 정본 장착!
"""

import json

SOFT_PENCIL_TEMPLATE = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame with equal narrow breathing margins on the left and right. The subjects remain centered while both outer edges stay clear. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are {subjects}.

0-5.5s: delicate fine graphite pencil linework appears progressively from the empty white field. Every outline is soft and thin, drawn in pure pencil graphite. {reveal_steps} Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

5.5-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. The restrained palette is {palette}. All surrounding space stays untouched pure white with no wash of any kind extending behind the subjects. {motion} All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: delicate graphite pencil sketch, luminous transparent watercolor, restrained tonal contrast, generous white space, sophisticated museum-quality editorial illustration."""

set11_scenes = [
    {
        "title": "도자기 티스푼과 각설탕 두 알", "words": ["spoon", "sugar", "sweet", "stir"],
        "subjects": "one delicate porcelain teaspoon resting flat at center beside two neat square white sugar cubes",
        "reveal_steps": "The slender contoured handle and oval bowl of the ceramic spoon are revealed first through clean light pencil segments. The two square crystalline sugar cubes then appear one by one, followed by the fine edge highlights on the cubes.",
        "palette": "only the palest warm-white on the porcelain spoon with sheer sparkling white on the sugar cubes",
        "motion": "A single tiny grain of sugar detaches softly and rests beside the cube on the clean white surface."
    },
    {
        "title": "원목 후추 그라인더 밀", "words": ["peppermill", "spice", "season", "flavor"],
        "subjects": "one tall turned wooden pepper mill standing upright at center with top brass adjustment knob",
        "reveal_steps": "The cylindrical turned wooden body and curved waist are revealed first through clean pencil line segments. The rotating top dome and small brass screw knob then appear one by one, followed by the lower grinding base rings.",
        "palette": "only the palest warm chestnut on the wooden body and sheer polished brass on the top knob",
        "motion": "The top wooden knob rotates smoothly a quarter turn and comes to a complete rest."
    },
    {
        "title": "도자기 버터 디쉬와 나무 스프레더", "words": ["butter", "knife", "spread", "dairy"],
        "subjects": "one rectangular white ceramic butter dish with dome lid handle at center, and a small wooden butter spreader",
        "reveal_steps": "The rectangular flanged ceramic tray is revealed first through clean light line segments. The dome cover and top loop handle then appear one by one, followed by the flat wooden spreader lying beside it.",
        "palette": "only the palest porcelain-white on the covered dish and sheer honey-maple on the wooden spreader",
        "motion": "The butter dish and spreader rest in immaculate breakfast peace."
    },
    {
        "title": "유리 꿀단지와 원목 허니 디퍼", "words": ["honey", "dipper", "jar", "drizzle"],
        "subjects": "one ribbed clear glass honey jar at center with one turned wooden grooved honey dipper resting angled inside",
        "reveal_steps": "The rounded glass honey pot with ribbed rings is revealed first through clean curved pencil segments. The wooden honey wand with concentric discs then appears, followed by the liquid honey level line inside the pot.",
        "palette": "only the palest translucent golden-amber in the honey pot and sheer birch-blonde on the wooden dipper",
        "motion": "A single viscous amber drop of honey hangs from the lowest dipper disc in quiet suspension."
    },
    {
        "title": "도자기 머그컵과 계피 스틱", "words": ["mug", "cinnamon", "spice", "warmth"],
        "subjects": "one stout ceramic hot cocoa mug standing at center with an arched handle, holding one curled cinnamon stick",
        "reveal_steps": "The cylindrical ceramic mug body and sturdy ear handle are revealed first through clean pencil segments. The rolled bark scroll of the cinnamon stick peeking from the rim then appears, followed by the smooth rim circle.",
        "palette": "only the palest warm oatmeal-beige on the mug and a rich sheer cinnamon-tan on the bark stick",
        "motion": "A single curling whisper of transparent white steam rises slowly from the mug."
    },
    {
        "title": "원목 계량 스푼 세트", "words": ["measure", "portion", "recipe", "bake"],
        "subjects": "a nested set of four graduated wooden measuring spoons held together on a brass ring at center",
        "reveal_steps": "The circular brass connecting loop ring is revealed first through clean pencil line segments. The four fan-shaped nested wooden spoon handles then appear one by one, followed by the graduated round spoon bowls.",
        "palette": "only the palest natural beech-wood on the four spoons with sheer brass on the loop ring",
        "motion": "The smallest spoon in the nest settles with a tiny soft adjustment and rests."
    },
    {
        "title": "유리 소금 셰이커 양념통", "words": ["salt", "shaker", "pour", "pinch"],
        "subjects": "one classic faceted glass salt shaker standing upright at center with perforated dome metal cap",
        "reveal_steps": "The faceted vertical glass body is revealed first through clean geometric pencil segments. The screw-on domed stainless steel cap and tiny shake holes then appear, followed by the fine crystalline salt level line inside.",
        "palette": "only the palest cool glass-blue on the shaker walls and sheer polished chrome on the metal cap",
        "motion": "The clear salt shaker stands in crisp, clean culinary stillness."
    },
    {
        "title": "도자기 에스프레소 잔과 받침대", "words": ["espresso", "saucer", "crema", "sip"],
        "subjects": "one small fluted white porcelain espresso cup resting on its circular matching saucer at center",
        "reveal_steps": "The circular saucer plate and center depression are revealed first through clean circular pencil segments. The small thick-walled espresso cup and tiny loop handle then appear, followed by the rich crema surface level line.",
        "palette": "only the palest clean porcelain-white with a delicate whisper of hazelnut-tan crema on the surface",
        "motion": "A tiny wisp of transparent steam curls gently once from the warm cup surface."
    },
    {
        "title": "도자기 레몬 스퀴저 착즙기", "words": ["lemon", "citrus", "squeeze", "juice"],
        "subjects": "one ribbed white porcelain lemon citrus squeezer saucer sitting at center with sharp fluted cone",
        "reveal_steps": "The circular shallow collecting dish and side pouring spout are revealed first through clean light pencil segments. The pointed radial squeezing cone then appears, followed by the small handle loop and seed catching slots.",
        "palette": "only the palest clean porcelain-white with a delicate whisper of sunny pastel-lemon on the inner saucer",
        "motion": "A single tiny crystal drop of fresh citrus juice drips softly from the spout into the dish."
    },
    {
        "title": "원목 빵 도마와 올리브 가지", "words": ["board", "olive", "sprig", "fresh"],
        "subjects": "one round carved wooden paddle cutting board resting flat at center, holding one fresh leafy olive sprig",
        "reveal_steps": "The circular paddle board and handle with hanging hole are revealed first through clean pencil segments. The slender woody olive twig and five slender leaves then appear, followed by the two smooth oval green olives.",
        "palette": "only the palest warm olive-wood tan on the board and sheer sage-green on the fresh leaves",
        "motion": "The fresh olive leaf rests peaceful and still on the clean wooden surface."
    }
]

set11_prompts = []
for idx, sc in enumerate(set11_scenes):
    p_text = SOFT_PENCIL_TEMPLATE.format(
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

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for s in data:
    if s["set_id"] == "set11":
        s["prompts"] = set11_prompts

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("_작업/bulk_sets/set11_10.txt", "w", encoding="utf-8") as f:
    for p in set11_prompts:
        f.write(p["prompt"] + "\n\n")

print("Set 11 부드러운 연필 스케치 정본 완벽 이식 완료!")

