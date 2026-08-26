# -*- coding: utf-8 -*-
"""
대표님 명령: Set 04부터 Set 13까지 10개 세트 (총 100편) 전체를
'딱정벌레 성인 자연사 도감 (Beetle Adult Natural-History Atlas)' 최고 정본으로 100% 전면 재건축!

핵심 원칙:
1. 사물 나열 금지: 중앙에 1~2개 핵심 소품만 콤팩트하게 배치 (Hero Subject)
2. 순백 100% 락: no board, no panel, no background scenery, no darkness
3. 선단 자라남 문법 + 내부 빗금/해칭 0% 완전 박멸
4. 물 95% 투명 파스텔 글레이즈
5. Style: sophisticated museum-quality editorial illustration for an adult natural-history atlas
"""

import json

PERFECT_ATLAS_TEMPLATE = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. The background is one single continuous field of pure white reaching every outer edge, and the subjects sit directly on that white with nothing underneath them - no board, no panel, no card, no mat, no textured surface and no visible edge of any kind. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The subjects remain centered while both outer edges stay clear. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are {subjects}. There is no visible person, driver, student, live action element, wall, ceiling, darkness or heavy architecture anywhere.

0-4s: hair-thin pale graphite linework appears progressively from the empty white field. Throughout the whole sequence the field contains only the flat white surface and the marks already made on it; nothing else is ever present at any moment. Each line is drawn as a moving point that travels from one end to the other, its advancing tip clearly visible the whole way, one line at a time, so the eye can follow the growing tip of every single stroke. Nothing is revealed by a sweeping wipe and nothing fades into view - every line extends from its own tip. {draw_steps} Most of each form stays deliberately economical and free of internal lines, with strictly zero cross-hatching and zero line shading. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is {palette}. All surrounding space stays untouched pure white with no wash of any kind extending behind the subjects. {motion} All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, precise pale graphite strokes and sophisticated control, maximum line value 20% grey, luminous transparent watercolor, restrained tonal contrast, generous untouched white space, sophisticated museum-quality editorial illustration for an adult natural-history atlas, mature and understated, with hairline strokes and no heavy outlines anywhere."""

ALL_SETS_DATA = [
    # Set 04: 자연탐험 & 캠핑 (10편)
    {
        "set_id": "set04",
        "set_name": "Set 04 (자연탐험 & 캠핑)",
        "target_chapter": "ch2 VITA & ch1 INVENTIO",
        "target_branches": "시간과 때, 자리와 방향, 캠핑과 탐험",
        "scenes": [
            {
                "title": "삼각 캠핑 텐트와 나무 접이식 의자", "words": ["tent", "camp", "chair", "shelter", "breeze"],
                "subjects": "one small A-structure cotton tent pitched at the optical center, one simple folding wood-and-cloth camp stool propped beside it, and three small smooth river pebbles on the clean white ground",
                "draw_steps": "The clean triangular contour of the tent pitched on its ridgepole comes first with precise hairline strokes. The low wooden folding stool beside it follows with economical open lines, then the three tiny pebbles.",
                "palette": "only the palest weathered linen-tan on the tent fabric, the faintest warm pine on the stool wood, and one very light translucent stone-grey on the pebbles",
                "motion": "The small front fabric flap of the tent flutters gently once in the quiet breeze and settles still."
            },
            {
                "title": "황동 호롱 랜턴과 작은 나뭇가지 불꽃", "words": ["lantern", "flame", "warmth", "glow", "twigs"],
                "subjects": "one classic brass candle lantern standing at center, a neat cluster of four dry twigs lying beside it, and a tiny single flame burning quietly within the glass",
                "draw_steps": "The delicate cylindrical glass body and domed brass top of the lantern are drawn first with fine open contours. The four slender crossed twigs lying on the ground follow, then the tiny inner teardrop flame.",
                "palette": "only the palest translucent brass-gold on the lantern cap, a whisper of warm amber in the tiny glass flame, and the faintest dry bark-grey on the twigs",
                "motion": "The tiny flame inside the glass flickers softly once and burns steadily."
            },
            {
                "title": "가죽 등산화와 깎아 만든 나무 지팡이", "words": ["boots", "staff", "trail", "leather", "journey"],
                "subjects": "one pair of sturdy leather hiking boots resting side by side at center, and one smooth carved walking stick propped lightly against them",
                "draw_steps": "The economical outer silhouette of the two leather boots comes first with light single strokes. The tall slender wooden staff propped beside the boots follows with clean hairline precision.",
                "palette": "only the palest weathered tan-leather wash on the boots and the faintest soft cedar-brown on the walking stick",
                "motion": "A single tiny dry pine needle drifts gently to rest beside the boot toe and stays still."
            },
            {
                "title": "원목 카누와 나무 노, 잔잔한 수면 파문", "words": ["kayak", "paddle", "ripple", "lake", "glide"],
                "subjects": "one slender wooden canoe resting level horizontally at center, one carved single-blade wooden paddle lying across its gunwale, and two faint concentric water ripple lines",
                "draw_steps": "The graceful horizontal curves of the wooden canoe hull come first with pure economical strokes. The symmetrical paddle laid across the top follows, then two delicate oval water ripples.",
                "palette": "only the palest cedar-wood wash on the canoe, sheer pine-grey on the paddle, and a faint whisper of translucent water-blue around the ripples",
                "motion": "The two delicate water ripples expand softly outward once and fade into the still surface."
            },
            {
                "title": "황동 쌍안경과 한 장의 관측 수첩", "words": ["binoculars", "observe", "feathers", "field", "lens"],
                "subjects": "one compact brass-and-leather field binocular standing upright at center, and a single dropped bird feather resting quietly beside it",
                "draw_steps": "The twin cylindrical optical tubes and central focus screw of the binoculars are drawn with delicate hairline contours. The graceful curved quill of the small dropped feather beside it follows.",
                "palette": "only the palest warm brass on the binocular rings, sheer cool slate on the barrels, and a faint whisper of earthy fawn-brown on the feather",
                "motion": "The small dropped feather shifts softly once on the white ground and rests completely still."
            },
            {
                "title": "작은 캠핑 찻주전자와 한 잔의 머그", "words": ["kettle", "mug", "brew", "cozy", "sip"],
                "subjects": "one small rounded camping tea kettle resting on three low stones at center, and one ceramic mug standing closely beside it",
                "draw_steps": "The round contour of the kettle body, spout and arched handle are drawn first with simple unbroken lines. The three supporting ground stones follow, then the single clean outline of the mug.",
                "palette": "only the palest sky-water tint on the kettle body, delicate warm-sand on the ceramic mug, and sheer stone-grey on the three rocks",
                "motion": "One thin, curling ribbon of transparent white steam rises slowly from the kettle spout."
            },
            {
                "title": "대나무 낚싯대와 작은 목조 부표 찌", "words": ["rod", "float", "stream", "calm", "bamboo"],
                "subjects": "one segmented bamboo fishing rod propped lightly on a small notched stick at left, and a small round wooden bobber float resting on a faint water baseline at center",
                "draw_steps": "The slender segmented bamboo cane line is drawn first with fine joint marks. The notched wooden support fork follows, then the small circular float and its hairline stem.",
                "palette": "only the palest straw-yellow on the bamboo rod and the faintest coral-red tint on the upper half of the small float",
                "motion": "The small round float bobs gently once in the water line and comes to complete rest."
            },
            {
                "title": "포켓 황동 나침반과 접이식 등고선 지도", "words": ["compass", "needle", "map", "route", "explore"],
                "subjects": "one round brass pocket compass with its hinged lid open at center, and a neatly folded single document sheet of topographic map resting quietly beside it",
                "draw_steps": "The circular casing and open lid of the compass are drawn with delicate hairline precision. The cardinal markings and slender needle follow, then the crisp folded edges of the map sheet.",
                "palette": "only the palest translucent brass-gold on the compass rim and a faint whisper of sage-green on the map contour lines",
                "motion": "The delicate magnetic needle swings smoothly once to north and settles completely still."
            },
            {
                "title": "작은 숲속 통나무 대피소와 나무 풍향계", "words": ["cabin", "timber", "vane", "peace", "shelter"],
                "subjects": "one small open timber lean-to shelter resting at center with clean cut log ends, and one slender wooden stake topped with a small silhouette weather vane beside it",
                "draw_steps": "The simple angled roofline and stacked notched log ends of the small lean-to shelter come first with economical lines. The slender vertical post and arrow weather vane follow.",
                "palette": "only the palest weathered pine-grey on the timber logs and a faint whisper of soft earth-beige under the shelter roof",
                "motion": "The small arrow of the weather vane turns slowly once to catch the breeze and stops."
            },
            {
                "title": "원형으로 감긴 삼베 로프와 두 개의 황동 카라비너", "words": ["rope", "knot", "climb", "secure", "link"],
                "subjects": "one neat circular coil of hemp rope resting flat at center, and two polished brass oval carabiner rings hooked together beside it",
                "draw_steps": "The clean concentric outer curves of the coiled hemp rope are drawn first with delicate spiral lines. The two linked oval carabiner loops follow with smooth hairline contours.",
                "palette": "only the palest natural hemp-buff on the coiled rope and the faintest translucent warm-brass on the two metal rings",
                "motion": "The two linked carabiners shift with a tiny soft click once on the rope and rest still."
            }
        ]
    },

    # Set 05: 홈 카페 & 베이커리 (10편)
    {
        "set_id": "set05",
        "set_name": "Set 05 (홈 카페 & 베이커리)",
        "target_chapter": "ch6 SALUS & ch14 MERCATUS",
        "target_branches": "많고 적음, 음식과 조리, 카페와 계량",
        "scenes": [
            {
                "title": "세라믹 드립 드리퍼와 유리 서버", "words": ["brew", "drip", "aroma", "server", "filter"],
                "subjects": "one elegant white ceramic cone dripper resting over a clear glass carafe at center, and three roasted coffee beans beside it",
                "draw_steps": "The precise geometric cone of the ceramic dripper is drawn first with fine hairline contours. The clear glass carafe below follows, then the three small oval beans on the white ground.",
                "palette": "only the palest porcelain-white on the dripper, sheer faint amber-tea wash in the glass base, and delicate warm-roast brown on the beans",
                "motion": "A single dark amber droplet drips smoothly from the cone tip into the carafe and settles still."
            },
            {
                "title": "원목 핸드밀 수동 그라인더", "words": ["grind", "mill", "crank", "fresh", "powder"],
                "subjects": "one classic compact wooden box manual mill grinder with curved brass crank at center, and a tiny mound of ground coffee beside its drawer",
                "draw_steps": "The square wooden body and open lower drawer come first with economical straight strokes. The curved brass handle and hopper lid follow, then the fine contour of the ground mound.",
                "palette": "only the palest honey-oak wash on the wooden box and translucent warm-brass on the curved crank",
                "motion": "The curved brass crank turns smoothly half a circle and rests at peace."
            },
            {
                "title": "프랑스 바게트 빵과 클래식 빵칼", "words": ["loaf", "crust", "slice", "bake", "flour"],
                "subjects": "one long golden baguette loaf with crisp diagonal crust cuts lying horizontally at center, and one wooden-handled bread knife beside it",
                "draw_steps": "The slender horizontal oval silhouette of the baguette and its four diagonal scoring marks are drawn first with fine lines. The straight serrated knife beside it follows.",
                "palette": "only the palest warm-wheat gold on the bread crust and sheer light timber-tan on the knife handle",
                "motion": "A few tiny delicate breadcrumbs settle softly onto the clean white surface beside the crust."
            },
            {
                "title": "치즈 휠 한 조각과 와이어 슬라이서", "words": ["cheese", "wedge", "slice", "dairy", "mild"],
                "subjects": "one triangular wedge of firm cheese with three round eye holes at center, and one simple stainless wire cheese cutter beside it",
                "draw_steps": "The clean triangular wedge silhouette and three circular internal holes come first with economical outlines. The arched wire cutter follows.",
                "palette": "only the palest buttery pastel-warm-white on the cheese wedge and sheer faint cool-grey on the wire mount",
                "motion": "One thin shaved ribbon of cheese curls gently beside the wedge and stays still."
            },
            {
                "title": "도자기 믹싱볼과 와이어 거품기", "words": ["whisk", "bowl", "blend", "batter", "mix"],
                "subjects": "one fluted ceramic mixing bowl sitting upright at center, and one delicate wire balloon whisk resting angled across its rim",
                "draw_steps": "The wide flared bowl contour and gentle rim are drawn with soft single strokes. The curved balloon wire loops of the whisk follow.",
                "palette": "only the palest pastel sky-blue on the ceramic bowl and sheer hairline steel-grey on the whisk wires",
                "motion": "The balloon whisk rocks slightly once against the bowl edge and comes to complete rest."
            },
            {
                "title": "클래식 도자기 티팟과 찻잔", "words": ["teapot", "cup", "herbal", "fragrance", "warm"],
                "subjects": "one plump porcelain teapot with curved spout at center, and one matching teacup on a saucer beside it",
                "draw_steps": "The rounded spherical body, lid knob and elegant spout of the teapot are drawn first. The teacup and saucer follow with delicate hairline contours.",
                "palette": "only the palest celadon-mint on the teapot and cup with pure white surface showing through",
                "motion": "A tiny whisper of translucent steam curls once from the teapot spout."
            },
            {
                "title": "유리 오일병과 발사믹 디캔터", "words": ["bottle", "pour", "olive", "liquid", "pure"],
                "subjects": "one tall slender glass olive oil bottle with spout stopper at center, and one small round glass vinegar cruet beside it",
                "draw_steps": "The clean vertical contours of the glass bottle and pouring spout are drawn with precise hairline strokes. The small spherical cruet follows.",
                "palette": "only the palest translucent golden-olive tint in the bottle base and sheer delicate plum-grey in the cruet",
                "motion": "The liquid surface in the tall bottle settles completely level and still."
            },
            {
                "title": "클래식 토스터와 구운 식빵 한 조각", "words": ["toast", "crisp", "warm", "slice", "breakfast"],
                "subjects": "one compact retro two-slot toaster standing at center, and one golden toasted bread slice popped halfway up",
                "draw_steps": "The rounded rectangular toaster body and top slots come first with minimal lines. The warm toasted slice peeking from the slot follows.",
                "palette": "only the palest vintage warm-white-white on the toaster casing and a whisper of warm-toast tan on the bread top",
                "motion": "The bread slice settles with a tiny click softly in its slot."
            },
            {
                "title": "유리 돔 케이크 스탠드", "words": ["stand", "dome", "dessert", "sweet", "display"],
                "subjects": "one footed ceramic cake platter with a clear bell-shaped glass dome lid over a small round pastry at center",
                "draw_steps": "The flared pedestal base, flat platter rim and arched glass dome are drawn with fine unbroken curves. The small pastry inside follows.",
                "palette": "only the palest translucent cool-glass tone on the dome and sheer faint honey-apricot on the pastry",
                "motion": "A single tiny bright light glint gleams softly on the glass dome knob and stays steady."
            },
            {
                "title": "주철 팬과 나무 조리 주걱", "words": ["skillet", "cook", "spatula", "meal", "heat"],
                "subjects": "one round cast-iron skillet resting flat at center, and one carved wooden spatula lying angled beside its handle",
                "draw_steps": "The circular pan rim, flat base and straight handle come first with light economical strokes. The flat wooden spatula blade follows.",
                "palette": "only the palest translucent slate-grey on the pan and faint warm-beech on the wooden spatula",
                "motion": "A tiny wisp of transparent heat shimmer rises softly once above the pan."
            }
        ]
    },

    # Set 06: 정원 & 원예 (10편)
    {
        "set_id": "set06",
        "set_name": "Set 06 (정원 & 원예)",
        "target_chapter": "ch2 VITA (숲과 생명)",
        "target_branches": "식물과 생장, 만들고 고치기, 원예",
        "scenes": [
            {
                "title": "테라코타 화분과 몬스테라 새싹", "words": ["sprout", "leaf", "plant", "grow", "pot"],
                "subjects": "one classic tapered terracotta flower pot standing at center, and one young green monstera shoot unfurling from the soil",
                "draw_steps": "The flared rim and tapered sides of the clay pot are drawn first with clean lines. The slender green stem and split leaf contour follow.",
                "palette": "only the palest warm terracotta-peach on the pot and a delicate wash of translucent spring-green on the leaf",
                "motion": "The young leaf tip uncurls smoothly a fraction of an inch and rests still."
            },
            {
                "title": "아연 물뿌리개와 모종 삽", "words": ["water", "can", "trowel", "tend", "garden"],
                "subjects": "one vintage zinc watering can with long rose spout at center, and one small wooden-handled garden trowel resting beside it",
                "draw_steps": "The cylindrical can body, arched handle and slender angled spout come first. The pointed steel trowel blade follows.",
                "palette": "only the palest weathered zinc-grey on the watering can and sheer pine-tan on the trowel handle",
                "motion": "A single crystal clear water drop hangs from the spout rose and falls softly to the ground."
            },
            {
                "title": "유리 테라리움 속 작은 다육식물", "words": ["succulent", "glass", "vessel", "pebble", "flora"],
                "subjects": "one geometric faceted glass terrarium bowl standing at center with a single rosette succulent inside",
                "draw_steps": "The clean pentagonal glass facet lines are drawn with fine hairline precision. The layered succulent petals follow.",
                "palette": "only the palest translucent glass-blue on the facets and a whisper of soft jade-green with pink tips on the plant",
                "motion": "The plant rests completely motionless in its pristine quiet sanctuary."
            },
            {
                "title": "정원 꽃가위와 라벤더 세 줄기", "words": ["shears", "cut", "bloom", "lavender", "stem"],
                "subjects": "one pair of classic forged steel pruning shears resting open at center, and three slender sprigs of blooming lavender beside them",
                "draw_steps": "The curved bypass blades and spring pivot of the shears come first with crisp outlines. The three slender flower spikes follow.",
                "palette": "only the palest cool slate on the metal shears and a faint wash of translucent lilac-purple on the flower buds",
                "motion": "A single tiny purple petal drifts gently to rest beside the shears blade."
            },
            {
                "title": "목조 새집과 매달린 모이통", "words": ["birdhouse", "nest", "perch", "roof", "timber"],
                "subjects": "one quaint peaked-roof wooden birdhouse propped on a low cedar stump at center, with a small round doorway and perch peg",
                "draw_steps": "The sloped roof eaves, front wooden face and round entry hole are drawn with economical strokes. The small perch peg follows.",
                "palette": "only the palest weathered barn-grey on the birdhouse timber and faint moss-green on the roof shingles",
                "motion": "The birdhouse rests peaceful and motionless in the clean open space."
            },
            {
                "title": "라탄 수확 바구니와 작은 호박", "words": ["basket", "harvest", "crop", "autumn", "ripe"],
                "subjects": "one shallow woven wicker basket resting flat at center, holding one small round ribbed pumpkin and two dried wheat stalks",
                "draw_steps": "The curved woven rim and horizontal basket weave lines come first. The ribbed pumpkin contour and wheat stalks follow.",
                "palette": "only the palest straw-tan on the wicker and a delicate translucent pastel-apricot on the pumpkin",
                "motion": "The wheat stalk head sways softly once and settles at rest."
            },
            {
                "title": "나무 꽃누르개 압화틀", "words": ["press", "flower", "preserve", "dry", "petal"],
                "subjects": "one square wooden flower press with four brass corner wing nuts at center, with one pressed daisy flower peeking from the side",
                "draw_steps": "The top square wooden board and four corner screw threads are drawn with fine geometry. The pressed white daisy blossom follows.",
                "palette": "only the palest birch-warm-white on the press boards and faint butter-yellow on the daisy center",
                "motion": "The press rests completely solid, balanced and still."
            },
            {
                "title": "원예용 외발 손수레", "words": ["wheelbarrow", "carry", "wheel", "garden", "load"],
                "subjects": "one rustic wooden garden wheelbarrow with single spoke wheel resting level horizontally at center",
                "draw_steps": "The sloped wooden hopper, twin rear handles and single forward wheel are drawn with clean open contours.",
                "palette": "only the palest weathered pine-buff on the hopper and sheer iron-grey on the wheel rim",
                "motion": "The wheelbarrow rests squarely and firmly on its ground supports."
            },
            {
                "title": "유리 온실 미니어처 프레임", "words": ["greenhouse", "sunlight", "warm", "pane", "protect"],
                "subjects": "one small tabletop Victorian glass greenhouse case standing at center, with pitched glass roof panes",
                "draw_steps": "The clean architectural grid of glass roof panes and base tray are drawn with hairline precision.",
                "palette": "only the palest luminous aqua-glass tint on the roof panels and sheer bronze on the casing joints",
                "motion": "A gentle shaft of warm pure white light glints once across the glass roof."
            },
            {
                "title": "해바라기 한 송이와 격자 울타리", "words": ["sunflower", "bloom", "fence", "tall", "sunny"],
                "subjects": "one tall single blooming sunflower standing at center, propped against a low section of wooden garden trellis",
                "draw_steps": "The round seed disk, radiating petal ring and sturdy leafy stem are drawn with soft single strokes. The crisscross trellis follows.",
                "palette": "only the palest sunny butter-yellow on the petals, warm earth-brown on the center, and faint olive on the stem",
                "motion": "The heavy sunflower head nods gently once in the light breeze and pauses."
            }
        ]
    },

    # Set 07: 미술 & 공예 (10편)
    {
        "set_id": "set07",
        "set_name": "Set 07 (미술 & 공예)",
        "target_chapter": "ch8 MOTUS & ch13 FORUM",
        "target_branches": "일과 직업, 공예와 도구, 사람과 관계",
        "scenes": [
            {
                "title": "나무 이젤과 빈 화판", "words": ["easel", "art", "cotton fabric", "create", "studio"],
                "subjects": "one tripod wooden studio easel standing at center holding a blank rectangular wooden art board, and three small paint jars beside it",
                "draw_steps": "The three tapered wooden tripod legs and horizontal mast are drawn with fine straight lines. The blank board and paint jars follow.",
                "palette": "only the palest natural beech-wood on the easel and faint whispers of pastel ultramarine and ochre on the jars",
                "motion": "The easel stands perfectly steady and still inside the generous white space."
            },
            {
                "title": "도예 물레와 점토 화병", "words": ["clay", "pottery", "wheel", "shape", "craft"],
                "subjects": "one circular potter's wheel head at center with a smooth unfinished clay vase resting on its center hub",
                "draw_steps": "The circular rotating disc rim and the smooth symmetrical curves of the clay vase are drawn with continuous fine contours.",
                "palette": "only the palest wet terracotta-buff on the clay vase and sheer steel-grey on the wheel head",
                "motion": "The potter's disc spins smoothly half a turn and comes to gentle rest."
            },
            {
                "title": "클래식 주철 재봉틀", "words": ["sew", "stitch", "thread", "machine", "fabric"],
                "subjects": "one vintage cast-iron sewing machine with rotary balance wheel at center, and a wooden spool of thread beside it",
                "draw_steps": "The graceful arched neck, needle bar and round balance wheel of the machine are drawn with delicate outlines. The thread spool follows.",
                "palette": "only the palest antique slate-charcoal on the machine body and a faint wash of sky-blue on the thread spool",
                "motion": "The balance wheel turns smoothly once and the needle bar rests in place."
            },
            {
                "title": "목공 손대패와 대팻밥", "words": ["plane", "wood", "shave", "smooth", "carpenter"],
                "subjects": "one classic wooden block plane with angled steel blade at center, and two curling wooden shavings resting beside it",
                "draw_steps": "The rectangular timber plane block and wedge-clamped blade are drawn with crisp geometry. The thin curled wood shavings follow.",
                "palette": "only the palest warm walnut-tan on the plane body and sheer straw-white on the whisper-thin shavings",
                "motion": "One delicate curly wood shaving shifts softly once and settles on the ground."
            },
            {
                "title": "가죽 공예 펀치와 스티칭 도구", "words": ["leather", "punch", "seam", "device", "crafted"],
                "subjects": "one steel leather prong punch standing upright at center, beside a folded strip of natural tan leather with stitched holes",
                "draw_steps": "The knurled steel device shaft and sharp prongs come first with fine precision. The thick leather strip and neat stitch line follow.",
                "palette": "only the palest brushed steel-grey on the punch and a delicate honey-tan wash on the leather",
                "motion": "The implements rest completely stable and motionless on the pure white field."
            },
            {
                "title": "스테인드글라스 유리 조각과 납선", "words": ["glass", "color", "mosaic", "light", "window"],
                "subjects": "a flower-shaped arrangement of four cut colored glass segments framed by soldered lead came strips at center",
                "draw_steps": "The clean dark outlines of the lead solder lines are drawn first. The smooth curved contours of the cut glass petals follow.",
                "palette": "only the palest translucent rose-pink, amber-yellow and sea-blue washes inside the glass segments",
                "motion": "A gentle prism light gleams softly through the translucent glass petals."
            },
            {
                "title": "조각용 석고 흉상과 나무 헤라", "words": ["sculpture", "form", "marble", "chisel", "statue"],
                "subjects": "one minimalist classical plaster bust sculpture at center, with a carved wooden sculpting spatula resting at its base",
                "draw_steps": "The noble facial profile, neck and pedestal of the bust are drawn with sparse elegant contours. The wooden device follows.",
                "palette": "only the palest cool stone-white on the bust and faint warm cedar-tan on the spatula",
                "motion": "The bust rests timeless, poised and completely still."
            },
            {
                "title": "판화 롤러와 목판 블록", "words": ["print", "roller", "ink", "press", "carve"],
                "subjects": "one rubber printmaking brayer roller with wire mount at center, propped beside an engraved wooden relief block",
                "draw_steps": "The cylindrical brayer roller, curved wire handle and the carved surface lines of the woodblock are drawn with clean strokes.",
                "palette": "only the palest graphite on the roller cylinder and sheer pine-wood tone on the relief block",
                "motion": "The printmaking roller rests steadily on its metal stand feet."
            },
            {
                "title": "직조 베틀과 실타래 북", "words": ["weave", "loom", "yarn", "fabric", "shuttle"],
                "subjects": "one tabletop wooden weaving loom structure at center with stretched warp threads, and a pointed wooden shuttle lying across them",
                "draw_steps": "The square wooden loom structure and parallel vertical thread lines are drawn with fine spacing. The boat-shaped shuttle follows.",
                "palette": "only the palest beech-wood on the loom and delicate pastel lavender-blue on the woven fabric band",
                "motion": "The smooth wooden shuttle slides softly across the warp and rests."
            },
            {
                "title": "보석 세공 핀셋과 다이아몬드 원석", "words": ["gem", "diamond", "facet", "precision", "jewelry"],
                "subjects": "one pair of fine jeweler's tweezers holding a faceted cut brilliant gemstone at center, and a small velvet display cushion",
                "draw_steps": "The slender converging arms of the steel tweezers and the geometric hexagonal facets of the diamond are drawn with hairline precision.",
                "palette": "only the palest cool steel on the tweezers and a luminous clear aqua-white sparkle on the gemstone",
                "motion": "The faceted diamond gives a tiny delicate crystalline sparkle softly once."
            }
        ]
    },

    # Set 08: 바다 & 항해 (10편)
    {
        "set_id": "set08",
        "set_name": "Set 08 (바다 & 항해)",
        "target_chapter": "ch1 INVENTIO & ch8 MOTUS",
        "target_branches": "항해와 바다, 방향과 도구, 규칙",
        "scenes": [
            {
                "title": "선박 조타실 키와 원형 레이더", "words": ["helm", "steer", "course", "radar", "vessel"],
                "subjects": "one polished brass marine helm steering wheel at center, and a circular analog compass binnacle beside it",
                "draw_steps": "The circular outer ring, turned wooden spokes and central hub of the ship's wheel are drawn with crisp symmetry. The compass binnacle follows.",
                "palette": "only the palest warm teak-wood on the wheel grips and luminous translucent brass on the center hub",
                "motion": "The ship's wheel turns smoothly one spoke and settles perfectly steady."
            },
            {
                "title": "등대 랜턴 룸과 프레넬 렌즈", "words": ["lighthouse", "beacon", "lens", "guide", "coast"],
                "subjects": "one intricate glass Fresnel lighthouse lens standing on a cast-iron pedestal at center, with concentric glass prism rings",
                "draw_steps": "The stepped concentric circular glass prism rings and central bullseye lens are drawn with hairline precision. The pedestal follows.",
                "palette": "only the palest translucent sea-glass aqua on the prisms and sheer iron-grey on the structure",
                "motion": "A gentle beam of warm white light pulses softly once through the glass lens."
            },
            {
                "title": "빈티지 잠수 헬멧과 공기 밸브", "words": ["dive", "helmet", "depth", "ocean", "explore"],
                "subjects": "one classic copper-and-brass deep sea diving helmet at center, with circular grilled viewport windows and side inlet valves",
                "draw_steps": "The rounded spherical copper dome, bolted breastplate and front glass port grill are drawn with fine open contours.",
                "palette": "only the palest weathered verdigris-green and translucent rose-copper washes on the helmet dome",
                "motion": "A tiny single air bubble floats upward beside the helmet and disappears."
            },
            {
                "title": "선박 구명환과 투척 로프", "words": ["buoy", "rescue", "safety", "rope", "harbor"],
                "subjects": "one circular marine lifebuoy ring hanging from a simple wooden post at center, with a neat coil of white braided line",
                "draw_steps": "The thick circular life ring silhouette and four reflective quadrant bands are drawn first. The coiled safety line follows.",
                "palette": "only the palest coral-orange on the buoy bands and sheer clean white on the foam ring",
                "motion": "The hanging lifebuoy sways gently once on its peg and comes to rest."
            },
            {
                "title": "항해 육분의와 접이식 해도", "words": ["sextant", "navigate", "star", "chart", "sea"],
                "subjects": "one delicate brass navigation sextant with index lever and telescope at center, resting on an open sea chart with rhumb lines",
                "draw_steps": "The curved graduated arc, mirror index lever and small viewing scope are drawn with micro-precision. The chart grid follows.",
                "palette": "only the palest translucent brass-gold on the sextant structure and faint ocean-blue on the chart lines",
                "motion": "The index lever adjusts smoothly one millimeter along the graduated arc."
            },
            {
                "title": "어선 그물과 유리 부표 공", "words": ["net", "float", "mesh", "fisher", "tide"],
                "subjects": "one spherical manual-blown glass fishing float wrapped in knotted twine mesh at center, resting over a draped hemp net",
                "draw_steps": "The perfect spherical glass ball and knotted diamond twine harness are drawn with delicate lines. The draped net follows.",
                "palette": "only the palest translucent emerald-sea-green in the glass float and sheer buff on the twine",
                "motion": "The glass float rests serene, luminous and still on the white ground."
            },
            {
                "title": "원목 노와 목조 카누 선수", "words": ["oar", "row", "canoe", "glide", "water"],
                "subjects": "one pair of carved wooden rowing oars crossed symmetrically at center, propped on a clean horizontal baseline",
                "draw_steps": "The long slender looms, shaped spoon blades and rounded leather collars of both oars are drawn with crisp symmetry.",
                "palette": "only the palest ash-wood wash on the oar shafts and sheer slate-blue on the blade tips",
                "motion": "The crossed oars stand perfectly balanced and still."
            },
            {
                "title": "잠수함 잠망경 렌즈와 계기판", "words": ["periscope", "scope", "sight", "marine", "gauge"],
                "subjects": "one vertical brass periscope viewing tube with twin folding handles and round ocular eyepiece at center",
                "draw_steps": "The cylindrical periscope housing, top prism window and dual horizontal handgrips are drawn with fine geometry.",
                "palette": "only the palest brushed bronze on the scope body and sheer cool optical-blue on the glass lens",
                "motion": "The dual handgrips rotate softly a fraction and lock steadily in place."
            },
            {
                "title": "선박 3엽 프로펠러와 방향타", "words": ["propeller", "thrust", "rudder", "steer", "power"],
                "subjects": "one sculpted three-blade marine bronze propeller mounted on a shaft hub at center, resting beside a sleek rudder blade",
                "draw_steps": "The three twisted helical propeller blades and central cone cap are drawn with flowing geometric contours. The rudder follows.",
                "palette": "only the palest luminous marine bronze on the propeller blades and sheer iron-grey on the rudder",
                "motion": "The propeller blades give a single tiny metallic light glint softly."
            },
            {
                "title": "진주 조개와 흑진주 한 알", "words": ["shell", "pearl", "treasure", "reef", "rare"],
                "subjects": "one open scallop shell with radiating ridges resting at center, cradling one lustrous iridescent pearl inside its cup",
                "draw_steps": "The ribbed fan-shaped ridges of the lower shell valve and the smooth perfect sphere of the pearl are drawn with delicate strokes.",
                "palette": "only the palest mother-of-pearl opalescent pink and faint sea-aqua tints inside the shell",
                "motion": "The lustrous pearl gleams softly with a quiet inner glow."
            }
        ]
    },

    # Set 09: 과학 & 실험 (10편)
    {
        "set_id": "set09",
        "set_name": "Set 09 (과학 & 실험)",
        "target_chapter": "ch11 COSMOS (우주와 과학)",
        "target_branches": "기계와 도구, 실험과 관측, 인과",
        "scenes": [
            {
                "title": "황동 현미경과 유리 슬라이드", "words": ["microscope", "lens", "specimen", "focus", "lab"],
                "subjects": "one classic brass monocular compound microscope standing at center, with one rectangular glass specimen slide on the stage",
                "draw_steps": "The arched brass limb, optical tube, coarse focus knob and circular stage are drawn with fine hairline contours. The glass slide follows.",
                "palette": "only the palest warm brass-gold on the microscope barrel and sheer cool glass-blue on the stage slide",
                "motion": "The knurled focus knob rotates smoothly half a turn and stops in sharp focus."
            },
            {
                "title": "분젠 버너와 삼각대, 유리 플라스크", "words": ["flask", "burner", "heat", "chemistry", "boil"],
                "subjects": "one glass Erlenmeyer flask resting on a wire gauze tripod over a slender Bunsen burner at center, with a tiny blue cone flame",
                "draw_steps": "The conical glass flask body, narrow neck and steel tripod legs are drawn with clean lines. The burner and small inner flame follow.",
                "palette": "only the palest translucent sky-water tint in the flask and a whisper of cobalt-blue in the tiny flame",
                "motion": "A single tiny transparent bubble rises softly from the flask base."
            },
            {
                "title": "유리 비커 세트와 눈금 스포이트", "words": ["beaker", "pipette", "drop", "measure", "liquid"],
                "subjects": "one cylindrical glass beaker with graduated measurement markings at center, and one glass dropper pipette resting angled across its spout",
                "draw_steps": "The cylindrical beaker contour, spout lip and delicate horizontal volume lines come first. The glass pipette follows.",
                "palette": "only the palest translucent aqua-teal wash inside the beaker base and sheer glass-white on the dropper",
                "motion": "A single tiny droplet forms at the pipette tip and hangs motionless."
            },
            {
                "title": "뉴턴의 진자 요람과 금속 구슬", "words": ["pendulum", "motion", "energy", "physics", "swing"],
                "subjects": "one polished steel Newton's cradle structure with five hanging steel balls at center, with one outer ball pulled slightly outward",
                "draw_steps": "The rectangular metal stand, fine suspended V-wires and five aligned spherical balls are drawn with micro-precision.",
                "palette": "only the palest cool steel-grey on the cradle structure and luminous silvery highlights on the spheres",
                "motion": "The outer sphere releases, strikes the row with a tiny click, and the opposite ball lifts softly."
            },
            {
                "title": "말굽 자석과 쇠가루 자기력선", "words": ["magnet", "pole", "attract", "iron", "field"],
                "subjects": "one classic red-and-silver horseshoe magnet standing upright at center, with delicate radiating lines of iron filings between its poles",
                "draw_steps": "The U-shaped curved magnet bar and two squared pole tips are drawn with clean symmetry. The fine dotted magnetic field arcs follow.",
                "palette": "only the palest muted coral-red on the magnet arch and sheer graphite-grey on the poles and filings",
                "motion": "A few tiny loose iron particles align smoothly along the curved magnetic arc."
            },
            {
                "title": "테슬라 방전 코일과 유리 방전구", "words": ["coil", "spark", "voltage", "current", "charge"],
                "subjects": "one copper-wound cylindrical Tesla coil tower standing at center, topped with a polished toroidal metal ring",
                "draw_steps": "The tight helical copper winding lines and smooth donut-shaped top electrode are drawn with micro-precision.",
                "palette": "only the palest warm copper on the coil windings and sheer silver-grey on the top torus",
                "motion": "A single hairline filament of electric violet light flashes softly once at the tip."
            },
            {
                "title": "분자 구조 볼앤스틱 모형", "words": ["molecule", "atom", "bond", "element", "structure"],
                "subjects": "one balanced geometric ball-and-stick molecular model of a water molecule at center, with one central sphere and two bonded spheres",
                "draw_steps": "The three spheres and two angled connecting bond rods are drawn with clean spatial geometric outlines.",
                "palette": "only the palest translucent sky-blue on the central atom and sheer pastel coral on the two outer atoms",
                "motion": "The molecular structure model rotates slowly a quarter turn and rests poised."
            },
            {
                "title": "수은 기압계와 눈금 다이얼", "words": ["barometer", "pressure", "gauge", "dial", "weather"],
                "subjects": "one round polished brass aneroid barometer dial at center with fine graduated scale and slender indicator needle",
                "draw_steps": "The circular brass casing, Roman and millibar scale markings, and dual indicator needles are drawn with micro-hairline precision.",
                "palette": "only the palest warm brass-gold on the bezel rim and sheer vellum sheet-white on the dial face",
                "motion": "The slender brass needle moves smoothly half a tick and settles steady."
            },
            {
                "title": "유리 벨자 항아리와 진공 펌프", "words": ["vacuum", "bell", "jar", "air", "chamber"],
                "subjects": "one heavy bell-shaped glass jar inverted over a flat brass baseplate at center, with a single delicate feather resting inside",
                "draw_steps": "The domed glass jar contour, heavy rim flange and circular baseplate are drawn with clean lines. The inner feather follows.",
                "palette": "only the palest translucent glass-blue on the dome and sheer brass-gold on the baseplate",
                "motion": "The feather inside the quiet glass chamber floats completely still."
            },
            {
                "title": "복합 도르래와 균형 황동 추", "words": ["pulley", "weight", "balance", "lift", "force"],
                "subjects": "one double-sheave brass pulley block suspended from a top hook at center, with a fine cord supporting a slotted brass weight",
                "draw_steps": "The teardrop pulley structure, twin grooved wheels and vertical cord lines are drawn with fine mechanical symmetry. The cylindrical weight follows.",
                "palette": "only the palest warm brass on the pulley wheels and sheer hemp-tan on the thin cord",
                "motion": "The suspended weight adjusts smoothly a fraction of an inch and hangs in perfect balance."
            }
        ]
    },

    # Set 10: 건축 & 공구 (10편)
    {
        "set_id": "set10",
        "set_name": "Set 10 (건축 & 공구)",
        "target_chapter": "ch8 MOTUS & ch11 COSMOS",
        "target_branches": "대장간과 목공, 물리와 메커니즘",
        "scenes": [
            {
                "title": "대장간 모루와 단조 망치", "words": ["anvil", "forge", "hammer", "steel", "craft"],
                "subjects": "one solid steel blacksmith anvil with pointed horn resting flat on a wooden log base at center, with a cross-peen hammer propped beside it",
                "draw_steps": "The classic horn, flat stepping face and flared base of the anvil are drawn with strong clean contours. The hammer follows.",
                "palette": "only the palest cool iron-grey on the anvil body and sheer weathered timber-tan on the log block",
                "motion": "The anvil stands completely solid, immovable and still on the white ground."
            },
            {
                "title": "기계식 톱니바퀴 기어 트레인", "words": ["gear", "mesh", "wheel", "mechanic", "teeth"],
                "subjects": "a pair of interlocking brass spur gears mounted on parallel shafts at center, with precisely machined teeth meshing together",
                "draw_steps": "The circular pitch lines, radial spokes and involute gear teeth of both meshed wheels are drawn with geometric precision.",
                "palette": "only the palest translucent brass-gold on the larger gear and sheer steel-grey on the smaller pinion",
                "motion": "Both meshed gears rotate smoothly two teeth in unison and lock in place."
            },
            {
                "title": "버니어 캘리퍼스와 마이크로미터", "words": ["caliper", "measure", "scale", "precision", "gauge"],
                "subjects": "one stainless steel vernier caliper lying horizontally at center with sliding jaw opened to a small gap",
                "draw_steps": "The main beam, fixed jaw, sliding vernier scale and fine millimeter graduations are drawn with hairline precision.",
                "palette": "only the palest brushed stainless-steel wash across the caliper beam with pure white showing through",
                "motion": "The sliding vernier jaw closes smoothly half a millimeter and locks."
            },
            {
                "title": "건축가 T자 삼각자와 도면", "words": ["square", "draft", "ruler", "blueprint", "angle"],
                "subjects": "one wooden drafting T-square crossed over a large 45-degree transparent set square at center",
                "draw_steps": "The long straight blade and cross head of the T-square are drawn first. The triangular drafting set square with inner cutout follows.",
                "palette": "only the palest honey-maple on the wooden ruler and sheer translucent acrylic-blue on the triangle",
                "motion": "The drafting implements rest in crisp, flawless geometric alignment."
            },
            {
                "title": "스피릿 레벨 수평계와 다림줄", "words": ["level", "bubble", "plumb", "align", "true"],
                "subjects": "one rectangular wooden spirit level with central brass-framed glass bubble vial at center, and a brass plumb bob beside it",
                "draw_steps": "The straight rectangular level body, central viewing window and curved glass bubble tube are drawn with clean lines. The plumb bob follows.",
                "palette": "only the palest warm mahogany-brown on the level body and a whisper of neon-lime tint in the glass bubble",
                "motion": "The tiny air bubble inside the vial floats smoothly to the exact center line and rests."
            },
            {
                "title": "벤치 바이스와 고정 레버", "words": ["vise", "clamp", "grip", "jaw", "workshop"],
                "subjects": "one heavy cast-iron bench vise with serrated steel jaws and sliding T-handle screw at center",
                "draw_steps": "The fixed base, moving dynamic jaw, Acme lead screw and horizontal tommy bar handle are drawn with crisp mechanical outlines.",
                "palette": "only the palest vintage machine-grey on the vise body and sheer polished steel on the sliding handle",
                "motion": "The T-handle rotates smoothly half a turn and tightens the jaws firm."
            },
            {
                "title": "핸드 크랭크 전동 드릴과 드릴 비트", "words": ["drill", "bore", "hole", "bit", "device"],
                "subjects": "one classic rotary-crank eggbeater drill standing at center with a fine spiral fluted twist bit in its chuck",
                "draw_steps": "The drive gear wheel, side wooden crank knob and three-jaw chuck are drawn with fine mechanical contours.",
                "palette": "only the palest brushed steel on the structure and warm cherry-wood on the turning handle",
                "motion": "The drive wheel turns smoothly one rotation and pauses still."
            },
            {
                "title": "조합 렌치 스패너와 황동 볼트 너트", "words": ["wrench", "bolt", "nut", "thread", "tighten"],
                "subjects": "one double-ended combination wrench resting beside a threaded hexagonal bolt and matching nut at center",
                "draw_steps": "The open end, ring box end and slender handle of the chrome wrench are drawn first. The threaded hex bolt follows.",
                "palette": "only the palest chrome-silver wash on the wrench and sheer warm-brass on the hex nut",
                "motion": "The wrench and bolt rest in clean mechanical harmony on the white surface."
            },
            {
                "title": "벽돌공 흙손과 쌓은 세 겹 벽돌", "words": ["trowel", "brick", "mason", "wall", "mortar"],
                "subjects": "one diamond-bladed pointing trowel resting over a neat stack of three red clay building bricks at center",
                "draw_steps": "The flat triangular trowel blade, swan neck shank and wooden handle are drawn first. The three rectangular bricks follow.",
                "palette": "only the palest terracotta-rust on the bricks and sheer polished steel on the trowel blade",
                "motion": "The mason's trowel rests balanced, steady and quiet on the brick stack."
            },
            {
                "title": "주철 리프팅 샤클과 쇠사슬 고리", "words": ["shackle", "chain", "link", "hoist", "heavy"],
                "subjects": "one U-shaped bow shackle with threaded pin through its eyes, linked to three interlocking oval chain links at center",
                "draw_steps": "The curved U-body, threaded cross pin with eye hole and three linked oval chain rings are drawn with clean outlines.",
                "palette": "only the palest forged steel-grey on the shackle and sheer zinc-silver on the chain links",
                "motion": "The chain links settle with a soft quiet click and hang motionless."
            }
        ]
    },

    # Set 11: 음악 & 악기 (10편)
    {
        "set_id": "set11",
        "set_name": "Set 11 (음악 & 악기)",
        "target_chapter": "ch15 VOX (말과 소리)",
        "target_branches": "소리와 음악, 악기와 공연, 표현",
        "scenes": [
            {
                "title": "클래식 바이올린과 나무 활", "words": ["violin", "bow", "string", "melody", "sound"],
                "subjects": "one handcrafted wooden violin resting horizontally at center with graceful F-holes, and one horsehair bow laid beside it",
                "draw_steps": "The curvaceous waist, carved scroll, bridge and twin F-hole sound slits are drawn with micro-precision. The slender bow follows.",
                "palette": "only the palest warm amber-spruce wash on the violin belly and sheer ebony-charcoal on the fingerboard",
                "motion": "A single tiny luminous shimmer glints softly once along the highest violin string."
            },
            {
                "title": "어쿠스틱 클래식 기타와 목조 사운드홀", "words": ["guitar", "acoustic", "strum", "chord", "music"],
                "subjects": "one acoustic wooden guitar body resting angled at center, showing its round rosette soundhole and bridge pins",
                "draw_steps": "The graceful figure-eight body contour, circular soundhole rosette inlay and bridge are drawn with flowing clean strokes.",
                "palette": "only the palest cedar-blonde on the guitar top and sheer mahogany-tan on the sides",
                "motion": "The six slender strings vibrate gently once with a pure silent resonance."
            },
            {
                "title": "골드 알토 색소폰과 마우스피스", "words": ["saxophone", "brass", "reed", "jazz", "tone"],
                "subjects": "one curved brass alto saxophone resting horizontally at center with open flared bell and key mechanism",
                "draw_steps": "The S-curved neck, conical tube, flared bell and intricate key pad cups are drawn with fine mechanical precision.",
                "palette": "only the palest translucent gold-lacquer wash across the brass body with pure white showing through",
                "motion": "A delicate bright light glint traces smoothly along the curved brass bell."
            },
            {
                "title": "은빛 플루트와 전용 벨벳 케이스", "words": ["flute", "silver", "wind", "pipe", "clear"],
                "subjects": "one three-piece transverse silver concert flute lying assembled at center with open embouchure lip plate",
                "draw_steps": "The long cylindrical silver body, headjoint lip plate and delicate inline key mechanisms are drawn with hairline precision.",
                "palette": "only the palest polished silver-chrome wash on the flute tube with bright white highlights",
                "motion": "The slender flute rests in immaculate, quiet poise on the white field."
            },
            {
                "title": "그랜드 첼로와 스틸 엔드핀", "words": ["cello", "bass", "deep", "instrument", "resonance"],
                "subjects": "one resonant wooden cello standing upright at center with arched bridge and extending steel endpin",
                "draw_steps": "The broad waist contours, high carved bridge, four thick strings and slender endpin spike are drawn with graceful lines.",
                "palette": "only the palest warm chestnut-brown on the cello body and sheer black on the tailpiece",
                "motion": "The cello stands dignified, grounded and completely still."
            },
            {
                "title": "오케스트라 팀파니 드럼과 펠트 말렛", "words": ["timpani", "drum", "beat", "rhythm", "percussion"],
                "subjects": "one polished copper bowl timpani kettle drum on three tripod legs at center, with one felt-headed mallet resting on its skin",
                "draw_steps": "The deep spherical copper bowl, tension counterhoop and wooden mallet handle are drawn with clean lines.",
                "palette": "only the palest rose-copper on the kettle drum bowl and sheer vellum sheet-buff on the head skin",
                "motion": "The timpani drum rests deep, resonant and still."
            },
            {
                "title": "콘서트 페달 하프와 현 프레임", "words": ["harp", "pedal", "pluck", "grace", "harmony"],
                "subjects": "one tall golden concert harp standing at center with carved pillar column and radiating angled strings",
                "draw_steps": "The vertical fluted pillar, sweeping neck arch and angled vertical string lines are drawn with micro-precision.",
                "palette": "only the palest leaf-gold on the harp pillar and sheer crystalline white on the string array",
                "motion": "The harp strings gleam with a soft quiet radiance."
            },
            {
                "title": "실버 트롬본과 슬라이드 바", "words": ["trombone", "slide", "brass", "blast", "horn"],
                "subjects": "one tenor silver-plated trombone lying horizontally at center with flared bell and extended sliding tube",
                "draw_steps": "The parallel outer slide tubes, bell flare and cup mouthpiece are drawn with crisp mechanical outlines.",
                "palette": "only the palest bright silver wash on the bell and slide with pure white reflection",
                "motion": "The sliding tube shifts smoothly half an inch and locks in perfect tune."
            },
            {
                "title": "피아노 건반과 황동 소리굽쇠", "words": ["piano", "key", "tune", "pitch", "note"],
                "subjects": "one horizontal octave row of seven white and five black piano keys at center, with one two-pronged steel tuning fork beside them",
                "draw_steps": "The neat rectangular piano keys, ebony sharps and U-shaped tuning fork prongs are drawn with crisp geometry.",
                "palette": "only the palest ivory-warm-white on the natural keys and sheer cool steel on the tuning fork",
                "motion": "The tuning fork prongs vibrate with an invisible silent frequency."
            },
            {
                "title": "클래식 아코디언과 접이식 벨로우즈", "words": ["accordion", "reed", "bellows", "folk", "air"],
                "subjects": "one vintage accordion at center showing its pleated folding air bellows and treble keyboard grille",
                "draw_steps": "The accordion treble casing, accordion pleated bellows folds and pearl treble keys are drawn with fine lines.",
                "palette": "only the palest vintage warm-white on the body and sheer slate on the bellows folds",
                "motion": "The pleated bellows compress gently once with a soft sigh of air."
            }
        ]
    },

    # Set 12: 의학 & 보건 (10편)
    {
        "set_id": "set12",
        "set_name": "Set 12 (의학 & 보건)",
        "target_chapter": "ch7 SENSUS & ch13 FORUM",
        "target_branches": "돌봄과 치료, 보건과 케어, 감각",
        "scenes": [
            {
                "title": "의사용 청진기와 혈압계 커프", "words": ["stethoscope", "heart", "pulse", "listen", "doctor"],
                "subjects": "one classic binaural stethoscope lying in a graceful curve around its circular chest piece at center",
                "draw_steps": "The dual metal earpieces, flexible Y-tubing and circular diaphragm chest piece are drawn with flowing clean lines.",
                "palette": "only the palest cool slate on the tubing and luminous polished silver on the chest piece",
                "motion": "The circular chest piece diaphragm gleams softly once with a quiet pulse of light."
            },
            {
                "title": "수은 체온계와 멸균 붕대 롤", "words": ["thermometer", "fever", "bandage", "care", "heal"],
                "subjects": "one slim glass clinical thermometer with mercury column at center, resting beside one rolled gauze bandage",
                "draw_steps": "The slender glass stem, bulb reservoir and fine temperature graduation marks are drawn with micro-precision. The gauze roll follows.",
                "palette": "only the palest mercury-silver in the tube and sheer soft cotton-white on the bandage roll",
                "motion": "The mercury column settles steadily at the normal temperature mark."
            },
            {
                "title": "원형 안경과 시력 검사표", "words": ["glasses", "vision", "lens", "optics", "sight"],
                "subjects": "one pair of classic round wire-rimmed reading glasses standing at center, showing clean circular transparent lenses",
                "draw_steps": "The twin circular lens rims, curved bridge piece and slender hinged temple arms are drawn with micro-hairline precision.",
                "palette": "only the palest warm tortoise-shell tan on the rims and sheer crystalline glass-aqua on the lenses",
                "motion": "A gentle reflection glints softly across the glass lens surface."
            },
            {
                "title": "치과용 탐침 프로브와 소형 구강 미러", "words": ["mirror", "dental", "probe", "examine", "care"],
                "subjects": "one angled dental mouth mirror and one slender curved explorer probe resting crossed at center",
                "draw_steps": "The knurled steel handles, angled mirror stem and fine sickle probe tip are drawn with surgical precision.",
                "palette": "only the palest surgical stainless-steel wash across both implements with pure white highlights",
                "motion": "The round dental mirror reflects a tiny point of bright clear light."
            },
            {
                "title": "약사 조제용 유발과 막자", "words": ["mortar", "pestle", "herb", "remedy", "cure"],
                "subjects": "one heavy white porcelain mortar bowl at center with its matching round-headed pestle resting inside",
                "draw_steps": "The thick flanged porcelain bowl lip, heavy base and smooth contoured pestle handle are drawn with clean lines.",
                "palette": "only the palest clean porcelain-white with a whisper of sage-green leaf dust inside the bowl",
                "motion": "The pestle rests steady, balanced and quiet in the clean bowl."
            },
            {
                "title": "초음파 진단 탐촉자 프로브", "words": ["ultrasound", "scan", "probe", "sensor", "health"],
                "subjects": "one ergonomic handheld ultrasound transducer probe with curved cable resting flat at center",
                "draw_steps": "The contoured plastic probe casing, acoustic lens face and flexible cable loop are drawn with smooth modern outlines.",
                "palette": "only the palest clinical off-white on the probe and sheer cool grey on the cable",
                "motion": "The acoustic lens face pulses with a single tiny blue glow indicator."
            },
            {
                "title": "수술용 가위와 지혈 겸자", "words": ["scissors", "forceps", "sterile", "surgery", "precise"],
                "subjects": "one pair of fine surgical iris scissors resting beside one curved hemostatic locking forceps at center",
                "draw_steps": "The ring ring loops, box locks and sharp delicate scissor blades are drawn with surgical hairline precision.",
                "palette": "only the palest polished surgical steel on both instruments with pure white reflection",
                "motion": "The instruments rest in sterile, quiet and flawless alignment."
            },
            {
                "title": "휴대용 산소통과 흡입 마스크", "words": ["oxygen", "breathe", "mask", "relief", "pure"],
                "subjects": "one compact lightweight aluminum medical oxygen cylinder with pressure regulator valve at center",
                "draw_steps": "The cylindrical tank body, brass valve assembly and pressure gauge dial are drawn with crisp outlines.",
                "palette": "only the palest medical green on the cylinder shoulder and sheer brushed aluminum below",
                "motion": "The tiny pressure gauge needle rests steady in the green zone."
            },
            {
                "title": "클래식 목제 목발 한 쌍", "words": ["crutch", "walk", "support", "recover", "aid"],
                "subjects": "one pair of crafted wooden underarm crutches standing upright at center with padded lever rests and handgrips",
                "draw_steps": "The curved dual wooden side rails, adjustable cross handgrip and rubber bottom tip are drawn with clean symmetry.",
                "palette": "only the palest natural ash-wood on the crutch shafts and sheer tan on the pads",
                "motion": "The crutches stand firmly upright, offering dependable quiet support."
            },
            {
                "title": "접이식 알루미늄 휠체어", "words": ["wheelchair", "mobile", "wheel", "comfort", "assist"],
                "subjects": "one modern lightweight folding transport wheelchair shown in neat side profile at center",
                "draw_steps": "The tubular metal stand, rear spoked push wheels, footrests and side rests are drawn with clean mechanical strokes.",
                "palette": "only the palest titanium-silver on the tubular structure and sheer charcoal on the cotton fabric seat",
                "motion": "The spoked wheel settles smoothly and the parking brake locks firm."
            }
        ]
    },

    # Set 13: 사회 & 금융 (10편)
    {
        "set_id": "set13",
        "set_name": "Set 13 (사회 & 금융)",
        "target_chapter": "ch14 MERCATUS & ch13 FORUM",
        "target_branches": "돈과 계산, 사회와 제도, 우편과 기록",
        "scenes": [
            {
                "title": "클래식 우체통과 봉인된 편지 봉투", "words": ["postbox", "letter", "mail", "envelope", "send"],
                "subjects": "one traditional pillar postbox standing at center, and one crisp white envelope with red postage stamp beside it",
                "draw_steps": "The cylindrical postbox column, domed roof cap and letter posting slot are drawn first. The sealed letter envelope follows.",
                "palette": "only the palest translucent coral-red on the postbox and clean crisp white on the envelope",
                "motion": "The posting slot flap drops with a tiny soft click and rests closed."
            },
            {
                "title": "은행 원형 금고문과 휠 핸들", "words": ["vault", "bank", "secure", "lock", "dial"],
                "subjects": "one heavy circular vault door with central spoke wheel and combination lock dial shown at center",
                "draw_steps": "The massive circular door rim, locking bolt pins around the perimeter and central spoke wheel are drawn with micro-precision.",
                "palette": "only the palest brushed stainless-steel and sheer warm brass on the locking bolts",
                "motion": "The central spoke wheel turns smoothly a quarter circle and locks."
            },
            {
                "title": "황동 양팔 저울과 금화 더미", "words": ["scale", "balance", "coin", "gold", "value"],
                "subjects": "one classical brass balance scale with two hanging pans at center, with five neat gold coins on one pan",
                "draw_steps": "The central fulcrum pillar, horizontal balance beam and two suspended pan dishes are drawn with perfect symmetry.",
                "palette": "only the palest luminous brass-gold on the balance structure and delicate gold-amber on the coins",
                "motion": "The two balance pans rock gently twice and settle in perfect horizontal equilibrium."
            },
            {
                "title": "도서관 책 반납함과 대출 카드", "words": ["library", "book", "borrow", "card", "read"],
                "subjects": "one classic wooden library book cart at center holding three neatly stacked hardback volumes",
                "draw_steps": "The sloped wooden shelves, side support panels and three rectangular book spines are drawn with clean lines.",
                "palette": "only the palest warm oak-tan on the cart and sheer pastel sage and burgundy on the book cloth",
                "motion": "The books rest in orderly, quiet studious peace."
            },
            {
                "title": "선거 투표함과 접힌 투표용지", "words": ["ballot", "vote", "elect", "choice", "citizen"],
                "subjects": "one clean wooden ballot box with top slot at center, with one folded sheet ballot slipping halfway through",
                "draw_steps": "The square wooden box silhouette, metal corner brackets and narrow top drop slot are drawn with crisp geometry.",
                "palette": "only the palest natural pine on the box and crisp white on the sheet ballot",
                "motion": "The folded sheet ballot drops cleanly through the slot into the secure interior."
            },
            {
                "title": "가죽 여권 케이스와 탑승권 티켓", "words": ["passport", "travel", "ticket", "flight", "border"],
                "subjects": "one navy leather passport booklet with gold emblem at center, and one perforated airline boarding pass tucked inside",
                "draw_steps": "The clean rectangular passport cover, corner stitching and boarding pass barcode lines are drawn with hairline precision.",
                "palette": "only the palest deep navy wash on the passport cover with faint gold emblem glint",
                "motion": "The passport rests ready, poised and still on the white field."
            },
            {
                "title": "우편 저울과 소포 요금 스탬프", "words": ["parcel", "weight", "stamp", "package", "post"],
                "subjects": "one brass spring letter scale with round dial at center, holding a neat brown sheet parcel tied with string",
                "draw_steps": "The circular dial face, top weighing pan and square string-tied postal package are drawn with fine outlines.",
                "palette": "only the palest warm brass on the scale and natural kraft-sheet brown on the tied parcel",
                "motion": "The dial indicator needle settles steadily at the exact weight mark."
            },
            {
                "title": "가죽 서류가방과 황동 버클 잠금장치", "words": ["briefcase", "leather", "lock", "business", "formal"],
                "subjects": "one structured leather attaché briefcase standing upright at center with dual brass clasp locks",
                "draw_steps": "The rectangular box case, top leather handle and two polished brass lock clasps are drawn with crisp symmetry.",
                "palette": "only the palest warm caramel-leather wash across the case and translucent brass on the clasps",
                "motion": "The twin brass clasp locks snap with a tiny soft click and stay closed."
            },
            {
                "title": "기계식 시계탑 탈진기 클락워크", "words": ["clockwork", "time", "pendulum", "tick", "precise"],
                "subjects": "one precision skeleton clock movement mechanism with brass escapement wheel and swinging pendulum at center",
                "draw_steps": "The intricate gear teeth, deadbeat escapement pallet and slender pendulum rod are drawn with micro-precision.",
                "palette": "only the palest luminous brass on the gear wheels and sheer steel on the structure",
                "motion": "The pendulum swings smoothly once with a quiet rhythmic tick."
            },
            {
                "title": "국제 조약 서명용 깃털펜과 왁스 씰", "words": ["treaty", "accord", "seal", "diplomacy", "pledge"],
                "subjects": "one engraved brass signet stamp and one round crimson melted wax seal impression on heavy vellum sheet at center",
                "draw_steps": "The turned brass seal handle, circular wax seal crest and fine vellum sheet edges are drawn with fine precision.",
                "palette": "only the palest warm brass on the stamp and a rich translucent cherry-red on the wax seal",
                "motion": "The wax seal impression rests sharp, permanent and completely still."
            }
        ]
    }
]

# 100편 전체 프롬프트 조립
complete_100_final = []

for s in ALL_SETS_DATA:
    set_prompts = []
    for idx, sc in enumerate(s["scenes"]):
        prompt_text = PERFECT_ATLAS_TEMPLATE.format(
            subjects=sc["subjects"],
            draw_steps=sc["draw_steps"],
            palette=sc["palette"],
            motion=sc["motion"]
        )
        clean_p = " ".join(prompt_text.split())
        set_prompts.append({
            "id": f"{s['set_id']}-{str(idx+1).zfill(2)}",
            "chapter": f"{s['set_id'].upper()} ({s['target_branches']})",
            "title": sc["title"],
            "words": sc["words"],
            "prompt": clean_p
        })
    
    # 텍스트 파일 저장
    filename = f"_작업/bulk_sets/{s['set_id']}_10.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for p in set_prompts:
            f.write(p["prompt"] + "\n\n")
            
    complete_100_final.append({
        "set_id": s["set_id"],
        "set_name": s["set_name"],
        "target_chapter": s["target_chapter"],
        "target_branches": s["target_branches"],
        "filename": filename,
        "prompts": set_prompts
    })

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(complete_100_final, f, ensure_ascii=False, indent=2)

print("10개 세트 100편 전체 [딱정벌레 성인 자연사 도감] 헌법으로 100% 완전 재건축 완료!")

