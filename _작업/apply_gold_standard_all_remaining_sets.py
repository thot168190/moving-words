# -*- coding: utf-8 -*-
"""
대표님 골드 스탠다드 템플릿을 Set 12 (음악/소리), Set 13 (사회/제도)까지 완벽 확장 적용!
"""

import json

GOLD_STANDARD_TEMPLATE = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is evenly balanced around the optical center. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are {subjects}.

0-4s: ultra-fine pale warm-grey graphite linework is actively traced stroke by stroke progressively from the empty white field. Each new stroke begins at one visible point and travels forward to its endpoint, leaving the finished graphite line behind. The drawing is constructed progressively through clearly visible moving strokes, never by fading in, dissolving, materializing or revealing a completed image. Only the lines already traced may be visible; every unfinished part remains completely blank white.

{draw_steps}

Every detail becomes visible sequentially, never all at once. The subjects must not exist before their individual strokes are traced. Previously completed lines remain delicate, completely stable and unchanged.

Every outline is very thin, soft and light, never black or dark charcoal. There are no bold contours, heavy edge lines, dense hatch marks, realistic reflections, glossy highlights, cast shadows or photographic material textures. Keep the graphite lines pale but clearly readable, never darker than 25% grey.

4-8s: an extremely pale, water-heavy watercolor wash develops gently inside the completed graphite outlines. The watercolor appears gradually in small transparent painted areas rather than covering the objects all at once. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled.

Use distinct, believable illustrated colors for different materials. The restrained palette is {palette}. Restraint means low saturation, not realistic rendering or fewer distinguishable colors.

All surrounding space stays untouched pure white, with no background wash extending behind the subjects. {motion} All other elements remain still.

The final composition remains centered, clearly readable and surrounded by generous untouched white space.

Style: master-level hand-drawn fine-line illustration with exceptionally thin pale warm-grey graphite strokes, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, visible stroke-by-stroke drawing process, generous white space. Flat 2D illustration only, never photorealistic, never live action, never 3D or CGI.

No text, labels, borders, panels, extra subjects, hands, fingers, arms, pencils, pens, brushes, drawing tools or visible artist. Completely silent."""

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Set 12 세부 묘사
set12_draw_data = [
    {
        "subjects": "exactly one handcrafted wooden violin bow lying level horizontally at the optical center with ebony frog and pearl slide, and one tiny rosin dust speck",
        "draw_steps": "Begin by actively tracing the long slender tapered wooden bow stick from one endpoint to the other. Trace the ebony frog block, metal winding and pearl slide next. Draw the straight flat ribbon of white horsehair below with a traveling stroke. Add only a few fine pointed tip marks and one tiny rosin dust speck last.",
        "palette": "a very pale warm amber-varnish on the wood stick, sheer pearl-white on the hair ribbon, and a tiny warm-grey accent on the frog",
        "motion": "A single hairline shimmer of light traces softly once along the horsehair ribbon and comes to rest."
    },
    {
        "subjects": "exactly one suspended equilateral steel musical triangle hanging by a fine cord at the optical center beside one polished striker beater",
        "draw_steps": "Begin by actively tracing the open triangular steel bar contour from one endpoint to the other. Trace the slender cylindrical striking beater beside it next. Construct the thin hanging suspension loop above. Add only a few fine metallic reflection lines last.",
        "palette": "a very pale cool silver-grey wash on the triangle bar, sheer champagne on the cord, and faint grey cast shadow lines",
        "motion": "The suspended steel triangle gives a microscopic, silent high-frequency shimmer and comes to rest."
    },
    {
        "subjects": "exactly one polished two-pronged steel musical tuning fork standing upright at the optical center atop its small wooden resonance box",
        "draw_steps": "Begin by actively tracing the small rectangular wooden resonance box base from one endpoint to the other. Trace the vertical cylindrical stem and U-shaped parallel steel prongs next. Construct the two fine prong tips. Add only a few clean resonance box woodgrain lines last.",
        "palette": "a very pale cool steel-silver on the tuning fork and sheer natural pine-blonde on the wooden resonance box",
        "motion": "The two steel prongs give a microscopic, silent high-frequency shimmer and come to rest."
    },
    {
        "subjects": "exactly one classic ten-hole diatonic harmonica lying flat in clean perspective at the optical center with engraved metal cover plates",
        "draw_steps": "Begin by actively tracing the rectangular metal cover plates from one endpoint to the other. Trace the ten square blow holes and numbered scale along the front edge next. Construct the corner mounting screws. Add only a few fine metallic reflection lines last.",
        "palette": "a very pale polished chrome-silver on the cover plates and a delicate whisper of golden-reed tint on the comb",
        "motion": "The harmonica rests in immaculate, gleaming, quiet graphic stillness."
    },
    {
        "subjects": "exactly one solid silver-plated musical instrument mouthpiece standing upright at the optical center with rounded cup and tapered shank",
        "draw_steps": "Begin by actively tracing the circular rounded rim and cup contour from one endpoint to the other. Trace the flared throat collar and long tapered shank tube next. Construct the central axis symmetry lines. Add only a few delicate reflection arcs last.",
        "palette": "a very pale cool silver-chrome wash across the mouthpiece body with luminous untouched pure white highlights",
        "motion": "A single point of clear light sparkles softly once on the curved silver rim and comes to rest."
    },
    {
        "subjects": "exactly one conductor's baton lying horizontally at the optical center with tapered white shaft and teardrop cork handle",
        "draw_steps": "Begin by actively tracing the teardrop-shaped natural cork grip handle from one endpoint to the other. Trace the long slender shaft tapering to a fine point next. Construct the delicate balance line. Add only a few fine shaft reflection lines last.",
        "palette": "a very pale natural cork-buff on the handle and crisp clean white on the tapered shaft",
        "motion": "The fine tip of the conductor's baton dips a millimeter in a silent, poised cue and comes to rest."
    },
    {
        "subjects": "exactly one carved rosewood tone bar resting at the optical center with one yarn-wound percussion mallet laid across it",
        "draw_steps": "Begin by actively tracing the rectangular rosewood tone bar contour from one endpoint to the other. Trace the round yarn-wrapped mallet head and thin birch handle next. Construct the two mounting node holes. Add only a few woodgrain marks last.",
        "palette": "a very pale warm rosewood-tan on the bar and sheer pastel lilac-wash on the yarn mallet head",
        "motion": "The yarn mallet head rests gently poised and motionless upon the tone bar."
    },
    {
        "subjects": "exactly one pair of circular domed circular brass clash cymbals connected by an elastic strap loop at the optical center",
        "draw_steps": "Begin by actively tracing the circular saucer rims of both brass discs from one endpoint to the other. Trace the raised central dome cups and strap loops next. Construct the concentric turning grooves. Add only a few fine metallic reflection lines last.",
        "palette": "a very pale luminous champagne-brass on the cymbal plates and sheer tan on the strap loops",
        "motion": "The two brass cymbal discs rest in clear, vibrating, quiet acoustic resonance."
    },
    {
        "subjects": "exactly one compact mother-of-pearl and brass opera glasses binocular standing upright at the optical center with collapsible side handle",
        "draw_steps": "Begin by actively tracing the twin short optical barrels and central bridge from one endpoint to the other. Trace the mother-of-pearl inlays and brass ring trims next. Construct the slender collapsible side handle. Add only a few round lens marks last.",
        "palette": "a very pale iridescent pearl-ivory on the barrels and luminous warm champagne-brass on the metal fittings",
        "motion": "A delicate pearl glint gleams softly across the focus bridge and comes to rest."
    },
    {
        "subjects": "exactly one minimalist metal sheet music stand head standing open at the optical center with twin wire page holding fingers",
        "draw_steps": "Begin by actively tracing the wide V-shaped sheet music tray from one endpoint to the other. Trace the two spring-loaded wire page retaining fingers next. Construct the vertical telescoping shaft collar. Add only a few clean symmetry lines last.",
        "palette": "a very pale matte slate-grey on the metal stand tray with sheer untouched pure white background",
        "motion": "The wire page clips stand in crisp, neat, and quiet rehearsal readiness."
    }
]

# Set 13 세부 묘사
set13_draw_data = [
    {
        "subjects": "exactly one traditional cylindrical pillar postbox standing upright at the optical center with domed cap and rectangular mail posting slot",
        "draw_steps": "Begin by actively tracing the vertical column body outlines from one endpoint to the other. Trace the domed top cap and horizontal mail drop slot next. Construct the collection time plaque mount below. Add only a few circular base plinth lines last.",
        "palette": "a very pale translucent coral-red on the postbox body with pure white background showing through",
        "motion": "The small metal posting slot flap closes with a tiny soft click and comes to rest."
    },
    {
        "subjects": "exactly one carved hardwood judge's gavel resting angled atop its circular wooden sound block base at the optical center",
        "draw_steps": "Begin by actively tracing the circular stepped wooden sound block disk from one endpoint to the other. Trace the turned wooden gavel head with brass band and contoured handle next. Construct the cylindrical striking faces. Add only a few fine woodgrain rings last.",
        "palette": "a very pale warm walnut-brown on the gavel and sound block, with sheer champagne-brass on the center band",
        "motion": "The wooden gavel rests in solemn, dignified and final judicial peace."
    },
    {
        "subjects": "exactly one circular polished brass vault combination lock dial standing at the optical center with knurled knob and index ring",
        "draw_steps": "Begin by actively tracing the circular outer bezel plate from one endpoint to the other. Trace the rotating knurled center knob and index pointer next. Construct the graduation markings around the rim. Add only a few fine metallic reflection lines last.",
        "palette": "a very pale brushed champagne-brass on the lock dial with sheer cool steel on the index marker",
        "motion": "The knurled brass combination knob turns smoothly two tick marks and locks securely."
    },
    {
        "subjects": "exactly one closed formal leather passport booklet standing at the optical center with gold-foil stamped crest emblem",
        "draw_steps": "Begin by actively tracing the rectangular booklet silhouette and edge stitching from one endpoint to the other. Trace the gold-foil stamped national crest emblem next. Construct the smooth spine crease. Add only a few neat rounded corner marks last.",
        "palette": "a very pale deep navy-charcoal on the leather cover with a luminous faint gold glint on the crest",
        "motion": "The leather passport booklet stands poised, ready and still on the clean white space."
    },
    {
        "subjects": "exactly one clean square wooden ballot box standing at the optical center with metal corner brackets and a narrow top drop slot",
        "draw_steps": "Begin by actively tracing the cubic wooden box walls from one endpoint to the other. Trace the top lid with narrow center drop slot next. Construct the four brass corner reinforcing brackets. Add only a few front keyhole plate marks last.",
        "palette": "a very pale natural pine-buff on the wooden box and sheer warm brass on the corner hardware",
        "motion": "The ballot box stands secure, balanced and still in the quiet open space."
    },
    {
        "subjects": "exactly one antique brass postal letter scale standing at the optical center with top letter pan and curved weight graduation plate",
        "draw_steps": "Begin by actively tracing the heavy stepped base and vertical fulcrum post from one endpoint to the other. Trace the curved pointer dial and weight chart next. Construct the top rectangular letter weighing pan. Add only a few pivot marks last.",
        "palette": "a very pale luminous brass on the scale mount with sheer ivory on the chart face",
        "motion": "The top letter pan settles smoothly with a delicate micro-balance and rests level."
    },
    {
        "subjects": "exactly one circular scalloped red sealing wax impression at the optical center with sharp embossed emblem",
        "draw_steps": "Begin by actively tracing the irregular outer wax rim with organic droplet contours from one endpoint to the other. Trace the circular inner crest perimeter next. Construct the crisp embossed shield emblem in the center. Add only a few surface seal marks last.",
        "palette": "a very pale translucent cherry-crimson on the wax seal with bright white highlights on the crest ridges",
        "motion": "The embossed wax seal rests crisp, permanent and completely still."
    },
    {
        "subjects": "exactly one structured leather attaché briefcase standing upright at the optical center with twin polished brass clasp locks",
        "draw_steps": "Begin by actively tracing the rectangular box silhouette and edge welt seams from one endpoint to the other. Trace the centered top handle and dual brass clasp locks next. Construct the keyholes and corner protector studs. Add only a few base lines last.",
        "palette": "a very pale warm caramel-tan on the leather case and sheer sparkling brass on the dual latches",
        "motion": "The twin brass clasp latches give a tiny soft mechanical alignment and stay firmly shut."
    },
    {
        "subjects": "exactly one classic curved rocker ink blotter standing at the optical center with turned wooden handle and brass clamping plate",
        "draw_steps": "Begin by actively tracing the curved semicircular wooden rocker base from one endpoint to the other. Trace the top clamping plate and turned knob handle next. Construct the wrapped felt blotting sheet layer below. Add only a few side brass screws last.",
        "palette": "a very pale warm walnut-brown on the wooden blotter body and sheer polished brass on the top knob",
        "motion": "The curved rocker blotter rocks smoothly once along its rounded base and rests level."
    },
    {
        "subjects": "exactly one clean two-shelf wooden library book cart standing in side profile at the optical center on four small wheels",
        "draw_steps": "Begin by actively tracing the upright wooden upright pillars and curved top push handles from one endpoint to the other. Trace the two sloped V-shelves next. Construct the four small caster wheels at the base. Add only a few neat joinery marks last.",
        "palette": "a very pale warm oak-blonde on the wooden cart with sheer grey on the wheel casters",
        "motion": "The library book cart rests in quiet, studious, orderly stillness on the white surface."
    }
]

# Set 12 적용
for s in data:
    if s["set_id"] == "set12":
        for idx, item in enumerate(set12_draw_data):
            p_text = GOLD_STANDARD_TEMPLATE.format(
                subjects=item["subjects"],
                draw_steps=item["draw_steps"],
                palette=item["palette"],
                motion=item["motion"]
            )
            s["prompts"][idx]["prompt"] = " ".join(p_text.split())

# Set 13 적용
for s in data:
    if s["set_id"] == "set13":
        for idx, item in enumerate(set13_draw_data):
            p_text = GOLD_STANDARD_TEMPLATE.format(
                subjects=item["subjects"],
                draw_steps=item["draw_steps"],
                palette=item["palette"],
                motion=item["motion"]
            )
            s["prompts"][idx]["prompt"] = " ".join(p_text.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("_작업/bulk_sets/set12_10.txt", "w", encoding="utf-8") as f:
    for p in data[8]["prompts"]: # set12
        f.write(p["prompt"] + "\n\n")

with open("_작업/bulk_sets/set13_10.txt", "w", encoding="utf-8") as f:
    for p in data[9]["prompts"]: # set13
        f.write(p["prompt"] + "\n\n")

print("Set 12 & Set 13 대표님 골드 스탠다드 정본 100% 탑재 완료!")

