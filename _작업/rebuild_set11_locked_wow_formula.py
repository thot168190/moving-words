# -*- coding: utf-8 -*-
"""
대표님이 직접 채택하신 [산호 협곡 WOW 잠금 공식] 100% 원형 복원:
_작업/01_지시서/프롬프트_공식_잠금.md 에 명시된 8블록 골격을 단 1글자도 창작 없이 그대로 적용!
"""

import json

WOW_TEMPLATE = """Cinematic progressive ink-line construction and kitchen-tableware motion animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are {subject1}, {subject2}, {subject3}, {subject4} and {subject5}. 0-3.5s: fine dark-charcoal ink strokes are visibly traced from one endpoint to the other across the completely empty white field. {structure1} forms first through many short contour and hatching strokes. {structure2} then grows progressively from the base structure. Finally, {hero} is constructed stroke by stroke in the center. Each individual stroke has a clear beginning and ending; the illustration is built progressively rather than fading into view. 3.5-5.5s: transparent watercolor develops in layered depth. {color1} settles into the background base first, followed by {color2} in the middle accents, then a small area of {color3} at the center. The main subject remains luminous with a narrow untouched white rim. The fittings receive restrained {color4} and {color5} accents. 5.5-8s: {hero} performs one slow gentle movement with one subtle detail shift. {accessory} sways subtly in a quiet kitchen draft, while a few tiny steam particles drift upward at different depths. All fine ink lines remain stable. There is no visible person, chef or room interior boundary. Strong foreground, middle-ground and distant layers create the feeling of quiet morning tableware. Style: intricate natural-history engraving, luminous transparent watercolor, restrained tableware palette, cinematic depth, graceful realistic motion, sophisticated museum-quality editorial illustration."""

scenes_set11 = [
    {
        "title": "도자기 티스푼과 각설탕 두 알", "words": ["spoon", "sugar", "sweet", "stir"],
        "s1": "one illustrated porcelain teaspoon", "s2": "two square sugar cubes", "s3": "a delicate saucer rim", "s4": "soft tea droplets", "s5": "a few restrained steam particles",
        "st1": "A delicate saucer baseline", "st2": "Two crystalline sugar cubes", "hero": "one graceful porcelain teaspoon",
        "c1": "Pale warm-warm-ivory", "c2": "sheer sparkling white", "c3": "muted amber-tan", "c4": "porcelain white", "c5": "soft tea gold",
        "hero_motion": "the porcelain teaspoon glides slowly across the saucer with one gentle stirring angle", "acc": "The two sugar cubes"
    },
    {
        "title": "원목 후추 그라인더 밀", "words": ["peppermill", "spice", "season", "flavor"],
        "s1": "one tall turned wooden pepper mill", "s2": "a brass adjustment knob", "s3": "a solid tabletop baseline", "s4": "three cracked peppercorns", "s5": "a few restrained spice specks",
        "st1": "A solid wooden tabletop baseline", "st2": "The cylindrical turned wooden body and waist", "hero": "the top rotating dome and brass screw knob",
        "c1": "Pale warm chestnut", "c2": "sheer honey-tan", "c3": "luminous brass-gold", "c4": "walnut brown", "c5": "subtle gold",
        "hero_motion": "the top wooden knob turns slowly by one small quarter increment", "acc": "The cracked peppercorns"
    },
    {
        "title": "도자기 버터 디쉬와 나무 스프레더", "words": ["butter", "knife", "spread", "dairy"],
        "s1": "one rectangular ceramic butter dish", "s2": "a flanged ceramic lid", "s3": "a flat wooden spreader", "s4": "a clean table baseline", "s5": "a few restrained light particles",
        "st1": "A clean rectangular dish base", "st2": "The dome cover and top loop handle", "hero": "one slender wooden butter spreader",
        "c1": "Pale porcelain-white", "c2": "sheer butter-yellow", "c3": "muted honey-maple", "c4": "cool ceramic grey", "c5": "soft birch tan",
        "hero_motion": "the wooden spreader rests gently with one tiny subtle angle shift", "acc": "The flanged ceramic dish"
    },
    {
        "title": "유리 꿀단지와 원목 허니 디퍼", "words": ["honey", "dipper", "jar", "drizzle"],
        "s1": "one ribbed clear glass honey jar", "s2": "one grooved wooden honey dipper", "s3": "a level table baseline", "s4": "one hanging amber honey drop", "s5": "a few restrained golden reflections",
        "st1": "A rounded glass honey pot base", "st2": "The concentric glass rib rings and rim", "hero": "one turned wooden honey dipper",
        "c1": "Pale watery aqua-glass", "c2": "luminous golden-amber", "c3": "sheer birch-blonde", "c4": "warm honey gold", "c5": "clear glass white",
        "hero_motion": "the lowest honey dipper disc releases one slow hanging amber drop", "acc": "The clear glass jar"
    },
    {
        "title": "도자기 머그컵과 계피 스틱", "words": ["mug", "cinnamon", "spice", "warmth"],
        "s1": "one stout ceramic cocoa mug", "s2": "one curled cinnamon stick", "s3": "a sturdy ear handle", "s4": "a clean coaster baseline", "s5": "a few restrained steam particles",
        "st1": "A solid cylindrical mug baseline", "st2": "The smooth ceramic cup wall and loop handle", "hero": "one rolled cinnamon bark stick",
        "c1": "Pale oatmeal-beige", "c2": "sheer cinnamon-tan", "c3": "muted cocoa-brown", "c4": "warm warm-ivory", "c5": "soft bark grey",
        "hero_motion": "a single whisper of transparent white steam curls gently from the cup rim", "acc": "The curled cinnamon stick"
    },
    {
        "title": "원목 계량 스푼 세트", "words": ["measure", "portion", "recipe", "bake"],
        "s1": "a nested set of four wooden measuring spoons", "s2": "a circular brass loop ring", "s3": "a level counter baseline", "s4": "four contoured spoon bowls", "s5": "a few restrained woodgrain lines",
        "st1": "A level wooden countertop baseline", "st2": "The circular brass connecting loop ring", "hero": "four nested wooden spoon handles and bowls",
        "c1": "Pale natural beech-wood", "c2": "sheer warm-birch", "c3": "luminous brass-gold", "c4": "soft oak tan", "c5": "subtle champagne",
        "hero_motion": "the smallest spoon in the nest settles smoothly by one tiny millimeter", "acc": "The brass connecting loop"
    },
    {
        "title": "유리 소금 셰이커 양념통", "words": ["salt", "shaker", "pour", "pinch"],
        "s1": "one faceted clear glass salt shaker", "s2": "a perforated steel dome cap", "s3": "a level table baseline", "s4": "fine crystalline salt grains", "s5": "a few restrained light glints",
        "st1": "A faceted vertical glass baseline", "st2": "The internal crystalline salt level", "hero": "the domed perforated steel cap",
        "c1": "Pale cool glass-blue", "c2": "sheer sparkling salt-white", "c3": "polished chrome-silver", "c4": "cool grey", "c5": "bright steel white",
        "hero_motion": "a single micro-glint of light sparkles softly once across the metal dome cap", "acc": "The faceted glass walls"
    },
    {
        "title": "도자기 에스프레소 잔과 받침대", "words": ["espresso", "saucer", "crema", "sip"],
        "s1": "one small porcelain espresso cup", "s2": "a matching circular saucer", "s3": "a rich crema surface", "s4": "a clean table baseline", "s5": "a few restrained steam wisps",
        "st1": "A circular saucer baseline", "st2": "The thick-walled ceramic espresso cup and handle", "hero": "the rich golden-hazelnut crema layer",
        "c1": "Pale porcelain-white", "c2": "sheer hazelnut-tan", "c3": "muted espresso-brown", "c4": "warm warm-ivory", "c5": "soft gold",
        "hero_motion": "a single tiny wisp of transparent steam rises slowly from the crema surface", "acc": "The circular saucer plate"
    },
    {
        "title": "도자기 레몬 스퀴저 착즙기", "words": ["lemon", "citrus", "squeeze", "juice"],
        "s1": "one ribbed porcelain lemon squeezer", "s2": "a shallow collecting dish", "s3": "a sharp fluted cone", "s4": "a level counter baseline", "s5": "a few restrained juice droplets",
        "st1": "A shallow circular dish baseline", "st2": "The handle loop and pouring spout", "hero": "the sharp radial squeezing cone",
        "c1": "Pale porcelain-white", "c2": "sheer pastel-lemon", "c3": "luminous citrus-gold", "c4": "cool white", "c5": "subtle yellow",
        "hero_motion": "a single tiny crystal drop of fresh juice drips softly from the spout into the dish", "acc": "The fluted porcelain cone"
    },
    {
        "title": "원목 빵 도마와 올리브 가지", "words": ["board", "olive", "sprig", "fresh"],
        "s1": "one round wooden cutting board", "s2": "one fresh leafy olive sprig", "s3": "two smooth oval green olives", "s4": "a level table baseline", "s5": "a few restrained leaf veins",
        "st1": "A level wooden table baseline", "st2": "The circular wooden paddle board with handle", "hero": "one leafy olive branch with two olives",
        "c1": "Pale warm olive-wood", "c2": "sheer sage-green", "c3": "muted olive-tan", "c4": "birch blonde", "c5": "soft leaf jade",
        "hero_motion": "the fresh olive leaf tip settles gently with one quiet micro-motion", "acc": "The round wooden paddle board"
    }
]

set11_prompts = []
for idx, sc in enumerate(scenes_set11):
    p_text = WOW_TEMPLATE.format(
        subject1=sc["s1"], subject2=sc["s2"], subject3=sc["s3"], subject4=sc["s4"], subject5=sc["s5"],
        structure1=sc["st1"], structure2=sc["st2"], hero=sc["hero"],
        color1=sc["c1"], color2=sc["c2"], color3=sc["c3"], color4=sc["c4"], color5=sc["c5"],
        hero_motion=sc["hero_motion"], accessory=sc["acc"]
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

print("Set 11 [산호협곡 WOW 잠금 정본 공식 100%] 원형 복원 완료!")

