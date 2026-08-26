# -*- coding: utf-8 -*-
"""
대표님 황금 정본(새벽 시골길 씬) 100% 복제형 Set 04 완전 재건축:
- 쇳덩이/실사/먹물 사물 100% 폐기
- 서정적이고 아기자기한 감성 캠핑 & 자연 탐험 10편
"""

import json

GOLDEN_TEMPLATE = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject element in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted axis, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are {subjects}.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. {draw_steps} Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is {palette}. {motion} All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration, generous untouched white space. """

SET04_RAW = [
    {
        "id": "set4-01",
        "chapter": "ch2 VITA & ch1 INVENTIO",
        "title": "삼각 캠핑 텐트와 우드 롤테이블, 접이식 체어",
        "words": ["tent (텐트)", "camp (캠프)", "table (테이블)", "chair (의자)", "shelter (쉼터)"],
        "subjects": "one cosy triangle cotton fabric camping tent resting at the optical center, a low wooden roll-top table balancing the left, a compact folding cotton fabric camp chair balancing the right, and a slender enamel kettle",
        "draw_steps": "Begin with one perfectly level ground baseline across the bottom. Draw the triangle cotton fabric tent at center with delicate contour lines. Draw the wooden slatted table at left and the folding cotton fabric chair at right. Add the small enamel kettle resting neatly on the table.",
        "palette": "pale linen-warm-white on the tent cotton fabric, soft honey-wood on the table, muted sage-green on the folding chair and faint sky-blue on the kettle",
        "motion": "A tiny gentle drift of pale steam rises softly once from the kettle spout "
    },
    {
        "id": "set4-02",
        "chapter": "ch2 VITA (숲과 생명)",
        "title": "빈티지 황동 캠핑 랜턴과 작은 나뭇가지 모닥불",
        "words": ["lantern (랜턴)", "flame (불꽃)", "warmth (온기)", "glow (빛나다)", "twigs (나뭇가지)"],
        "subjects": "one vintage brass camping lantern hanging from a simple wooden tripod stake at left, a neat circle of river stones with small burning twigs at center, and a stacked bundle of dry firewood at right",
        "draw_steps": "Begin with a level ground line. Draw the stacked stone hearth and crossed twigs at center. Draw the slender wooden tripod with the classic glass-and-brass lantern at left, and the neatly tied firewood bundle at right.",
        "palette": "faint warm amber on the lantern glass, pale river-grey on the hearth stones, and a translucent whisper of honey-orange in the small fire",
        "motion": "The small fire flame flickers gently once "
    },
    {
        "id": "set4-03",
        "chapter": "ch8 MOTUS (운동과 도전)",
        "title": "클래식 가죽 등산화와 나무 지팡이",
        "words": ["boots (등산화)", "staff (지팡이)", "trail (오솔길)", "leather (가죽)", "journey (여정)"],
        "subjects": "a pair of classic leather hiking boots resting side by side at center, a polished wooden walking staff propped on the left, and a small trail signpost balancing the right",
        "draw_steps": "Begin with one level ground baseline. Draw the pair of sturdy leather hiking boots at center with soft contour lines. Draw the tall wooden walking staff standing at left, and a clean blank wooden trail marker at right.",
        "palette": "sheer pale tan on the boots, soft warm-timber brown on the walking staff, and delicate earth-grey on the trail marker",
        "motion": "A single dried autumn leaf drifts gently onto the ground near the boots "
    },
    {
        "id": "set4-04",
        "chapter": "ch8 MOTUS & ch1 INVENTIO",
        "title": "원목 투어링 카약과 패들 노, 잔잔한 수면 파문",
        "words": ["kayak (카약)", "paddle (노)", "ripple (파문)", "lake (호수)", "glide (미끄러지다)"],
        "subjects": "a slender wooden touring kayak floating level horizontally at the optical center, a carved wooden double-ended paddle resting across its cockpit, and two concentric gentle water ripples",
        "draw_steps": "Begin with one perfectly level horizontal water baseline. Draw the sleek double-ended wooden kayak body horizontally across center. Draw the symmetrical wooden paddle resting across the rim, followed by two delicate oval water ripples.",
        "palette": "pale cedar-gold on the kayak hull, sheer pine-grey on the paddle, and a faint wash of translucent pale water-blue around the ripples",
        "motion": "The two delicate water ripples expand softly outward once "
    },
    {
        "id": "set4-05",
        "chapter": "ch1 INVENTIO (세상을 발견해요)",
        "title": "클래식 필드 쌍안경과 펼쳐진 탐조 도감",
        "words": ["binoculars (쌍안경)", "observe (관찰하다)", "guidebook (도감)", "feathers (깃털)", "field (들판)"],
        "subjects": "a classic black-and-brass field binocular standing upright at center, a slender strap draped at left, an open illustrated bird field guide resting at right, and a single dropped feather",
        "draw_steps": "Begin with a horizontal tabletop baseline. Draw the twin cylindrical lenses and focus wheel of the binoculars at center. Draw the curved neck strap resting at left, and the open illustrated nature guide book at right.",
        "palette": "sheer pale graphite on the binocular body, faint warm-brass on the adjustment dial, and a whisper of olive-green on the book page illustration",
        "motion": "The single dropped feather flutters gently once in the light breeze "
    },
    {
        "id": "set4-06",
        "chapter": "ch6 SALUS (음식과 건강)",
        "title": "법랑 캠핑 주전자와 두 개의 세라믹 머그잔",
        "words": ["kettle (주전자)", "mug (머그잔)", "brew (달이다)", "cozy (아늑한)", "sip (한 모금)"],
        "subjects": "one speckled enamel camping kettle sitting over a small flat cooking grate at center, two ceramic camp mugs propped on the left and right, and a small metal tea tin",
        "draw_steps": "Begin with one level ground baseline. Draw the low cooking grate and the round enamel kettle at center. Draw one ceramic mug at left, a matching mug at right, and a simple square tea container.",
        "palette": "sheer pastel mint-green on the kettle, delicate warm-sand on the ceramic mugs, and pale slate on the cooking grate",
        "motion": "A tiny wisp of transparent steam curls softly from the kettle lid "
    },
    {
        "id": "set4-07",
        "chapter": "ch8 MOTUS & ch2 VITA",
        "title": "대나무 낚싯대와 나무 찌, 루어 태클 상자",
        "words": ["rod (낚싯대)", "float (찌)", "tackle (낚시도구)", "stream (시냇물)", "calm (평온한)"],
        "subjects": "a slender segmented bamboo fishing rod propped diagonally on a wooden forked stick at left, a red-and-white wooden bobber float floating in center, and an open wooden lure tackle box at right",
        "draw_steps": "Begin with a level horizontal stream bank line. Draw the angled bamboo rod resting on its wooden Y-stake at left. Draw the small round bobber in the center water line, and the open divided lure box with miniature lures at right.",
        "palette": "pale straw-yellow on the bamboo rod, delicate coral-red on the top of the float, and natural light pine on the tackle box",
        "motion": "The small round float bobs gently once in the clear water "
    },
    {
        "id": "set4-08",
        "chapter": "ch1 INVENTIO & ch8 MOTUS",
        "title": "황동 포켓 나침반과 접이식 지도, 필드 수첩",
        "words": ["compass (나침반)", "needle (지침)", "map (지도)", "route (경로)", "explore (탐험하다)"],
        "subjects": "one round brass pocket compass with open lid at the optical center, a neatly folded topographic map extending at left, and a small leather field notebook with elastic band at right",
        "draw_steps": "Begin with a clean level baseline. Draw the open circular brass compass casing and dial markings at center. Draw the folded contour line map at left, and the closed pocket notebook at right.",
        "palette": "luminous pale brass-gold on the compass case, faint topographic sage-green on the map, and sheer warm-caramel on the notebook cover",
        "motion": "The delicate magnetic needle swings smoothly once and settles north "
    },
    {
        "id": "set4-09",
        "chapter": "ch2 VITA & ch3 DOMUS",
        "title": "숲속 통나무 오두막과 나무 풍향계",
        "words": ["cabin (오두막)", "timber (목재)", "vane (풍향계)", "chimney (굴뚝)", "peace (평화)"],
        "subjects": "a picturesque small timber log cabin with stone chimney just right of center, a slender wooden post topped with a rooster weather vane balancing at left, and a neat stack of logs",
        "draw_steps": "Begin with one perfectly level forest ground line. Draw the rustic log cabin with gable roof and stone chimney at center-right. Draw the vertical post with the silhouette rooster weather vane at left, and the stacked logs on the ground.",
        "palette": "soft weathered timber-grey on the cabin walls, pale slate-blue on the roof tiles, and delicate meadow-green on the grass tufts",
        "motion": "The rooster weather vane turns smoothly once in the breeze "
    },
    {
        "id": "set4-10",
        "chapter": "ch8 MOTUS (운동과 도전)",
        "title": "등산 로프 코일과 황동 잠금 카라비너",
        "words": ["rope (로프)", "knot (매듭)", "climb (등반하다)", "secure (안전한)", "link (연결고리)"],
        "subjects": "a neatly coiled climbing rope resting horizontally at center, two polished brass locking carabiner clips linked at left, and a small chalk bag with drawstring balancing at right",
        "draw_steps": "Begin with one level horizontal baseline. Draw the symmetrical oval coil of woven climbing rope at center with delicate spiral lines. Draw the two oval carabiner rings hooked together at left, and the upright cotton fabric chalk pouch at right.",
        "palette": "pale natural hemp-gold on the coiled rope, sheer warm-brass on the carabiners, and faint sky-slate on the chalk bag",
        "motion": "The linked carabiners give a tiny metallic glint softly once "
    }
]

set04_prompts = []
for item in SET04_RAW:
    prompt_text = GOLDEN_TEMPLATE.format(
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

print("Set 04 황금 정본 기반 전면 재건축 완료!")

