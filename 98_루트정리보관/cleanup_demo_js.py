import re

with open('public/demo.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove WORDS array
html = re.sub(r'const WORDS = \[.*?\];', '', html, flags=re.DOTALL)

# Remove buildCard through morph
html = re.sub(r'const SPEED = 0.45;.*?function wait\(ms\)\{ return new Promise\(r=>setTimeout\(r,ms\)\); \}', 'function wait(ms){ return new Promise(r=>setTimeout(r,ms)); }', html, flags=re.DOTALL)

# Keep the speak() block.
# Remove 데모 그리드, 자동 모드, 사운드 토글, 히어로 루프
html = re.sub(r'/\* ================= 데모 그리드 ================= \*/.*?heroLoop\(\);', '', html, flags=re.DOTALL)

with open('public/demo.html', 'w', encoding='utf-8') as f:
    f.write(html)
