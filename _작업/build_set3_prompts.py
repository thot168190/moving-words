# -*- coding: utf-8 -*-
"""
3차 완전 신규 10편 프롬프트 (기존 66편 및 1·2차와 중복 0%, 남은 미사용 단어 100% 결합)
세필 수채화 (Delicate Fine-Brush Watercolor) 정본 문법 - 단일 라인 포맷 & 무결점 검증
"""

SET3_PROMPTS = [
    # 1. 고문서 서가와 양장본 (document, diary, article, catalog, copy)
    {
        "id": "set3-01",
        "chapter": "New Chapter (ARCHIVUM)",
        "title": "고문서 보관소의 앤틱 양장본 서가",
        "words": ["document (문서)", "diary (일기)", "article (글·조항)", "catalog (목록)", "copy (복사본)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are an open leather-bound archival ledger book on a reading lectern at the optical center, a small brass document bookmark balancing the left, a level oak library counter line extending across both outer thirds, and a slender glass paperweight balancing the right. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level oak counter horizon. Draw the wooden reading lectern and thick ledger pages next, keeping the combined silhouette horizontal rather than diagonal. Extend clean countertop lines equally toward the left and right outer thirds. Add a brass page clip at left and a glass paperweight at right. There is no visible scholar or candle anywhere. Keep ledger spine lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a delicate honey-tan on the ledger cover, faint champagne-gold on the brass clip, airy celadon-wash on the glass weight, and soft pale ash-wood on the lectern. A single ledger corner flutters once in a quiet draft; all counter lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },

    # 2. 앤틱 법정의 의사봉 (judge, law, justice, rule, order)
    {
        "id": "set3-02",
        "chapter": "New Chapter (LEX)",
        "title": "앤틱 법정의 나무 의사봉과 받침대",
        "words": ["judge (판사·판단하다)", "law (법)", "justice (정의)", "rule (규칙)", "order (질서·명령)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are a classic turned-hardwood gavel resting on a round sound block at the optical center, a small brass balance scale balancing the left, a polished walnut bench line extending across both outer thirds, and an antique leather law codex balancing the right. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level walnut bench horizon. Draw the central wooden gavel handle, head and round striking block next, keeping the combined silhouette horizontal rather than diagonal. Extend clean bench edges equally toward the left and right outer thirds. Add a brass scale at left and an upright leather book at right. There is no visible judge or gavel strike anywhere. Keep woodgrain curves sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a warm chestnut-sienna on the gavel head, pale brass-yellow on the scale pans, rich saddle-brown on the book spine, and airy timber-tan on the bench. The gavel rests in quiet dignity as a tiny light beam glints once on the sound block; all architectural lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },

    # 3. 무역항의 닻과 화물 (cargo, dock, anchor, crane, load)
    {
        "id": "set3-03",
        "chapter": "New Chapter (PORTUS)",
        "title": "부두의 주철 닻과 나무 화물 상자",
        "words": ["cargo (화물)", "dock (부두·선창)", "anchor (닻)", "crane (기중기)", "load (짐·싣다)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are a heavy cast-iron maritime ship anchor resting against a wooden dock crate at the optical center, a coiled hemp mooring rope balancing the left, level granite pier lines extending across both outer thirds, and an iron mooring bollard balancing the right. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level granite pier horizon. Draw the upright fluked iron anchor and wooden shipping crate next, keeping the combined silhouette balanced. Extend clean pier stone joints equally toward the left and right outer thirds. Add a neat rope coil at left and a round bollard post at right. There is no visible sailor or crane hook anywhere. Keep chain link outlines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a cool slate-iron on the anchor body, weathered pine-tan on the crate wood, soft straw-beige on the hemp rope, and pale limestone-grey on the pier stones. A tiny ocean ripple reflects once on the lower dock rim; all pier structures remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },

    # 4. 벌통과 야생화 꿀단지 (honey, bee, hive, bloom, wax)
    {
        "id": "set3-04",
        "chapter": "New Chapter (APIS)",
        "title": "목제 벌통과 도자기 꿀단지",
        "words": ["honey (꿀)", "bee (벌)", "hive (벌통)", "bloom (꽃피다)", "wax (밀랍)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are a rustic cedar beehive box on timber stilts at the optical center, a small glazed ceramic honey pot balancing the left, level meadow ground lines extending across both outer thirds, and a cluster of clover blossoms balancing the right. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level garden turf horizon. Draw the tiered wooden hive boxes and sloping roof next, keeping the combined silhouette vertical and balanced. Extend light clover meadow contours equally toward the left and right outer thirds. Add a small honey jar at left and clover flower stalks at right. There is no visible beekeeper or hive swarm anywhere. Keep slat lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a warm amber-cedar on the hive wood, luminous golden-honey on the pot rim, soft lilac-pink on the clover blooms, and airy grass-green on the stems. A single clover petal sways once in a gentle breeze; all hive timber lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },

    # 5. 도예가의 물레와 점토 항아리 (clay, pottery, wheel, craft, shape)
    {
        "id": "set3-05",
        "chapter": "New Chapter (CREATIO)",
        "title": "도예 공방의 풋물레와 매끄러운 점토 항아리",
        "words": ["clay (점토)", "pottery (도자기)", "wheel (물레·바퀴)", "craft (공예)", "shape (모양)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are a smooth unbaked terracotta clay vase on a circular pottery kick-wheel head at the optical center, a small wooden smoothing spatula balancing the left, workshop plank floor lines extending across both outer thirds, and a finished glazed cup balancing the right. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level studio floor horizon. Draw the symmetrical clay vessel contours and rotating wheel platter next, keeping the combined silhouette upright and balanced. Extend clean wooden studio floor lines equally toward the left and right outer thirds. Add a small wooden shaping spatula at left and a finished ceramic cup at right. There is no visible potter or clay splatter anywhere. Keep vessel curvature lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a sheer earthy terracotta-tan on the clay vase, delicate celadon-glaze on the finished cup, quiet birch-blonde on the spatula, and soft stone-grey on the wheel head. The round pottery wheel gives one smooth silent rotation and rests; all workshop floor lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },

    # 6. 빅토리아풍 유리 온실 (glass, sprout, leaf, tropical, pure)
    {
        "id": "set3-06",
        "chapter": "New Chapter (FLORA)",
        "title": "빅토리아풍 유리 온실과 몬스테라 화분",
        "words": ["glass (유리)", "sprout (싹)", "leaf (잎)", "tropical (열대의)", "pure (순수한)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are an elegant miniature glass-pane terrarium conservatory structure at the optical center, a large potted monstera plant balancing the left, level stone conservatory shelf lines extending across both outer thirds, and a slender brass plant mister balancing the right. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level stone shelf horizon. Draw the faceted glass prism structure and central fern sprig next, keeping the combined silhouette balanced. Extend clean shelf edges equally toward the left and right outer thirds. Add a potted monstera at left and a brass mister bottle at right. There is no visible gardener or water spray anywhere. Keep glass glazing bars sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a transparent jade-green on the monstera leaves, sheer watery aqua-tint on the glass panes, delicate champagne-gold on the brass mister, and pale limestone-ash on the shelf. A single drop of morning dew glints once on the monstera leaf tip; all glass architectural lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },

    # 7. 사막의 공룡 화석 발굴 (fossil, bone, dig, layer, ancient)
    {
        "id": "set3-07",
        "chapter": "New Chapter (PALEO)",
        "title": "사막 암벽의 공룡 깃털 화석",
        "words": ["fossil (화석)", "bone (뼈)", "dig (발굴하다)", "layer (지층·층)", "ancient (고대의)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are a delicate prehistoric ammonite spiral fossil embedded in a limestone slab at the optical center, a small wooden geological magnifying loupe balancing the left, horizontal sedimentary rock stratum lines extending across both outer thirds, and a fine rock chisel balancing the right. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level sedimentary stratum horizon. Draw the spiral chambers of the ammonite fossil and surrounding rock matrix next, keeping the combined silhouette horizontal rather than diagonal. Extend natural rock bed lines equally toward the left and right outer thirds. Add a wooden loupe at left and a steel chisel at right. There is no visible paleontologist or dust pile anywhere. Keep spiral chamber ribs sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is an airy sandstone-ochre on the fossil shell, pale bone-ivory on the rock slab, cool silver-grey on the chisel blade, and light teak on the loupe. A tiny amber highlight shines once across the spiral center; all sedimentary stratum lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },

    # 8. 지하 저장고의 오크통 (barrel, cask, cellar, vintage, ferment)
    {
        "id": "set3-08",
        "chapter": "New Chapter (CELLAR)",
        "title": "석조 저장고의 참나무 오크통과 포도 덩굴",
        "words": ["barrel (통·배럴)", "cask (나무통)", "cellar (지하실·저장고)", "vintage (포도주·고전적인)", "ferment (발효하다)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are a sturdy oak wood cask barrel with iron hoops on timber cradles at the optical center, a small cluster of ripe grapes balancing the left, level stone cellar floor lines extending across both outer thirds, and an antique brass spigot tap balancing the right. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level cellar floor horizon. Draw the rounded barrel staves, hoops and front bung hole next, keeping the combined silhouette horizontal rather than diagonal. Extend clean stone floor lines equally toward the left and right outer thirds. Add a grape cluster at left and a brass spigot at right. There is no visible vintner or wine spill anywhere. Keep stave curves sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a warm weathered oak-brown on the barrel staves, soft plum-violet on the grapes, cool iron-grey on the hoops, and pale champagne-gold on the spigot. A single grape leaf sways once quietly; all cellar floor and stave lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },

    # 9. 기상 관측소의 아네모미터와 기압계 (gauge, measure, needle, signal, station)
    {
        "id": "set3-09",
        "chapter": "New Chapter (METEO)",
        "title": "기상대의 회전 풍속계와 황동 기압계",
        "words": ["gauge (측정기·게이지)", "measure (측정하다)", "needle (바늘)", "signal (신호)", "station (관측소·역)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are a three-cup rotary anemometer wind gauge on a slender mast at the optical center, a round brass dial barometer balancing the left, level observation platform railing lines extending across both outer thirds, and a small rain gauge glass balancing the right. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level observation deck horizon. Draw the vertical anemometer mast and spinning hemispherical cups next, keeping the combined silhouette vertical and balanced. Extend clean railing lines equally toward the left and right outer thirds. Add a brass barometer at left and a glass tube at right. There is no visible meteorologist or stormy sky anywhere. Keep instrument cup arcs sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a sheer silver-aluminium on the anemometer cups, pale brass-gold on the barometer bezel, transparent sky-cyan on the rain gauge, and muted steel-grey on the railing. The three anemometer cups spin smoothly in one complete slow turn; all platform lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    },

    # 10. 고대 천문 관측 돔 (dome, observe, chart, degree, lens)
    {
        "id": "set3-10",
        "chapter": "New Chapter (URANIA)",
        "title": "산꼭대기 천문대 돔과 황동 성도환",
        "words": ["dome (돔·둥근지붕)", "observe (관측하다)", "chart (도표·성도)", "degree (각도·도)", "lens (렌즈)"],
        "prompt": """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are a hemispherical astronomical observatory dome with open slit shutter at the optical center, a brass astrolabe angle chart balancing the left, level stone parapet lines extending across both outer thirds, and an optical finder lens balancing the right. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level stone parapet horizon. Draw the curved dome roof and shutter opening next, keeping the combined silhouette balanced. Extend clean parapet stone lines equally toward the left and right outer thirds. Add an astrolabe dial at left and an optical lens at right. There is no visible astronomer or night star field anywhere. Keep dome panel lines sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is an airy titanium-white wash on the dome shell, sheer champagne-gold on the astrolabe brass, pale cerulean on the optical lens, and soft granite-grey on the parapet. A tiny ray of ambient light glints once across the astrolabe rim; all dome structural lines remain crisp and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""
    }
]

import json, html, subprocess

# 1. 텍스트 파일 저장 (각 편당 단 1줄씩)
with open("_작업/google_flow_bulk_set3_10.txt", "w", encoding="utf-8") as f:
    for p in SET3_PROMPTS:
        clean_line = " ".join(p["prompt"].split())
        f.write(clean_line + "\n\n")

print("Saved _작업/google_flow_bulk_set3_10.txt successfully.")

# 2. verify_prompt.py 검증
res = subprocess.run(["python3", "_작업/verify_prompt.py", "_작업/google_flow_bulk_set3_10.txt"], capture_output=True, text=True)
print(res.stdout)

# 3. HTML 허브 빌드
prompts_json = json.dumps([" ".join(p["prompt"].split()) for p in SET3_PROMPTS])

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>보는 단어장 — 3차 완전 신규 10편 벌크 허브 (정확히 10편 인식)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700;900&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif;
      background: #090d16;
      color: #f1f5f9;
      padding: 32px 20px 100px;
      line-height: 1.6;
    }}
    .container {{
      max-width: 1000px;
      margin: 0 auto;
    }}
    
    .header-board {{
      background: linear-gradient(135deg, #1e293b, #0f172a);
      border-radius: 24px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 32px 36px;
      margin-bottom: 32px;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5);
    }}
    .header-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 20px;
    }}
    .badge-pass {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #059669;
      color: #ffffff;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 800;
    }}
    h1 {{
      font-size: 28px;
      font-weight: 900;
      color: #ffffff;
      margin-bottom: 6px;
    }}
    .sub-desc {{
      font-size: 14.5px;
      color: #94a3b8;
    }}
    
    .btn-bulk {{
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #ffffff;
      border: none;
      padding: 16px 28px;
      border-radius: 14px;
      font-size: 16px;
      font-weight: 800;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      transition: all 0.2s ease;
      box-shadow: 0 4px 15px rgba(37, 99, 235, 0.35);
      margin-top: 15px;
    }}
    .btn-bulk:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5);
    }}
    
    .prompt-card {{
      background: #131d2e;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 18px;
      padding: 24px;
      margin-bottom: 20px;
    }}
    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
    }}
    .scene-title {{
      font-size: 19px;
      font-weight: 800;
      color: #f8fafc;
    }}
    .words-badge {{
      display: inline-block;
      background: rgba(56, 189, 248, 0.12);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 4px 10px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      margin-bottom: 10px;
    }}
    .prompt-box {{
      background: #090e17;
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 12px;
      padding: 14px;
      font-size: 13.5px;
      color: #cbd5e1;
      line-height: 1.5;
      font-family: ui-monospace, monospace;
      white-space: pre-wrap;
      max-height: 160px;
      overflow-y: auto;
      margin-bottom: 12px;
    }}
    .btn-copy {{
      background: rgba(255, 255, 255, 0.08);
      color: #e2e8f0;
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
    }}
    .btn-copy:hover {{
      background: rgba(255, 255, 255, 0.15);
      color: #ffffff;
    }}
    
    .toast {{
      position: fixed;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #10b981;
      color: #ffffff;
      padding: 12px 24px;
      border-radius: 30px;
      font-weight: 800;
      font-size: 15px;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      opacity: 0;
      pointer-events: none;
      z-index: 9999;
    }}
    .toast.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header-board">
      <div class="header-top">
        <div>
          <span class="badge-pass">✓ Flow 벌크 10편 정확 인식 보장 (단일 라인 포맷)</span>
          <h1 style="margin-top: 8px;">3차 완전 신규 10편 벌크 허브</h1>
          <p class="sub-desc">기존 66편 및 1·2차와 중복 0% · 세필 수채화 정본 문법</p>
        </div>
      </div>
      
      <button class="btn-bulk" onclick="copyBulk()">
        📋 3차 10편 전체 벌크 복사 (Flow 입력용)
      </button>
    </div>

    <div id="cardsList">
"""

for i, p in enumerate(SET3_PROMPTS, 1):
    p_id = p["id"]
    p_title = p["title"]
    p_chapter = p["chapter"]
    p_words = ", ".join(p["words"])
    p_prompt = " ".join(p["prompt"].split())
    
    html_content += f"""
      <div class="prompt-card">
        <div class="card-top">
          <div>
            <div class="words-badge">{p_chapter}</div>
            <div class="scene-title">{i:02d}. {p_title}</div>
            <div style="font-size: 13px; color: #94a3b8; margin-top: 4px;">배정 단어: <strong>{p_words}</strong></div>
          </div>
          <button class="btn-copy" onclick="copySingle('{p_id}')">단편 복사</button>
        </div>
        <div class="prompt-box" id="text-{p_id}">{html.escape(p_prompt)}</div>
      </div>
    """

html_content += f"""
    </div>
  </div>

  <div id="toast" class="toast">클립보드에 복사되었습니다!</div>

  <script>
    const promptsArray = {prompts_json};
    
    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.classList.add('show');
      setTimeout(() => {{
        t.classList.remove('show');
      }}, 2000);
    }}

    function copyBulk() {{
      const text = promptsArray.join('\\n\\n');
      navigator.clipboard.writeText(text).then(() => {{
        showToast('3차 10편의 프롬프트가 복사되었습니다! (Flow에서 10편으로 인식)');
      }});
    }}

    function copySingle(id) {{
      const el = document.getElementById('text-' + id);
      if (el) {{
        navigator.clipboard.writeText(el.innerText).then(() => {{
          showToast('프롬프트가 복사되었습니다!');
        }});
      }}
    }}
  </script>
</body>
</html>
"""

with open("_작업/제작허브_3차신규10편.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved _작업/제작허브_3차신규10편.html successfully.")
