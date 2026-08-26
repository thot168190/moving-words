# -*- coding: utf-8 -*-
"""
대표님 확정 [세필 수채 정본 공식]으로 Set 12(악기와 소리 10편) & Set 13(사회와 제도 10편) 전면 변환 탑재:
- 헤더: Progressive detailed fine-pencil construction, transparent watercolor and gentle object-motion animation on a solid pure bright white background (#FFFFFF), edge to edge. The first frame is an entirely empty pure white field. Static locked-off camera, one continuous 8-second take. The only visible subjects are ...
- 0-3.5s: exceptionally fine pale-neutral 2H graphite strokes are visibly traced one by one across the empty white field. ... Each stroke has a clear beginning and endpoint. The illustration is built progressively rather than fading into view. Previously completed lines remain stable.
- 3.5-5.5s: clear transparent watercolor develops in layered color. ...
- 5.5-8s: ...
- Style: intricate premium pencil-and-watercolor plate, numerous hair-thin pale graphite construction lines, accurate object anatomy, luminous layered transparent watercolor, sophisticated museum-quality illustrated-dictionary artwork, clearly hand-drawn and never photographic.
- 배제: No dark outline, black ink, sepia ink, charcoal, thick contour, product photography, studio lighting, realistic reflection, glossy highlight, cast shadow, 3D, CGI, text, label, border, hand, artist or visible drawing tool. Completely silent.
"""

import json

PENCIL_TEMPLATE = """Progressive detailed fine-pencil construction, transparent watercolor and gentle object-motion animation on a solid pure bright white background (#FFFFFF), edge to edge. The first frame is an entirely empty pure white field. Static locked-off camera, one continuous 8-second take. The only visible subjects are {subjects}.

0-3.5s: exceptionally fine pale-neutral 2H graphite strokes are visibly traced one by one across the empty white field. {draw_steps} Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines. Each stroke has a clear beginning and endpoint. The illustration is built progressively rather than fading into view. Previously completed lines remain stable.

3.5-5.5s: clear transparent watercolor develops in layered color. {color_steps} Preserve narrow white-paper highlights while keeping the colors fresh, luminous and distinguishable, with graphite details visible through every layer.

5.5-8s: {motion} All other elements remain fixed. All graphite construction lines and watercolor boundaries remain stable.

Style: intricate premium pencil-and-watercolor plate, numerous hair-thin pale graphite construction lines, accurate object anatomy, luminous layered transparent watercolor, sophisticated museum-quality illustrated-dictionary artwork, clearly hand-drawn and never photographic.

No dark outline, black ink, sepia ink, charcoal, thick contour, product photography, studio lighting, realistic reflection, glossy highlight, cast shadow, 3D, CGI, text, label, border, hand, artist or visible drawing tool. Completely silent."""

# Set 12 (악기와 소리 10편)
set12_scenes = [
    {
        "title": "바이올린 활과 송진 가루", "words": ["bow", "string", "rosin", "play"],
        "subjects": "exactly one illustrated handcrafted wooden violin bow lying level horizontally at the optical center and one tiny rosin dust speck",
        "draw_steps": "Construct the long slender tapered wooden bow stick first from tip to frog, followed by the ebony frog block, metal winding, mother-of-pearl slide, and the straight flat ribbon of white horsehair below. Add fine pointed tip contours and one tiny rosin dust speck last.",
        "color_steps": "A pale warm amber-varnish wash settles across the wooden stick first, followed by soft pearl-white along the hair ribbon and a muted charcoal-grey accent on the ebony frog.",
        "motion": "A single hairline shimmer of light traces softly once along the horsehair ribbon and comes to rest."
    },
    {
        "title": "뮤지컬 트라이앵글과 타봉", "words": ["triangle", "percussion", "strike", "ring"],
        "subjects": "exactly one illustrated open equilateral steel musical triangle hanging by a fine cord at the optical center and one slender striker beater beside it",
        "draw_steps": "Build the open triangular steel bar through separate outer and inner contours, the small open corner gap, the thin hanging suspension loop above, and the slender cylindrical striking beater beside it. Add delicate corner curve lines last.",
        "color_steps": "A very pale cool silver-grey wash defines the steel bar facets, followed by a faint champagne-gold tint on the hanging cord and light steel-grey on the beater.",
        "motion": "The suspended steel triangle gives a microscopic, silent high-frequency shimmer and comes to rest."
    },
    {
        "title": "음향 공명 박스 소리굽쇠", "words": ["tuning", "fork", "pitch", "vibrate"],
        "subjects": "exactly one illustrated polished two-pronged steel tuning fork standing upright at the optical center atop its small wooden resonance box",
        "draw_steps": "Construct the rectangular wooden resonance box first with open acoustic chamber end, then the vertical cylindrical stem and parallel U-shaped steel prongs. Add fine woodgrain contour strokes across the box walls.",
        "color_steps": "A pale cool steel-grey wash settles along the metal prongs, followed by warm natural pine-buff and light honey-brown layers on the wooden resonance box.",
        "motion": "The two steel prongs give a microscopic, silent high-frequency shimmer and come to rest."
    },
    {
        "title": "10홀 다이아토닉 하모니카", "words": ["harmonica", "reed", "blow", "note"],
        "subjects": "exactly one illustrated classic ten-hole diatonic harmonica lying flat at the optical center with engraved metal cover plates",
        "draw_steps": "Build the rectangular upper and lower metal cover plates first, then the ten individual square blow holes along the front comb, corner mounting screws, and subtle side acoustic vents.",
        "color_steps": "A pale polished silver-grey wash defines the cover plates, followed by a delicate golden-reed wash inside the comb openings and faint cool grey accents.",
        "motion": "The harmonica rests in immaculate, gleaming, quiet graphic stillness."
    },
    {
        "title": "금관악기 실버 마우스피스", "words": ["mouthpiece", "brass", "cup", "buzz"],
        "subjects": "exactly one illustrated silver-plated trumpet mouthpiece standing upright at the optical center with rounded cup and tapered shank",
        "draw_steps": "Construct the circular rounded rim and wide inner cup first, followed by the throat collar ring, outer curved backbore, and the long tapered shank tube below.",
        "color_steps": "A very pale cool silver-chrome wash settles across the curved outer contours, with delicate aqua-grey accents defining the cup ellipse and collar.",
        "motion": "A single point of clear light sparkles softly once on the curved silver rim and comes to rest."
    },
    {
        "title": "지휘봉과 코르크 손잡이", "words": ["baton", "conduct", "tempo", "lead"],
        "subjects": "exactly one illustrated conductor's baton lying horizontally at the optical center with tapered shaft and teardrop cork handle",
        "draw_steps": "Draw the teardrop-shaped natural cork grip handle first, then the long slender shaft tapering smoothly to a fine tip point, adding delicate cork cell contour marks.",
        "color_steps": "A pale natural cork-buff and soft ochre wash settle into the handle, while a sheer warm-white wash defines the slender tapered shaft.",
        "motion": "The fine tip of the conductor's baton dips a millimeter in a silent, poised cue and comes to rest."
    },
    {
        "title": "마림바 로즈우드 음판과 말렛", "words": ["mallet", "bar", "strike", "tone"],
        "subjects": "exactly one illustrated carved rosewood tone bar resting at the optical center and one yarn-wound percussion mallet laid across it",
        "draw_steps": "Build the rectangular rosewood tone bar with side arch undercut and two mounting node holes first, then construct the round yarn-wound mallet head and slender birch handle.",
        "color_steps": "A rich transparent rosewood-tan and warm umber wash cover the tone bar, while a delicate pastel lavender-blue wash tints the yarn mallet head.",
        "motion": "The yarn mallet head rests gently poised and motionless upon the tone bar."
    },
    {
        "title": "황동 핑거 심벌즈 쌍", "words": ["cymbal", "brass", "crash", "rhythm"],
        "subjects": "exactly one illustrated pair of circular domed brass clash cymbals connected by an elastic strap loop at the optical center",
        "draw_steps": "Construct the circular saucer rims of both brass discs first, then their raised central dome cups, strap attachment slots, and fine concentric turning rings.",
        "color_steps": "A pale luminous champagne-brass wash spreads across the cymbal plates, complemented by a soft tan wash on the elastic strap loops.",
        "motion": "The two brass cymbal discs rest in clear, vibrating, quiet acoustic resonance."
    },
    {
        "title": "오페라 자개 망원경 쌍안경", "words": ["glasses", "opera", "view", "stage"],
        "subjects": "exactly one illustrated mother-of-pearl and brass opera glasses binocular standing upright at the optical center with collapsible side handle",
        "draw_steps": "Build the twin short cylindrical optical barrels and central bridge axle first, followed by the mother-of-pearl panel inlays, brass rim bezels, and slender collapsible side handle.",
        "color_steps": "A delicate iridescent pearl-white and faint lavender wash settle across the barrel panels, paired with a warm champagne-brass wash on the metal fittings.",
        "motion": "A delicate pearl glint gleams softly across the focus bridge and comes to rest."
    },
    {
        "title": "악보대 보면대 트레이", "words": ["stand", "sheet", "music", "hold"],
        "subjects": "exactly one illustrated minimalist metal sheet music stand tray standing open at the optical center with twin wire page holding clips",
        "draw_steps": "Construct the wide V-shaped sheet music tray plate and bottom book ledge first, then the two spring-loaded wire page retaining fingers and vertical collar sleeve below.",
        "color_steps": "A pale matte slate-grey wash defines the sheet music tray surface, while light silver-grey accents tint the wire page holding clips.",
        "motion": "The wire page clips stand in crisp, neat, and quiet rehearsal readiness."
    }
]

# Set 13 (사회와 제도 10편)
set13_scenes = [
    {
        "title": "영국식 원통형 우체통", "words": ["postbox", "mail", "letter", "send"],
        "subjects": "exactly one illustrated traditional cylindrical pillar postbox standing upright at the optical center with domed cap and mail slot",
        "draw_steps": "Construct the vertical cylindrical column body first, followed by the domed top cap, horizontal mail posting slot flap, and the collection time plaque mount below.",
        "color_steps": "A pale translucent coral-red wash covers the postbox body, followed by soft vermilion and warm rose layers, with white paper highlights preserved along the curved plinth.",
        "motion": "The small metal posting slot flap closes with a tiny soft click and comes to rest."
    },
    {
        "title": "원목 판사봉 가벨과 받침대", "words": ["gavel", "judge", "court", "order"],
        "subjects": "exactly one illustrated carved hardwood judge's gavel resting angled atop its circular wooden sound block base at the optical center",
        "draw_steps": "Build the stepped circular sound block disc first, then the turned wooden gavel head with central brass band, cylindrical striking faces, and contoured handle.",
        "color_steps": "A pale warm walnut-brown and chestnut wash settle across the gavel and sound block, accented by a delicate champagne-brass wash on the center band.",
        "motion": "The wooden gavel rests in solemn, dignified and final judicial peace."
    },
    {
        "title": "금고 다이얼 번호 자물쇠", "words": ["vault", "dial", "lock", "secure"],
        "subjects": "exactly one illustrated circular polished brass vault combination lock dial standing at the optical center with knurled center knob",
        "draw_steps": "Construct the circular outer bezel plate and index pointer first, then the rotating knurled center knob and precise graduation markings around the perimeter.",
        "color_steps": "A pale brushed champagne-brass wash defines the dial face, complemented by cool silver-grey accents along the index marker and perimeter ring.",
        "motion": "The knurled brass combination knob turns smoothly two tick marks and locks securely."
    },
    {
        "title": "양장 가죽 여권 수첩", "words": ["passport", "travel", "border", "entry"],
        "subjects": "exactly one illustrated closed formal leather passport booklet standing at the optical center with gold-stamped crest emblem",
        "draw_steps": "Draw the rectangular booklet silhouette and edge stitching first, then the gold-stamped national crest emblem in the center, and smooth spine crease.",
        "color_steps": "A pale deep navy-indigo wash settles across the textured leather cover, with a delicate luminous gold wash highlighting the embossed crest.",
        "motion": "The leather passport booklet stands poised, ready and still on the clean white space."
    },
    {
        "title": "원목 투표함과 금속 투입구", "words": ["ballot", "vote", "elect", "choose"],
        "subjects": "exactly one illustrated square wooden ballot box standing at the optical center with metal corner brackets and top drop slot",
        "draw_steps": "Build the cubic wooden box walls and top lid first, then the narrow rectangular center drop slot, four brass corner reinforcing brackets, and keyhole plate.",
        "color_steps": "A pale natural pine-buff wash covers the wooden box, paired with warm champagne-brass layers on the corner hardware and slot rim.",
        "motion": "The ballot box stands secure, balanced and still in the quiet open space."
    },
    {
        "title": "골동품 우편 저울", "words": ["scale", "weigh", "postage", "balance"],
        "subjects": "exactly one illustrated antique brass postal letter scale standing at the optical center with top letter pan and weight graduation plate",
        "draw_steps": "Construct the heavy stepped base and vertical fulcrum post first, followed by the curved weight graduation chart plate, pointer indicator, and top letter weighing pan.",
        "color_steps": "A pale warm brass-gold wash settles across the cast base, with a delicate soft ivory wash on the graduation chart face.",
        "motion": "The top letter pan settles smoothly with a delicate micro-balance and rests level."
    },
    {
        "title": "원형 붉은 실링 왁스 인장", "words": ["seal", "wax", "stamp", "official"],
        "subjects": "exactly one illustrated circular scalloped red sealing wax impression at the optical center with sharp embossed emblem",
        "draw_steps": "Draw the irregular scalloped outer wax rim with droplet contours first, followed by the circular inner boundary, and the crisp embossed shield emblem in the center.",
        "color_steps": "A pale translucent cherry-crimson wash spreads across the wax seal, with deeper ruby-red layers defining the recessed crest contours.",
        "motion": "The embossed wax seal rests crisp, permanent and completely still."
    },
    {
        "title": "가죽 아타셰 서류 가방", "words": ["briefcase", "case", "document", "work"],
        "subjects": "exactly one illustrated structured leather attaché briefcase standing upright at the optical center with twin polished brass clasp locks",
        "draw_steps": "Construct the rectangular box silhouette and welted perimeter seams first, then the centered top handle, dual brass clasp locks, keyholes, and base studs.",
        "color_steps": "A pale warm caramel-tan wash covers the leather case body, complemented by crisp champagne-gold accents on the dual latches and handle rings.",
        "motion": "The twin brass clasp latches give a tiny soft mechanical alignment and stay firmly shut."
    },
    {
        "title": "원목 로커 잉크 흡인지", "words": ["blotter", "absorb", "ink", "dry"],
        "subjects": "exactly one illustrated classic curved rocker ink blotter standing at the optical center with turned wooden handle and brass plate",
        "draw_steps": "Build the curved semicircular wooden rocker base and felt blotting pad layer first, followed by the top brass clamping plate, turned knob handle, and side screws.",
        "color_steps": "A pale warm walnut-brown wash settles into the wooden blotter body, paired with sheer polished brass on the top knob and ivory on the felt layer.",
        "motion": "The curved rocker blotter rocks smoothly once along its rounded base and rests level."
    },
    {
        "title": "도서관 2단 원목 북 카트", "words": ["cart", "library", "shelf", "book"],
        "subjects": "exactly one illustrated clean two-shelf wooden library book cart standing in side profile at the optical center on four small wheels",
        "draw_steps": "Construct the upright wooden vertical pillars and curved top push handles first, then the two angled V-shelves, base shelf, and four small caster wheels below.",
        "color_steps": "A pale warm oak-blonde wash defines the wooden cart structure, with soft slate-grey accents on the wheel casters and joinery hardware.",
        "motion": "The library book cart rests in quiet, studious, orderly stillness on the white surface."
    }
]

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Set 12 적용
set12_prompts = []
for idx, sc in enumerate(set12_scenes):
    p_text = PENCIL_TEMPLATE.format(
        subjects=sc["subjects"],
        draw_steps=sc["draw_steps"],
        color_steps=sc["color_steps"],
        motion=sc["motion"]
    )
    clean_p = " ".join(p_text.split())
    set12_prompts.append({
        "id": f"set12-{str(idx+1).zfill(2)}",
        "chapter": "SET12 (악기와 소리)",
        "title": sc["title"],
        "words": sc["words"],
        "prompt": clean_p
    })

for s in data:
    if s["set_id"] == "set12":
        s["prompts"] = set12_prompts

# Set 13 적용
set13_prompts = []
for idx, sc in enumerate(set13_scenes):
    p_text = PENCIL_TEMPLATE.format(
        subjects=sc["subjects"],
        draw_steps=sc["draw_steps"],
        color_steps=sc["color_steps"],
        motion=sc["motion"]
    )
    clean_p = " ".join(p_text.split())
    set13_prompts.append({
        "id": f"set13-{str(idx+1).zfill(2)}",
        "chapter": "SET13 (사회와 제도)",
        "title": sc["title"],
        "words": sc["words"],
        "prompt": clean_p
    })

for s in data:
    if s["set_id"] == "set13":
        s["prompts"] = set13_prompts

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("_작업/bulk_sets/set12_10.txt", "w", encoding="utf-8") as f:
    for p in set12_prompts:
        f.write(p["prompt"] + "\n\n")

with open("_작업/bulk_sets/set13_10.txt", "w", encoding="utf-8") as f:
    for p in set13_prompts:
        f.write(p["prompt"] + "\n\n")

print("Set 12 & Set 13 대표님 확정 세필 수채 정본 100% 일괄 변환 완료!")

