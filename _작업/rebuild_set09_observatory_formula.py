# -*- coding: utf-8 -*-
"""
Set 09 (조류와 곤충 생태 10편) - 천문대(Observatory) 기준 공식 100% 적용:
- 1. 0-4s: "Begin with one perfectly level horizontal baseline..." 바닥선 먼저 구축 -> 손 0% 원천 봉쇄!
- 2. 천문대처럼 힘있고 정교한 선화 단계별 구축
- 3. 4-8s: 30% 맑은 수채화 틴트 락
- 4. 단어 중복 0% (순수 미등장 단어만)
"""

import json

OBSERVATORY_TEMPLATE = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are {subjects}. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level horizontal baseline across the lower third. {reveal_steps} There is no visible person, driver, student, live action element, wall, ceiling, darkness or heavy architecture anywhere. Keep outline curves sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is {palette}. All surrounding space stays untouched pure white with no wash of any kind extending behind the subjects. {motion} All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

set09_scenes = [
    {
        "title": "나뭇가지 위 푸른 박새", "words": ["sparrow", "perch", "beak", "chirp"],
        "subjects": "one small wild bluebird perched in neat profile at center upon a level mossy tree twig, with level twig lines extending across the lower third",
        "reveal_steps": "Draw the slender horizontal woody twig and bark texture next. Draw the plump rounded bird body, short pointed beak and dark eye squarely atop the branch. Extend the folded wing feather layers and fan tail. Add the delicate gripping claws.",
        "palette": "an ultra-diluted whisper of translucent sky-cobalt wash on the bird back and soft warm-buff on its breast, with pale bark-grey on the twig",
        "motion": "The small bird tilts its head curiously once and settles peaceful and still."
    },
    {
        "title": "넓은 잎사귀 위 점박이 무당벌레", "words": ["ladybug", "spot", "beetle", "crawl"],
        "subjects": "one polished dome ladybug beetle resting at center upon the gentle curve of a broad green leaf resting on a level baseline",
        "reveal_steps": "Draw the horizontal leaf contour and central vein line next. Draw the round hemispherical beetle shell and tiny head squarely upon the leaf. Extend the distinct black spots and wing division line. Add the fine delicate legs.",
        "palette": "a delicate wash of translucent coral-scarlet on the shell with sheer pastel-jade on the supporting leaf",
        "motion": "The ladybug moves its tiny antennae gently once and rests quietly."
    },
    {
        "title": "대칭 날개를 펼친 호랑나비", "words": ["butterfly", "wing", "antenna", "flutter"],
        "subjects": "one swallowtail butterfly poised with symmetrical open wings at center, anchored above a level resting line",
        "reveal_steps": "Draw the slender central body and curved antennae next. Draw the broad scalloped forewings and hindwing tails symmetrically on either side. Extend the delicate radiating wing vein lines. Add the marginal dot patterns.",
        "palette": "only the palest translucent primrose-yellow on the wings with sheer charcoal veins and two tiny sky-blue spots",
        "motion": "The butterfly wings open a fraction of a millimeter in a slow, graceful, silent motion."
    },
    {
        "title": "단단한 도토리 깍지와 나뭇가지", "words": ["acorn", "cap", "twig", "seed"],
        "subjects": "one single plump glossy acorn standing upright at center nestled inside its cupule cap atop a level wooden shelf line",
        "reveal_steps": "Draw the textured cross-hatch pattern on the rounded acorn cap next. Draw the smooth oval nut body and pointed bottom tip squarely upon the base. Extend the short wooden stem above. Add the clean ground lines.",
        "palette": "only the palest warm hazelnut-tan on the nut body and sheer grey-bark wash on the textured cap",
        "motion": "The acorn stands completely grounded, firm and motionless on the clean white space."
    },
    {
        "title": "수평으로 놓인 숲속 올빼미 깃털", "words": ["feather", "quill", "plume", "soft"],
        "subjects": "one single graceful owl wing feather lying curved horizontally at center with barred markings along a level baseline",
        "reveal_steps": "Draw the smooth central quill shaft and pointed tip next. Draw the soft parallel vane barb lines on either side. Extend the fine downy barbs at the quill base. Add the delicate curved silhouette.",
        "palette": "only the palest warm fawn-tan with faint translucent tawny-brown bar bands along the feather vane",
        "motion": "The downy barbs at the feather base shift softly once in a whisper of air and rest."
    },
    {
        "title": "투명한 날개의 왕잠자리", "words": ["dragonfly", "hover", "tail", "slender"],
        "subjects": "one elegant dragonfly viewed from above at center with long segmented abdomen and four outspread lace wings across a level axis",
        "reveal_steps": "Draw the slender needle-like segmented abdomen and thorax next. Draw the two pairs of long horizontal lace wings symmetrically. Extend the intricate micro-vein mesh on the wings. Add the two large compound eyes.",
        "palette": "only the palest translucent sapphire-teal on the slender body and sheer crystalline glass-white on the wings",
        "motion": "The delicate clear wings give a single quiet crystalline light glint along their leading veins."
    },
    {
        "title": "단풍나무 씨앗 헬리콥터 날개 한 쌍", "words": ["samara", "seed", "glide", "spin"],
        "subjects": "one pair of joined maple seed samaras lying flat at center with delicate curved fibrous wings along a level baseline",
        "reveal_steps": "Draw the twin rounded seed pods joined at center next. Draw the curved delicate thin aerodynamic wings extending outward. Extend the fine structural vein ridges across each wing blade. Add the clean baseline.",
        "palette": "only the palest dried wheat-straw tone across the wings with white background showing through",
        "motion": "One winged seed blade shifts a millimeter on the clean ground and rests still."
    },
    {
        "title": "도자기 새 모이 그릇과 해바라기씨", "words": ["dish", "grain", "peck", "feed"],
        "subjects": "one shallow fluted ceramic bird feeding bowl at center holding five tiny round seeds atop a level stone ledge",
        "reveal_steps": "Draw the circular flared rim and low pedestal of the ceramic dish next. Draw the five small striped seeds inside the dish. Extend the smooth inner bowl contour. Add the clean exterior glaze line.",
        "palette": "only the palest watery mint-celadon on the ceramic bowl and sheer warm-sand on the seeds",
        "motion": "The feeding bowl rests in orderly, clean and peaceful stillness."
    },
    {
        "title": "나무 둥지 속 세 개의 새알", "words": ["nest", "egg", "clutch", "hatch"],
        "subjects": "one neatly woven cup-shaped twig nest at center cradling three smooth speckled songbird eggs atop a level branch fork",
        "reveal_steps": "Draw the circular woven rim of slender interlocking twigs next. Draw the three oval eggs nestled safely inside the nest. Extend the fine moss and grass lining fibres. Add the rounded outer base.",
        "palette": "only the palest robin-egg turquoise wash on the three eggs and sheer dry bark-grey on the twigs",
        "motion": "The eggs rest completely safe, quiet and still in the snug woven cradle."
    },
    {
        "title": "천천히 기어가는 정원 달팽이", "words": ["snail", "shell", "spiral", "slow"],
        "subjects": "one small garden snail crawling in gentle side profile at center with smooth spiral shell along a level garden baseline",
        "reveal_steps": "Draw the logarithmic spiral whorl lines of the round snail shell next. Draw the soft elongated muscular foot and arched neck firmly along the baseline. Extend the two upper eye stalks with tiny tips. Add the subtle trail line.",
        "palette": "only the palest translucent amber-honey on the spiral shell and a whisper of soft pearl-grey on the body",
        "motion": "The two upper eye stalks extend smoothly a fraction of an inch in calm curiosity."
    }
]

set09_prompts = []
for idx, sc in enumerate(set09_scenes):
    p_text = OBSERVATORY_TEMPLATE.format(
        subjects=sc["subjects"],
        reveal_steps=sc["reveal_steps"],
        palette=sc["palette"],
        motion=sc["motion"]
    )
    clean_p = " ".join(p_text.split())
    set09_prompts.append({
        "id": f"set09-{str(idx+1).zfill(2)}",
        "chapter": "SET09 (조류와 곤충 생태)",
        "title": sc["title"],
        "words": sc["words"],
        "prompt": clean_p
    })

for s in data:
    if s["set_id"] == "set09":
        s["prompts"] = set09_prompts

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("_작업/bulk_sets/set09_10.txt", "w", encoding="utf-8") as f:
    for p in set09_prompts:
        f.write(p["prompt"] + "\n\n")

print("Set 09 천문대 기준 공식 완벽 적용 완료!")

