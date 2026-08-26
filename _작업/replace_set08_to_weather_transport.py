# -*- coding: utf-8 -*-
"""
대표님 지적: "바다 항해가 또 있어???" (바다/항해 중복 100% 퇴출!)
Set 08을 [시간·계절·날씨 & 철도·교통]으로 전면 교체!
"""

import json

NEW_SET08 = {
    "set_id": "set08",
    "set_name": "Set 08 (철도·교통 & 계절·날씨)",
    "target_chapter": "ch5 CIVITAS & ch10 TEMPUS",
    "target_branches": "철도와 교통, 사계절과 날씨, 시간과 때",
    "scenes": [
        {
            "title": "클래식 증기 기관차와 수평 철길 선로", "words": ["train", "rail", "track", "engine", "whistle"],
            "subjects": "one classic black steam locomotive engine resting on level horizontal steel rails at center, with clean drive wheels and cowcatcher",
            "draw_steps": "Begin with the perfectly level twin steel rail lines. Draw the heavy boiler cylinder, cab window and cowcatcher next. Extend the track lines equally toward both outer thirds. Add the tall smokestack and headlamp.",
            "palette": "only the palest translucent charcoal-grey on the locomotive body and sheer warm brass on the boiler fittings",
            "motion": "One soft puff of transparent white steam curls gently from the smokestack and floats away."
        },
        {
            "title": "클래식 자전거와 가죽 안장, 라탄 바구니", "words": ["bicycle", "pedal", "spoke", "saddle", "wheel"],
            "subjects": "one vintage roadster bicycle standing in clean side profile at center, with slender spoked wheels, leather saddle and front wicker basket",
            "draw_steps": "Begin with the circular contours of the two spoked wheels. Draw the diamond chassis tubes and swept handlebars next. Extend the pedal crank and leather saddle. Add the small front woven basket.",
            "palette": "only the palest British racing green on the bike chassis, warm honey-tan on the leather saddle, and sheer straw-buff on the basket",
            "motion": "The front wheel turns smoothly a tiny quarter turn and comes to a complete gentle rest."
        },
        {
            "title": "복엽기 프로펠러와 아날로그 고도계", "words": ["airplane", "propeller", "flight", "altitude", "cockpit"],
            "subjects": "one sculpted wooden aircraft propeller mounted on a nose hub at center, resting beside a circular analog altimeter dial",
            "draw_steps": "Begin with the central propeller hub. Draw the two twisted aerodynamic wooden blades next. Extend the circular dial casing beside it. Add the fine needle and graduated feet markings.",
            "palette": "only the palest laminated birch-blonde on the propeller and sheer brushed aluminum on the altimeter bezel",
            "motion": "The dual propeller blades give a single soft metallic gleam of light along their leading edge."
        },
        {
            "title": "클래식 장우산과 노란 장화 한 켤레", "words": ["umbrella", "boots", "rain", "puddle", "shelter"],
            "subjects": "one neatly furled black walking umbrella with curved wooden handle standing upright at center, beside a pair of bright yellow rubber rain boots",
            "draw_steps": "Begin with the straight shaft and hooked wooden cane handle of the umbrella. Draw the folded waterproof canopy next. Extend the two rubber boots side by side. Add two delicate concentric puddle rings.",
            "palette": "only the palest charcoal on the umbrella cloth, a cheerful whisper of pastel yellow on the boots, and faint translucent sky-blue around the base",
            "motion": "A single crystal clear raindrop slides gently down the umbrella tip and rests still."
        },
        {
            "title": "포근한 털목도리를 두른 작은 눈사람", "words": ["snowman", "scarf", "frost", "winter", "chill"],
            "subjects": "one charming round snowman standing at center with a plaid knitted scarf and small twig arms, topped with three pebble buttons",
            "draw_steps": "Begin with the two stacked spherical snow globes. Draw the draped knitted scarf and fringe next. Extend the two slender branching twig arms. Add three tiny pebble buttons down the front.",
            "palette": "only the palest pure snow-white with sheer sky-blue cast shadows, and a faint whisper of berry-red on the scarf",
            "motion": "A single delicate white snowflake drifts softly down to rest upon the snowman's head."
        },
        {
            "title": "가을 단풍잎과 도토리, 벌어진 밤송이", "words": ["autumn", "maple", "acorn", "chestnut", "harvest"],
            "subjects": "a graceful cluster of three serrated red maple leaves at center, resting with two smooth brown acorns and one prickly open chestnut burr",
            "draw_steps": "Begin with the radiating veins and five pointed lobes of the main maple leaf. Draw the companion leaves next. Extend the two glossy acorns in their textured cups. Add the spiky outer chestnut shell.",
            "palette": "only the palest translucent amber-orange and crimson on the maple leaves, and sheer warm fawn-brown on the acorns",
            "motion": "One small maple leaf stem shifts gently once in the quiet autumn air and stays still."
        },
        {
            "title": "봄 벚꽃 나뭇가지와 내려앉은 나비", "words": ["spring", "blossom", "petal", "butterfly", "flutter"],
            "subjects": "one slender flowering cherry blossom twig arching gracefully at center with delicate five-petal blooms, and a single swallowtail butterfly resting on one blossom",
            "draw_steps": "Begin with the organic curving woody branch. Draw the clusters of open cherry blossoms and round buds next. Extend the delicate veined wings of the perched butterfly. Add the fine pollen stamens.",
            "palette": "only the palest translucent blush-pink on the flower petals, soft bark-grey on the branch, and a delicate pastel yellow on the butterfly",
            "motion": "The butterfly wings open and close once in a slow, silent, graceful flutter."
        },
        {
            "title": "여름 밀짚모자와 대나무 부채", "words": ["summer", "straw", "hat", "shade", "breeze"],
            "subjects": "one wide-brimmed woven straw sun hat resting flat at center with a pale linen ribbon, beside a traditional flat bamboo fan",
            "draw_steps": "Begin with the rounded crown and circular woven brim of the sun hat. Draw the tied fabric ribbon next. Extend the radial bamboo fan ribs and paper leaf. Add the turned wooden handle.",
            "palette": "only the palest sunlit wheat-straw on the hat, sheer sky-blue on the ribbon, and pale natural bamboo-buff on the fan",
            "motion": "The delicate ribbon ends flutter softly once in a warm summer draft and come to rest."
        },
        {
            "title": "황동 회중시계와 유리 모래시계", "words": ["pocket", "watch", "hourglass", "time", "seconds"],
            "subjects": "one open-faced vintage brass pocket watch with geometric hour markers at center, resting beside a slender glass hourglass with falling fine sand",
            "draw_steps": "Begin with the circular bezel and top winding crown of the pocket watch. Draw the fine indicator pointers and chapter ring next. Extend the waist of the blown glass hourglass beside it. Add the wooden end plates.",
            "palette": "only the palest warm brass-gold on the watch case and sheer translucent honey-amber in the hourglass sand",
            "motion": "A continuous hairline trickle of golden sand grains falls steadily inside the quiet glass waist."
        },
        {
            "title": "클래식 수은 온도계와 금속 풍향계", "words": ["thermometer", "forecast", "degree", "weather", "vane"],
            "subjects": "one slender vertical glass weather thermometer mounted on a brass plaque at center, beside a rotating arrow wind vane atop a compass rose",
            "draw_steps": "Begin with the rectangular mounting board and glass thermometer tube. Draw the Fahrenheit and Celsius scale marks next. Extend the vertical pivot shaft and arrow wind vane. Add the four cardinal direction arms.",
            "palette": "only the palest verdigris-bronze on the weather vane and sheer mercury-silver in the thermometer stem",
            "motion": "The arrow of the wind vane swings smoothly once to the east and points steady into the breeze."
        }
    ]
}

# 검증 정본 템플릿으로 프롬프트 빌드
PROVEN_SAFE_TEMPLATE = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are {subjects}.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. {draw_steps} There is no visible person, driver, student, live action element, wall, ceiling, darkness or heavy architecture anywhere. Keep lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is {palette}. All surrounding space stays untouched pure white with no wash of any kind extending behind the subjects. {motion} All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

set08_prompts = []
for idx, sc in enumerate(NEW_SET08["scenes"]):
    p_text = PROVEN_SAFE_TEMPLATE.format(
        subjects=sc["subjects"],
        draw_steps=sc["draw_steps"],
        palette=sc["palette"],
        motion=sc["motion"]
    )
    clean_p = " ".join(p_text.split())
    # 지뢰어 정제
    clean_p = clean_p.replace("paper", "sheet")
    clean_p = clean_p.replace("arm", "lever")
    clean_p = clean_p.replace("arms", "levers")
    clean_p = clean_p.replace("branching twig levers", "branching twig twigs")
    
    set08_prompts.append({
        "id": f"set08-{str(idx+1).zfill(2)}",
        "chapter": "SET08 (철도와 교통, 사계절과 날씨)",
        "title": sc["title"],
        "words": sc["words"],
        "prompt": clean_p
    })

# complete_100_data.json 내부 교체
for s in data:
    if s["set_id"] == "set08":
        s["set_name"] = NEW_SET08["set_name"]
        s["target_chapter"] = NEW_SET08["target_chapter"]
        s["target_branches"] = NEW_SET08["target_branches"]
        s["prompts"] = set08_prompts

with open("_작업/bulk_sets/set08_10.txt", "w", encoding="utf-8") as f:
    for p in set08_prompts:
        f.write(p["prompt"] + "\n\n")

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Set 08 바다/항해 100% 완전 퇴출 -> [철도·교통 & 계절·날씨 10편]으로 전면 교체 완료!")

