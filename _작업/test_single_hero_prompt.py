# -*- coding: utf-8 -*-
"""
'제품 카탈로그 나열' -> '하나의 이야기(Storybook Scene)'로 전환
왜 꽉 차고 실사처럼 나왔는가?
1. 좌/우/중앙에 소품을 4~5개 나열(주전자+받침대+틴케이스+머그잔2개)하라고 하니 -> AI가 가로로 꽉 찬 '쇼핑몰 제품 진열 사진(Product Photography)'을 찍음!
2. 'High-key lighting', 'locked-off camera', 금속/법랑 묘사가 합쳐져 스튜디오 조명 아래의 3D 실사 렌더링으로 굳음!

해결책:
1. 소품 나열 금지: 좌우 끝에 물건 채우라는 문구(in each outer third) 완전 삭제!
2. 중앙 1개 메인 오브젝트(Hero Scene) 집중: 그림책 삽화처럼 하나의 응집된 장면만 콤팩트하게 그림.
3. 2D 손그림 펜화(Hand-drawn pen & watercolor illustration) 명시, 스튜디오 조명/제품 사진 톤 원천 제거.
"""

sample_prompt = """Delicate 2D storybook line-reveal animation on an empty pure white background (#FFFFFF). The very first frame is an entirely empty white field. A charming, compact hand-drawn storybook illustration resting at the center with wide, generous untouched white space all around. The subject is one single cozy camping tea scene: a small whistling kettle resting over a warm little flame on a single light baseline, with one ceramic cup beside it. 0-4s: light, delicate graphite pen outlines draw themselves progressively from the white field. Every line is a clean, thin, soft single-stroke contour. Strictly zero cross-hatching, zero shading, zero dark ink masses. The interiors remain completely empty and unshaded. 4-8s: extremely pale, transparent pastel watercolor washes fill gently inside the contours. A whisper of soft pastel blue on the kettle, faint warm beige on the cup, and a tiny translucent coral flame. Strictly zero watercolor wash on the background; the vast surrounding space remains 100% untouched pure white #FFFFFF. A tiny wisp of pale steam curls softly from the kettle spout. All lines remain stable. Style: timeless children's storybook hand-drawn illustration, delicate light graphite lines, luminous transparent watercolor, pure 2D flat artwork, strictly zero photorealism, zero 3D CGI, generous untouched white space."""

print("샘플 프롬프트 생성 완료!")
