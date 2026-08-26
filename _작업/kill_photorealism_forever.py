# -*- coding: utf-8 -*-
"""
3D 실사화 원천 종결 (Kill Photorealism Forever):
1. 3D 유발 단어 영구 소탕: 'cinematic depth', 'realistic motion', 'layered depth', 'Strong foreground... layers'
2. 2D 수채화 삽화 락:
   - "an extremely pale, water-heavy watercolor wash develops gently as a delicate 20% transparent tint. Over 80% of the interior area remains completely unpainted pure white. All color remains strictly flat, non-photorealistic, and luminous."
3. Style: "Style: delicate fine-line illustration, luminous transparent watercolor wash, flat 2D editorial picture-book aesthetic, generous pure white space."
"""

import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Set 11 프롬프트 전면 2D 수채화 락 적용
PURE_2D_TEMPLATE = """Cinematic progressive ink-line construction on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are {subject1}, {subject2}, {subject3}, {subject4} and {subject5}. 0-3.5s: fine dark-charcoal ink strokes are visibly traced from one endpoint to the other across the completely empty white field. {structure1} forms first through many short contour and hatching strokes. {structure2} then grows progressively from the base structure. Finally, {hero} is constructed stroke by stroke in the center. Each individual stroke has a clear beginning and ending; the illustration is built progressively rather than fading into view. 3.5-5.5s: an extremely pale, water-heavy watercolor wash develops gently as a sparse, sheer accent tint. Over 80% of the object interior remains unfilled pure white, preserving flat 2D line art. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. The restrained palette is {palette}. 5.5-8s: {hero} performs one slow gentle movement with one subtle detail shift. {accessory} sways subtly in a quiet kitchen draft, while a few tiny steam particles drift upward at different depths. All fine ink lines remain stable. There is no visible person, chef or room interior boundary. The final composition remains strictly flat 2D editorial line art surrounded by generous untouched white space. Style: delicate fine-line illustration, luminous transparent watercolor, restrained tableware palette, flat 2D picture-book art, sophisticated museum-quality editorial illustration."""

# Set 11에 적용
scenes_set11_2d = [
    ("one illustrated porcelain teaspoon", "two square sugar cubes", "a delicate saucer rim", "soft tea droplets", "a few restrained steam particles",
     "A delicate saucer baseline", "Two crystalline sugar cubes", "one graceful porcelain teaspoon",
     "only the palest whisper of warm-white and translucent tea-amber tint",
     "the porcelain teaspoon glides slowly across the saucer with one gentle stirring angle", "The two sugar cubes"),
     
    ("one tall turned wooden pepper mill", "a brass adjustment knob", "a solid tabletop baseline", "three cracked peppercorns", "a few restrained spice specks",
     "A solid wooden tabletop baseline", "The cylindrical turned wooden body and waist", "the top rotating dome and brass screw knob",
     "only the palest sheer honey-tan wash on the wood and faint brass tint on the knob",
     "the top wooden knob turns slowly by one small quarter increment", "The cracked peppercorns"),
     
    ("one rectangular ceramic butter dish", "a flanged ceramic lid", "a flat wooden spreader", "a clean table baseline", "a few restrained light particles",
     "A clean rectangular dish base", "The dome cover and top loop handle", "one slender wooden butter spreader",
     "only a faint whisper of pastel-yellow tint and sheer maple-tan on the spreader",
     "the wooden spreader rests gently with one tiny subtle angle shift", "The flanged ceramic dish"),
     
    ("one ribbed clear glass honey jar", "one grooved wooden honey dipper", "a level table baseline", "one hanging amber honey drop", "a few restrained golden reflections",
     "A rounded glass honey pot base", "The concentric glass rib rings and rim", "one turned wooden honey dipper",
     "only the palest translucent honey-gold wash and sheer birch-tan on the dipper",
     "the lowest honey dipper disc releases one slow hanging amber drop", "The clear glass jar"),
     
    ("one stout ceramic cocoa mug", "one curled cinnamon stick", "a sturdy ear handle", "a clean coaster baseline", "a few restrained steam particles",
     "A solid cylindrical mug baseline", "The smooth ceramic cup wall and loop handle", "one rolled cinnamon bark stick",
     "only the palest warm oatmeal wash on the mug and a whisper of cinnamon-tan on the stick",
     "a single whisper of transparent white steam curls gently from the cup rim", "The curled cinnamon stick"),
     
    ("a nested set of four wooden measuring spoons", "a circular brass loop ring", "a level counter baseline", "four contoured spoon bowls", "a few restrained woodgrain lines",
     "A level wooden countertop baseline", "The circular brass connecting loop ring", "four nested wooden spoon handles and bowls",
     "only the palest sheer beech-tan wash with luminous white showing through",
     "the smallest spoon in the nest settles smoothly by one tiny millimeter", "The brass connecting loop"),
     
    ("one faceted clear glass salt shaker", "a perforated steel dome cap", "a level table baseline", "fine crystalline salt grains", "a few restrained light glints",
     "A faceted vertical glass baseline", "The internal crystalline salt level", "the domed perforated steel cap",
     "only a sheer watery-cyan tint on the glass edges and pale steel on the cap",
     "a single micro-glint of light sparkles softly once across the metal dome cap", "The faceted glass walls"),
     
    ("one small porcelain espresso cup", "a matching circular saucer", "a rich crema surface", "a clean table baseline", "a few restrained steam wisps",
     "A circular saucer baseline", "The thick-walled ceramic espresso cup and handle", "the rich golden-hazelnut crema layer",
     "only the palest porcelain wash with a faint whisper of hazelnut-tan crema",
     "a single tiny wisp of transparent steam rises slowly from the crema surface", "The circular saucer plate"),
     
    ("one ribbed porcelain lemon squeezer", "a shallow collecting dish", "a sharp fluted cone", "a level counter baseline", "a few restrained juice droplets",
     "A shallow circular dish baseline", "The handle loop and pouring spout", "the sharp radial squeezing cone",
     "only the palest clean porcelain-white with a sheer pastel-lemon tint in the dish",
     "a single tiny crystal drop of fresh juice drips softly from the spout into the dish", "The fluted porcelain cone"),
     
    ("one round wooden cutting board", "one fresh leafy olive sprig", "two smooth oval green olives", "a level table baseline", "a few restrained leaf veins",
     "A level wooden table baseline", "The circular wooden paddle board with handle", "one leafy olive branch with two olives",
     "only the palest sheer olive-wood tan on the board and delicate watery sage-green on the leaves",
     "the fresh olive leaf tip settles gently with one quiet micro-motion", "The round wooden paddle board")
]

for s in data:
    if s["set_id"] == "set11":
        for idx, sc in enumerate(scenes_set11_2d):
            p_text = PURE_2D_TEMPLATE.format(
                subject1=sc[0], subject2=sc[1], subject3=sc[2], subject4=sc[3], subject5=sc[4],
                structure1=sc[5], structure2=sc[6], hero=sc[7],
                palette=sc[8], hero_motion=sc[9], accessory=sc[10]
            )
            s["prompts"][idx]["prompt"] = " ".join(p_text.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("_작업/bulk_sets/set11_10.txt", "w", encoding="utf-8") as f:
    for p in data[7]["prompts"]: # set11
        f.write(p["prompt"] + "\n\n")

print("3D 실사화 원천 종결 -> [80% 순백 여백 + 2D 평면 수채화 락] 적용 완료!")

