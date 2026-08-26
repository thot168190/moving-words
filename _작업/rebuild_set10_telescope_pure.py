# -*- coding: utf-8 -*-
"""
Set 10 (일상 도구와 서재 10편) - 망원경 100% 정본 공식 + 손 0% + 단어 중복 0%
"""

import json

TELESCOPE_TEMPLATE = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame with equal narrow breathing margins on the left and right. The subjects remain centered while both outer edges stay clear. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are {subjects}.

0-5.5s: fine dark-charcoal linework appears progressively from the empty white field. {reveal_steps} Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

5.5-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. The restrained palette is {palette}. All surrounding space stays untouched pure white with no wash of any kind extending behind the subjects. {motion} All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: delicate fine-line engraving, luminous transparent watercolor, restrained tonal contrast, generous white space, sophisticated museum-quality editorial illustration."""

set10_scenes = [
    {
        "title": "황동 펜촉 만년필 촉대", "words": ["fountain", "nib", "ink", "write"],
        "subjects": "one classic black-and-gold fountain writing instrument lying angled horizontally at center with split gold nib",
        "reveal_steps": "The long cylindrical barrel and tapered grip are revealed first through many clean short line segments. The fine triangular gold nib and breather slit then appear one by one, followed by the curved clip on the cap and gold trim rings.",
        "palette": "only the palest translucent charcoal on the resin body and delicate champagne-gold on the metal nib",
        "motion": "A single tiny light glint traces smoothly once along the polished gold nib slit."
    },
    {
        "title": "황동 독서 돋보기 렌즈", "words": ["magnifier", "lens", "glass", "focus"],
        "subjects": "one classic round reading magnifying glass resting flat at center with turned wooden handle and brass rim",
        "reveal_steps": "The turned wooden handle and brass ferrule are revealed first through many clean short line segments. The circular brass lens bezel then appears, followed by the thick transparent convex optical lens and delicate reflection crescent.",
        "palette": "only the palest warm walnut on the handle, translucent brass on the rim, and sheer optical-cyan on the lens",
        "motion": "A soft ray of pure white light glints quietly across the clear convex glass surface."
    },
    {
        "title": "작은 황동 탁상종 핸드벨", "words": ["bell", "ring", "chime", "sound"],
        "subjects": "one classic flared brass call bell standing upright at center with turned dark wood handle and top finial",
        "reveal_steps": "The turned vertical wooden handle is revealed first through clean line segments. The wide flared conical brass bell body and round lip rim then appear one by one, followed by the interior clapper ball and top brass collar.",
        "palette": "only the palest luminous brass-gold wash on the bell flare and sheer ebony-charcoal on the wooden handle",
        "motion": "The small internal clapper ball gives a tiny soft vibration and rests still."
    },
    {
        "title": "유리 잉크병과 스포이트 피펫", "words": ["inkwell", "well", "pipette", "drop"],
        "subjects": "one square cut-glass inkwell at center with hinged brass flip lid, standing with a glass dropper pipette",
        "reveal_steps": "The heavy bevelled square glass base is revealed first through clean geometric line segments. The circular neck and hinged domed brass lid then appear one by one, followed by the slender angled glass dropper pipette.",
        "palette": "only the palest translucent indigo-blue tint in the inkwell base and sheer cool glass-white on the walls",
        "motion": "The liquid level inside the clear inkwell settles perfectly horizontal and still."
    },
    {
        "title": "원목 접이식 독서대 북스탠드", "words": ["easel", "stand", "rest", "study"],
        "subjects": "one compact folding wooden book lectern standing open at center with brass page retention clips",
        "reveal_steps": "The flat base board and angled hinged backrest are revealed first through clean line segments. The lower book ledge and two swiveling brass page clips then appear one by one, followed by the stepped adjustment prop behind.",
        "palette": "only the palest natural birch-tan on the wooden stand with sheer warm brass on the page clips",
        "motion": "The wooden lectern stands in solid, quiet and studious equilibrium on the white field."
    },
    {
        "title": "클래식 금속 스테이플러", "words": ["stapler", "bind", "fasten", "desk"],
        "subjects": "one vintage heavy steel tabletop stapler shown in clean side profile at center with spring-loaded top lever",
        "reveal_steps": "The flat rectangular base and anvil plate are revealed first through clean line segments. The pivoting metal magazine lever and top pressing cap then appear one by one, followed by the internal spring guide channel.",
        "palette": "only the palest vintage industrial slate-grey on the stapler body with pure white showing through",
        "motion": "The top pressing cap settles with a tiny crisp alignment and rests motionless."
    },
    {
        "title": "휴대용 황동 연필깎이", "words": ["sharpener", "blade", "point", "shave"],
        "subjects": "one compact wedge-shaped brass pencil sharpener at center with steel blade screwed to its sloped side",
        "reveal_steps": "The rectangular brass block and ridged grip grooves are revealed first through clean line segments. The cone-shaped entry hole and steel blade then appear one by one, followed by the single center clamping screw.",
        "palette": "only the palest brushed brass on the wedge body and sheer cool steel on the cutting blade",
        "motion": "The small sharpener rests balanced and still on the pure white ground."
    },
    {
        "title": "도서관 양장본 비단 책갈피", "words": ["ribbon", "mark", "page", "read"],
        "subjects": "one closed thick hardcover volume lying flat at center with an embroidered silk ribbon bookmark trailing out",
        "reveal_steps": "The rectangular book spine and front cloth cover are revealed first through clean line segments. The layered page edges along the side then appear one by one, followed by the flowing S-curve silk ribbon bookmark.",
        "palette": "only the palest sage-green on the book cloth and sheer crimson-silk wash on the trailing ribbon",
        "motion": "The trailing silk ribbon tip flutters gently once in the quiet room and settles."
    },
    {
        "title": "스틸 와이어 페이퍼클립과 핀", "words": ["clip", "pin", "wire", "hold"],
        "subjects": "one large classic looped steel wire paperclip resting flat at center beside three small brass pushpins",
        "reveal_steps": "The outer curved loop of the steel wire clip is revealed first through clean curved line segments. The concentric inner gripping wire loops then appear one by one, followed by the three small round-headed brass drawing pins.",
        "palette": "only the palest polished steel on the wire clip and delicate warm-brass on the pushpin heads",
        "motion": "The paperclip and pins rest in orderly, clean stillness on the white surface."
    },
    {
        "title": "클래식 황동 인장 스탬프", "words": ["stamp", "emblem", "crest", "mark"],
        "subjects": "one turned brass seal stamp standing upright at center with round engraved bottom crest",
        "reveal_steps": "The turned brass handle and rounded top knob are revealed first through clean vertical line segments. The cylindrical neck and wide circular stamping base then appear one by one, followed by the delicate engraved crest lines on the lower rim.",
        "palette": "only the palest luminous warm-brass wash on the stamp body with bright white highlights",
        "motion": "The heavy brass seal stands perfectly vertical, poised and motionless."
    }
]

set10_prompts = []
for idx, sc in enumerate(set10_scenes):
    p_text = TELESCOPE_TEMPLATE.format(
        subjects=sc["subjects"],
        reveal_steps=sc["reveal_steps"],
        palette=sc["palette"],
        motion=sc["motion"]
    )
    clean_p = " ".join(p_text.split())
    set10_prompts.append({
        "id": f"set10-{str(idx+1).zfill(2)}",
        "chapter": "SET10 (일상 도구와 서재)",
        "title": sc["title"],
        "words": sc["words"],
        "prompt": clean_p
    })

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for s in data:
    if s["set_id"] == "set10":
        s["prompts"] = set10_prompts

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("_작업/bulk_sets/set10_10.txt", "w", encoding="utf-8") as f:
    for p in set10_prompts:
        f.write(p["prompt"] + "\n\n")

print("Set 10 망원경 정본 공식 완벽 이식 완료!")

