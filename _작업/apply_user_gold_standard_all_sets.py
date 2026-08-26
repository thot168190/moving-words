# -*- coding: utf-8 -*-
"""
대표님이 직접 주신 [절대 기준 골드 스탠다드 프롬프트] 100% 전면 적용:
- 1. 0-4s: ultra-fine pale warm-grey graphite linework is actively traced stroke by stroke...
- 2. 4-8s: an extremely pale, water-heavy watercolor wash develops gently inside the completed graphite outlines...
- 3. Style + No 블록 100% 완비
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

# Set 10 세부 묘사
set10_draw_data = [
    {
        "subjects": "exactly one classic fountain writing instrument lying angled horizontally at the optical center with split gold nib, and two tiny ink droplets beside it",
        "draw_steps": "Begin by actively tracing the long cylindrical writing instrument barrel outline from one endpoint to the other. Trace the tapered front grip section next. Draw the triangular split gold nib with two traveling curved strokes. Construct the curved pocket clip on the cap, then construct the circular gold trim rings. Add only a few fine metal slit markings and two small round ink droplets last.",
        "palette": "a very pale warm charcoal on the resin instrument body, sheer champagne-gold on the metal nib, and a tiny deep-blue accent on the ink droplets",
        "motion": "A single tiny light glint traces softly once along the polished gold nib slit and comes to rest."
    },
    {
        "subjects": "exactly one classic round reading magnifying glass resting flat at the optical center with turned wooden handle and brass rim",
        "draw_steps": "Begin by actively tracing the turned wooden handle contour from one endpoint to the other. Trace the circular brass lens bezel next with two continuous traveling arcs. Construct the inner convex glass contour. Add only a few delicate reflection arcs across the glass lens last.",
        "palette": "a very pale warm walnut-tan on the wooden handle, sheer champagne-brass on the lens rim, and a delicate optical-cyan tint on the glass",
        "motion": "A soft ray of light glints quietly across the clear convex glass surface and comes to rest."
    },
    {
        "subjects": "exactly one classic flared brass call bell standing upright at the optical center with turned dark wood handle and top finial",
        "draw_steps": "Begin by actively tracing the vertical turned wooden handle outline from one endpoint to the other. Trace the wide flared conical brass bell body next. Construct the circular bottom rim and interior clapper ball. Add only a few delicate metallic reflection lines and top brass collar last.",
        "palette": "a very pale warm brass-gold wash on the bell flare, sheer ebony-charcoal on the handle, and a tiny warm-grey accent on the clapper",
        "motion": "The small internal clapper ball gives a tiny soft vibration and comes to rest."
    },
    {
        "subjects": "exactly one square cut-glass inkwell at the optical center with hinged brass flip lid, standing beside a slender glass dropper pipette",
        "draw_steps": "Begin by actively tracing the bevelled square glass base outlines from one endpoint to the other. Trace the cylindrical neck and hinged domed brass lid next. Construct the slender angled glass dropper pipette beside it. Add only a few fine glass facet lines and liquid level line last.",
        "palette": "a very pale translucent indigo-blue wash inside the inkwell, sheer cool glass-white on the walls, and delicate brass on the lid",
        "motion": "The liquid level inside the clear inkwell settles smoothly horizontal and comes to rest."
    },
    {
        "subjects": "exactly one compact folding wooden book lectern standing open at the optical center with two brass page retention clips",
        "draw_steps": "Begin by actively tracing the flat base board and angled backrest outlines from one endpoint to the other. Trace the lower book shelf ledge next. Construct the two swiveling brass page retention clips one by one. Add only a few fine wood grain lines and rear adjustment prop last.",
        "palette": "a very pale natural birch-tan on the wooden stand, sheer warm brass on the page clips, and faint grey cast shadow lines",
        "motion": "The two small brass page clips settle with a tiny soft alignment and come to rest."
    },
    {
        "subjects": "exactly one vintage heavy steel tabletop stapler shown in clean side profile at the optical center with spring-loaded top pressing lever",
        "draw_steps": "Begin by actively tracing the flat rectangular base and anvil plate outlines from one endpoint to the other. Trace the pivoting metal magazine lever and top pressing cap next. Construct the internal spring channel. Add only a few clean mechanical alignment marks and rubber base pads last.",
        "palette": "a very pale vintage industrial slate-grey on the metal body, sheer brushed chrome on the anvil, and faint black on the rubber base",
        "motion": "The top pressing cap settles with a tiny crisp alignment and comes to rest."
    },
    {
        "subjects": "exactly one compact wedge-shaped brass pencil sharpener at the optical center with steel blade screwed to its sloped side",
        "draw_steps": "Begin by actively tracing the rectangular brass block and side grip ridges from one endpoint to the other. Trace the cone-shaped pencil entry hole next. Construct the sloped steel cutting blade and center clamping screw. Add only a few fine metallic reflection lines last.",
        "palette": "a very pale brushed champagne-brass on the sharpener body and sheer cool steel-silver on the cutting blade",
        "motion": "The small sharpener rests balanced and still on the clean white space."
    },
    {
        "subjects": "exactly one closed thick hardcover volume lying flat at the optical center with an embroidered silk ribbon bookmark trailing out",
        "draw_steps": "Begin by actively tracing the rectangular book spine and front cloth cover outlines from one endpoint to the other. Trace the layered page edges along the side next. Construct the flowing S-curve silk ribbon bookmark trailing from the top spine. Add only a few fine cloth weave marks last.",
        "palette": "a very pale sage-green on the book cloth cover, sheer crimson-silk wash on the trailing ribbon, and warm-ivory on the page edges",
        "motion": "The trailing silk ribbon tip flutters softly once in a quiet room draft and comes to rest."
    },
    {
        "subjects": "exactly one large classic looped steel wire paperclip resting flat at the optical center beside three small round brass pushpins",
        "draw_steps": "Begin by actively tracing the outer curved loop of the steel wire clip from one endpoint to the other. Trace the concentric inner gripping wire loops next. Construct the three small round-headed brass drawing pins one by one. Add only a few fine metallic reflection lines last.",
        "palette": "a very pale polished steel-grey on the wire paperclip and delicate warm champagne-brass on the pushpin heads",
        "motion": "The paperclip and pins rest in orderly, clean graphic stillness."
    },
    {
        "subjects": "exactly one turned brass seal stamp standing upright at the optical center with round engraved bottom crest",
        "draw_steps": "Begin by actively tracing the turned brass handle and rounded top knob from one endpoint to the other. Trace the cylindrical neck and wide circular stamping base next. Construct the engraved crest lines on the lower rim. Add only a few fine turned groove highlights last.",
        "palette": "a very pale luminous champagne-brass wash on the stamp body with bright white untouched highlights",
        "motion": "The heavy brass seal stands perfectly vertical, poised and still."
    }
]

# Set 11 세부 묘사 (대표님 주신 기준 완벽 탑재)
set11_draw_data = [
    {
        "subjects": "exactly one delicate ceramic teaspoon resting flat at the optical center, exactly two neat square white sugar cubes beside it, and one tiny loose sugar grain",
        "draw_steps": "Begin by actively tracing the slender outer curve of the teaspoon handle from one endpoint to the other. Trace the opposite edge of the handle next. Draw the oval spoon bowl with two separate traveling curved strokes. Construct the first sugar cube one straight edge at a time, then construct the second sugar cube one straight edge at a time. Add only a few tiny edge marks and one small loose sugar grain last.",
        "palette": "a very pale warm ivory on the ceramic teaspoon, sheer cool blue-grey on one face of each sugar cube, and a tiny warm-grey accent on the loose sugar grain",
        "motion": "One tiny sugar grain shifts softly away from the nearest cube and comes to rest."
    },
    {
        "subjects": "exactly one tall turned wooden pepper mill standing upright at the optical center with brass adjustment screw knob and three cracked peppercorns",
        "draw_steps": "Begin by actively tracing the cylindrical wooden body and curved waist outlines from one endpoint to the other. Trace the rotating top dome and small brass screw knob next. Construct the lower grinding base. Add only a few fine wood grain lines and three small cracked peppercorns last.",
        "palette": "a very pale warm chestnut-tan on the wooden body, sheer champagne-brass on the adjustment knob, and dark-grey on the peppercorns",
        "motion": "The top wooden knob rotates smoothly by a quarter turn and comes to rest."
    },
    {
        "subjects": "exactly one rectangular white ceramic butter dish with dome lid handle at the optical center, and one flat wooden butter spreader",
        "draw_steps": "Begin by actively tracing the rectangular flanged ceramic tray outlines from one endpoint to the other. Trace the dome cover and top loop handle next. Construct the flat wooden butter spreader beside it. Add only a few fine dish rim lines and spreader bevel marks last.",
        "palette": "a very pale warm-white on the ceramic covered dish and sheer honey-maple on the wooden spreader",
        "motion": "The flat wooden spreader settles with a tiny soft alignment and comes to rest."
    },
    {
        "subjects": "exactly one ribbed clear glass honey jar at the optical center holding one turned wooden grooved honey dipper, and one hanging amber honey drop",
        "draw_steps": "Begin by actively tracing the rounded glass honey pot outlines from one endpoint to the other. Trace the concentric horizontal glass rib rings next. Construct the wooden honey wand with concentric discs and one hanging drop. Add only a few fine glass reflection lines last.",
        "palette": "a very pale translucent golden-amber in the honey pot and sheer birch-blonde on the wooden dipper",
        "motion": "One tiny viscous amber drop of honey hangs from the lowest dipper disc and rests still."
    },
    {
        "subjects": "exactly one stout ceramic cocoa mug standing at the optical center with an arched handle, holding one rolled cinnamon bark stick",
        "draw_steps": "Begin by actively tracing the cylindrical ceramic mug body and sturdy ear handle outlines from one endpoint to the other. Trace the rolled bark scroll of the cinnamon stick next. Construct the smooth circular rim. Add only a few fine ceramic wall highlights last.",
        "palette": "a very pale warm oatmeal-beige on the mug and a sheer whisper of cinnamon-tan on the bark stick",
        "motion": "A single transparent white steam wisp rises gently from the cup rim and dissipates."
    },
    {
        "subjects": "exactly one nested set of four graduated wooden measuring spoons held together on a simple brass ring at the optical center",
        "draw_steps": "Begin by actively tracing the circular brass connecting loop ring from one endpoint to the other. Trace the four fan-shaped nested wooden spoon handle outlines next. Construct the four graduated round spoon bowls one by one. Add only a few fine nested contour lines last.",
        "palette": "a very pale natural beech-tan wash on the wooden spoons and sheer champagne-brass on the loop ring",
        "motion": "The smallest spoon in the nest settles with a tiny soft adjustment and comes to rest."
    },
    {
        "subjects": "exactly one classic faceted clear glass salt shaker standing upright at the optical center with perforated metal dome cap and loose salt grains",
        "draw_steps": "Begin by actively tracing the vertical faceted glass body outlines from one endpoint to the other. Trace the domed metal cap and tiny shake hole dots next. Construct the crystalline salt level line inside. Add only a few fine loose salt grains at the base last.",
        "palette": "a very pale cool glass-blue on the shaker walls and sheer polished chrome-silver on the metal cap",
        "motion": "A single tiny salt crystal shifts softly on the surface and comes to rest."
    },
    {
        "subjects": "exactly one small fluted white ceramic espresso cup resting on its circular matching saucer at the optical center with golden crema surface",
        "draw_steps": "Begin by actively tracing the circular saucer plate and center depression from one endpoint to the other. Trace the small thick-walled espresso cup and loop handle next. Construct the rich crema surface level line. Add only a few fine fluted cup facet lines last.",
        "palette": "a very pale clean warm-white on the ceramic cup and saucer, with a delicate whisper of hazelnut-tan crema",
        "motion": "A tiny wisp of transparent steam curls gently once from the warm cup surface and comes to rest."
    },
    {
        "subjects": "exactly one ribbed white ceramic lemon citrus squeezer dish at the optical center with sharp fluted cone and one crystal juice drop",
        "draw_steps": "Begin by actively tracing the circular shallow saucer outline and side pouring spout from one endpoint to the other. Trace the radial pointed squeezing cone next. Construct the small handle loop. Add only a few seed catching slots and one juice droplet last.",
        "palette": "a very pale clean warm-white on the ceramic dish with a sheer whisper of pastel-lemon tint in the saucer",
        "motion": "A single tiny crystal drop of citrus juice drips softly from the spout into the dish and comes to rest."
    },
    {
        "subjects": "exactly one round carved wooden paddle cutting board resting flat at the optical center, holding one fresh leafy olive sprig with two olives",
        "draw_steps": "Begin by actively tracing the circular paddle board and handle outline from one endpoint to the other. Trace the slender woody olive twig and five pointed leaves next. Construct the two smooth oval olives. Add only a few fine wood grain lines last.",
        "palette": "a very pale warm olive-wood tan on the board and sheer delicate sage-green on the fresh leaves",
        "motion": "The fresh olive leaf tip settles gently with one quiet micro-motion and comes to rest."
    }
]

# Set 10 적용
for s in data:
    if s["set_id"] == "set10":
        for idx, item in enumerate(set10_draw_data):
            p_text = GOLD_STANDARD_TEMPLATE.format(
                subjects=item["subjects"],
                draw_steps=item["draw_steps"],
                palette=item["palette"],
                motion=item["motion"]
            )
            s["prompts"][idx]["prompt"] = " ".join(p_text.split())

# Set 11 적용
for s in data:
    if s["set_id"] == "set11":
        for idx, item in enumerate(set11_draw_data):
            p_text = GOLD_STANDARD_TEMPLATE.format(
                subjects=item["subjects"],
                draw_steps=item["draw_steps"],
                palette=item["palette"],
                motion=item["motion"]
            )
            s["prompts"][idx]["prompt"] = " ".join(p_text.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("_작업/bulk_sets/set10_10.txt", "w", encoding="utf-8") as f:
    for p in data[6]["prompts"]: # set10
        f.write(p["prompt"] + "\n\n")

with open("_작업/bulk_sets/set11_10.txt", "w", encoding="utf-8") as f:
    for p in data[7]["prompts"]: # set11
        f.write(p["prompt"] + "\n\n")

print("대표님 골드 스탠다드 기준 프롬프트 Set 10 & Set 11 전면 탑재 완료!")

