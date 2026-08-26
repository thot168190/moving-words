# -*- coding: utf-8 -*-
import io, csv, json, os

# 141편 대장 읽기
csv_path = "_작업/141편_대장.csv"
rows = []
if os.path.exists(csv_path):
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)

# 남은 794개 단어
all_1200 = set(io.open("_작업/all1200.txt", encoding="utf-8").read().split())
s = io.open("public/learning/index.html", encoding="utf-8").read()
i = s.index("const chapterData = {"); st = s.index("{", i); d = 0
for j in range(st, len(s)):
    if s[j] == "{": d += 1
    elif s[j] == "}":
        d -= 1
        if d == 0: en = j + 1; break
data = json.loads(s[st:en])
used_words = {a for ch in data for w in data[ch]["works"] for a, b in w["words"]}
free_words = sorted(list(all_1200 - used_words))

# 갈래별 분류
cats = json.load(io.open("_작업/1200_분류.json", encoding="utf-8"))["갈래"]
cat_summary = {}
for c, words in cats.items():
    avail = [w for w in words if w in free_words]
    if avail:
        cat_summary[c] = avail

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>91편 실물 포스터 & 단어 진실 매칭 상황실</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f4f6f8; color: #1a1a1a; margin: 0; padding: 20px; }}
  .header {{ background: #07533f; color: white; padding: 24px; border-radius: 12px; margin-bottom: 24px; }}
  .header h1 {{ margin: 0 0 8px 0; font-size: 24px; }}
  .header p {{ margin: 0; opacity: 0.9; font-size: 15px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }}
  .card {{ background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border: 1px solid #e2e8f0; display: flex; flex-direction: column; }}
  .poster {{ width: 100%; aspect-ratio: 16/9; background: #eee; position: relative; }}
  .poster img {{ width: 100%; height: 100%; object-fit: cover; }}
  .badge {{ position: absolute; top: 10px; left: 10px; background: rgba(7,83,63,0.9); color: white; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: bold; }}
  .info {{ padding: 16px; flex: 1; }}
  .info h3 {{ margin: 0 0 6px 0; font-size: 18px; color: #07533f; }}
  .info p {{ margin: 0 0 12px 0; color: #64748b; font-size: 14px; }}
  .tags {{ display: flex; flex-wrap: wrap; gap: 6px; }}
  .tag {{ background: #f1f5f9; padding: 4px 8px; border-radius: 6px; font-size: 12px; color: #334155; }}
</style>
</head>
<body>
<div class="header">
  <h1>🌿 91편 실물 포스터 전수 감리실 (총 91편)</h1>
  <p>그림을 먼저 보고 → 그림에 실제로 존재하는 단어만 1:1로 매칭합니다. (남은 정본 단어: {len(free_words)}개)</p>
</div>

<div class="grid">
"""

for r in rows:
    poster_src = f"/learning/{r.get('target_poster', '')}"
    html += f"""
  <div class="card">
    <div class="poster">
      <span class="badge">{r.get('target_ch')} ({r.get('batch_name')})</span>
      <img src="{poster_src}" alt="{r.get('scene_title')}">
    </div>
    <div class="info">
      <h3>{r.get('scene_no')}. {r.get('scene_title')}</h3>
      <p>{r.get('scene_sub')}</p>
      <div class="tags">
        <span class="tag">📁 {r.get('target_mp4')}</span>
      </div>
    </div>
  </div>
"""

html += """
</div>
</body>
</html>
"""

with open("public/learning/91_matching_room.html", "w", encoding="utf-8") as f:
    f.write(html)

print("91편 실물 감리실 생성 완료!")

