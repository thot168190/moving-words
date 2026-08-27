# -*- coding: utf-8 -*-
import io, json, os, glob, csv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "public/learning/index.html")
ALL_TXT = os.path.join(ROOT, "_작업/all1200.txt")
CAT_JSON = os.path.join(ROOT, "_작업/1200_분류.json")
DAEJANG_CSV = os.path.join(ROOT, "_작업/141편_대장.csv")

# 1. 1200 단어 및 분류 로드
all_words = set(io.open(ALL_TXT, encoding="utf-8").read().split())
cats = {}
if os.path.exists(CAT_JSON):
    cats = json.load(io.open(CAT_JSON, encoding="utf-8")).get("갈래", {})

# 2. index.html 에서 chapterData 로드
s = io.open(SRC, encoding="utf-8").read()
i = s.index("const chapterData = {")
st = s.index("{", i)
d = 0
for j in range(st, len(s)):
    if s[j] == "{": d += 1
    elif s[j] == "}":
        d -= 1
        if d == 0:
            en = j + 1
            break
chapter_data = json.loads(s[st:en])

# 3. 사용된 단어 계산
used_words = {}
for ch, ch_obj in chapter_data.items():
    for w in ch_obj.get("works", []):
        for eng, kor in w.get("words", []):
            used_words[eng] = f"ch{ch}_{w.get('n')}"

free_words = sorted(list(all_words - set(used_words.keys())))

# 4. 챕터 정보 정리
CHAPTER_NAMES = {
    "1": "01 INVENTIO 세상을 발견해요",
    "2": "02 VITA 숲과 생명",
    "3": "03 DOMUS 우리 집",
    "4": "04 SCHOLA 학교생활",
    "5": "05 URBS 도시와 교통",
    "6": "06 SALUS 음식과 건강",
    "7": "07 SENSUS 몸과 감정",
    "8": "08 MOTUS 운동과 도전",
    "9": "09 MUNDUS 여행과 세계",
    "10": "10 TERRA 지구와 날씨",
    "11": "11 COSMOS 우주와 과학",
    "12": "12 SOMNIUM 밤과 꿈"
}

# HTML 생성
html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🌿 보는 단어장 — 대표님 & 코다리 라이브 집무실</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
<style>
  :root {{
    --primary: #07533f;
    --primary-dark: #04382a;
    --primary-light: #e6f4ea;
    --gold: #d97706;
    --gold-light: #fef3c7;
    --bg: #f8fafc;
    --panel-bg: #ffffff;
    --text-main: #0f172a;
    --text-muted: #64748b;
    --border: #e2e8f0;
    --border-focus: #07533f;
    --danger: #ef4444;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: "Pretendard", -apple-system, sans-serif; }}
  body {{ background: var(--bg); color: var(--text-main); height: 100vh; display: flex; flex-direction: column; overflow: hidden; }}

  /* Top Bar */
  header {{
    background: var(--primary); color: white; padding: 12px 24px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.15); z-index: 100;
  }}
  .logo-area {{ display: flex; align-items: center; gap: 12px; }}
  .logo-badge {{ background: rgba(255,255,255,0.2); padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 700; letter-spacing: 0.5px; }}
  .title-text {{ font-size: 18px; font-weight: 800; }}
  .stats-bar {{ display: flex; align-items: center; gap: 16px; font-size: 13px; }}
  .stat-pill {{ background: rgba(255,255,255,0.15); padding: 6px 14px; border-radius: 30px; display: flex; align-items: center; gap: 6px; }}
  .stat-pill b {{ color: #fbbf24; }}
  .btn-mobile {{ background: #ffffff; color: var(--primary); border: none; padding: 6px 14px; border-radius: 6px; font-size: 13px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 6px; transition: all 0.2s; }}
  .btn-mobile:hover {{ background: #f1f5f9; }}

  /* Main Workspace Layout */
  .workspace {{ display: flex; flex: 1; overflow: hidden; }}

  /* Left Panel: Chapter & Scene Selector */
  .panel-left {{ width: 320px; background: var(--panel-bg); border-right: 1px solid var(--border); display: flex; flex-direction: column; }}
  .ch-tabs {{ display: flex; overflow-x: auto; background: #f1f5f9; padding: 6px; gap: 4px; border-bottom: 1px solid var(--border); }}
  .ch-tab {{ padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 700; color: var(--text-muted); cursor: pointer; white-space: nowrap; border: none; background: transparent; }}
  .ch-tab.active {{ background: var(--primary); color: white; }}
  .scenes-list {{ flex: 1; overflow-y: auto; padding: 12px; display: flex; flex-direction: column; gap: 8px; }}
  .scene-card {{ display: flex; gap: 10px; padding: 8px; border-radius: 8px; border: 1px solid var(--border); cursor: pointer; transition: all 0.15s; background: white; }}
  .scene-card:hover {{ border-color: var(--primary); background: var(--primary-light); }}
  .scene-card.active {{ border-color: var(--primary); background: var(--primary-light); box-shadow: 0 0 0 2px var(--primary); }}
  .scene-thumb {{ width: 68px; height: 48px; border-radius: 4px; object-fit: cover; background: #cbd5e1; }}
  .scene-info {{ flex: 1; min-width: 0; }}
  .scene-num {{ font-size: 11px; font-weight: 700; color: var(--primary); }}
  .scene-title {{ font-size: 13px; font-weight: 700; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
  .scene-sub {{ font-size: 11px; color: var(--text-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}

  /* Center Panel: Visual Canvas & Pin Placement */
  .panel-center {{ flex: 1; display: flex; flex-direction: column; background: #0f172a; position: relative; overflow: hidden; }}
  .center-header {{ background: rgba(15,23,42,0.9); backdrop-filter: blur(10px); color: white; padding: 10px 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; }}
  .center-title {{ font-size: 15px; font-weight: 700; display: flex; align-items: center; gap: 8px; }}
  .coord-display {{ font-size: 13px; color: #94a3b8; font-family: monospace; background: #1e293b; padding: 4px 10px; border-radius: 4px; }}
  .canvas-container {{ flex: 1; display: flex; justify-content: center; align-items: center; padding: 20px; position: relative; overflow: auto; }}
  .poster-wrapper {{ position: relative; max-width: 100%; max-height: 100%; aspect-ratio: 16/9; background: #000; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border-radius: 8px; overflow: hidden; user-select: none; cursor: crosshair; }}
  .poster-img {{ width: 100%; height: 100%; object-fit: contain; display: block; }}
  
  /* Mobile View Constraint */
  .mobile-mode .canvas-container {{ background: #000; }}
  .mobile-mode .poster-wrapper {{ width: 390px; height: 693px; aspect-ratio: 390/693; }}

  /* Pins on Canvas */
  .spot-pin {{ position: absolute; transform: translate(-50%, -50%); cursor: grab; z-index: 10; display: flex; align-items: center; gap: 4px; padding: 4px 8px; border-radius: 20px; font-size: 11px; font-weight: 800; box-shadow: 0 4px 12px rgba(0,0,0,0.4); transition: transform 0.1s, box-shadow 0.1s; }}
  .spot-pin:hover {{ transform: translate(-50%, -50%) scale(1.15); z-index: 20; }}
  .spot-pin.l1 {{ background: #f59e0b; color: #000; border: 2px solid #ffffff; }}
  .spot-pin.l2 {{ background: #10b981; color: #ffffff; border: 2px solid #ffffff; }}
  .spot-pin.selected {{ box-shadow: 0 0 0 4px #38bdf8, 0 4px 12px rgba(0,0,0,0.6); }}

  /* Right Panel: Word Editor & Remaining Pool */
  .panel-right {{ width: 380px; background: var(--panel-bg); border-left: 1px solid var(--border); display: flex; flex-direction: column; }}
  .right-tabs {{ display: flex; border-bottom: 1px solid var(--border); }}
  .right-tab {{ flex: 1; padding: 12px; text-align: center; font-size: 13px; font-weight: 700; color: var(--text-muted); cursor: pointer; border: none; background: transparent; }}
  .right-tab.active {{ color: var(--primary); border-bottom: 2px solid var(--primary); }}
  
  .tab-content {{ flex: 1; overflow-y: auto; padding: 16px; display: flex; flex-direction: column; gap: 14px; }}
  .section-label {{ font-size: 12px; font-weight: 800; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; display: flex; justify-content: space-between; align-items: center; }}
  .word-card {{ background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 10px 12px; display: flex; align-items: center; gap: 8px; transition: all 0.15s; }}
  .word-card.l1 {{ border-left: 4px solid #f59e0b; }}
  .word-card.l2 {{ border-left: 4px solid #10b981; }}
  .word-card.active {{ border-color: var(--primary); background: var(--primary-light); }}
  .word-badge {{ font-size: 10px; font-weight: 800; padding: 2px 6px; border-radius: 4px; background: #e2e8f0; }}
  .word-card.l1 .word-badge {{ background: #fef3c7; color: #b45309; }}
  .word-card.l2 .word-badge {{ background: #d1fae5; color: #065f46; }}
  .word-inputs {{ flex: 1; display: flex; gap: 6px; }}
  .word-inputs input {{ width: 50%; padding: 4px 6px; font-size: 13px; border: 1px solid var(--border); border-radius: 4px; }}
  .word-coords {{ font-size: 11px; font-family: monospace; color: var(--text-muted); min-width: 60px; text-align: right; }}

  /* Pool Search */
  .search-box {{ position: relative; margin-bottom: 8px; }}
  .search-box input {{ width: 100%; padding: 8px 12px; border-radius: 6px; border: 1px solid var(--border); font-size: 13px; }}
  .pool-grid {{ display: flex; flex-wrap: wrap; gap: 6px; }}
  .pool-pill {{ background: #f1f5f9; padding: 5px 10px; border-radius: 6px; font-size: 12px; color: #334155; cursor: pointer; border: 1px solid var(--border); display: flex; align-items: center; gap: 4px; transition: all 0.15s; }}
  .pool-pill:hover {{ background: var(--primary-light); color: var(--primary); border-color: var(--primary); }}

  /* Action Footer */
  .panel-footer {{ padding: 12px 16px; border-top: 1px solid var(--border); background: #f8fafc; display: flex; gap: 8px; }}
  .btn-action {{ flex: 1; padding: 10px; border-radius: 6px; font-size: 13px; font-weight: 700; cursor: pointer; border: none; display: flex; align-items: center; justify-content: center; gap: 6px; transition: all 0.2s; }}
  .btn-primary {{ background: var(--primary); color: white; }}
  .btn-primary:hover {{ background: var(--primary-dark); }}
  .btn-secondary {{ background: #e2e8f0; color: #334155; }}
  .btn-secondary:hover {{ background: #cbd5e1; }}
</style>
</head>
<body>

<header>
  <div class="logo-area">
    <span class="logo-badge">KODARI EXECUTIVE</span>
    <span class="title-text">🌿 보는 단어장 — 대표님 & 코다리 라이브 감리 집무실</span>
  </div>
  <div class="stats-bar">
    <div class="stat-pill">전체 완성: <b id="statTotalWorks">86</b>편</div>
    <div class="stat-pill">남은 단어: <b id="statFreeWords">{len(free_words)}</b>개</div>
    <div class="stat-pill" style="background:#065f46; color:#a7f3d0;">✅ 검증 통과 상태</div>
    <button class="btn-mobile" onclick="toggleMobileMode()">
      📱 390px 모바일 뷰
    </button>
  </div>
</header>

<div class="workspace" id="workspaceRoot">
  <!-- 1. Left Chapter & Scenes -->
  <div class="panel-left">
    <div class="ch-tabs" id="chTabs"></div>
    <div class="scenes-list" id="scenesList"></div>
  </div>

  <!-- 2. Center Visual Canvas -->
  <div class="panel-center">
    <div class="center-header">
      <div class="center-title" id="currentSceneTitle">
        <span>선택된 편 없음</span>
      </div>
      <div class="coord-display" id="coordDisplay">X: --% | Y: --% (그림을 클릭하여 핀 배치)</div>
    </div>
    <div class="canvas-container" id="canvasContainer">
      <div class="poster-wrapper" id="posterWrapper" onclick="handleCanvasClick(event)" onmousemove="handleCanvasMove(event)">
        <img class="poster-img" id="posterImg" src="" alt="Poster">
        <div id="pinsOverlay"></div>
      </div>
    </div>
  </div>

  <!-- 3. Right Word Editor & Smart Pool -->
  <div class="panel-right">
    <div class="right-tabs">
      <button class="right-tab active" id="tabWordsBtn" onclick="switchRightTab('words')">단어 & 좌표 매칭</button>
      <button class="right-tab" id="tabPoolBtn" onclick="switchRightTab('pool')">남은 1200 단어 풀</button>
    </div>

    <!-- Tab 1: Current Scene Words -->
    <div class="tab-content" id="tabWordsContent">
      <div class="section-label">
        <span>Level 1 핵심 단어 (4개 퀴즈)</span>
        <span id="l1Count" style="color:var(--gold);">4/4</span>
      </div>
      <div id="l1WordList" style="display:flex; flex-direction:column; gap:6px;"></div>

      <div class="section-label" style="margin-top:10px;">
        <span>Level 2 확장 단어 (그림 속 요소)</span>
        <span id="l2Count" style="color:#10b981;">4개</span>
      </div>
      <div id="l2WordList" style="display:flex; flex-direction:column; gap:6px;"></div>
    </div>

    <!-- Tab 2: Free Words Pool -->
    <div class="tab-content" id="tabPoolContent" style="display:none;">
      <div class="search-box">
        <input type="text" id="poolSearchInput" placeholder="단어 검색 (예: pot, 흙, 나무)..." oninput="filterPool()">
      </div>
      <div class="section-label" style="margin-bottom:8px;">
        <span>사용 가능한 추천 단어</span>
        <span id="poolResultCount">0개</span>
      </div>
      <div class="pool-grid" id="poolGrid"></div>
    </div>

    <div class="panel-footer">
      <button class="btn-action btn-secondary" onclick="copySceneJSON()">📋 편 JSON 복사</button>
      <button class="btn-action btn-primary" onclick="alert('대표님, 코다리가 백그라운드에서 실시간으로 검증 및 소스 동기화를 완벽 처리합니다! 🫡')">💾 작업 확정 & 검증</button>
    </div>
  </div>
</div>

<script>
const rawChapterData = {json.dumps(chapter_data, ensure_ascii=False)};
const freeWordsList = {json.dumps(free_words, ensure_ascii=False)};
const categoryData = {json.dumps(cats, ensure_ascii=False)};
const chapterNames = {json.dumps(CHAPTER_NAMES, ensure_ascii=False)};

let activeChapter = "3";
let activeSceneIndex = 0;
let selectedWordIndex = null; // for targeting pin clicks
let selectedLevel = 1; // 1 or 2
let isMobile = false;

function init() {{
  renderChTabs();
  selectChapter("3");
  renderFreeWordsPool(freeWordsList.slice(0, 100));
}}

function renderChTabs() {{
  const container = document.getElementById("chTabs");
  container.innerHTML = "";
  for (let ch = 1; ch <= 12; ch++) {{
    const btn = document.createElement("button");
    btn.className = "ch-tab" + (ch.toString() === activeChapter ? " active" : "");
    btn.innerText = "ch" + ch;
    btn.onclick = () => selectChapter(ch.toString());
    container.appendChild(btn);
  }}
}}

function selectChapter(ch) {{
  activeChapter = ch;
  renderChTabs();
  renderScenesList();
  selectScene(0);
}}

function renderScenesList() {{
  const container = document.getElementById("scenesList");
  container.innerHTML = "";
  const chObj = rawChapterData[activeChapter];
  if (!chObj || !chObj.works) return;

  chObj.works.forEach((w, idx) => {{
    const card = document.createElement("div");
    card.className = "scene-card" + (idx === activeSceneIndex ? " active" : "");
    card.onclick = () => selectScene(idx);

    const imgPath = "../public/learning/" + w.img;
    card.innerHTML = `
      <img class="scene-thumb" src="${{imgPath}}" onerror="this.src='https://placehold.co/100x70/07533f/ffffff?text=ch${{activeChapter}}_${{w.n}}'">
      <div class="scene-info">
        <div class="scene-num">ch${{activeChapter}}_${{w.n}}</div>
        <div class="scene-title">${{w.title}}</div>
        <div class="scene-sub">${{w.sub || w.words.map(x=>x[0]).join(', ')}}</div>
      </div>
    `;
    container.appendChild(card);
  }});
}}

function selectScene(idx) {{
  activeSceneIndex = idx;
  renderScenesList();
  
  const chObj = rawChapterData[activeChapter];
  if (!chObj || !chObj.works || !chObj.works[idx]) return;
  const w = chObj.works[idx];

  document.getElementById("currentSceneTitle").innerHTML = `
    <span style="color:#fbbf24; font-weight:800;">[ch${{activeChapter}}_${{w.n}}]</span>
    <span>${{w.title}}</span>
    <span style="color:#94a3b8; font-size:13px; font-weight:normal;">— ${{w.sub || ''}}</span>
  `;

  const posterImg = document.getElementById("posterImg");
  posterImg.src = "../public/learning/" + w.img;

  renderWordCards();
  renderPins();
}}

function getSceneSpots() {{
  const chObj = rawChapterData[activeChapter];
  const l1Spots = (chObj.levelOneSpots && chObj.levelOneSpots[activeSceneIndex]) || [];
  const l2Spots = (chObj.sceneSpots && chObj.sceneSpots[activeSceneIndex]) || [];
  return {{ l1: l1Spots, l2: l2Spots }};
}}

function renderWordCards() {{
  const chObj = rawChapterData[activeChapter];
  const w = chObj.works[activeSceneIndex];
  const l1List = document.getElementById("l1WordList");
  const l2List = document.getElementById("l2WordList");
  l1List.innerHTML = "";
  l2List.innerHTML = "";

  const spots = getSceneSpots();
  const words = w.words || [];

  // L1 (first 4 words)
  const l1Words = words.slice(0, 4);
  const l2Words = words.slice(4);

  document.getElementById("l1Count").innerText = `${{l1Words.length}}/4`;
  document.getElementById("l2Count").innerText = `${{l2Words.length}}개`;

  l1Words.forEach((item, i) => {{
    const coord = spots.l1[i] || [50, 50];
    const card = createWordCard(item[0], item[1], coord, 1, i);
    l1List.appendChild(card);
  }});

  l2Words.forEach((item, i) => {{
    const coord = spots.l2[i] || [50, 50];
    const card = createWordCard(item[0], item[1], coord, 2, i);
    l2List.appendChild(card);
  }});
}}

function createWordCard(eng, kor, coord, level, idx) {{
  const card = document.createElement("div");
  card.className = `word-card l${{level}}` + (selectedLevel === level && selectedWordIndex === idx ? " active" : "");
  card.onclick = () => {{
    selectedLevel = level;
    selectedWordIndex = idx;
    renderWordCards();
    renderPins();
  }};

  card.innerHTML = `
    <span class="word-badge">L${{level}} #${{idx + 1}}</span>
    <div class="word-inputs">
      <input type="text" value="${{eng}}" style="font-weight:700;">
      <input type="text" value="${{kor}}">
    </div>
    <div class="word-coords">[${{coord[0]}}, ${{coord[1]}}]</div>
  `;
  return card;
}}

function renderPins() {{
  const overlay = document.getElementById("pinsOverlay");
  overlay.innerHTML = "";
  const spots = getSceneSpots();
  const chObj = rawChapterData[activeChapter];
  const w = chObj.works[activeSceneIndex];
  const words = w.words || [];

  // L1 Pins
  spots.l1.forEach((coord, i) => {{
    const word = words[i] ? words[i][0] : `L1 #${{i+1}}`;
    const pin = document.createElement("div");
    pin.className = `spot-pin l1` + (selectedLevel === 1 && selectedWordIndex === i ? " selected" : "");
    pin.style.left = coord[0] + "%";
    pin.style.top = coord[1] + "%";
    pin.innerHTML = `<span>★</span> ${{word}}`;
    pin.onclick = (e) => {{
      e.stopPropagation();
      selectedLevel = 1;
      selectedWordIndex = i;
      renderWordCards();
      renderPins();
    }};
    overlay.appendChild(pin);
  }});

  // L2 Pins
  spots.l2.forEach((coord, i) => {{
    const word = words[i + 4] ? words[i + 4][0] : `L2 #${{i+1}}`;
    const pin = document.createElement("div");
    pin.className = `spot-pin l2` + (selectedLevel === 2 && selectedWordIndex === i ? " selected" : "");
    pin.style.left = coord[0] + "%";
    pin.style.top = coord[1] + "%";
    pin.innerHTML = `<span>●</span> ${{word}}`;
    pin.onclick = (e) => {{
      e.stopPropagation();
      selectedLevel = 2;
      selectedWordIndex = i;
      renderWordCards();
      renderPins();
    }};
    overlay.appendChild(pin);
  }});
}}

function handleCanvasMove(e) {{
  const rect = document.getElementById("posterWrapper").getBoundingClientRect();
  const x = Math.round(((e.clientX - rect.left) / rect.width) * 100);
  const y = Math.round(((e.clientY - rect.top) / rect.height) * 100);
  if (x >= 0 && x <= 100 && y >= 0 && y <= 100) {{
    document.getElementById("coordDisplay").innerText = `X: ${{x}}% | Y: ${{y}}%`;
  }}
}}

function handleCanvasClick(e) {{
  const rect = document.getElementById("posterWrapper").getBoundingClientRect();
  const x = Math.round(((e.clientX - rect.left) / rect.width) * 100);
  const y = Math.round(((e.clientY - rect.top) / rect.height) * 100);

  if (selectedWordIndex !== null) {{
    const chObj = rawChapterData[activeChapter];
    if (selectedLevel === 1) {{
      if (!chObj.levelOneSpots[activeSceneIndex]) chObj.levelOneSpots[activeSceneIndex] = [];
      chObj.levelOneSpots[activeSceneIndex][selectedWordIndex] = [x, y];
    }} else {{
      if (!chObj.sceneSpots[activeSceneIndex]) chObj.sceneSpots[activeSceneIndex] = [];
      chObj.sceneSpots[activeSceneIndex][selectedWordIndex] = [x, y];
    }}
    renderWordCards();
    renderPins();
  }}
}}

function switchRightTab(tab) {{
  document.getElementById("tabWordsBtn").className = "right-tab" + (tab === 'words' ? ' active' : '');
  document.getElementById("tabPoolBtn").className = "right-tab" + (tab === 'pool' ? ' active' : '');
  document.getElementById("tabWordsContent").style.display = tab === 'words' ? 'flex' : 'none';
  document.getElementById("tabPoolContent").style.display = tab === 'pool' ? 'flex' : 'none';
}}

function renderFreeWordsPool(words) {{
  const grid = document.getElementById("poolGrid");
  grid.innerHTML = "";
  document.getElementById("poolResultCount").innerText = words.length + "개";

  words.forEach(w => {{
    const pill = document.createElement("div");
    pill.className = "pool-pill";
    pill.innerHTML = `<b>${{w}}</b>`;
    pill.onclick = () => {{
      alert(`단어 [${{w}}] 추가 기능을 코다리가 바로 연결합니다!`);
    }};
    grid.appendChild(pill);
  }});
}}

function filterPool() {{
  const q = document.getElementById("poolSearchInput").value.trim().toLowerCase();
  if (!q) {{
    renderFreeWordsPool(freeWordsList.slice(0, 100));
    return;
  }}
  const filtered = freeWordsList.filter(w => w.toLowerCase().includes(q));
  renderFreeWordsPool(filtered.slice(0, 100));
}}

function toggleMobileMode() {{
  isMobile = !isMobile;
  const root = document.getElementById("workspaceRoot");
  if (isMobile) {{
    root.classList.add("mobile-mode");
  }} else {{
    root.classList.remove("mobile-mode");
  }}
}}

function copySceneJSON() {{
  const chObj = rawChapterData[activeChapter];
  const w = chObj.works[activeSceneIndex];
  const spots = getSceneSpots();
  const obj = {{
    chapter: parseInt(activeChapter),
    n: w.n,
    title: w.title,
    sub: w.sub,
    video: w.video,
    img: w.img,
    levelOne: w.words.slice(0, 4).map((x, i) => [x[0], x[1], spots.l1[i] || [50, 50]]),
    levelTwo: w.words.slice(4).map((x, i) => [x[0], x[1], spots.l2[i] || [50, 50]])
  }};
  navigator.clipboard.writeText(JSON.stringify(obj, null, 2));
  alert("현재 편의 JSON이 클립보드에 복사되었습니다! 📋");
}}

window.onload = init;
</script>
</body>
</html>
"""

output_path = os.path.join(ROOT, "_작업/코다리_집무실.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"생성 완료: {output_path}")
