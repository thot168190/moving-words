# -*- coding: utf-8 -*-
import io, json, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "public/learning/index.html")

s = io.open(SRC, encoding="utf-8").read()
i = s.index("const chapterData = {")
st = s.index("{", i)
d = 0
for j in range(st, len(s)):
    if s[j] == "{": d += 1
    elif s[j] == "}":
        d -= 1
        if d == 0: en = j + 1; break
data = json.loads(s[st:en])

html = ["""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>전체 157편 그림 vs 목차 전수 대조 감리관</title>
<style>
  body { font-family: -apple-system, sans-serif; background: #0f172a; color: #fff; padding: 20px; }
  h1 { color: #38bdf8; text-align: center; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; margin-top: 20px; }
  .card { background: #1e293b; border-radius: 8px; padding: 12px; border: 1px solid #334155; }
  .card img { width: 100%; aspect-ratio: 16/9; object-fit: contain; background: #fff; border-radius: 4px; }
  .ch-badge { display: inline-block; background: #0284c7; color: #fff; font-size: 11px; padding: 2px 6px; border-radius: 4px; font-weight: bold; }
  .title { font-size: 15px; font-weight: bold; margin: 8px 0 4px; color: #f8fafc; }
  .file { font-size: 12px; color: #94a3b8; word-break: break-all; }
  .words { font-size: 13px; color: #38bdf8; margin-top: 6px; }
</style>
</head>
<body>
<h1>🔍 전체 157편 그림 vs 목차 전수 대조 감리관</h1>
"""]

for ch in range(1, 13):
    ch_k = str(ch)
    ch_obj = data[ch_k]
    html.append(f"<h2>Chapter {ch} ({len(ch_obj['works'])}편)</h2><div class='grid'>")
    for idx, w in enumerate(ch_obj["works"]):
        img_path = f"../public/learning/{w['img']}"
        l1 = ", ".join([f"{a}({b})" for a, b in ch_obj["levelOneWords"][idx]])
        html.append(f"""
        <div class="card">
          <img src="{img_path}" alt="{w['title']}">
          <div style="margin-top:8px;"><span class="ch-badge">ch{ch}_{w['n']}</span></div>
          <div class="title">{w['title']}</div>
          <div class="file">{w['img']}</div>
          <div class="words"><strong>L1:</strong> {l1}</div>
        </div>
        """)
    html.append("</div>")

html.append("</body></html>")

out_path = os.path.join(ROOT, "_작업/전체_그림_감리관.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(html))

print(f"생성 완료: {out_path}")
