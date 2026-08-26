# -*- coding: utf-8 -*-
import io, csv, json, os, glob

# public/learning/ch*/ch*_*-poster.jpg 목록 수집
posters = sorted(glob.glob("public/learning/ch*/ch*_*-poster.jpg"))

html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>91편 실물 포스터 전수 감리실</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f8fafc; color: #0f172a; margin: 0; padding: 24px; }}
  .header {{ background: #07533f; color: white; padding: 24px 30px; border-radius: 14px; margin-bottom: 24px; box-shadow: 0 4px 12px rgba(7,83,63,0.15); }}
  .header h1 {{ margin: 0 0 8px 0; font-size: 24px; font-weight: 800; }}
  .header p {{ margin: 0; opacity: 0.9; font-size: 15px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }}
  .card {{ background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; display: flex; flex-direction: column; }}
  .poster {{ width: 100%; aspect-ratio: 16/9; background: #ffffff; position: relative; border-bottom: 1px solid #f1f5f9; }}
  .poster img {{ width: 100%; height: 100%; object-fit: contain; }}
  .badge {{ position: absolute; top: 8px; left: 8px; background: rgba(7,83,63,0.85); color: white; padding: 3px 8px; border-radius: 6px; font-size: 12px; font-weight: bold; }}
  .info {{ padding: 14px 16px; flex: 1; display: flex; flex-direction: column; justify-content: space-between; }}
  .info h3 {{ margin: 0 0 6px 0; font-size: 16px; font-weight: 700; color: #07533f; }}
  .video-link {{ display: inline-block; font-size: 12px; color: #2563eb; text-decoration: none; word-break: break-all; margin-top: 4px; }}
</style>
</head>
<body>
<div class="header">
  <h1>🌿 91편 실물 포스터 전수 감리실 (총 {len(posters)}편)</h1>
  <p>그림이 완전히 완성된 마지막 프레임(-sseof -0.5) 포스터입니다. 그림을 보면서 단어 매칭을 진행할 수 있습니다.</p>
</div>

<div class="grid">
"""

for p in posters:
    rel_poster = p.replace("public/learning/", "")
    mp4_file = rel_poster.replace("-poster.jpg", ".mp4")
    name = os.path.basename(rel_poster).replace("-poster.jpg", "")
    ch_dir = rel_poster.split("/")[0]

    html += f"""
  <div class="card">
    <div class="poster">
      <span class="badge">{ch_dir}</span>
      <img src="/learning/{rel_poster}" alt="{name}" loading="lazy">
    </div>
    <div class="info">
      <h3>{name}</h3>
      <a class="video-link" href="/learning/{mp4_file}" target="_blank">🎬 {mp4_file} 영상 보기</a>
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

print(f"91편 실물 감리실 ({len(posters)}개 포스터) 재생성 완료!")

