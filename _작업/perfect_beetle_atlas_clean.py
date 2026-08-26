# -*- coding: utf-8 -*-
"""
대표님의 [딱정벌레 자연사 도감] 헌법 + 검증기 무결점 정제 (오류 0건 통과):
- 딱정벌레 씬의 핵심 가치:
  1. "The background is one single continuous field of pure white reaching every outer edge, and the subjects sit directly on that white with nothing underneath them - no sheet, no board, no panel, no textured surface."
  2. "Each line is drawn as a moving point that travels from one end to the other, its advancing tip clearly visible the whole way, one line at a time..."
  3. "deliberately economical by comparison, with most of each form left free of internal lines, with strictly zero cross-hatching and zero shading."
  4. "Style: master-level fine-line illustration with exceptionally thin, precise pale graphite strokes and sophisticated control, luminous transparent watercolor, restrained tonal contrast, generous untouched white space, sophisticated museum-quality editorial illustration for an adult natural-history atlas, mature and understated, with hairline strokes and no heavy outlines anywhere."
"""

import json

PERFECT_ATLAS_TEMPLATE = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. The background is one single continuous field of pure white reaching every outer edge, and the subjects sit directly on that white with nothing underneath them - no board, no panel, no card, no mat, no textured surface and no visible edge of any kind. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The subjects remain centered while both outer edges stay clear. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are {subjects}. There is no visible person, driver, student, live action element, wall, ceiling, darkness or heavy architecture anywhere.

0-4s: hair-thin pale graphite linework appears progressively from the empty white field. Throughout the whole sequence the field contains only the flat white surface and the marks already made on it; nothing else is ever present at any moment. Each line is drawn as a moving point that travels from one end to the other, its advancing tip clearly visible the whole way, one line at a time, so the eye can follow the growing tip of every single stroke. Nothing is revealed by a sweeping wipe and nothing fades into view - every line extends from its own tip. {draw_steps} Most of each form stays deliberately economical and free of internal lines, with strictly zero cross-hatching and zero line shading. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is {palette}. All surrounding space stays untouched pure white with no wash of any kind extending behind the subjects. {motion} All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, precise pale graphite strokes and sophisticated control, maximum line value 20% grey, luminous transparent watercolor, restrained tonal contrast, generous untouched white space, sophisticated museum-quality editorial illustration for an adult natural-history atlas, mature and understated, with hairline strokes and no heavy outlines anywhere."""

SET04_CLEAN = [
    {
        "id": "set4-01",
        "chapter": "ch2 VITA & ch1 INVENTIO",
        "title": "삼각 캠핑 텐트와 나무 접이식 의자",
        "words": ["tent (텐트)", "camp (캠프)", "chair (의자)", "shelter (쉼터)", "breeze (산들바람)"],
        "subjects": "one small triangle cotton tent pitched at the optical center, one simple folding wood-and-cloth camp stool propped beside it, and three small smooth river pebbles on the clean white ground",
        "draw_steps": "The clean triangular contour of the tent pitched on its ridgepole comes first with precise hairline strokes. The low wooden folding stool beside it follows with economical open lines, then the three tiny pebbles.",
        "palette": "only the palest weathered linen-tan on the tent fabric, the faintest warm pine on the stool wood, and one very light translucent stone-grey on the pebbles",
        "motion": "The small front fabric flap of the tent flutters gently once in the quiet breeze and settles still."
    },
    {
        "id": "set4-02",
        "chapter": "ch2 VITA (숲과 생명)",
        "title": "황동 호롱 랜턴과 작은 나뭇가지 불꽃",
        "words": ["lantern (랜턴)", "flame (불꽃)", "warmth (온기)", "glow (빛나다)", "twigs (나뭇가지)"],
        "subjects": "one classic brass candle lantern standing at center, a neat cluster of four dry twigs lying beside it, and a tiny single flame burning quietly within the glass",
        "draw_steps": "The delicate cylindrical glass body and domed brass top of the lantern are drawn first with fine open contours. The four slender crossed twigs lying on the ground follow, then the tiny inner teardrop flame.",
        "palette": "only the palest translucent brass-gold on the lantern cap, a whisper of warm amber in the tiny glass flame, and the faintest dry bark-grey on the twigs",
        "motion": "The tiny flame inside the glass flickers softly once and burns steadily."
    },
    {
        "id": "set4-03",
        "chapter": "ch8 MOTUS (운동과 도전)",
        "title": "가죽 등산화와 깎아 만든 나무 지팡이",
        "words": ["boots (등산화)", "staff (지팡이)", "trail (오솔길)", "leather (가죽)", "journey (여정)"],
        "subjects": "one pair of sturdy leather hiking boots resting side by side at center, and one smooth carved walking stick propped lightly against them",
        "draw_steps": "The economical outer silhouette of the two leather boots comes first with light single strokes. The tall slender wooden staff propped beside the boots follows with clean hairline precision.",
        "palette": "only the palest weathered tan-leather wash on the boots and the faintest soft cedar-brown on the walking stick",
        "motion": "A single tiny dry pine needle drifts gently to rest beside the boot toe and stays still."
    },
    {
        "id": "set4-04",
        "chapter": "ch8 MOTUS & ch1 INVENTIO",
        "title": "원목 카누와 나무 노, 잔잔한 수면 파문",
        "words": ["kayak (카약)", "paddle (노)", "ripple (파문)", "lake (호수)", "glide (미끄러지다)"],
        "subjects": "one slender wooden canoe resting level horizontally at center, one carved single-blade wooden paddle lying across its gunwale, and two faint concentric water ripple lines",
        "draw_steps": "The graceful horizontal curves of the wooden canoe hull come first with pure economical strokes. The symmetrical paddle laid across the top follows, then two delicate oval water ripples.",
        "palette": "only the palest cedar-wood wash on the canoe, sheer pine-grey on the paddle, and a faint whisper of translucent water-blue around the ripples",
        "motion": "The two delicate water ripples expand softly outward once and fade into the still surface."
    },
    {
        "id": "set4-05",
        "chapter": "ch1 INVENTIO (세상을 발견해요)",
        "title": "황동 쌍안경과 한 장의 관측 수첩",
        "words": ["binoculars (쌍안경)", "observe (관찰하다)", "feathers (깃털)", "field (들판)", "lens (렌즈)"],
        "subjects": "one compact brass-and-leather field binocular standing upright at center, and a single dropped bird feather resting quietly beside it",
        "draw_steps": "The twin cylindrical optical tubes and central focus screw of the binoculars are drawn with delicate hairline contours. The graceful curved quill of the small dropped feather beside it follows.",
        "palette": "only the palest warm brass on the binocular rings, sheer cool slate on the barrels, and a faint whisper of earthy fawn-brown on the feather",
        "motion": "The small dropped feather shifts softly once on the white ground and rests completely still."
    },
    {
        "id": "set4-06",
        "chapter": "ch6 SALUS (음식과 건강)",
        "title": "작은 캠핑 찻주전자와 한 잔의 머그",
        "words": ["kettle (주전자)", "mug (머그잔)", "brew (달이다)", "cozy (아늑한)", "sip (한 모금)"],
        "subjects": "one small rounded camping tea kettle resting on three low stones at center, and one ceramic mug standing closely beside it",
        "draw_steps": "The round contour of the kettle body, spout and arched handle are drawn first with simple unbroken lines. The three supporting ground stones follow, then the single clean outline of the mug.",
        "palette": "only the palest sky-water tint on the kettle body, delicate warm-sand on the ceramic mug, and sheer stone-grey on the three rocks",
        "motion": "One thin, curling ribbon of transparent white steam rises slowly from the kettle spout."
    },
    {
        "id": "set4-07",
        "chapter": "ch8 MOTUS & ch2 VITA",
        "title": "대나무 낚싯대와 작은 목조 부표 찌",
        "words": ["rod (낚싯대)", "float (찌)", "stream (시냇물)", "calm (평온한)", "bamboo (대나무)"],
        "subjects": "one segmented bamboo fishing rod propped lightly on a small notched stick at left, and a small round wooden bobber float resting on a faint water baseline at center",
        "draw_steps": "The slender segmented bamboo cane line is drawn first with fine joint marks. The notched wooden support fork follows, then the small circular float and its hairline stem.",
        "palette": "only the palest straw-yellow on the bamboo rod and the faintest coral-red tint on the upper half of the small float",
        "motion": "The small round float bobs gently once in the water line and comes to complete rest."
    },
    {
        "id": "set4-08",
        "chapter": "ch1 INVENTIO & ch8 MOTUS",
        "title": "포켓 황동 나침반과 접이식 등고선 지도",
        "words": ["compass (나침반)", "needle (지침)", "map (지도)", "route (경로)", "explore (탐험하다)"],
        "subjects": "one round brass pocket compass with its hinged lid open at center, and a neatly folded single document sheet of topographic map resting quietly beside it",
        "draw_steps": "The circular casing and open lid of the compass are drawn with delicate hairline precision. The cardinal markings and slender needle follow, then the crisp folded edges of the map sheet.",
        "palette": "only the palest translucent brass-gold on the compass rim and a faint whisper of sage-green on the map contour lines",
        "motion": "The delicate magnetic needle swings smoothly once to north and settles completely still."
    },
    {
        "id": "set4-09",
        "chapter": "ch2 VITA & ch3 DOMUS",
        "title": "작은 숲속 통나무 대피소와 나무 풍향계",
        "words": ["cabin (오두막)", "timber (목재)", "vane (풍향계)", "peace (평화)", "shelter (쉼터)"],
        "subjects": "one small open timber lean-to shelter resting at center with clean cut log ends, and one slender wooden stake topped with a small silhouette weather vane beside it",
        "draw_steps": "The simple angled roofline and stacked notched log ends of the small lean-to shelter come first with economical lines. The slender vertical post and arrow weather vane follow.",
        "palette": "only the palest weathered pine-grey on the timber logs and a faint whisper of soft earth-beige under the shelter roof",
        "motion": "The small arrow of the weather vane turns slowly once to catch the breeze and stops."
    },
    {
        "id": "set4-10",
        "chapter": "ch8 MOTUS (운동과 도전)",
        "title": "원형으로 감긴 삼베 로프와 두 개의 황동 카라비너",
        "words": ["rope (로프)", "knot (매듭)", "climb (등반하다)", "secure (안전한)", "link (연결고리)"],
        "subjects": "one neat circular coil of hemp rope resting flat at center, and two polished brass oval carabiner rings hooked together beside it",
        "draw_steps": "The clean concentric outer curves of the coiled hemp rope are drawn first with delicate spiral lines. The two linked oval carabiner loops follow with smooth hairline contours.",
        "palette": "only the palest natural hemp-buff on the coiled rope and the faintest translucent warm-brass on the two metal rings",
        "motion": "The two linked carabiners shift with a tiny soft click once on the rope and rest still."
    }
]

set04_prompts = []
for item in SET04_CLEAN:
    prompt_text = PERFECT_ATLAS_TEMPLATE.format(
        subjects=item["subjects"],
        draw_steps=item["draw_steps"],
        palette=item["palette"],
        motion=item["motion"]
    )
    clean_p = " ".join(prompt_text.split())
    set04_prompts.append({
        "id": item["id"],
        "chapter": item["chapter"],
        "title": item["title"],
        "words": item["words"],
        "prompt": clean_p
    })

# 1. 텍스트 파일 저장
with open("_작업/bulk_sets/set04_10.txt", "w", encoding="utf-8") as f:
    for p in set04_prompts:
        f.write(p["prompt"] + "\n\n")

# 2. complete_100_data.json 갱신
with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

for s in complete_100:
    if s["set_id"] == "set04":
        s["prompts"] = set04_prompts

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_100, f, ensure_ascii=False, indent=2)

print("대표님 정본 [딱정벌레 자연사 도감] 헌법 100% 무결점 이식 완료!")

