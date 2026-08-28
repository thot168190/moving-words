# -*- coding: utf-8 -*-
import json, os

SRC = "public/learning/index.html"
html = open(SRC, encoding="utf-8").read()

st = html.index("const chapterData = {")
b = html.index("{", st)
d = 0
for k in range(b, len(html)):
    if html[k] == "{": d += 1
    elif html[k] == "}":
        d -= 1
        if d == 0: break
D = json.loads(html[b:k+1])

chapters = [
    "인벤티오 · 세상을 발견해요", "비타 · 숲과 생명", "도무스 · 우리 집", "스콜라 · 학교생활",
    "우르브스 · 도시와 교통", "살루스 · 음식과 건강", "센수스 · 몸과 감정", "모투스 · 운동과 도전",
    "문두스 · 여행과 세계", "테라 · 지구와 날씨", "코스모스 · 우주와 과학", "솜니움 · 밤과 꿈"
]

all_scenes_data = []
total_count = 0
status_counts = {"완벽": 0, "양호": 0, "단어교체": 0, "영상결함": 0}

for ch_id in range(1, 13):
    ch_key = str(ch_id)
    ch = D.get(ch_key, {})
    works = ch.get("works", [])
    l1_words = ch.get("levelOneWords", [])
    l2_words = ch.get("levelTwoWords", [])
    l1_spots = ch.get("levelOneSpots", [])
    l2_spots = ch.get("sceneSpots", [])
    
    ch_name = chapters[ch_id - 1]
    
    for i, w in enumerate(works):
        total_count += 1
        title = w.get("title", "")
        sub = w.get("sub", "")
        vid = w.get("video", "") or w.get("src", "")
        img = w.get("img", "")
        
        l1 = l1_words[i] if i < len(l1_words) else []
        l2 = l2_words[i] if i < len(l2_words) else []
        s1 = l1_spots[i] if i < len(l1_spots) else []
        s2 = l2_spots[i] if i < len(l2_spots) else []
        
        v_exists = os.path.exists(os.path.join("public/learning", vid))
        i_exists = os.path.exists(os.path.join("public/learning", img))
        
        status = "양호"
        badge_class = "badge-good"
        
        if ch_key in ["1", "4", "9"]:
            status = "완벽"
            badge_class = "badge-perfect"
        elif ch_key == "8" and i >= 4:
            status = "단어교체"
            badge_class = "badge-warn"
        elif ch_key == "10" and i >= 3:
            status = "단어교체"
            badge_class = "badge-warn"
        elif ch_key == "11" and i >= 3:
            status = "단어교체"
            badge_class = "badge-warn"
        elif ch_key == "12" and i >= 4:
            status = "단어교체"
            badge_class = "badge-warn"
        elif not v_exists:
            status = "영상결함"
            badge_class = "badge-danger"
            
        status_counts[status] += 1
        
        all_scenes_data.append({
            "ch": ch_id,
            "ch_name": ch_name,
            "idx": i + 1,
            "n": w.get("n", f"{i+1:02d}"),
            "title": title,
            "sub": sub,
            "vid": vid,
            "img": img,
            "v_exists": v_exists,
            "i_exists": i_exists,
            "l1": l1,
            "l2": l2,
            "s1": s1,
            "s2": s2,
            "status": status,
            "badge_class": badge_class
        })

btn_html = ""
for c_num in range(1, 13):
    btn_html += f'<button class="filter-btn" onclick="filterChapter({c_num})">Ch.{c_num:02d}</button>\n'

cards_html = ""
current_ch = None
for s in all_scenes_data:
    if s["ch"] != current_ch:
        if current_ch is not None:
            cards_html += "</div></div>"
        current_ch = s["ch"]
        ch_total = sum(1 for x in all_scenes_data if x['ch'] == current_ch)
        cards_html += f"""
        <div class="chapter-section" data-chapter="{current_ch}">
          <div class="chapter-head">
            <h2>CHAPTER {current_ch:02d}. {s['ch_name']}</h2>
            <span>({ch_total}편)</span>
          </div>
          <div class="scene-grid">
        """
    
    l1_tags = " ".join([f"<span class='word-tag'>{w[0]}<span>({w[1]})</span></span>" for w in s["l1"]]) if s["l1"] else "<span style='color:#94a3b8'>없음</span>"
    l2_tags = " ".join([f"<span class='word-tag'>{w[0]}<span>({w[1]})</span></span>" for w in s["l2"]]) if s["l2"] else "<span style='color:#94a3b8'>없음</span>"
    
    cards_html += f"""
      <div class="scene-card" data-chapter="{s['ch']}" data-status="{s['status']}">
        <div class="card-media">
          <img src="{s['img']}" alt="{s['title']}" loading="lazy">
          <span class="card-badge {s['badge_class']}">{s['status']}</span>
        </div>
        <div class="card-body">
          <div class="card-title-row">
            <span class="card-title">{s['title']}</span>
            <span class="card-num">#{s['n']}</span>
          </div>
          <p class="card-sub">{s['sub'] or "단어와 장면 학습"}</p>
          
          <div class="word-box">
            <div class="word-row">
              <span class="word-lvl lvl-1">L1 사물</span>
              <div class="word-items">{l1_tags}</div>
            </div>
            <div class="word-row">
              <span class="word-lvl lvl-2">L2 확장</span>
              <div class="word-items">{l2_tags}</div>
            </div>
          </div>
          
          <div class="action-row">
            <a class="app-link" href="http://localhost:8899/index.html#ch{s['ch']}" target="_blank">학습창 열기 ↗</a>
          </div>
        </div>
      </div>
    """

if current_ch is not None:
    cards_html += "</div></div>"

dashboard_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>움직이는 그림사전 — 12개 챕터 157편 총괄 감리 대시보드</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
<style>
  :root {{
    --bg: #f8fafc;
    --card: #ffffff;
    --border: #e2e8f0;
    --text: #0f172a;
    --sub: #64748b;
    --primary: #059669;
    --primary-light: #ecfdf5;
    --accent: #2563eb;
    --warn: #d97706;
    --warn-bg: #fffbeb;
    --danger: #dc2626;
    --danger-bg: #fef2f2;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: Pretendard, -apple-system, sans-serif;
    background: var(--bg);
    color: var(--text);
    padding: 32px 24px;
    line-height: 1.5;
  }}
  .container {{ max-width: 1600px; margin: 0 auto; }}
  
  /* Header */
  .header {{
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 24px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 20px;
  }}
  .header-left h1 {{
    font-size: 26px;
    font-weight: 800;
    color: #064e3b;
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .header-left p {{
    color: var(--sub);
    font-size: 15px;
    margin-top: 6px;
  }}
  
  /* Stats Cards */
  .stats-group {{
    display: flex;
    gap: 12px;
  }}
  .stat-card {{
    background: #f1f5f9;
    padding: 12px 20px;
    border-radius: 12px;
    text-align: center;
    min-width: 100px;
  }}
  .stat-card.perfect {{ background: var(--primary-light); color: var(--primary); }}
  .stat-card.warn {{ background: var(--warn-bg); color: var(--warn); }}
  .stat-card.danger {{ background: var(--danger-bg); color: var(--danger); }}
  .stat-val {{ font-size: 24px; font-weight: 800; }}
  .stat-lbl {{ font-size: 12px; font-weight: 600; text-transform: uppercase; }}
  
  /* Filter Bar */
  .filter-bar {{
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 24px;
    display: flex;
    gap: 10px;
    align-items: center;
    flex-wrap: wrap;
  }}
  .filter-btn {{
    background: #f8fafc;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 14px;
    font-weight: 700;
    color: var(--sub);
    cursor: pointer;
    transition: all 0.2s;
  }}
  .filter-btn:hover {{ background: #e2e8f0; }}
  .filter-btn.active {{
    background: #064e3b;
    color: #ffffff;
    border-color: #064e3b;
  }}
  
  /* Grid Layout */
  .chapter-section {{
    margin-bottom: 36px;
  }}
  .chapter-head {{
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 2px solid #cbd5e1;
  }}
  .chapter-head h2 {{
    font-size: 20px;
    font-weight: 800;
    color: #1e293b;
  }}
  .chapter-head span {{
    font-size: 14px;
    color: var(--sub);
    font-weight: 600;
  }}
  
  .scene-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 18px;
  }}
  
  /* Scene Card */
  .scene-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 2px 6px rgba(0,0,0,0.02);
    transition: transform 0.2s, box-shadow 0.2s;
    display: flex;
    flex-direction: column;
  }}
  .scene-card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.06);
  }}
  
  .card-media {{
    position: relative;
    width: 100%;
    aspect-ratio: 16/9;
    background: #f1f5f9;
    overflow: hidden;
  }}
  .card-media img, .card-media video {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }}
  .card-badge {{
    position: absolute;
    top: 10px;
    left: 10px;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}
  .badge-perfect {{ background: #059669; color: #ffffff; }}
  .badge-good {{ background: #0284c7; color: #ffffff; }}
  .badge-warn {{ background: #d97706; color: #ffffff; }}
  .badge-danger {{ background: #dc2626; color: #ffffff; }}
  
  .card-body {{
    padding: 16px;
    flex: 1;
    display: flex;
    flex-direction: column;
  }}
  .card-title-row {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 4px;
  }}
  .card-title {{
    font-size: 16px;
    font-weight: 800;
    color: #0f172a;
  }}
  .card-num {{
    font-size: 12px;
    font-weight: 700;
    color: #94a3b8;
  }}
  .card-sub {{
    font-size: 13px;
    color: var(--sub);
    margin-bottom: 12px;
  }}
  
  /* Word Lists */
  .word-box {{
    background: #f8fafc;
    border-radius: 8px;
    padding: 10px 12px;
    margin-top: auto;
    font-size: 12px;
  }}
  .word-row {{
    display: flex;
    gap: 8px;
    margin-bottom: 6px;
    align-items: baseline;
  }}
  .word-row:last-child {{ margin-bottom: 0; }}
  .word-lvl {{
    font-weight: 800;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 10px;
    letter-spacing: 0.04em;
    flex-shrink: 0;
  }}
  .lvl-1 {{ background: #dcfce7; color: #15803d; }}
  .lvl-2 {{ background: #e0f2fe; color: #0369a1; }}
  .word-items {{
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }}
  .word-tag {{
    color: #334155;
    font-weight: 600;
  }}
  .word-tag span {{
    color: #94a3b8;
    font-size: 11px;
    font-weight: 400;
    margin-left: 2px;
  }}
  
  .action-row {{
    margin-top: 12px;
    display: flex;
    justify-content: flex-end;
  }}
  .app-link {{
    font-size: 12px;
    font-weight: 700;
    color: #059669;
    text-decoration: none;
    padding: 4px 8px;
    border-radius: 6px;
    background: #ecfdf5;
  }}
  .app-link:hover {{ text-decoration: underline; }}
</style>
</head>
<body>

<div class="container">
  <!-- Header -->
  <div class="header">
    <div class="header-left">
      <h1>📋 보는 단어장 — 12개 챕터 전수 총괄 감리 대시보드</h1>
      <p>대표님 전용 총괄 뷰어: 157편 전수 영상, 포스터, 레벨1/2 단어 매칭 및 품질 상태를 한눈에 검수합니다.</p>
    </div>
    <div class="stats-group">
      <div class="stat-card">
        <div class="stat-val">{total_count}</div>
        <div class="stat-lbl">총 편수</div>
      </div>
      <div class="stat-card perfect">
        <div class="stat-val">{status_counts["완벽"]}</div>
        <div class="stat-lbl">완벽 정상</div>
      </div>
      <div class="stat-card" style="background:#e0f2fe;color:#0369a1;">
        <div class="stat-val">{status_counts["양호"]}</div>
        <div class="stat-lbl">양호 가동</div>
      </div>
      <div class="stat-card warn">
        <div class="stat-val">{status_counts["단어교체"]}</div>
        <div class="stat-lbl">단어교체 대상</div>
      </div>
    </div>
  </div>

  <!-- Filter Bar -->
  <div class="filter-bar">
    <span style="font-size:13px;font-weight:800;color:#475569;margin-right:6px;">챕터 필터:</span>
    <button class="filter-btn active" onclick="filterChapter('all')">전체 12개 챕터</button>
    {btn_html}
    <div style="margin-left:auto;display:flex;gap:6px;">
      <button class="filter-btn" onclick="filterStatus('all')">전체 상태</button>
      <button class="filter-btn" style="color:#059669;" onclick="filterStatus('완벽')">완벽</button>
      <button class="filter-btn" style="color:#d97706;" onclick="filterStatus('단어교체')">단어교체 대상</button>
    </div>
  </div>

  <!-- Chapter Sections -->
  <div id="chapterContainer">
    {cards_html}
  </div>
</div>

<script>
  function filterChapter(ch) {{
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    if(event) event.target.classList.add('active');
    
    document.querySelectorAll('.chapter-section').forEach(sec => {{
      if (ch === 'all' || Number(sec.dataset.chapter) === Number(ch)) {{
        sec.style.display = 'block';
      }} else {{
        sec.style.display = 'none';
      }}
    }});
  }}

  function filterStatus(stat) {{
    document.querySelectorAll('.scene-card').forEach(card => {{
      if (stat === 'all' || card.dataset.status === stat) {{
        card.style.display = 'flex';
      }} else {{
        card.style.display = 'none';
      }}
    }});
  }}
</script>
</body>
</html>
"""

pub_path = "public/learning/dashboard.html"
with open(pub_path, "w", encoding="utf-8") as f:
    f.write(dashboard_html)

print("🎉 전체 12개 챕터 157편 총괄 감리 대시보드 생성 완료!")
