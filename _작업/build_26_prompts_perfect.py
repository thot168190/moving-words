# -*- coding: utf-8 -*-
import os, re

# 3대 정본 원칙 엄격 적용:
# 1. 모든 사물 앞에 반드시 'illustrated' 명시 (2D 그림 락)
# 2. 실사 유발어 완전 삭제: polished, metallic, 35mm, classic, radiant 삭제
# 3. 색상 표현을 100% 맑은 수채화 어휘(pale, transparent, soft, watercolor wash, sheer)로 정제

scenes = [
    # 01. 우체국 창구
    {
        "id": "01",
        "title": "우체국 창구 (Post office counter)",
        "subjects": "exactly one illustrated vintage post office counter with a small glass partition window, one illustrated brown parcel box, one illustrated sheet of postage stamps and one illustrated brass letter scale",
        "draw_steps": "The wooden counter frame is constructed first through separate hair-thin graphite lines, followed by the arched clerk window, the rectangular parcel box with twine string, the serrated outline of the stamp sheet, and the delicate brass balancing scale. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "A warm pale amber wash settles over the wooden counter and parcel, soft sheer teal-grey tints the glass partition, pale vermilion and cobalt accent the tiny stamp sheet, and soft transparent ochre wash fills the brass scale.",
        "motion": "the small brass scale pan gently tilts down two millimetres under a parcel's weight and settles. The counter, stamps and window remain fixed.",
        "extra_style": "delicate postal artifact textures,",
        "subject_lock": "Exactly one parcel and one scale."
    },
    # 02. 응급실 앞
    {
        "id": "02",
        "title": "응급실 앞 (Emergency ambulance)",
        "subjects": "exactly one illustrated white medical ambulance with red cross markings, one illustrated rooftop beacon light and one illustrated folded wheeled stretcher beside it",
        "draw_steps": "The boxy contours of the ambulance body are traced first through clean graphite lines, followed by the wheel arches, headlights, rooftop beacon housing, side window panels and the delicate frame of the wheeled stretcher. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "A crisp pale white-grey watercolor wash defines the ambulance panels, soft crimson red glazes the cross and stripe markings, transparent pale cobalt tints the windows, and soft amber wash colors the rooftop beacon.",
        "motion": "the rooftop amber beacon pulses with a gentle rhythmic transparent glow once and dims slightly. The vehicle and stretcher remain fixed.",
        "extra_style": "crisp hand-drawn vehicle contours,",
        "subject_lock": "Exactly one ambulance and one stretcher."
    },
    # 03. 법정
    {
        "id": "03",
        "title": "법정 (Courtroom bench & gavel)",
        "subjects": "exactly one illustrated wooden judge gavel resting on its round sound block, exactly one illustrated leather-bound law book and one illustrated brass justice balance scale",
        "draw_steps": "The cylindrical head of the gavel and its turned handle are traced first with fine graphite ellipses, followed by the beveled sound block, the thick spine of the open law book with stacked pages, and the symmetrical brass balance scale. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Warm mahogany brown watercolor wash layers across the gavel and sound block, soft burnt umber tones the antique book leather with creamy parchment pages, and clear transparent golden ochre wash develops over the brass scale.",
        "motion": "the gavel head tilts slightly upwards one centimetre and settles firmly back onto the sound block. The book and balance remain fixed.",
        "extra_style": "dignified antique legal textures,",
        "subject_lock": "Exactly one gavel, one book and one scale."
    },
    # 04. 기차역 승강장
    {
        "id": "04",
        "title": "기차역 승강장 (Steam locomotive & railway station)",
        "subjects": "exactly one illustrated vintage steam locomotive engine at a platform, exactly two illustrated parallel steel railway tracks and one illustrated hanging round station clock",
        "draw_steps": "The cylindrical boiler, smokestack, cowcatcher, and spoked driving wheels are constructed through intricate graphite contours, followed by the straight parallel steel rails, wooden sleepers, and the circular hanging station clock. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Layered pale charcoal-grey watercolor washes define the locomotive body, soft pale steel-blue glazes the rails, and warm transparent ochre wash trims the clock casing.",
        "motion": "a tiny wisp of soft transparent grey steam rises three centimetres from the chimney stack and drifts. The train, tracks and clock remain fixed.",
        "extra_style": "intricate hand-drawn machinery details,",
        "subject_lock": "Exactly one locomotive and one clock."
    },
    # 05. 박물관 전시실
    {
        "id": "05",
        "title": "박물관 전시실 (Museum exhibition showcase)",
        "subjects": "exactly one illustrated museum glass showcase cabinet on a marble pedestal, displaying one illustrated ancient carved clay urn and one illustrated brass descriptive plaque",
        "draw_steps": "The rectilinear glass cabinet frame is drawn with sharp graphite lines, followed by the fluted marble pedestal, the delicate handles and textured relief band of the ancient clay urn, and the rectangular brass museum label. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Cool transparent mint-grey watercolor tints the glass panes, earthy terracotta ochre wash layers over the urn with subtle patina, and pale warm grey veins pattern the marble stand.",
        "motion": "a soft focused ray of pale golden light illuminates the urn for a moment across the glass. The cabinet and urn remain completely fixed.",
        "extra_style": "museum-quality artifact precision,",
        "subject_lock": "Exactly one cabinet and one urn."
    },
    # 06. 호텔 로비
    {
        "id": "06",
        "title": "호텔 로비 (Hotel front desk)",
        "subjects": "exactly one illustrated curved wooden hotel front reception desk, one illustrated brass service call bell, exactly one illustrated vintage key with a numbered brass tag and one illustrated leather luggage suitcase",
        "draw_steps": "The sweep of the wooden reception counter is traced with fine graphite, followed by the domed service bell, the notched antique key with its oval tag, and the buckled straps and corners of the leather suitcase. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Warm walnut brown watercolor wash glazes the counter, soft transparent ochre develops on the desk bell and key tag, and rich tan leather wash tones the luggage.",
        "motion": "the brass key tag sways gently side to side two millimetres and comes to rest. The desk, bell and suitcase remain fixed.",
        "extra_style": "vintage hospitality brass and leather textures,",
        "subject_lock": "Exactly one bell, one key and one suitcase."
    },
    # 07. 영화관
    {
        "id": "07",
        "title": "영화관 (Cinema film projector)",
        "subjects": "exactly one illustrated vintage cinema film projector with two spoked reels, one illustrated projector lens and one illustrated trailing strip of perforated celluloid film",
        "draw_steps": "The mechanical body of the projector, dual circular film reels with detailed cutouts, optical lens barrel, and the winding film strip are drawn with hair-thin graphite lines. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Pale slate-grey watercolor wash layers over the projector chassis, soft transparent ochre wash highlights the lens rim, and transparent sepia glaze colors the translucent film ribbon.",
        "motion": "the top film reel slowly rotates one quarter turn and stops. The projector body, lens and film stand remain fixed.",
        "extra_style": "intricate vintage cinema apparatus details,",
        "subject_lock": "Exactly one film projector."
    },
    # 08. 옛 성
    {
        "id": "08",
        "title": "옛 성 (Medieval castle watchtower)",
        "subjects": "exactly one illustrated medieval stone castle fortress with crenellated battlements, one illustrated high arched watchtower, one illustrated wooden portcullis gate and one illustrated gold royal crown emblem",
        "draw_steps": "The stone block masonry of the fortress walls is constructed block by block with fine graphite, followed by the rounded watchtower, wooden timber portcullis lattice, and the jeweled peaks of the royal crown. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Weathered sandstone-grey and olive-tinted stone watercolor washes layer across the castle walls, soft oak-brown colors the wooden gate, and pale transparent yellow accents the crown.",
        "motion": "a tiny cloth pennant atop the highest tower flutter-waves gently once in a breeze and settles. The stone castle remains fixed.",
        "extra_style": "historical architectural stone masonry details,",
        "subject_lock": "Exactly one castle fortress."
    },
    # 09. 감옥 창살
    {
        "id": "09",
        "title": "감옥 창살 (Prison cell iron bars)",
        "subjects": "exactly five illustrated vertical iron prison cell bars, one illustrated horizontal crossbar, exactly one illustrated antique iron padlock and one illustrated large skeleton key in the keyhole",
        "draw_steps": "The straight cylindrical iron bars with subtle texture marks are drawn with graphite, followed by the bolted crossbar, the curved shackle of the padlock, and the notched skeleton key. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Deep charcoal-grey watercolor wash layers over the bars with subtle rust-orange specks along the joints, and cool slate-black tones darken the padlock.",
        "motion": "the skeleton key slowly turns forty-five degrees inside the padlock keyhole and stops. The iron bars and padlock remain fixed.",
        "extra_style": "vintage iron and lock craftsmanship,",
        "subject_lock": "Exactly five iron bars and one padlock."
    },
    # 10. 실험실 작업대
    {
        "id": "10",
        "title": "실험실 작업대 (Science laboratory workbench)",
        "subjects": "exactly one illustrated brass laboratory microscope, one illustrated glass conical flask containing liquid and one illustrated open scientific research logbook with diagrams",
        "draw_steps": "The curved brass arm, eyepiece, objective lenses and stage of the microscope are drawn with hair-thin graphite, followed by the transparent flask contour with meniscus liquid line, and the open logbook pages. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Soft transparent golden ochre watercolor wash covers the microscope body, pale transparent cyan-blue wash fills the flask liquid, and warm sepia tones the notes in the logbook.",
        "motion": "one tiny transparent bubble rises inside the flask liquid to the surface and pops. The microscope, flask and notebook remain fixed.",
        "extra_style": "precise scientific instrument engravings,",
        "subject_lock": "Exactly one microscope and one flask."
    },
    # 11. 방직 공장
    {
        "id": "11",
        "title": "방직 공장 (Textile mill & weaving loom)",
        "subjects": "exactly one illustrated historic wooden weaving loom machine with wooden frame, harness reeds, one illustrated flying shuttle with thread and three illustrated wound yarn spools",
        "draw_steps": "The timber frame of the loom is constructed with graphite lines, followed by the parallel warp threads, the wooden shuttle, and the three cylindrical spools of colorful wound thread. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Warm honey-pine watercolor wash develops over the loom wood, cobalt blue, crimson and saffron-yellow washes layer over the three thread spools, with fine white thread highlights preserved.",
        "motion": "the wooden shuttle slides three centimetres smoothly across the warp threads and stops. The loom frame and spools remain fixed.",
        "extra_style": "intricate textile weaving mechanics,",
        "subject_lock": "Exactly one loom, one shuttle and three spools."
    },
    # 12. 구조 헬리콥터
    {
        "id": "12",
        "title": "구조 헬리콥터 (Rescue helicopter)",
        "subjects": "exactly one illustrated rescue helicopter resting flat, with four illustrated overhead rotor blades, tail boom rotor, landing skids and red rescue cross marking",
        "draw_steps": "The aerodynamic fuselage, curved cockpit glass, overhead rotor hub with long narrow blades, tail boom, and tubular landing skids are traced with precise graphite lines. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Soft lemon-yellow and white watercolor washes color the fuselage panels, crisp red glazes the rescue emblem, and transparent cerulean-blue tints the canopy glass.",
        "motion": "the overhead rotor blades make a gentle slow half-rotation and come to a soft stop. The fuselage and landing skids remain fixed.",
        "extra_style": "clean hand-drawn aeronautical contours,",
        "subject_lock": "Exactly one rescue helicopter."
    },
    # 13. 발사대의 로켓
    {
        "id": "13",
        "title": "발사대의 로켓 (Space rocket on launchpad)",
        "subjects": "exactly one illustrated multi-stage space rocket standing vertical, with aerodynamic nose cone, rocket booster engines, service gantry tower arm and umbilical cables",
        "draw_steps": "The cylindrical rocket stages with panel seams are drawn in graphite, followed by the conical engine nozzles, aerodynamic fins, and the structural steel trusswork of the gantry service arm. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Clean porcelain-white watercolor wash defines the rocket hull with orange insulation accents, soft slate-grey tones the metal truss gantry, and pale charcoal shades the engine bells.",
        "motion": "a thin soft plume of white condensation vapor vents gently from the rocket flank and fades. The rocket and launch tower remain fixed.",
        "extra_style": "detailed aerospace hand-drawn schematics,",
        "subject_lock": "Exactly one rocket and one launch tower."
    },
    # 14. 거리 행진
    {
        "id": "14",
        "title": "거리 행진 (Parade brass band van)",
        "subjects": "exactly one illustrated vintage open-back parade van decorated with festive bunting, exactly one illustrated upright bass drum and one illustrated brass sousaphone tuba",
        "draw_steps": "The retro vehicle body, spoked wheels, decorative fabric festoons, large circular bass drum with tension rods, and the wide flared bell of the brass tuba are drawn in fine graphite. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Pastel sky-blue watercolor wash layers over the van, soft golden ochre and pale yellow glaze the brass tuba bell, and festive red-and-white stripes color the bunting.",
        "motion": "one decorative pennant flag on the van corner flutters gently once in the air and settles. The vehicle, drum and tuba remain fixed.",
        "extra_style": "cheerful vintage celebration iconography,",
        "subject_lock": "Exactly one van, one drum and one tuba."
    },
    # 15. 가게 계산대
    {
        "id": "15",
        "title": "가게 계산대 (Shop cash register counter)",
        "subjects": "exactly one illustrated antique mechanical brass cash register with numbered popup flags, one illustrated paper receipt roll, one illustrated price tag and three illustrated silver coins",
        "draw_steps": "The filigree housing of the cash register, mechanical keys, crank handle, cash drawer, looped paper receipt, and three round coins are drawn with hair-thin graphite lines. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Soft transparent ochre and bronze watercolor washes layer over the register body, crisp white wash defines the paper receipt, and pale silver-grey tints the coins.",
        "motion": "the paper receipt curls slightly further down by five millimetres and stops. The register and coins remain fixed.",
        "extra_style": "ornate vintage mercantile brasswork,",
        "subject_lock": "Exactly one cash register and three coins."
    },
    # 16. 은행 창구
    {
        "id": "16",
        "title": "은행 창구 (Bank counter & vault)",
        "subjects": "exactly one illustrated circular bank vault door with spoke wheel lock, one illustrated leather financial ledger book and one illustrated brass official seal stamp",
        "draw_steps": "The concentric circles, locking bolts and wheel handle of the vault door are drawn in fine graphite, followed by the thick open ledger with ruled columns, and the turned brass handle of the seal stamp. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Soft slate-grey and pale graphite watercolor washes tone the vault door, dark forest-green leather glazes the ledger cover, and warm transparent gold shines on the seal stamp.",
        "motion": "the circular spoke wheel on the vault door rotates thirty degrees smoothly and clicks locked. The vault door and ledger remain fixed.",
        "extra_style": "vintage secure banking vault mechanics,",
        "subject_lock": "Exactly one vault door, one ledger and one stamp."
    },
    # 17. 식당 차림표
    {
        "id": "17",
        "title": "식당 차림표 (Restaurant menu board & spice jars)",
        "subjects": "exactly one illustrated wooden chalkboard menu stand, one illustrated handwritten recipe notebook, exactly two illustrated glass spice seasoning shakers and one illustrated fresh herb sprig",
        "draw_steps": "The timber frame of the menu board, chalk script lines, spiral-bound recipe notebook, faceted glass shakers with metal tops, and herb leaves are drawn with delicate graphite contours. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Dark charcoal-slate watercolor wash fills the chalkboard with pale chalk highlights, warm pine wood frames the stand, and transparent sage green colors the fresh herb.",
        "motion": "one herb leaf on the sprig sways gently two millimetres and rests. The menu board, notebook and jars remain fixed.",
        "extra_style": "charming culinary bistro aesthetics,",
        "subject_lock": "Exactly one menu board, one notebook and two jars."
    },
    # 18. 사람의 머리와 목 해부도
    {
        "id": "18",
        "title": "사람의 머리와 목 해부도 (Human head & throat anatomy)",
        "subjects": "an anatomical medical illustration plate showing exactly one illustrated human head profile with brain cross-section, illustrated throat vocal anatomy and one illustrated knee joint structural study",
        "draw_steps": "The profile head contour, convoluted cerebral cortex lobes, cerebellum, spinal column, throat larynx structure, and articulated knee joint bones are drawn with fine medical graphite precision. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Soft translucent dusty-rose and lavender-pink watercolor washes define the brain tissue, warm beige-ochre tones the skin contour, and delicate bone-ivory washes color the knee joint.",
        "motion": "the subtle nerve pathway highlights pulse softly once with a faint luminous golden glow and stabilize. All anatomical structures remain fixed.",
        "extra_style": "classical medical encyclopedia anatomical plate,",
        "subject_lock": "Anatomical study plate layout."
    },
    # 19. 기계 제어반
    {
        "id": "19",
        "title": "기계 제어반 (Industrial control panel)",
        "subjects": "exactly one illustrated vintage industrial control panel with analog pressure gauges, toggle switch levers, one illustrated hydraulic pump knob and one illustrated CRT monitor screen",
        "draw_steps": "The rectangular metal panel face, round dial meters with needles, heavy toggle switches, rotary pump valve wheel, and curved CRT monitor bezel are constructed with crisp graphite lines. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Soft olive-grey and pale cream enamel watercolor washes color the metal console, soft ochre accents the dials, and transparent amber-green glows faintly inside the monitor display.",
        "motion": "the needle on the central round pressure dial shifts gently by ten degrees and settles steadily. The panel, switches and screen remain fixed.",
        "extra_style": "precise analog industrial instrumentation,",
        "subject_lock": "Exactly one control panel console."
    },
    # 20. 석탄 광차
    {
        "id": "20",
        "title": "석탄 광차 (Coal mining cart)",
        "subjects": "exactly one illustrated iron mining rail cart heaped with jagged black coal lumps, resting on two steel rails, with one illustrated miner's iron shovel beside it",
        "draw_steps": "The riveted steel hopper of the ore cart, flanged iron wheels, rugged faceted coal rocks, timber ties with steel rails, and the long wooden handle shovel are drawn with hair-thin graphite lines. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Deep layered charcoal and indigo watercolor washes develop across the coal chunks, soft iron-brown wash patinas the cart, and ash-grey tones the rails.",
        "motion": "one small coal pebble rolls down two centimetres from the heap into the cart and stops. The cart, rails and shovel remain fixed.",
        "extra_style": "historical mineral mining equipment textures,",
        "subject_lock": "Exactly one coal cart and one shovel."
    },
    # 21. 가족 사진틀
    {
        "id": "21",
        "title": "가족 사진틀 (Family photo frame & rings)",
        "subjects": "exactly one illustrated ornate carved oval wooden picture frame containing a vintage family portrait, beside two illustrated interlocking gold wedding rings on a lace cloth",
        "draw_steps": "The baroque leaf carvings of the oval frame, delicate sepia portrait silhouettes of family members, the interlocking double rings with circular ellipses, and lace fabric patterns are traced in graphite. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Rich antique walnut-brown watercolor wash layers over the frame, warm nostalgic sepia tones the portrait, soft transparent gold shines on the wedding rings, and soft ivory washes the lace.",
        "motion": "one gold ring catches a soft bright glint of light across its curve and stabilizes. The frame, portrait and rings remain fixed.",
        "extra_style": "tender heirloom portraiture details,",
        "subject_lock": "Exactly one frame and two rings."
    },
    # 22. 광장의 군중
    {
        "id": "22",
        "title": "광장의 군중 (Historic town square assembly)",
        "subjects": "an illustrated historical town square scene with cobblestone pavement, one illustrated wooden speaker podium, two illustrated waving fabric banners and assembled citizen silhouettes",
        "draw_steps": "The perspective of cobblestones, classical building facade in background, timber speaker podium, drapery folds of the banner flags, and distinct group silhouettes are drawn with fine graphite lines. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Warm sandstone ochre and terracotta watercolor washes tint the square buildings, soft crimson and cobalt glaze the waving flags, and neutral charcoal-sepia washes the crowd.",
        "motion": "the fabric corner of the main red banner ripples gently once in the air and settles. The square, podium and crowd remain fixed.",
        "extra_style": "classical historical civic gathering panorama,",
        "subject_lock": "Town square assembly composition."
    },
    # 23. 군용 장비
    {
        "id": "23",
        "title": "군용 장비 (Military field equipment)",
        "subjects": "exactly one illustrated steel military helmet with chin strap, one illustrated leather field boot and one illustrated brass field binoculars in its canvas case",
        "draw_steps": "The rounded dome of the steel helmet with rim seam, stitched eyelets of the leather boot, cylindrical barrels of the binoculars, and canvas texture of the case are drawn with fine graphite. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Soft matte olive-drab watercolor wash covers the helmet, deep distressed brown leather washes the boot, and pale khaki-tan develops over the canvas case.",
        "motion": "the leather chin strap of the helmet sways two millimetres and rests. The helmet, boot and binoculars remain fixed.",
        "extra_style": "vintage military field gear craftsmanship,",
        "subject_lock": "Exactly one helmet, one boot and one binoculars."
    },
    # 24. 시인의 책상
    {
        "id": "24",
        "title": "시인의 책상 (Poet's writing desk)",
        "subjects": "exactly one illustrated rustic wooden writing desk with handwritten poem manuscript pages, one illustrated feather dip pen with ink bottle, and one illustrated lit wax candle in a brass holder",
        "draw_steps": "The wooden plank grain of the desk, cursive lines on the paper manuscript, delicate barbs of the feather quill, square glass ink bottle, and dripping wax candle are drawn with hair-thin graphite. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Warm cedar-brown watercolor wash tones the desk, creamy parchment washes color the paper with sepia ink lines, and soft amber-yellow glow radiates from the candle flame.",
        "motion": "the small golden candle flame wavers gently once sideways and stands upright and steady. The desk, pen and manuscript remain fixed.",
        "extra_style": "romantic literary manuscript atmosphere,",
        "subject_lock": "Exactly one quill pen, one ink bottle and one candle."
    },
    # 25. 골프 그린
    {
        "id": "25",
        "title": "골프 그린 (Golf green & pin)",
        "subjects": "exactly one illustrated golf putting green with cup hole, one illustrated flagstick with red numbered flag, one illustrated white dimpled golf ball resting near the cup, and one illustrated steel iron club head",
        "draw_steps": "The smooth curved contours of the green turf, circular cup lip, vertical flagstick, triangular flag fabric, dimpled sphere of the golf ball, and steel club face are traced with precise graphite lines. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Fresh layered emerald and lime-green watercolor washes tone the grass, soft scarlet red colors the flag, and clean pale white-grey with subtle shadows glazes the ball.",
        "motion": "the white golf ball rolls forward three centimetres directly toward the cup and stops right at the edge. The green, flagstick and club remain fixed.",
        "extra_style": "crisp sporting equipment anatomy,",
        "subject_lock": "Exactly one golf ball, one flagstick and one club."
    },
    # 26. 초원의 얼룩말
    {
        "id": "26",
        "title": "초원의 얼룩말 (Savanna zebra)",
        "subjects": "exactly one illustrated African zebra standing calmly in side profile on a savanna ground, with black-and-white stripe patterns, mane, and sparse wild grasses",
        "draw_steps": "The anatomical musculature of the zebra, curved neck, upright mane, muzzle, hooves, tail, and each individual zebra stripe contour are drawn with delicate 2H graphite precision. Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons or basic outlines.",
        "color_steps": "Crisp paper-white body washes are overlaid with layered soft charcoal-black watercolor stripes, warm ochre-tan tones the savanna soil, and golden-straw washes the grasses.",
        "motion": "the zebra's tufted tail swishes gently once side to side and comes to a complete stop. The animal body, legs and head remain fixed.",
        "extra_style": "museum-quality zoological wildlife plate,",
        "subject_lock": "Exactly one zebra."
    }
]

def build_pure_single_line_prompt(s):
    raw = f"""Progressive detailed fine-pencil construction, transparent watercolor and gentle object-motion animation on a solid pure bright white background (#FFFFFF), edge to edge. The first frame is an entirely empty pure white field. Static locked-off camera, one continuous 8-second take. The only visible subjects are {s['subjects']}. 0-3.5s: exceptionally fine pale-neutral 2H graphite strokes are visibly traced one by one across the empty white field. {s['draw_steps']} Each stroke has a clear beginning and endpoint. The illustration is built progressively rather than fading into view. Previously completed lines remain stable. 3.5-5.5s: clear transparent watercolor develops in layered color. {s['color_steps']} Preserve narrow white-paper highlights while keeping the colors fresh, luminous and distinguishable, with graphite details visible through every layer. 5.5-8s: {s['motion']} All other elements remain fixed. All graphite construction lines and watercolor boundaries remain stable. Style: intricate premium pencil-and-watercolor plate, numerous hair-thin pale graphite construction lines, accurate object anatomy, luminous layered transparent watercolor, {s['extra_style']} sophisticated museum-quality illustrated-dictionary artwork, clearly hand-drawn and never photographic. No dark outline, black ink, sepia ink, charcoal, thick contour, product photography, studio lighting, realistic reflection, glossy highlight, cast shadow, 3D, CGI, text, label, border, hand, artist or visible drawing tool. {s['subject_lock']} Completely silent."""
    # 모든 줄바꿈과 연속 공백을 공백 1칸으로 완전 평탄화
    single_line = re.sub(r'\s+', ' ', raw).strip()
    return single_line

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BULK_DIR = os.path.join(ROOT, "_작업/bulk_26")
os.makedirs(BULK_DIR, exist_ok=True)

batches = [
    ("bulk_part1_01_07.txt", scenes[0:7]),
    ("bulk_part2_08_14.txt", scenes[7:14]),
    ("bulk_part3_15_20.txt", scenes[14:20]),
    ("bulk_part4_21_26.txt", scenes[20:26]),
]

for filename, batch_scenes in batches:
    filepath = os.path.join(BULK_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        single_line_prompts = [build_pure_single_line_prompt(sc) for sc in batch_scenes]
        f.write("\n\n".join(single_line_prompts) + "\n")
    print(f"정본 2D 세필수채 프롬프트 생성: {filepath} ({len(batch_scenes)}개)")

print("\n26편 전편: illustrated 100% 장착 + 실사유발어 완전제거 + 맑은 수채어휘 교체 완료!")
