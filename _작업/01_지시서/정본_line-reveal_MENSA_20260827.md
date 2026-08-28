# 🔒 정본 골격 — line-reveal (MENSA 계열, 2026-08-27 확인)

> 대표님이 실제 제작에 쓰시는 골격. `최종합격_단일사물_세필수채_공식_잠금_20260825.md`(세필수채 계열)와 **다른 계열**이며,
> 새 그림은 **이 골격**을 쓴다. 한 글자도 임의 변경하지 않는다. 슬롯 `{}` 만 채운다.

## 블록 구성

```text
[1] 오프닝 (배경·조명·구도·카메라)
Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty pure white field. The background is one single continuous field of pure white reaching every edge of the frame. The subjects sit directly on that white with nothing underneath them: no sheet, board, panel, card, mat, textured surface, visible edge or border. High-key lighting. The centered illustration occupies the central three-quarters of the frame with equal narrow white margins on both sides. Static locked-off camera, one continuous 8-second take.

[2] 사물 한정
The only visible subjects are {subjects}. These are the only objects present. No people, hands, animals, signs or drawing tools appear.

[3] 0-4s 선이 그려짐
0-4s: soft pale silver-grey graphite strokes appear progressively from the empty white field, each stroke drawn with natural hand variation—firmer where it begins and fading slightly, nothing measured, vectorized or stamped. The illustration draws itself. Each pale silver-grey graphite line appears progressively from its own endpoint, one complete line at a time. The lines themselves extend gradually across the empty field; no object, tool, tip, hand or instrument is ever visible. Nothing appears through a wipe, fade or dissolve. {draw_order} Use only a few economical contour lines for every object. Leave most interiors as untouched white space. No dense texture, no heavy shading and no realistic surface rendering.

[4] 4-7s 아주 옅은 수채
4-7s: an extremely pale, transparent watercolor wash develops gently inside the drawn contours. {color_steps} White remains clearly visible through every wash. No dark, dense or fully filled areas. No color spreads behind the objects. The illustration remains airy, quiet and clearly hand-drawn.

[5] 7-8s 미세 동작 1회
7-8s: {motion} All subjects remain 100% fully visible, crisp, opaque and completely still. No object fades, dissolves, disappears, morphs or changes position.

[6] 마무리 확인문
The finished composition still contains every subject listed above and nothing more, all lines crisp and completely stable, resting inside generous untouched white space. The finished image reads immediately as {reading}.

[7] 화풍
Style: delicate fine-line editorial illustration, exceptionally thin pale silver-grey graphite contours, sparse selective detail, luminous transparent watercolor, low saturation, restrained tonal contrast, generous untouched white space, mature and understated, illustrated rather than realistic, never photorealistic and never a children's cartoon.

[8] 무음
Audio: absolutely no audio of any kind. The output is completely silent with an empty audio track. No music, score, instruments, melody, ambient tone, sound effects, foley, narration, voice or background hum.

[9] 금지 목록
Never: hex codes, color codes, #FFFFFF, printed text, cabinet marks, fading out, opacity loss, ghosting, disappearing objects, vanishing objects, text, letters, numbers, labels, arrows, diagrams, human figures, hands, pens, pencils, brushes, drawing tools, picture frames, split screens, sheets, paper texture, visible paper grain, panels, mats, borders, background rectangles, photorealistic rendering, realistic still-life photography, CGI, 3D render, glossy surfaces, dense hatching, cross-hatching, engraving, black ink masses, heavy outlines, grey-dominant mood, sumi-e, dark watercolor, saturated colors, pink, yellow or orange background wash, paint blooms behind the objects, fully painted surfaces, paint splatter, camera movement, cuts, fade-in, dissolve, music, sound effects, or any subject disappearing.
```

## 이 골격이 이미 해결해 둔 것

| 증상 | 골격 안의 해법 |
| :--- | :--- |
| 그림에 `#FFFFFF` 글자가 인쇄됨 | [1]에서 색상코드를 쓰지 않고, [9] 맨 앞에 `hex codes, color codes, #FFFFFF, printed text` 를 둔다 |
| 사물이 화면을 꽉 채움 | [1] `occupies the central three-quarters of the frame with equal narrow white margins on both sides` |
| 선이 안 그려지고 스르륵 나타남 | [3] `Each line appears progressively from its own endpoint, one complete line at a time` · `Nothing appears through a wipe, fade or dissolve` |
| 색이 진함 | [3] `Leave most interiors as untouched white space` · [4] `extremely pale` · `No dark, dense or fully filled areas` |
| 손·도구가 나옴 | [2] `No people, hands, animals, signs or drawing tools appear` · [3] `no object, tool, tip, hand or instrument is ever visible` |

## 슬롯에 넣지 말 것

`numbered` · `dial face` · `ledger` · `menu` · `recipe` · `receipt` · `newspaper` · `type block` · `ruled` · `plaque` · `postage stamp` — **글자·숫자를 그리라는 신호**가 되어 [9] 금지와 충돌하고, 모델이 대신 다른 글자를 그려 넣는다.

---

# 🔒 정본 골격 — 인물 등장 장면 (pencil-and-ink 계열)

> 사람이 나오는 장면은 **위 MENSA 골격을 쓰지 않는다.** MENSA는 `Never:`에 `human figures, hands`가 있어 사람을 막는다.
> 인물 장면은 아래 골격을 쓴다. `_작업/벌크입력/벌크_01_013-027.txt` 등에서 실제로 검증된 것.

## 인물 규정 — 반드시 넣는다

```text
All people in the scene are Korean - natural Korean children and Korean adults.
```

또는

```text
Every person in the scene is Korean, with natural Korean facial features, drawn in the same delicate pencil-and-watercolor style as everything else - never photographic, never realistic.
```

**이 문장을 빼면 인도 사람·흑인이 나온다.** 학습 데이터가 옥스퍼드 계열 삽화로 치우쳐 있기 때문이다.
우리 상품은 한국 아이들 대상이므로 반드시 명시한다.

## 골격

```text
[1] Cinematic progressive pencil-and-ink line animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty white field. The illustration draws itself - no artist, no hand, no pen or tool ever appears in the frame at any moment. Static locked-off camera, one continuous 8-second take.

[2] The subjects: {subjects}. All people in the scene are Korean - natural Korean children and Korean adults.

[3] 0-3.5s: delicate light-graphite pencil strokes are traced visibly from endpoint to endpoint — soft, feather-light, barely pressed, like an artist's first gentle sketch, each line drawn once. No dense cross-hatching, no engraving-style shading; only airy contour lines. {draw_order} The composition is asymmetric — the main subject sits off-center. Built progressively, never fading in.

[4] 3.5-5.5s: pale watercolor tints rise FROM INSIDE the pencil lines, within the lines — {color_steps}, each heavily diluted with water. The larger the area, the lighter and more watery its wash. Color blooms ONLY onto the drawn subjects — all surrounding space stays pure untouched white. The delicate pencil drawing remains the protagonist; color is only a light stain resting on the lines. Generous areas of the paper stay untouched white, with generous white margins breathing on at least three sides of the image. The white background stays pure white.

[5] 5.5-8s: {motion} Everything else stays perfectly still.

[6] Style: delicate pencil-and-ink drawing with airy line weight and sparse, selective detail - generous untouched paper inside the forms, fresh luminous watercolor, clear daylight, the feel of a beautiful illustrated atlas for curious teenagers, never a kindergarten picture book. Museum-quality contemporary illustration.

[7] Never: text, letters, numbers, hashtags, watermarks, a visible drawing hand, pen, pencil or brush in frame, round cartoon faces, big glossy eyes, photorealistic faces, realistic human skin, primary crayon colors, muted grey or slate mood, sepia, ink-wash painting mood, fog, smiling sun, V-shaped birds, rainbows, dense cross-hatching, engraving-style shading, heavy dark outlines, dead-center composition, paint splatter, color outside the lines, paper texture, visible paper grain, window light streaks, ambient room shadows, vignette, camera movement, cuts, dissolve.
```

## 두 골격 고르는 법

| 장면 | 쓰는 골격 |
| :--- | :--- |
| 사물만 나온다 (도구·그릇·건물·탈것) | **MENSA line-reveal** |
| 사람이 나온다 (직원·손님·군중·가족·경찰·군인) | **pencil-and-ink 인물** + `All people ... are Korean` |

## 글자가 필요한 사물

우표·가격표·표·서류처럼 **글자가 있어야 뜻이 통하는 사물**은 인물 골격의 `Never:`에서 `text, letters, numbers` 를 뺀다.
빼지 않으면 모델이 글자를 못 쓰고 대신 엉뚱한 문자열(색상코드 등)을 그려 넣는다.

---

# 🔒 인물 화풍 표준 — 「머그잔 계열」 (대표님 확정 2026-08-27)

> 기준 그림: `ch7_03 머그잔과 휴식`. 대표님이 **"가능하면 이런 계열이면 좋겠어"** 라고 지정하셨다.
> 사람이 나오는 모든 새 그림은 이 화풍을 따른다.

## 그림에서 읽어낸 규격

| 요소 | 규격 | 프롬프트 문장 |
| :--- | :--- | :--- |
| 선 | 아주 가는 회색 연필선, 손 떨림이 살아 있음 | `extremely fine soft grey pencil contour lines ... with the gentle wobble of a human hand` |
| 얼굴 | 눈 두 획, 입 한 획, 볼 홍조만 | `two short curved eyes, one small curved mouth, and one soft pink blush on each cheek` |
| 피부 | **칠하지 않는다.** 흰 종이 그대로 | `skin, hands and necks are left as completely unpainted white paper with no skin tone of any kind` |
| 머리 | 검게만 칠한다 | `short straight black hair` · 금지에 `blond hair, brown hair, curly hair` |
| 옷 | 아주 옅은 한 색 | `pale butter-yellow` `pale sage-mint` |
| 배경 | 수채 얼룩 하나만, 선 밖으로 조금 번짐 | `one single soft yellow watercolor bloom resting loosely behind ..., spilling a little past the drawn lines` |
| 나머지 | 전부 흰 여백 | `Nothing else is painted.` `Generous white margins breathe on all four sides.` |

## 인종 사고를 막는 두 겹 장치

```text
[겹1 · 명시]  Every person is a Korean child with short straight black hair.
[겹2 · 금지]  Never: ... painted skin tone, dark skin, curly hair, blond hair, brown hair, western facial features, ...
```

**피부를 칠하는 순간 인종이 생긴다.** 그래서 아예 칠하지 않는 것이 가장 확실하다.
`ch7_04 알람시계`는 머리를 금색으로 칠해서 서양 사람이 됐고, `ch5_03 범퍼카`는 피부를 칠해서 흑인 아이가 나왔다.

## 사람 수 제한

```text
Never: ... more than two children, ...
```

**셋 이상이면 섞여 나온다.** `ch5_05 경품 부스`는 아이 다섯이 전부 서양 아이로 나왔다.
군중이 꼭 필요하면 **뒷모습이나 실루엣**으로 처리한다.

## 이미 나간 것 중 고쳐야 할 편

| 편 | 문제 |
| :--- | :--- |
| `ch5_03` 범퍼카 | 왼쪽 아이가 흑인 · 그림만 유독 어두움 → **재제작 확정** |
| `ch5_05` 경품 부스 | 아이 다섯 전부 서양 아이 |
| `ch7_04` 알람시계 | 금발 여성 |
| `ch8_04` 근위병 | 영국 근위병 (소재 자체가 서양) |
