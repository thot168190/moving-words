# -*- coding: utf-8 -*-
with open("public/learning/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. 초기 렌더링 시 단어가 화면에 미리 떠있지 않도록 visible 클래스 제거
# (영상이 다 그려진 후 onended 또는 재생 4초 이후에만 등장하도록)
html = html.replace('class="scene-word visible ${lengthClass}"', 'class="scene-word ${lengthClass}"')

with open("public/learning/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("단어 초기 노출 방지(그려짐의 법칙 준수) 패치 완료!")

# 2. 이제 20편에 대해 엉터리 뜻(achieve -> 사각형 등)을 100% 제거하고,
# 실제 1200 정본 단어와 진짜 사전 뜻으로 주입!

