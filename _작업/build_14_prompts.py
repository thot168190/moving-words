# -*- coding: utf-8 -*-
"""
정본 14편 프롬프트 일괄 생성 (이전 챕터 물개 바위섬 성공 정본 100% 이식)
"""

import json, os, subprocess

PROMPTS = [
    # ── ch8: MOTUS (운동과 이동) 3편 ──────────────────────────
    {
        "id": "ch8-05",
        "chapter": "Chapter 8 (MOTUS) 05편",
        "title": "시골 간이역과 철길 승강장",
        "type": "물개 바위섬 정본 문법",
        "words": ["station (역)", "platform (승강장)", "rail (철길)", "track (선로)", "bench (벤치)", "board (탑승하다)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are one sturdy countryside railway platform and parallel steel train tracks extending across both outer thirds, a classic wooden waiting bench and antique lamppost balancing the left, and a destination signpost balancing the right.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level platform edge and horizon. Draw the level tracks and waiting bench next, keeping the combined silhouette horizontal rather than diagonal. Extend two parallel steel rail lines equally toward the left and right outer thirds. Add one slender station lamppost at left and one neat destination signpost at right. There is no visible modern train or vehicle anywhere. Keep platform line sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is weathered timber-brown on the wooden bench, cool stone grey on the platform tiles, subtle steel-blue on the parallel rail lines, muted iron-grey on the lamppost, and a very pale sage-green in the distant grass edge. A tiny warm golden light stirs softly inside the station lamp glass; all structural lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },
    {
        "id": "ch8-06",
        "chapter": "Chapter 8 (MOTUS) 06편",
        "title": "야외 농구 코트와 골대",
        "type": "물개 바위섬 정본 문법",
        "words": ["court (코트·경기장)", "bounce (튀다)", "net (그물)", "shoot (쏘다)", "score (득점)", "pole (기둥)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a freestanding outdoor basketball hoop at the optical center, clean painted court key markings extending across both outer thirds, one round basketball resting at lower left, and a simple metal bench balancing the right edge.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level court baseline horizon. Draw the central steel post, backboard and net next, keeping the combined silhouette vertical and balanced. Extend clean boundary lines equally toward the left and right outer thirds. Add one round basketball at lower left and one simple bench at lower right. There is no visible player or crowd anywhere. Keep court lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a sheer translucent apricot-orange on the round basketball, muted slate-blue on the court boundary lines, cool silver-grey on the steel post, and soft pale umber on the bench. The round basketball gives one tiny gentle bounce and settles onto the court floor; all structural lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },
    {
        "id": "ch8-07",
        "chapter": "Chapter 8 (MOTUS) 07편",
        "title": "우체국 자전거와 빨간 우체통",
        "type": "물개 바위섬 정본 문법",
        "words": ["bicycle (자전거)", "post (우편·기둥)", "mail (우편물)", "route (경로)", "deliver (배달하다)", "bell (종)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a classic standalone delivery bicycle with carrier basket at the optical center, a vintage street pillar mailbox balancing the left, a cobblestone pathway extending across both outer thirds, and a modest cluster of roadside shrub balancing the right.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level cobblestone ground line. Draw the delivery bicycle with its slender tubes, wheels and front basket next, keeping the combined silhouette horizontal rather than diagonal. Extend light cobblestone contours equally toward the left and right outer thirds. Add one round pillar mailbox at left and one neat shrub cluster at right. There is no visible postman or vehicle anywhere. Keep cobblestone markings sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a restrained soft coral-red on the street mailbox, sheer watery silver-blue on the bicycle metal, quiet sage on the shrub leaves, and soft sand-grey on the cobblestones. The bicycle front wheel gives one tiny gentle roll forward and pauses smoothly; all structural lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },

    # ── ch12: SOMNIUM (자연과 신비) 3편 ──────────────────────────
    {
        "id": "ch12-05",
        "chapter": "Chapter 12 (SOMNIUM) 05편",
        "title": "천년의 거대한 고목과 숲길",
        "type": "물개 바위섬 정본 문법",
        "words": ["root (뿌리)", "branch (가지)", "shade (그늘)", "moss (이끼)", "timber (목재·나무)", "ancient (고대의)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are one magnificent ancient oak tree with broad ground roots at the optical center, smooth mossy river stones extending across both outer thirds, and two delicate forest songbirds perched on the arching branches.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level ground root line. Draw the sturdy central oak trunk and broad arching canopy branches next, keeping the combined silhouette balanced and majestic. Extend organic surface roots and mossy stones equally toward the left and right outer thirds. Add one songbird on a left branch and one on a lower right stone. There is no visible person or structure anywhere. Keep leaf clusters sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is pale umber and bark-grey on the oak trunk, airy tea-green through the canopy leaves, muted celadon on the mossy stones, and quiet warm rust on the songbird breast. A single songbird turns its head quietly; all majestic branches and roots remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },
    {
        "id": "ch12-06",
        "chapter": "Chapter 12 (SOMNIUM) 06편",
        "title": "사막의 푸른 오아시스와 야자수",
        "type": "물개 바위섬 정본 문법",
        "words": ["oasis (오아시스)", "palm (야자수)", "spring (샘물)", "pure (순수한)", "sand (모래)", "desert (사막)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a clear natural freshwater oasis pool with a graceful desert gazelle at the optical center, two slender curved palm trees balancing the left, and sweeping gentle sand dune ridgelines extending across both outer thirds.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level dune horizon. Draw the central reflective pool and drinking gazelle next, keeping the combined silhouette horizontal rather than diagonal. Extend sweeping dune crests equally toward the left and right outer thirds. Add two graceful palm trees at left and a gentle dune rise at right. There is no visible caravan or tent anywhere. Keep dune contours sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a transparent sky-cyan on the pool water, delicate champagne-sand on the dune lines, desaturated olive-sage on the palm fronds, and natural warm fawn on the gazelle. One tiny concentric water ring ripples outward smoothly across the pool; all other landscape elements remain still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },
    {
        "id": "ch12-07",
        "chapter": "Chapter 12 (SOMNIUM) 07편",
        "title": "비밀의 동굴과 앤틱 보물상자",
        "type": "물개 바위섬 정본 문법",
        "words": ["chest (궤·상자)", "treasure (보물)", "jewel (보석)", "coin (동전)", "cave (동굴)", "lock (자물쇠)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are an open antique wooden chest with coins and jewels at the optical center, a natural rock cave ledge extending across both outer thirds, a small brass padlock balancing the lower left, and a small crystal cluster balancing the lower right.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level rock ledge line. Draw the central timber chest with its open curved lid next, keeping the combined silhouette horizontal rather than diagonal. Extend natural rock contours equally toward the left and right outer thirds. Add one small padlock at lower left and crystal facets at lower right. There is no visible pirate or gold pile anywhere. Keep stone markings sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is weathered timber-brown on the chest, a delicate whisper of champagne-gold on the coins, pale aquamarine and crystal-tint on the jewels, and cool stone grey on the cave ledge. A single tiny crystal facet catches the light with a gentle glint; all structural lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },

    # ── ch7: SENSUS (감각과 일상) 3편 ──────────────────────────
    {
        "id": "ch7-05",
        "chapter": "Chapter 7 (SENSUS) 05편",
        "title": "창가의 흔들의자와 털실 바구니",
        "type": "물개 바위섬 정본 문법",
        "words": ["cotton (목화·면)", "sweater (스웨터)", "relax (휴식하다)", "gentle (부드러운)", "wool (양모·털실)", "weave (짜다)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a classic wooden rocking armchair with knitted throw blanket at the optical center, a clean horizontal wooden terrace line extending across both outer thirds, a woven yarn basket balancing the left, and a leafy potted plant balancing the right.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level terrace floor horizon. Draw the wooden armchair with its curved runners and spindle back next, keeping the combined silhouette balanced. Extend clean plank lines equally toward the left and right outer thirds. Add one woven yarn basket at left and one potted plant on a stool at right. There is no visible room corner or wall anywhere. Keep plank lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a pale oatmeal-tan on the wooden chair, soft powder-blue on the knitted throw, muted lilac on the yarn spheres, and fresh celadon-sage on the potted leaves. The wooden rocking chair sways once with a microscopic, soothing motion and settles into calm stillness. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },
    {
        "id": "ch7-06",
        "chapter": "Chapter 7 (SENSUS) 06편",
        "title": "온실 정원의 작은 분수와 테라코타 화분",
        "type": "물개 바위섬 정본 문법",
        "words": ["fountain (분수)", "plant (식물)", "spade (모종삽)", "bloom (꽃피다)", "seed (씨앗)", "trim (다듬다)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a small classical tier stone fountain with trickling water at the optical center, garden flagstones extending across both outer thirds, three terracotta flowerpots with herbs balancing the left, and an antique watering jug and spade balancing the right.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level garden ground line. Draw the circular stone fountain base and tiered basin next, keeping the combined silhouette centered and upright. Extend stone path contours equally toward the left and right outer thirds. Add three terracotta flowerpots at left and a standing watering jug and spade at right. There is no visible greenhouse wall or plastic pot anywhere. Keep flagstone lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is cool limestone-grey on the fountain, muted terracotta-peach on the flowerpots, airy herb-green on the leaves, and translucent sky-cyan in the fountain pool. A tiny stream of water trickles smoothly from the fountain top into the clear basin below; all structural lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },
    {
        "id": "ch7-07",
        "chapter": "Chapter 7 (SENSUS) 07편",
        "title": "호숫가 아침 산책로와 하얀 벤치",
        "type": "물개 바위섬 정본 문법",
        "words": ["path (길·산책로)", "lake (호수)", "breeze (산들바람)", "calm (고요한)", "morning (아침)", "reflect (비추다)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a painted white timber park bench beneath arching willow branches at the optical center, a meandering gravel path extending across the left outer third, and calm reflective lake water ripples extending across the right outer third.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level lake shoreline horizon. Draw the white garden bench and graceful arching willow canopy next, keeping the combined silhouette balanced. Extend gentle gravel path lines to the left and water ripples to the right. Add slender willow twigs in the upper space. There is no visible boat or dock anywhere. Keep water lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a delicate ivory-white on the bench, airy tea-green on the willow leaves, translucent cerulean-blue on the water ripples, and soft morning-sand on the path. The slender willow branch tips sway softly in a gentle morning breeze and settle into stillness. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },

    # ── ch11: COSMOS (과학과 탐구) 3편 ──────────────────────────
    {
        "id": "ch11-04",
        "chapter": "Chapter 11 (COSMOS) 04편",
        "title": "천문대의 대형 망원경과 성도시계",
        "type": "물개 바위섬 정본 문법",
        "words": ["telescope (망원경)", "star (별)", "planet (행성)", "orbit (궤도)", "measure (측정하다)", "focus (초점)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a classic brass astronomical telescope on an equatorial tripod at the optical center, an open observation dome window arc extending across the upper space, a rotating star chart map balancing the left, and faint constellation stars balancing the right.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level observation floor line. Draw the central telescope barrel and sturdy tripod stand next, keeping the combined silhouette upright and precise. Extend arching dome window contours equally toward the upper outer thirds. Add one spherical star chart map at left and delicate star points at right. There is no visible modern screen or clutter anywhere. Keep constellation lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a delicate sheer champagne-brass on the telescope barrel, cool silver-grey on the tripod legs, muted indigo-blue on the star chart map, and luminous soft-white on the stars. The telescope barrel elevates smoothly by a minute angle toward the stars and pauses with graceful precision. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },
    {
        "id": "ch11-05",
        "chapter": "Chapter 11 (COSMOS) 05편",
        "title": "초원의 풍력 발전기와 기상 풍향계",
        "type": "물개 바위섬 정본 문법",
        "words": ["wind (바람)", "current (흐름·전류)", "energy (에너지)", "direction (방향)", "weather (날씨)", "rotate (회전하다)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a tall slender modern wind turbine at the optical center, rolling meadow hill ridges extending across both outer thirds, a decorative wooden weathercock on a post balancing the right, and a few floating dandelion seeds balancing the left.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level rolling meadow horizon. Draw the tall slender turbine mast and three blades next, keeping the combined silhouette vertical and elegant. Extend grassy ridge contours equally toward the left and right outer thirds. Add floating seeds at left and a small weathercock post at right. There is no visible power pylon or building anywhere. Keep grass blades sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is pristine white-grey on the turbine mast, quiet spring-meadow sage on the grass, weathered cedar-brown on the weathercock, and airy pale-gold on the floating seed fluff. The three wind turbine blades rotate slowly and smoothly through one complete graceful cycle. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },
    {
        "id": "ch11-06",
        "chapter": "Chapter 11 (COSMOS) 06편",
        "title": "숲속 시냇물과 통나무 다리",
        "type": "물개 바위섬 정본 문법",
        "words": ["flask (플라스크·물병)", "glow (빛나다)", "cell (세포·칸)", "pure (순수한)", "liquid (액체)", "observe (관찰하다)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a gentle wooden plank bridge across a clear forest stream at the optical center, smooth river stones extending across both outer thirds, a glass canteen resting on a rock balancing the left, and a small water bird balancing the right.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level stream bank line. Draw the wooden footbridge and flowing water ripples next, keeping the combined silhouette horizontal rather than diagonal. Extend natural stream contours equally toward the left and right outer thirds. Add a glass canteen at lower left and a resting water bird at lower right. There is no visible fisherman or trash anywhere. Keep water lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a transparent sky-cyan in the stream water, weathered timber-brown on the footbridge, muted moss-green on the river stones, and soft silver-grey on the water bird. A clear water ripple circles gently under the bridge; all other landscape elements remain still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },

    # ── ch5: LUDUS (예술과 무대) 2편 ──────────────────────────
    {
        "id": "ch5-06",
        "chapter": "Chapter 5 (LUDUS) 06편",
        "title": "음악실의 그랜드 피아노와 악보대",
        "type": "물개 바위섬 정본 문법",
        "words": ["piano (피아노)", "tune (곡조)", "tone (음색)", "concert (연주회)", "band (밴드)", "score (악보)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are an open acoustic grand piano with sheet music stand at the optical center, a clean wooden stage floor extending across both outer thirds, a classic wooden tuning fork balancing the left, and an upright cello balancing the right.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level wooden floor line. Draw the grand piano with its elegant curved body and music stand next, keeping the combined silhouette balanced. Extend clean stage plank lines equally toward the left and right outer thirds. Add a small pyramid tuning fork at left and an upright cello at right. There is no visible pianist or audience anywhere. Keep piano lid curves sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a sheer translucent wash of warm grey-charcoal on the piano body, rich honey-amber on the cello wood, soft ivory on the sheet music, and pale cedar on the stage floor. The slender pendulum of the wooden tuning fork sways smoothly once to the right and left in a calm tempo. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },
    {
        "id": "ch5-07",
        "chapter": "Chapter 5 (LUDUS) 07편",
        "title": "야외 극장의 무대와 클래식 조명",
        "type": "물개 바위섬 정본 문법",
        "words": ["drama (연극)", "scene (장면)", "mask (가면)", "stage (무대)", "audience (관객)", "applause (박수)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are an elevated wooden theater stage with classical comedy and tragedy drama masks at the optical center, draped stage floor planks extending across both outer thirds, an antique stage spotlight silhouette balancing the left, and a draped satin curtain sash balancing the right.

0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level wooden stage horizon. Draw the two sculptural drama masks on a soft cushion next, keeping the combined silhouette centered. Extend plank lines equally toward the left and right outer thirds. Add an antique standing spotlight at left and an elegant draped curtain sash at right. There is no visible actor or audience anywhere. Keep stage plank lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable.

4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is delicate porcelain-ivory on the drama masks, soft velvet-burgundy on the cushion, warm golden-amber on the spotlight glass, and gentle lavender-rose on the satin sash. A single satin ribbon tip settles softly onto the wooden stage; all other elements remain still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space.

Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    }
]

# 개별 파일 저장 및 검증
print(f"총 {len(PROMPTS)}편 정본 문법 프롬프트 빌드 시작...")
err_total = 0

for p in PROMPTS:
    fn = f"_작업/prompt_{p['id']}.txt"
    with open(fn, "w") as f:
        f.write(p["prompt"].strip())
    
    # 검증 실행
    res = subprocess.run(["python3", "_작업/verify_prompt.py", fn], capture_output=True, text=True)
    if res.returncode != 0 or "★★ 오류" in res.stdout:
        print(f"❌ [오류 발생] {p['id']} - {p['title']}")
        print(res.stdout)
        err_total += 1
    else:
        print(f"✅ [검증 통과] {p['id']} - {p['title']}")

print(f"\n검증 결과: {len(PROMPTS)}편 중 {len(PROMPTS)-err_total}편 통과, {err_total}편 오류")
