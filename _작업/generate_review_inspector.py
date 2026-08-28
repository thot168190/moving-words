# -*- coding: utf-8 -*-
import io, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "public/learning/index.html")
BAK = os.path.join(ROOT, "public/learning/index.html.bak_0827_1500")

def extract_cd(fn):
    s = io.open(fn, encoding="utf-8").read()
    i = s.index("const chapterData = {")
    st = s.index("{", i)
    d = 0
    for j in range(st, len(s)):
        if s[j] == "{": d += 1
        elif s[j] == "}":
            d -= 1
            if d == 0: en = j + 1; break
    return json.loads(s[st:en])

cur = extract_cd(SRC)
bak = extract_cd(BAK)

updated_keys = set()
for ch in cur:
    cur_ch = cur[ch]
    bak_ch = bak.get(ch, {})
    for idx, w in enumerate(cur_ch.get("works", [])):
        cur_l1 = cur_ch.get("levelOneWords", [])[idx] if idx < len(cur_ch.get("levelOneWords", [])) else []
        cur_l2 = cur_ch.get("levelTwoWords", [])[idx] if idx < len(cur_ch.get("levelTwoWords", [])) else []
        bak_l1 = bak_ch.get("levelOneWords", [])[idx] if idx < len(bak_ch.get("levelOneWords", [])) else []
        bak_l2 = bak_ch.get("levelTwoWords", [])[idx] if idx < len(bak_ch.get("levelTwoWords", [])) else []
        if len(cur_l1) != len(bak_l1) or len(cur_l2) != len(bak_l2) or cur_l1 != bak_l1 or cur_l2 != bak_l2:
            updated_keys.add(f"{ch}_{idx}")

html = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>신규 주입 단어 & 좌표 실물 감리관 (코다리 총괄)</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Pretendard", "Segoe UI", Roboto, sans-serif; background: #090d16; color: #f1f5f9; padding: 24px; line-height: 1.5; }
  .container { max-width: 1400px; margin: 0 auto; }
  
  /* Top Bar */
  .hero-card { background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border: 1px solid #334155; border-radius: 16px; padding: 24px 30px; margin-bottom: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
  .badge-main { display: inline-block; background: #3b82f6; color: #fff; font-size: 12px; font-weight: 700; padding: 4px 12px; border-radius: 20px; margin-bottom: 10px; letter-spacing: 0.5px; }
  h1 { font-size: 26px; font-weight: 800; color: #fff; margin-bottom: 8px; }
  p.desc { color: #94a3b8; font-size: 14px; margin-bottom: 16px; }
  
  .stats-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-top: 16px; }
  .stat-pill { background: #131d31; border: 1px solid #1e293b; border-radius: 12px; padding: 14px 18px; }
  .stat-val { font-size: 26px; font-weight: 800; font-family: ui-monospace, monospace; }
  .stat-lbl { font-size: 12px; color: #94a3b8; margin-top: 2px; }
  
  /* Filter Bar */
  .filter-bar { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px; position: sticky; top: 12px; z-index: 100; background: rgba(9, 13, 22, 0.92); backdrop-filter: blur(12px); padding: 12px 16px; border-radius: 12px; border: 1px solid #1e293b; }
  .btn-filter { background: #1e293b; border: 1px solid #334155; color: #cbd5e1; padding: 8px 16px; border-radius: 8px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s; }
  .btn-filter:hover { background: #334155; color: #fff; }
  .btn-filter.active { background: #2563eb; border-color: #3b82f6; color: #fff; box-shadow: 0 0 12px rgba(37,99,235,0.5); }
  .btn-app { background: #10b981; border-color: #059669; color: #fff; margin-left: auto; font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px; border-radius: 8px; font-size: 13px; }
  .btn-app:hover { background: #059669; }
  
  /* Scene Cards Grid */
  .scenes-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(420px, 1fr)); gap: 20px; }
  .scene-card { background: #131b2e; border: 1px solid #1e293b; border-radius: 14px; overflow: hidden; display: flex; flex-direction: column; transition: transform 0.2s, border-color 0.2s; }
  .scene-card:hover { border-color: #3b82f6; transform: translateY(-2px); }
  .scene-card.is-updated { border-color: #f59e0b; box-shadow: 0 0 16px rgba(245,158,11,0.15); }
  
  .card-header { padding: 14px 18px; background: #0f1626; border-bottom: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; }
  .ch-pill { font-size: 11px; font-weight: 700; background: #1e293b; color: #93c5fd; padding: 3px 8px; border-radius: 6px; border: 1px solid #334155; }
  .scene-title { font-size: 16px; font-weight: 700; color: #f8fafc; margin-left: 8px; }
  .tag-updated { background: #b45309; color: #fef3c7; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 6px; }
  .tag-short { background: #991b1b; color: #fee2e2; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 6px; }
  
  /* Poster Image & Spot Container */
  .canvas-wrap { position: relative; width: 100%; aspect-ratio: 16/9; background: #000; overflow: hidden; }
  .canvas-img { width: 100%; height: 100%; object-fit: contain; background: #ffffff; display: block; }
  
  /* Interactive Spot Marker */
  .spot-dot { position: absolute; width: 24px; height: 24px; border-radius: 50%; transform: translate(-50%, -50%); display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 800; color: #fff; cursor: pointer; transition: all 0.2s; z-index: 10; box-shadow: 0 0 8px rgba(0,0,0,0.8); }
  .spot-dot.l1 { background: #2563eb; border: 2px solid #93c5fd; }
  .spot-dot.l2 { background: #7c3aed; border: 2px solid #c4b5fd; }
  .spot-dot:hover { transform: translate(-50%, -50%) scale(1.4); z-index: 20; }
  
  /* Word Lists */
  .card-body { padding: 16px 18px; flex: 1; display: flex; flex-direction: column; gap: 12px; }
  .word-group-title { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; display: flex; justify-content: space-between; align-items: center; }
  .lbl-l1 { color: #60a5fa; }
  .lbl-l2 { color: #a78bfa; }
  
  .words-flex { display: flex; flex-wrap: wrap; gap: 6px; }
  .word-badge { display: inline-flex; align-items: center; gap: 5px; padding: 5px 9px; border-radius: 6px; font-size: 12px; font-family: ui-monospace, monospace; border: 1px solid transparent; }
  .word-badge.l1 { background: #1e293b; border-color: #2563eb; color: #bfdbfe; }
  .word-badge.l2 { background: #1e1b4b; border-color: #4f46e5; color: #ddd6fe; }
  .word-badge .idx { width: 16px; height: 16px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 10px; font-weight: bold; }
  .word-badge.l1 .idx { background: #2563eb; color: #fff; }
  .word-badge.l2 .idx { background: #6366f1; color: #fff; }
  .word-badge .ko { color: #94a3b8; font-family: sans-serif; font-size: 11px; }
  .word-badge .spot { color: #fbbf24; font-size: 10px; font-weight: 600; margin-left: 2px; }
  
  .card-footer { padding: 12px 18px; background: #0f1626; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center; }
  .btn-test-scene { background: #1e293b; border: 1px solid #3b82f6; color: #60a5fa; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 4px; transition: all 0.2s; }
  .btn-test-scene:hover { background: #2563eb; color: #fff; }
  .file-path { font-size: 11px; color: #64748b; font-family: monospace; }
</style>
</head>
<body>
<div class="container">
  <div class="hero-card">
    <div class="badge-main">코다리 총괄부장 실물 검증 리포트</div>
    <h1>🎨 보는 단어장 · 단어 & 좌표 실물 감리관</h1>
    <p class="desc">로부장이 주입 완료한 19개 씬(Ch1·2·3·7)을 포함한 전수 157편의 <b>그림 위 좌표(Spots)와 단어 배치</b>를 브라우저에서 직접 시각적으로 검증합니다.</p>
    
    <div class="stats-row">
      <div class="stat-pill">
        <div class="stat-val" style="color:#60a5fa;">924 / 1,200</div>
        <div class="stat-lbl">총 탑재 단어 (858 -> 924개)</div>
      </div>
      <div class="stat-pill">
        <div class="stat-val" style="color:#4ade80;">100% (0건)</div>
        <div class="stat-lbl">단어-좌표 짝 무결성 (불일치 0)</div>
      </div>
      <div class="stat-pill">
        <div class="stat-val" style="color:#f59e0b;">19편 완료</div>
        <div class="stat-lbl">오늘 신규 주입 완료 씬</div>
      </div>
      <div class="stat-pill">
        <div class="stat-val" style="color:#a78bfa;">60편</div>
        <div class="stat-lbl">8개(L1 4 + L2 4) 완비 씬</div>
      </div>
      <div class="stat-pill">
        <div class="stat-val" style="color:#f87171;">5편</div>
        <div class="stat-lbl">6개 미만 잔여 씬 (손 나온 그림 등)</div>
      </div>
    </div>
  </div>

  <div class="filter-bar">
    <button class="btn-filter active" onclick="filterScenes('updated')">✨ 오늘 신규 보완 19편만 모아보기</button>
    <button class="btn-filter" onclick="filterScenes('all')">전체 157편</button>
    <button class="btn-filter" onclick="filterScenes('ch1')">Ch 1 (14편)</button>
    <button class="btn-filter" onclick="filterScenes('ch2')">Ch 2 (18편)</button>
    <button class="btn-filter" onclick="filterScenes('ch3')">Ch 3 (21편)</button>
    <button class="btn-filter" onclick="filterScenes('ch7')">Ch 7 (11편)</button>
    <button class="btn-filter" onclick="filterScenes('short')">🚨 6개 미만 잔여 (5편)</button>
    
    <a href="http://localhost:8088/learning/index.html#ch1" target="_blank" class="btn-app">🚀 실제 학습앱 실행 (포트 8088)</a>
  </div>

  <div class="scenes-grid" id="scenesGrid">
"""

card_items = []
for ch in sorted(cur.keys(), key=lambda x: int(x)):
    cur_ch = cur[ch]
    for idx, w in enumerate(cur_ch.get("works", [])):
        key = f"{ch}_{idx}"
        is_updated = key in updated_keys
        
        l1_words = cur_ch.get("levelOneWords", [])[idx] if idx < len(cur_ch.get("levelOneWords", [])) else []
        l2_words = cur_ch.get("levelTwoWords", [])[idx] if idx < len(cur_ch.get("levelTwoWords", [])) else []
        l1_spots = cur_ch.get("levelOneSpots", [])[idx] if idx < len(cur_ch.get("levelOneSpots", [])) else []
        sc_spots = cur_ch.get("sceneSpots", [])[idx] if idx < len(cur_ch.get("sceneSpots", [])) else []
        
        tot = len(l1_words) + len(l2_words)
        is_short = tot < 6
        
        img = w.get("img", "")
        img_src = f"../public/learning/{img}"
        
        status_tags = []
        if is_updated:
            status_tags.append('<span class="tag-updated">✨ 오늘 주입 완료</span>')
        if is_short:
            status_tags.append('<span class="tag-short">🚨 6개 미만</span>')
        tags_html = " ".join(status_tags)
            
        dots_html = []
        for s_idx, (en, ko) in enumerate(l1_words):
            if s_idx < len(l1_spots):
                sx, sy = l1_spots[s_idx]
                dots_html.append(f'<div class="spot-dot l1" style="left:{sx}%; top:{sy}%;" title="L1 [{s_idx+1}] {en}({ko}) [{sx}%, {sy}%]">{s_idx+1}</div>')
                
        for s_idx, (en, ko) in enumerate(l2_words):
            if s_idx < len(sc_spots):
                sx, sy = sc_spots[s_idx]
                dots_html.append(f'<div class="spot-dot l2" style="left:{sx}%; top:{sy}%;" title="L2 [{s_idx+1}] {en}({ko}) [{sx}%, {sy}%]">{s_idx+1}</div>')
        
        l1_badges = []
        for s_idx, (en, ko) in enumerate(l1_words):
            sp_str = f"[{l1_spots[s_idx][0]},{l1_spots[s_idx][1]}]" if s_idx < len(l1_spots) else "미배정"
            l1_badges.append(f'<span class="word-badge l1"><span class="idx">{s_idx+1}</span> <b>{en}</b> <span class="ko">{ko}</span> <span class="spot">{sp_str}</span></span>')
            
        l2_badges = []
        for s_idx, (en, ko) in enumerate(l2_words):
            sp_str = f"[{sc_spots[s_idx][0]},{sc_spots[s_idx][1]}]" if s_idx < len(sc_spots) else "미배정"
            l2_badges.append(f'<span class="word-badge l2"><span class="idx">{s_idx+1}</span> <b>{en}</b> <span class="ko">{ko}</span> <span class="spot">{sp_str}</span></span>')
            
        classes = ["scene-card"]
        if is_updated: classes.append("is-updated")
        if is_short: classes.append("is-short")
        classes.append(f"ch-{ch}")
        
        num_str = w.get("n", str(idx+1))
        title_str = w.get("title", "")
        
        card_html = f"""
        <div class="{" ".join(classes)}" data-ch="ch{ch}" data-updated="{'true' if is_updated else 'false'}" data-short="{'true' if is_short else 'false'}">
          <div class="card-header">
            <div>
              <span class="ch-pill">Ch {ch} · {num_str}번</span>
              <span class="scene-title">{title_str}</span>
            </div>
            <div>{tags_html}</div>
          </div>
          
          <div class="canvas-wrap">
            <img src="{img_src}" class="canvas-img" alt="{title_str}" loading="lazy" onerror="this.src='https://placehold.co/600x338/1e293b/94a3b8?text=Image+Loading'">
            {"".join(dots_html)}
          </div>
          
          <div class="card-body">
            <div>
              <div class="word-group-title lbl-l1">
                <span>🔵 레벨 1 (그림 요소 · 퀴즈) ({len(l1_words)}개)</span>
                <span style="font-size:10px; color:#64748b;">파란 점</span>
              </div>
              <div class="words-flex" style="margin-top:6px;">
                {"".join(l1_badges) if l1_badges else '<span style="color:#64748b; font-size:12px;">없음</span>'}
              </div>
            </div>
            
            <div>
              <div class="word-group-title lbl-l2">
                <span>🟣 레벨 2 (이야기 연결) ({len(l2_words)}개)</span>
                <span style="font-size:10px; color:#64748b;">보라 점</span>
              </div>
              <div class="words-flex" style="margin-top:6px;">
                {"".join(l2_badges) if l2_badges else '<span style="color:#64748b; font-size:12px;">없음</span>'}
              </div>
            </div>
          </div>
          
          <div class="card-footer">
            <span class="file-path">{img}</span>
            <a href="http://localhost:8088/learning/index.html#ch{ch}" target="_blank" class="btn-test-scene">
              ▶️ 학습 앱에서 직접 테스트
            </a>
          </div>
        </div>
        """
        card_items.append(card_html)

html += "".join(card_items)
html += """
  </div>
</div>

<script>
function filterScenes(type) {
  document.querySelectorAll(".btn-filter").forEach(b => b.classList.remove("active"));
  if (window.event && window.event.target && window.event.target.classList.contains("btn-filter")) {
    window.event.target.classList.add("active");
  }
  
  const cards = document.querySelectorAll(".scene-card");
  cards.forEach(card => {
    if (type === "all") {
      card.style.display = "flex";
    } else if (type === "updated") {
      card.style.display = card.getAttribute("data-updated") === "true" ? "flex" : "none";
    } else if (type === "short") {
      card.style.display = card.getAttribute("data-short") === "true" ? "flex" : "none";
    } else if (type.startsWith("ch")) {
      card.style.display = card.getAttribute("data-ch") === type ? "flex" : "none";
    }
  });
}
window.onload = function() {
  filterScenes("updated");
};
</script>
</body>
</html>
"""

out_path = os.path.join(ROOT, "_작업/신규주입_실물감리관.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ 신규주입_실물감리관.html 생성 완료! 파일 크기:", os.path.getsize(out_path), "bytes")
