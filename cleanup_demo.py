import re

with open('public/demo.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Font replacement
html = re.sub(r'<link href="https://fonts.googleapis.com/css2[^>]+>', '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">', html)
html = re.sub(r"font-family:'Gaegu',sans-serif;", "font-family:'Pretendard Variable', Pretendard, -apple-system, sans-serif;", html)
html = re.sub(r"font-family:'Patrick Hand','Gaegu',cursive", "font-family:'Pretendard Variable', Pretendard, -apple-system, sans-serif;", html)
html = re.sub(r"font-family:'Gaegu';", "font-family:'Pretendard Variable', Pretendard, -apple-system, sans-serif;", html)
html = re.sub(r"font-family:'Patrick Hand';", "font-family:'Pretendard Variable', Pretendard, -apple-system, sans-serif;", html)

# 2. Title and text standardization
html = html.replace('움직이는 그림사전', '보는 단어장')

# 3. Remove #demo section completely
html = re.sub(r'<section id="demo" class="wrap">.*?</section>', '', html, flags=re.DOTALL)

# 4. Remove #price section completely
html = re.sub(r'<section id="price" class="wrap">.*?</section>', '', html, flags=re.DOTALL)

# 5. Remove heroStage div
html = re.sub(r'<div class="hero-stage" id="heroStage"></div>', '', html)

# 6. Update "작동 원리" section texts
html = re.sub(r'<h3>손이 그림을 그립니다</h3><p>.*?</p>', r'<h3>그려지는 과정을 본다</h3><p>완성된 그림보다 그려지는 과정을 본 학생이 더 배웠습니다. 펜 끝을 따라가는 시선이 집중을 만듭니다.</p>', html)
html = re.sub(r'<h3>만지면 글자로 변신</h3><p>.*?</p>', r'<h3>만지면 글자로 변신</h3><p>완성된 그림을 터치하면 그림이 지워지며 철자가 튀어나옵니다. 이미지가 곧 철자가 됩니다.</p>', html)
html = re.sub(r'<h3>발음까지 한 번에</h3><p>.*?</p>', r'<h3>원어민 발음까지 한 번에</h3><p>변신하는 순간 발음이 재생됩니다. 눈·손·귀 — 세 갈래 기억이 동시에 새겨집니다.</p>', html)

# Also add the 4th step "장면 하나 = 단어 가족"
html = html.replace('</div>\n  </div>\n  <div class="global-box">', r'''</div>
    <div class="step"><div class="num">4</div><h3>장면 하나 = 단어 가족</h3><p>화산 장면 하나에서 VOLCANO·ERUPT·LAVA·ASH가 함께 각인됩니다. 낱단어가 아니라 의미망으로 묶어 기억합니다.</p></div>
  </div>
  <div class="global-box">''')

# 7. Replace cta-row with the new finishing block below the stage
# Find the old cta-row
html = re.sub(r'<div class="cta-row">\s*<a class="btn primary" href="#demo">.*?</a>\s*<a class="btn" href="#price">.*?</a>\s*</div>', '', html, flags=re.DOTALL)

# Insert the new finishing block after sceneStage wrap
new_block = """
  <div style="text-align:center; margin-top:40px; margin-bottom:20px;">
    <p style="font-size:20px; color:#555; margin-bottom:20px;">지금은 맛보기 2장면 — 정식판은 장면 100개, 800단어로 준비 중입니다</p>
    <div class="cta-row" style="margin-top:0;">
      <a class="btn primary" href="/#pricing">런칭가 ₩4,900 알아보기 →</a>
      <a class="btn" href="/">처음부터 보기 →</a>
    </div>
  </div>
"""
html = html.replace('</div>\n  </div>\n</header>', '</div>\n  </div>\n' + new_block + '\n</header>')

# 8. JS cleanup
# Remove WORDS array
html = re.sub(r'const WORDS = \[.*?\];', '', html, flags=re.DOTALL)

# Remove buildCard through playCardHero
# Since it's hard to regex precisely, I'll match from `const SPEED` down to `heroLoop();`
html = re.sub(r'const SPEED = 0.45;.*?heroLoop\(\);', '', html, flags=re.DOTALL)

# Wait, `speak()` was in that block, and it's needed by `scenePlay()`. Let me NOT regex delete all JS, but instead explicitly remove the unwanted parts. Let's do it carefully.
with open('public/demo.html', 'w', encoding='utf-8') as f:
    f.write(html)
