#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
20편 성공문법 프롬프트 허브 생성기 (2026-08-21)
정본 헌법 (00_성공문법_정본_마스터_20260820.md) 완벽 준수
"""

import json, html

scenes = [
    # 1. ch4-04: 서재의 만년필과 편지
    {
        "id": "ch4-04",
        "chapter": "Chapter 4 (SCHOLA) 04편",
        "title": "서재의 만년필과 편지",
        "words": ["envelope (봉투)", "spell (철자하다)", "text (글)", "message (메시지)", "paragraph (문단)", "diary (일기)", "seal (봉인)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a vintage brass fountain pen, an open parchment letter with neat handwriting, and a classic wax seal stamp on an envelope. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The vintage brass fountain pen is drawn first with clean minimal pencil contours.

1.5-3.0s: the parchment letter and the envelope form cleanly through sparse, elegant pencil line art.

3.0-4.5s: subtle script lines of handwriting and the round wax seal stamp appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as warm amber on the brass pen, soft cream on the letter, and deep crimson on the wax seal. All surrounding space remains untouched pure white.

7.2-8.0s: a tiny glimmer of light catches the polished nib of the fountain pen while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 2. ch4-05: 도서관의 백과사전과 지도
    {
        "id": "ch4-05",
        "chapter": "Chapter 4 (SCHOLA) 05편",
        "title": "도서관의 백과사전과 지도",
        "words": ["dictionary (사전)", "catalog (목록)", "chart (도표)", "graph (그래프)", "article (기사)", "essay (수필)", "topic (주제)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a thick open leather-bound reference book with illustrated chart diagrams and a rolled antique astronomical chart beside it. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The heavy open reference book is drawn first with clean minimal pencil contours.

1.5-3.0s: the rolled paper chart and book spine form cleanly through sparse, elegant pencil line art.

3.0-4.5s: delicate engraved circular chart markings, fine grid lines, and classic index tabs appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as pale chestnut on the leather binding, gentle sky-blue on the chart lines, and muted ochre on the paper edges. All surrounding space remains untouched pure white.

7.2-8.0s: a single page edge flutters with a microscopic breeze and settles, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 3. ch4-06: 인쇄소의 활자와 프레스기
    {
        "id": "ch4-06",
        "chapter": "Chapter 4 (SCHOLA) 06편",
        "title": "인쇄소의 활자와 프레스기",
        "words": ["press (프레스기)", "copy (복사본)", "edit (편집하다)", "register (등록하다)", "record (기록)", "print (인쇄하다)", "title (제목)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a classic cast-iron bookbinder press with a brass turning wheel and a freshly printed sheet of crisp rag paper. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The sculptural frame of the iron press is drawn first with clean minimal pencil contours.

1.5-3.0s: the central threaded screw, top handwheel, and the neat stack of paper sheets form cleanly through sparse, elegant pencil line art.

3.0-4.5s: geometric typography layout marks and the mechanical joints appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as slate-blue grey on the iron frame, soft brass gold on the wheel, and warm linen on the paper. All surrounding space remains untouched pure white.

7.2-8.0s: the top wheel rotates a hair's breadth and clicks into place, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 4. ch5-06: 음악실의 그랜드 피아노와 악보
    {
        "id": "ch5-06",
        "chapter": "Chapter 5 (LUDUS) 06편",
        "title": "음악실의 그랜드 피아노와 악보",
        "words": ["band (밴드)", "concert (연주회)", "tune (곡조)", "tone (음색)", "loud (소리 큰)", "noise (소음)", "whistle (휘파람)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are an open acoustic grand piano with its graceful curved body, a wooden music stand holding sheet music, and a polished brass metronome. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The sweeping curved rim of the piano and its slender legs are drawn first with clean minimal pencil contours.

1.5-3.0s: the row of delicate piano keys, the open wooden lid, and the music stand form cleanly through sparse, elegant pencil line art.

3.0-4.5s: the musical staff notation on the open score and the pendulum of the metronome appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as translucent ebony-tint on the piano rim, warm honey-oak on the music stand, and luminous champagne on the brass metronome. All surrounding space remains untouched pure white.

7.2-8.0s: the slender metronome pendulum sways smoothly once to the right, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 5. ch5-07: 무대 위의 연극과 가면
    {
        "id": "ch5-07",
        "chapter": "Chapter 5 (LUDUS) 07편",
        "title": "무대 위의 연극과 가면",
        "words": ["drama (연극)", "comedy (희극)", "scene (장면)", "mask (가면)", "applause (박수)", "entertain (즐겁게하다)", "humor (유머)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a pair of classical Venetian drama masks (one smiling, one contemplative) resting on a draped satin ribbon and a vintage theater spotlight silhouette. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The expressive contours of the two ceramic drama masks are drawn first with clean minimal pencil contours.

1.5-3.0s: the flowing satin ribbon underneath and the delicate feathered ornaments form cleanly through sparse, elegant pencil line art.

3.0-4.5s: fine decorative filigree patterns around the mask eyeholes and the vintage brass spotlight stand appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as soft porcelain-ivory on the masks, dusty rose-lavender on the ribbon, and subtle antique-gold along the edges. All surrounding space remains untouched pure white.

7.2-8.0s: a single satin ribbon tail gently settles onto the white surface, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 6. ch7-05: 뜨개질과 털실 바구니
    {
        "id": "ch7-05",
        "chapter": "Chapter 7 (SENSUS) 05편",
        "title": "뜨개질과 털실 바구니",
        "words": ["cotton (목화·면)", "sweater (스웨터)", "glove (장갑)", "curl (말리다)", "sew (바느질하다)", "gentle (부드러운)", "relax (휴식하다)"],
        "type": "인물·라이프스타일형 (Template B)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are one stylish youth character drawn in a clean minimalist lifestyle line-art style seated in side-profile on a light wooden stool, gently holding wooden knitting needles, with a woven basket of soft wool yarn spheres beside them. There are no frontal portraits, staring faces, webtoon idols or drawing tools anywhere in the scene.

0-1.5s: clean, smooth, medium-grey single-stroke line-art contours (30% grey) appear progressively from the empty white field. Every line is exceptionally crisp, clean and confident. The woven yarn basket and round balls of wool are drawn first on the floor.

1.5-3.0s: the stylish youth character forms in side-profile with clean, elegant outline contours inspired by contemporary lifestyle drawings. The relaxed posture, cozy oversized shirt, delicate hands holding knitting needles, and quiet posture are drawn effortlessly.

3.0-4.5s: charming minimal dot eyes with a peaceful expression, and a clean simple closed straight-line mouth appear sequentially to complete the line drawing. Every line remains thin, crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as a subtle peach-coral blush on the cheek, warm oatmeal-cream on the sweater, and muted sage-green on the yarn sphere. All surrounding space remains untouched pure white.

7.2-8.0s: the character quietly pauses hands with a gentle serene look, and the scene rests in complete, quiet stillness, surrounded by generous untouched white space.

Style: minimalist contemporary lifestyle line-art illustration, Noritake and Yu Nagaba inspired clean graphic line drawing, iconic simplified facial features, luminous transparent watercolor tint, generous untouched white space. Pure, stylish, chic, airy and modern.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: frontal portrait, direct camera stare, puckered lips, open mouth, exaggerated cartoon features, vertical border lines, webtoon, anime, K-pop idol faces, realistic shaded eyelashes, detailed lips, shaded hair strands, 3D render, photorealism, text, labels, dark heavy watercolor, cuts."""
    },
    # 7. ch7-06: 정원을 가꾸는 원예사
    {
        "id": "ch7-06",
        "chapter": "Chapter 7 (SENSUS) 06편",
        "title": "정원을 가꾸는 원예사",
        "words": ["plant (식물)", "dirt (흙)", "spade (모종삽)", "seed (씨앗)", "grow (자라다)", "trim (다듬다)", "bloom (꽃피다)"],
        "type": "인물·라이프스타일형 (Template B)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are one stylish youth character drawn in a clean minimalist lifestyle line-art style kneeling gracefully in side-profile, caring for a terracotta potted sprout with a small metal hand spade and watering can beside them. There are no frontal portraits, staring faces, webtoon idols or drawing tools anywhere in the scene.

0-1.5s: clean, smooth, medium-grey single-stroke line-art contours (30% grey) appear progressively from the empty white field. Every line is exceptionally crisp, clean and confident. The simple terracotta pot, leafy young sprout, and small spade are drawn first in the center.

1.5-3.0s: the stylish youth character forms in side-profile with clean, elegant outline contours inspired by contemporary lifestyle drawings. The comfortable gardening apron, rolled-up sleeves, relaxed kneeling posture, and focused gentle hand are drawn effortlessly.

3.0-4.5s: charming minimal dot eyes looking warmly downward at the plant, and a clean simple closed straight-line mouth appear sequentially to complete the line drawing. Every line remains thin, crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as a subtle peach-coral blush on the cheek, warm terracotta-clay on the pot, and luminous pale-mint on the fresh sprout leaf. All surrounding space remains untouched pure white.

7.2-8.0s: the character gently touches the leaf tip with a serene posture, and the scene rests in complete, quiet stillness, surrounded by generous untouched white space.

Style: minimalist contemporary lifestyle line-art illustration, Noritake and Yu Nagaba inspired clean graphic line drawing, iconic simplified facial features, luminous transparent watercolor tint, generous untouched white space. Pure, stylish, chic, airy and modern.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: frontal portrait, direct camera stare, puckered lips, open mouth, exaggerated cartoon features, vertical border lines, webtoon, anime, K-pop idol faces, realistic shaded eyelashes, detailed lips, shaded hair strands, 3D render, photorealism, text, labels, dark heavy watercolor, cuts."""
    },
    # 8. ch7-07: 아침 러닝과 운동화
    {
        "id": "ch7-07",
        "chapter": "Chapter 7 (SENSUS) 07편",
        "title": "아침 러닝과 운동화",
        "words": ["step (걸음)", "motion (동작)", "stride (보폭)", "track (트랙)", "breathe (숨쉬다)", "sweat (땀)", "active (활동적인)"],
        "type": "인물·라이프스타일형 (Template B)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are one stylish youth character drawn in a clean minimalist lifestyle line-art style standing in dynamic side-profile, lightly tying the shoelaces of a running sneaker on a simple low wooden step with a clear water bottle resting nearby. There are no frontal portraits, staring faces, webtoon idols or drawing tools anywhere in the scene.

0-1.5s: clean, smooth, medium-grey single-stroke line-art contours (30% grey) appear progressively from the empty white field. Every line is exceptionally crisp, clean and confident. The sleek sneaker, low step, and modern glass bottle are drawn first.

1.5-3.0s: the stylish youth character forms in side-profile with clean, elegant outline contours inspired by contemporary lifestyle drawings. The sporty windbreaker jacket, flexible posture, clean jawline, and tied shoelace gesture are drawn effortlessly.

3.0-4.5s: charming minimal dot eyes with a fresh morning gaze, and a clean simple closed straight-line mouth appear sequentially to complete the line drawing. Every line remains thin, crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as a subtle peach-coral blush on the cheek, pale cobalt-blue accent on the sneaker, and cool transparent aqua on the bottle. All surrounding space remains untouched pure white.

7.2-8.0s: the character finishes tying the lace and stands tall with poised confidence, and the scene rests in complete, quiet stillness, surrounded by generous untouched white space.

Style: minimalist contemporary lifestyle line-art illustration, Noritake and Yu Nagaba inspired clean graphic line drawing, iconic simplified facial features, luminous transparent watercolor tint, generous untouched white space. Pure, stylish, chic, airy and modern.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: frontal portrait, direct camera stare, puckered lips, open mouth, exaggerated cartoon features, vertical border lines, webtoon, anime, K-pop idol faces, realistic shaded eyelashes, detailed lips, shaded hair strands, 3D render, photorealism, text, labels, dark heavy watercolor, cuts."""
    },
    # 9. ch8-05: 기차역과 시계탑
    {
        "id": "ch8-05",
        "chapter": "Chapter 8 (MOTUS) 05편",
        "title": "기차역과 시계탑",
        "words": ["station (역)", "rail (철로)", "clock (시계)", "ticket (표)", "journey (여행)", "track (선로)", "depart (출발하다)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a classic iron railway station platform clock on an ornate arched post, a set of parallel steel rails leading into the distance, and an old leather suitcase with a paper travel ticket. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The tall cast-iron platform clock post and round double-faced clock are drawn first with clean minimal pencil contours.

1.5-3.0s: the smooth parallel steel tracks and the sturdy vintage suitcase on the platform form cleanly through sparse, elegant pencil line art.

3.0-4.5s: classic Roman numerals on the clock face, detailed track ballast gravel, and leather suitcase strap buckles appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as warm saddle-brown on the suitcase, soft steel-blue on the iron post, and pale ivory on the clock face. All surrounding space remains untouched pure white.

7.2-8.0s: the long clock hand ticks forward exactly one minute mark, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 10. ch8-06: 항구의 크레인과 컨테이너
    {
        "id": "ch8-06",
        "chapter": "Chapter 8 (MOTUS) 06편",
        "title": "항구의 크레인과 컨테이너",
        "words": ["port (항구)", "dock (부두)", "load (싣다)", "crane (크레인)", "cargo (화물)", "trade (무역)", "steel (강철)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a towering steel harbor gantry crane, three neatly stacked cargo containers on a clean concrete pier, and heavy mooring bollards with braided rope. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The geometric truss structure of the tall steel crane is drawn first with clean minimal pencil contours.

1.5-3.0s: the rectangular cargo containers and the edge of the quiet dock form cleanly through sparse, elegant pencil line art.

3.0-4.5s: pulley cables, container locking corners, and coiled dock ropes appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as soft maritime-navy and pastel-vermilion on the containers, pale zinc-grey on the crane, and sea-salt grey on the pier. All surrounding space remains untouched pure white.

7.2-8.0s: a slight cable tension adjusts smoothly at the crane hoist, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 11. ch8-07: 골목길의 우체통과 가로등
    {
        "id": "ch8-07",
        "chapter": "Chapter 8 (MOTUS) 07편",
        "title": "골목길의 우체통과 가로등",
        "words": ["lamp (가로등)", "post (기둥·우편)", "street (거리)", "brick (벽돌)", "corner (모퉁이)", "quiet (조용한)", "deliver (배달하다)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are an antique wrought-iron street lamp on a brick curb corner and a classic cylindrical red pillar postbox beside it. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The graceful curved neck of the vintage lamp post is drawn first with clean minimal pencil contours.

1.5-3.0s: the charming pillar postbox and the cobblestone curb edge form cleanly through sparse, elegant pencil line art.

3.0-4.5s: the glass lantern panels, mail drop slot flap, and neat brick texture seams appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as vibrant translucent scarlet on the postbox, soft forest-black on the lamp iron, and pale warm-amber inside the glass lantern. All surrounding space remains untouched pure white.

7.2-8.0s: a subtle warm glow breathes softly within the lantern glass, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 12. ch9-02: 법정과 정의의 저울
    {
        "id": "ch9-02",
        "chapter": "Chapter 9 (CIVIS) 02편",
        "title": "법정과 정의의 저울",
        "words": ["court (법정)", "judge (판사·판단)", "justice (정의)", "law (법)", "scale (저울)", "moral (도덕적인)", "balance (균형)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a gleaming balanced brass scales of justice standing on a polished walnut pedestal, and a classic wooden judicial gavel resting beside a heavy law ledger. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The symmetrical central pillar and fulcrum of the brass scale are drawn first with clean minimal pencil contours.

1.5-3.0s: the two suspended shallow pans, the turned wooden gavel, and the thick book base form cleanly through sparse, elegant pencil line art.

3.0-4.5s: delicate hanging chains, brass balance pointer needle, and embossed leather book spine details appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as glowing champagne-brass on the scale, warm walnut-brown on the gavel, and deep royal-navy on the book binding. All surrounding space remains untouched pure white.

7.2-8.0s: the two scale pans settle into absolute perfect horizontal equilibrium, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 13. ch9-03: 성벽과 깃발
    {
        "id": "ch9-03",
        "chapter": "Chapter 9 (CIVIS) 03편",
        "title": "성벽과 깃발",
        "words": ["castle (성)", "flag (깃발)", "crown (왕관)", "royal (왕실의)", "tower (탑)", "brick (벽돌)", "defense (방어)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are the crenellated stonework of a medieval castle tower, a fluttering heraldic pennant flag on a tall wooden flagpole, and an ornate golden royal crown resting on a velvet cushion. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The strong stone battlements and vertical tower silhouette are drawn first with clean minimal pencil contours.

1.5-3.0s: the waving flag swallowtail and the arched tower window form cleanly through sparse, elegant pencil line art.

3.0-4.5s: the filigree arches and pearl points of the golden crown on its tasseled cushion appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as soft limestone-grey on the battlements, royal crimson and azure on the flag, and radiant pure gold on the crown. All surrounding space remains untouched pure white.

7.2-8.0s: the heraldic flag ripples once gracefully in an unseen breeze, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 14. ch9-04: 광장의 분수대와 비둘기
    {
        "id": "ch9-04",
        "chapter": "Chapter 9 (CIVIS) 04편",
        "title": "광장의 분수대와 비둘기",
        "words": ["square (광장)", "fountain (분수)", "statue (조각상)", "pigeon (비둘기)", "peace (평화)", "splash (물보라)", "stone (돌)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a two-tiered classical stone fountain basin with clear flowing water streams and two graceful white doves perched quietly on the stone rim. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The symmetrical round bowls of the stone fountain are drawn first with clean minimal pencil contours.

1.5-3.0s: the smooth arch of flowing water and the delicate shapes of the perched white doves form cleanly through sparse, elegant pencil line art.

3.0-4.5s: fine feather contours on the doves, water ripples in the lower basin, and carved stone relief patterns appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as sunlit sandstone-ochre on the fountain, transparent sky-aqua on the water basin, and soft pearl-white on the doves. All surrounding space remains untouched pure white.

7.2-8.0s: a single water droplet falls from the upper tier creating one perfect concentric ring, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 15. ch11-04: 화학 실험실의 비커와 플라스크
    {
        "id": "ch11-04",
        "chapter": "Chapter 11 (SCIENTIA) 04편",
        "title": "화학 실험실의 비커와 플라스크",
        "words": ["lab (실험실)", "tube (시험관)", "flask (플라스크)", "liquid (액체)", "bubble (기포)", "experiment (실험)", "pour (따르다)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are an Erlenmeyer glass flask containing clear liquid, a glass beaker with measurement markings, and a wooden test tube rack with three clean glass tubes. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The conical silhouette of the glass flask and beaker are drawn first with clean minimal pencil contours.

1.5-3.0s: the wooden test tube rack and the curved glass lips of the vessels form cleanly through sparse, elegant pencil line art.

3.0-4.5s: precise graduated measurement ticks on the glass sides and a few tiny resting bubbles within the liquid level appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as luminous cyan-teal and pale amber inside the liquid solutions, and natural pine-wood tint on the test tube rack. All surrounding space remains untouched pure white.

7.2-8.0s: a single tiny bubble rises gracefully to the surface of the flask and vanishes, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 16. ch11-05: 시계공방의 기어와 태엽
    {
        "id": "ch11-05",
        "chapter": "Chapter 11 (SCIENTIA) 05편",
        "title": "시계공방의 기어와 태엽",
        "words": ["gear (톱니바퀴)", "spring (태엽·용수철)", "wheel (바퀴)", "clock (시계)", "precise (정밀한)", "repair (수리하다)", "metal (금속)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are an intricate brass clockwork escapement mechanism with interlocking toothed gears, a coiled steel mainspring, and fine watchmaker tweezers resting on a jeweler velvet pad. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The interlocking circular silhouettes of the brass gear train are drawn first with clean minimal pencil contours.

1.5-3.0s: the spiral balance spring and the slender stainless steel tweezers form cleanly through sparse, elegant pencil line art.

3.0-4.5s: razor-sharp gear teeth, ruby jewel bearings, and screw heads appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as warm polished gold-brass on the gears, iridescent ruby-red on the tiny bearing jewels, and deep indigo on the velvet pad. All surrounding space remains untouched pure white.

7.2-8.0s: the balance wheel pulses smoothly with one miniature tick-tock rotation, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 17. ch11-06: 전구와 전기 회로
    {
        "id": "ch11-06",
        "chapter": "Chapter 11 (SCIENTIA) 06편",
        "title": "전구와 전기 회로",
        "words": ["electric (전기의)", "switch (스위치)", "wire (전선)", "bulb (전구)", "battery (배터리)", "glow (빛나다)", "circuit (회로)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a vintage Edison glass filament bulb mounted on a wooden socket, a brass knife-blade toggle switch, and neatly curved copper connecting wires with a small vintage battery cell. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The teardrop glass dome of the Edison bulb and the wooden base are drawn first with clean minimal pencil contours.

1.5-3.0s: the brass knife switch, battery cylinder, and arched copper wires form cleanly through sparse, elegant pencil line art.

3.0-4.5s: the intricate coiled tungsten filament inside the bulb and screw terminals on the switch appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as warm copper-bronze on the wires, rich mahogany on the base, and soft honey-lemon on the filament bulb. All surrounding space remains untouched pure white.

7.2-8.0s: a soft, delicate golden warmth illuminates the inner filament with quiet elegance, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 18. ch12-05: 깊은 숲의 고목과 반딧불이
    {
        "id": "ch12-05",
        "chapter": "Chapter 12 (SOMNIUM) 05편",
        "title": "깊은 숲의 고목과 반딧불이",
        "words": ["glow (빛나다)", "spark (불꽃)", "moss (이끼)", "bark (나무껍질)", "fairy (요정)", "mystery (신비)", "quiet (고요한)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are an ancient mossy hollow tree stump with wild mushrooms sprouting along its bark, and three tiny luminous floating firefly orbs hovering near a leafy fern. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The organic twisting contours of the mossy old tree stump are drawn first with clean minimal pencil contours.

1.5-3.0s: the arching fern fronds and umbrella caps of the forest mushrooms form cleanly through sparse, elegant pencil line art.

3.0-4.5s: textured woodgrain ripples on the bark and three delicate circular firefly halo outlines appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as velvety olive-moss green on the bark, warm fawn-beige on the mushroom caps, and glowing chartreuse-gold on the floating firefly orbs. All surrounding space remains untouched pure white.

7.2-8.0s: one tiny firefly orb bobs gently upward by a couple of millimeters, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 19. ch12-06: 사막 오아시스와 야자수
    {
        "id": "ch12-06",
        "chapter": "Chapter 12 (SOMNIUM) 06편",
        "title": "사막 오아시스와 야자수",
        "words": ["oasis (오아시스)", "palm (야자수)", "desert (사막)", "shade (그늘)", "mirage (신기루)", "water (물)", "sand (모래)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are two slender curved date palm trees casting a graceful shade over a crystal-clear natural spring pool amidst undulating smooth sand dunes. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The sweeping arching trunks and feathery fronds of the palm trees are drawn first with clean minimal pencil contours.

1.5-3.0s: the kidney-shaped pool shoreline and the gentle crests of the desert dunes form cleanly through sparse, elegant pencil line art.

3.0-4.5s: palm bark segments, reed tufts at the water edge, and concentric pool ripples appear sequentially to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as warm champagne-sand on the dunes, vivid emerald-emerald on the palm canopy, and luminous turquoise-blue in the pool water. All surrounding space remains untouched pure white.

7.2-8.0s: a single palm frond sways with gentle grace in a warm desert breeze, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    },
    # 20. ch12-07: 보물상자와 황금 열쇠
    {
        "id": "ch12-07",
        "chapter": "Chapter 12 (SOMNIUM) 07편",
        "title": "보물상자와 황금 열쇠",
        "words": ["chest (상자)", "lock (자물쇠)", "key (열쇠)", "gold (금)", "jewel (보석)", "secret (비밀)", "hidden (숨겨진)"],
        "type": "사물·풍경형 (Template A)",
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. Static locked-off camera, one continuous 8-second take.

The only visible subjects throughout the sequence are a slightly ajar pirate treasure chest banded in carved iron straps, revealing a radiant gleam from within, and an ornate antique skeleton key tied with a golden silk tassel. There are no people, heavy rooms, 3D renders or drawing tools anywhere in the scene.

0-1.5s: ultra-fine pale warm-grey graphite lines appear progressively from the empty white field. The arched wooden dome lid and rectangular base of the chest are drawn first with clean minimal pencil contours.

1.5-3.0s: the keyhole escutcheon plate, the ornate skeleton key beside the chest, and iron corner brackets form cleanly through sparse, elegant pencil line art.

3.0-4.5s: heavy iron rivet studs, the filigree bow of the key, and faceted jewel silhouettes peek out to complete the pencil drawing. Every line is crisp, completely stable and unmoving.

4.5-7.2s: an extremely pale, water-heavy transparent watercolor wash develops gently. Pure white paper remains visible through every wash. Color blooms softly as weathered oak-brown on the chest planks, dark gunmetal on the iron bands, and dazzling pure honey-gold on the skeleton key and inner treasure glow. All surrounding space remains untouched pure white.

7.2-8.0s: a tiny spark of golden light glints gently on the tip of the key, while the surroundings remain peaceful, and the scene rests in complete stillness, surrounded by generous untouched white space.

Style: master-level fine-line editorial illustration, exceptionally sparse pale-graphite contours, soft silver-grey pencil lines, luminous transparent watercolor, restrained tonal contrast, generous untouched white space.

Audio: complete silence throughout. No music, no sound effects, no narration and no ambient sound.

Never: human figures, 3D render, photorealism, dark charcoal lines, black outlines, heavy graphite pressure, dark watercolor, dense color fills, camera movement, cuts."""
    }
]

html_content = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>20편 성공문법 프롬프트 작업 허브 — 보는 단어장</title>
  <style>
    :root {{
      --primary: #1e3a8a;
      --primary-hover: #1e40af;
      --accent: #3b82f6;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #0f172a;
      --subtext: #475569;
      --border: #e2e8f0;
      --badge-bg: #eff6ff;
      --badge-text: #1d4ed8;
      --success-bg: #dcfce7;
      --success-text: #15803d;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      padding-bottom: 100px;
      line-height: 1.6;
    }}
    header {{
      background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
      color: #fff;
      padding: 40px 20px;
      text-align: center;
      box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }}
    header h1 {{
      margin: 0 0 10px;
      font-size: 28px;
      letter-spacing: -0.02em;
    }}
    header p {{
      margin: 0;
      opacity: 0.9;
      font-size: 15px;
    }}
    .notice-box {{
      max-width: 900px;
      margin: 20px auto 0;
      background: rgba(255,255,255,0.1);
      border: 1px solid rgba(255,255,255,0.2);
      border-radius: 12px;
      padding: 16px 20px;
      text-align: left;
      font-size: 14px;
    }}
    .notice-box h3 {{
      margin: 0 0 8px;
      color: #93c5fd;
      font-size: 15px;
    }}
    .notice-box ul {{
      margin: 0;
      padding-left: 20px;
    }}
    .nav-bar {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255,255,255,0.95);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border);
      padding: 12px 20px;
      display: flex;
      gap: 10px;
      justify-content: center;
      flex-wrap: wrap;
    }}
    .nav-bar a {{
      text-decoration: none;
      background: #eff6ff;
      color: var(--primary);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 700;
      transition: all 0.2s;
    }}
    .nav-bar a:hover {{
      background: var(--primary);
      color: #fff;
    }}
    main {{
      max-width: 1000px;
      margin: 30px auto 0;
      padding: 0 20px;
    }}
    .scene-grid {{
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}
    .card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    }}
    .card-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .card-title-group {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .card-chapter {{
      font-size: 12px;
      font-weight: 700;
      color: var(--accent);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .card-title {{
      margin: 0;
      font-size: 20px;
      font-weight: 700;
      color: var(--text);
    }}
    .badge {{
      display: inline-block;
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      background: var(--badge-bg);
      color: var(--badge-text);
    }}
    .words-box {{
      background: #f1f5f9;
      border-radius: 8px;
      padding: 10px 14px;
      font-size: 13px;
      color: #334155;
      margin-bottom: 16px;
    }}
    .words-box strong {{
      color: #0f172a;
    }}
    .prompt-container {{
      position: relative;
      background: #0f172a;
      border-radius: 10px;
      padding: 18px 18px 48px;
      margin-bottom: 12px;
    }}
    .prompt-text {{
      color: #f8fafc;
      font-family: "SF Mono", Menlo, Consolas, Monaco, monospace;
      font-size: 13px;
      line-height: 1.6;
      white-space: pre-wrap;
      word-break: break-word;
      margin: 0;
    }}
    .copy-btn {{
      position: absolute;
      right: 14px;
      bottom: 12px;
      background: #2563eb;
      color: #fff;
      border: none;
      border-radius: 6px;
      padding: 8px 18px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: background 0.2s, transform 0.1s;
    }}
    .copy-btn:hover {{
      background: #1d4ed8;
    }}
    .copy-btn:active {{
      transform: scale(0.96);
    }}
    .copy-btn.copied {{
      background: #16a34a;
    }}
    .footer-summary {{
      text-align: center;
      margin-top: 40px;
      padding: 20px;
      color: var(--subtext);
      font-size: 14px;
    }}
  </style>
</head>
<body>

<header>
  <h1>🎬 20편 성공문법 프롬프트 작업 허브</h1>
  <p>보는 단어장 (inkword.site) · 정본 헌법 (Line-reveal 마스터 2026-08-20) 100% 준수</p>
  <div class="notice-box">
    <h3>💡 대표님 작업 가이드</h3>
    <ul>
      <li><strong>원클릭 복사:</strong> 각 카드 우측 하단의 [프롬프트 복사] 버튼을 누르면 Veo / Vidu / Flow 입력창에 바로 붙여넣기할 수 있습니다.</li>
      <li><strong>영상 생성 규격:</strong> 16:9 비율 · 8초 (8 seconds) · 순백 배경(Pure White) · 드로잉 후 투명 수채화 번짐.</li>
      <li><strong>철만이 병행 작업:</strong> 틈틈이 1편씩 뽑아 <code>_작업/신작영상/</code> 폴더에 저장해 주시면 코다리가 탑재합니다.</li>
    </ul>
  </div>
</header>

<nav class="nav-bar">
  <a href="#ch4-04">ch4 서재</a>
  <a href="#ch4-05">ch4 도서관</a>
  <a href="#ch4-06">ch4 인쇄소</a>
  <a href="#ch5-06">ch5 피아노</a>
  <a href="#ch5-07">ch5 연극</a>
  <a href="#ch7-05">ch7 뜨개질</a>
  <a href="#ch7-06">ch7 정원</a>
  <a href="#ch7-07">ch7 러닝</a>
  <a href="#ch8-05">ch8 기차역</a>
  <a href="#ch8-06">ch8 항구</a>
  <a href="#ch8-07">ch8 우체통</a>
  <a href="#ch9-02">ch9 법정</a>
  <a href="#ch9-03">ch9 성벽</a>
  <a href="#ch9-04">ch9 분수대</a>
  <a href="#ch11-04">ch11 실험실</a>
  <a href="#ch11-05">ch11 시계공방</a>
  <a href="#ch11-06">ch11 전구회로</a>
  <a href="#ch12-05">ch12 고목</a>
  <a href="#ch12-06">ch12 오아시스</a>
  <a href="#ch12-07">ch12 보물상자</a>
</nav>

<main>
  <div class="scene-grid">
"""

for idx, s in enumerate(scenes):
    pid = f"p-{s['id']}"
    words_str = " · ".join(s["words"])
    escaped_prompt = html.escape(s["prompt"])
    html_content += f"""
    <div class="card" id="{s['id']}">
      <div class="card-header">
        <div class="card-title-group">
          <span class="card-chapter">{s['chapter']}</span>
          <h2 class="card-title">#{idx+1:02d}. {s['title']}</h2>
        </div>
        <span class="badge">{s['type']}</span>
      </div>
      <div class="words-box">
        <strong>배정 단어:</strong> {words_str}
      </div>
      <div class="prompt-container">
        <pre class="prompt-text" id="{pid}">{escaped_prompt}</pre>
        <button class="copy-btn" onclick="copyPrompt('{pid}', this)">📋 프롬프트 복사</button>
      </div>
    </div>
"""

html_content += """
  </div>
  <div class="footer-summary">
    총 20편 프롬프트 정밀 조립 완료 · 코다리 총괄부장 발행 (2026-08-21)
  </div>
</main>

<script>
function copyPrompt(id, btn) {
  const text = document.getElementById(id).innerText;
  navigator.clipboard.writeText(text).then(() => {
    const originalText = btn.innerHTML;
    btn.innerHTML = '✅ 복사 완료!';
    btn.classList.add('copied');
    setTimeout(() => {
      btn.innerHTML = originalText;
      btn.classList.remove('copied');
    }, 1800);
  });
}
</script>

</body>
</html>
"""

with open("_작업/프롬프트허브_20편_20260821.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ _작업/프롬프트허브_20편_20260821.html 생성 완료! (총 {len(scenes)}편)")
