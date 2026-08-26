# -*- coding: utf-8 -*-
"""
오직 단 하나의 정본 상황실: [_작업/제작허브.html]
- 상단에 명확한 버전 숫자 [v5.0 FINAL (2026-08-25)] 크게 표시
- Set 08 ~ Set 13 100% 신규 단어 & 1씬 1사물 완벽 탑재
- 원클릭 벌크 복사 지원
"""

import json, datetime

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    sets_data = json.load(f)

html_template = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[v5.0 FINAL] 보는 단어장 1200단어 마스터 정본 상황실</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif;
      background: #050811;
      color: #f1f5f9;
      padding: 24px 20px 100px;
      line-height: 1.6;
    }
    .container {
      max-width: 1100px;
      margin: 0 auto;
    }
    
    /* 대시보드 헤더 */
    .master-header {
      background: linear-gradient(135deg, #0d1b32, #060e1c);
      border-radius: 24px;
      border: 2px solid #10b981;
      padding: 26px 32px;
      margin-bottom: 24px;
      box-shadow: 0 16px 40px rgba(16, 185, 129, 0.25);
    }
    .status-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 12px;
    }
    .version-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #10b981;
      color: #ffffff;
      padding: 8px 18px;
      border-radius: 20px;
      font-size: 16px;
      font-weight: 900;
      letter-spacing: 0.5px;
    }
    .live-dot {
      width: 10px;
      height: 10px;
      background: #ffffff;
      border-radius: 50%;
      box-shadow: 0 0 10px #ffffff;
      animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
      0% { transform: scale(0.95); opacity: 0.8; }
      50% { transform: scale(1.2); opacity: 1; }
      100% { transform: scale(0.95); opacity: 0.8; }
    }
    .time-tag {
      font-size: 13.5px;
      color: #94a3b8;
      font-weight: 600;
    }
    
    h1 {
      font-size: 26px;
      font-weight: 900;
      color: #ffffff;
      letter-spacing: -0.5px;
      margin-top: 4px;
    }
    
    /* 탭 바 */
    .tabs-container {
      margin-top: 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 12px;
    }
    .tabs-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .tab-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #94a3b8;
      padding: 9px 16px;
      border-radius: 12px;
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .tab-btn:hover {
      background: rgba(255, 255, 255, 0.1);
      color: #ffffff;
    }
    .tab-btn.active {
      background: #10b981;
      border-color: #10b981;
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);
    }
    
    /* 액션 바 */
    .action-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      background: #091222;
      border: 1px solid rgba(16, 185, 129, 0.3);
      border-radius: 16px;
      padding: 16px 22px;
      margin-top: 16px;
    }
    .btn-bulk-copy {
      background: linear-gradient(135deg, #10b981, #059669);
      color: #ffffff;
      border: none;
      padding: 13px 26px;
      border-radius: 12px;
      font-size: 15px;
      font-weight: 900;
      cursor: pointer;
      box-shadow: 0 4px 18px rgba(16, 185, 129, 0.4);
      transition: all 0.2s ease;
    }
    .btn-bulk-copy:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 24px rgba(16, 185, 129, 0.6);
    }
    
    /* 카드 리스트 */
    .cards-wrapper {
      margin-top: 20px;
    }
    .prompt-card {
      background: #0b1325;
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 18px;
      padding: 20px 24px;
      margin-bottom: 16px;
    }
    .card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 10px;
    }
    .scene-title {
      font-size: 17px;
      font-weight: 800;
      color: #38bdf8;
    }
    .word-badge {
      display: inline-block;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #6ee7b7;
      padding: 3px 9px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      margin-bottom: 6px;
    }
    .prompt-box {
      background: #040711;
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 10px;
      padding: 14px 16px;
      font-size: 13px;
      color: #cbd5e1;
      line-height: 1.5;
      font-family: ui-monospace, monospace;
      white-space: pre-wrap;
      max-height: 140px;
      overflow-y: auto;
      margin-bottom: 10px;
    }
    .btn-single-copy {
      background: rgba(255, 255, 255, 0.08);
      color: #e2e8f0;
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 7px 14px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
    }
    .btn-single-copy:hover {
      background: rgba(255, 255, 255, 0.15);
      color: #ffffff;
    }
    
    .toast {
      position: fixed;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #10b981;
      color: #ffffff;
      padding: 12px 28px;
      border-radius: 30px;
      font-weight: 900;
      font-size: 15px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      opacity: 0;
      pointer-events: none;
      z-index: 9999;
    }
    .toast.show {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="master-header">
      <div class="status-row">
        <span class="version-badge"><span class="live-dot"></span> v5.0 FINAL (최종 정본)</span>
        <span class="time-tag">최신 갱신: """ + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</span>
      </div>
      
      <h1>보는 단어장 1200단어 제작 상황실 (v5.0 FINAL)</h1>
      <p style="color: #34d399; font-size: 14px; margin-top: 6px; font-weight: 700;">
        ✓ 손(Hand) 0% 완전 박멸 · 단어 중복 0% · 1씬 1사물(단일 히어로) · 30% 수채화 틴트 락 장착
      </p>
      
      <!-- 세트 탭 버튼 -->
      <div class="tabs-container">
        <div class="tabs-bar" id="tabsBar"></div>
      </div>

      <!-- 액션 바 -->
      <div class="action-bar">
        <div>
          <div style="font-size: 16px; font-weight: 800; color: #f8fafc;" id="currentSetName">로딩 중...</div>
          <div style="font-size: 13px; color: #34d399; margin-top: 3px;" id="currentSetTarget"></div>
        </div>
        <button class="btn-bulk-copy" id="bulkCopyBtn" onclick="copyCurrentBulk()">
          📋 이 세트 10편 전체 벌크 복사
        </button>
      </div>
    </div>

    <!-- 카드 리스트 -->
    <div class="cards-wrapper" id="cardsList"></div>
  </div>

  <div class="toast" id="toast">📋 클립보드에 복사되었습니다!</div>

  <script>
    const allData = """ + json.dumps(sets_data, ensure_ascii=False) + """;
    let activeSetId = "set08"; // 기본 Set 08로 활성화!

    function renderTabs() {
      const bar = document.getElementById("tabsBar");
      bar.innerHTML = "";
      allData.forEach(s => {
        const btn = document.createElement("button");
        btn.className = "tab-btn" + (s.set_id === activeSetId ? " active" : "");
        btn.innerText = (s.set_id === "set08" ? "🚀 " : "") + s.set_name;
        btn.onclick = () => switchSet(s.set_id);
        bar.appendChild(btn);
      });
    }

    function switchSet(setId) {
      activeSetId = setId;
      renderTabs();
      renderContent();
    }

    function renderContent() {
      const curSet = allData.find(s => s.set_id === activeSetId) || allData[0];
      document.getElementById("currentSetName").innerText = curSet.set_name + " (10편)";
      document.getElementById("currentSetTarget").innerText = "타겟: " + curSet.target_chapter + " · " + curSet.target_branches;
      document.getElementById("bulkCopyBtn").innerText = "📋 " + curSet.set_name + " 10편 전체 벌크 복사";

      const container = document.getElementById("cardsList");
      container.innerHTML = "";

      curSet.prompts.forEach((p, idx) => {
        const card = document.createElement("div");
        card.className = "prompt-card";

        const wordsHtml = p.words.map(w => `<span class="word-badge">${w}</span>`).join(" ");

        card.innerHTML = `
          <div class="card-top">
            <div>
              <div class="scene-title">${idx + 1}. ${p.title}</div>
              <div style="margin-top: 6px;">${wordsHtml}</div>
            </div>
            <button class="btn-single-copy" onclick="copySinglePrompt('${p.id}')">단일 복사</button>
          </div>
          <div class="prompt-box" id="box_${p.id}">${p.prompt}</div>
        `;
        container.appendChild(card);
      });
    }

    function showToast(msg) {
      const toast = document.getElementById("toast");
      toast.innerText = msg;
      toast.classList.add("show");
      setTimeout(() => toast.classList.remove("show"), 2200);
    }

    function copyCurrentBulk() {
      const curSet = allData.find(s => s.set_id === activeSetId);
      if (!curSet) return;
      const text = curSet.prompts.map(p => p.prompt).join("\\n\\n");
      navigator.clipboard.writeText(text).then(() => {
        showToast("🚀 " + curSet.set_name + " 10편 전체가 클립보드에 복사되었습니다!");
      });
    }

    function copySinglePrompt(id) {
      let targetText = "";
      allData.forEach(s => {
        s.prompts.forEach(p => {
          if (p.id === id) targetText = p.prompt;
        });
      });
      if (targetText) {
        navigator.clipboard.writeText(targetText).then(() => {
          showToast("✓ 프롬프트 1편이 복사되었습니다!");
        });
      }
    }

    // 초기 실행
    renderTabs();
    renderContent();
  </script>
</body>
</html>
"""

with open("_작업/제작허브.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Saved _작업/제작허브.html (v5.0 FINAL) successfully!")

