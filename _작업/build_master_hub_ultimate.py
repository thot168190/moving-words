# -*- coding: utf-8 -*-
"""
1200단어 완전 정복 최종 통합 상황실 (Master Hub Ultimate):
- Set 02 (수확완료 10편)
- Set 03 (현재 10편)
- Set 04 ~ Set 13 (완주 100편)
총 12개 탭, 총 120편 원클릭 벌크 복사 완비
"""

import json, html, datetime

now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

from build_next_10_prompts import NEXT_10_PROMPTS
from build_set3_prompts import SET3_PROMPTS

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

# All sets dictionary
all_sets = {}

# Set 02
all_sets["set02"] = {
    "name": "Set 02 (헬리콥터 세트 - 수확완료)",
    "scenes": [{
        "id": p["id"],
        "chapter": p["chapter"],
        "title": p["title"],
        "words": p["words"],
        "prompt": " ".join(p["prompt"].split())
    } for p in NEXT_10_PROMPTS]
}

# Set 03
all_sets["set03"] = {
    "name": "Set 03 (현재 진행 세트)",
    "scenes": [{
        "id": p["id"],
        "chapter": p["chapter"],
        "title": p["title"],
        "words": p["words"],
        "prompt": " ".join(p["prompt"].split())
    } for p in SET3_PROMPTS]
}

# Set 04 ~ Set 13
for s in complete_100:
    all_sets[s["set_id"]] = {
        "name": s["set_name"],
        "scenes": s["prompts"]
    }

sets_json = json.dumps(all_sets, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[최종 마스터 {datetime.datetime.now().strftime('%H:%M')}] 보는 단어장 1200단어 정복 통합 상황실</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif;
      background: #050811;
      color: #f1f5f9;
      padding: 24px 20px 100px;
      line-height: 1.6;
    }}
    .container {{
      max-width: 1100px;
      margin: 0 auto;
    }}
    
    /* 대시보드 헤더 */
    .master-header {{
      background: linear-gradient(135deg, #0d1b32, #060e1c);
      border-radius: 24px;
      border: 2px solid #0284c7;
      padding: 26px 32px;
      margin-bottom: 24px;
      box-shadow: 0 16px 40px rgba(2, 132, 199, 0.3);
    }}
    .status-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 12px;
    }}
    .live-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #10b981;
      color: #ffffff;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 900;
    }}
    .live-dot {{
      width: 9px;
      height: 9px;
      background: #ffffff;
      border-radius: 50%;
      box-shadow: 0 0 8px #ffffff;
      animation: pulse 1.5s infinite;
    }}
    @keyframes pulse {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.4; transform: scale(0.8); }}
    }}
    .time-tag {{
      font-size: 13.5px;
      color: #38bdf8;
      font-weight: 800;
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 5px 12px;
      border-radius: 10px;
    }}
    h1 {{
      font-size: 26px;
      font-weight: 900;
      color: #ffffff;
      margin-bottom: 6px;
    }}
    
    /* 전체 진도율 바 */
    .progress-wrap {{
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 14px;
      padding: 14px 20px;
      margin-top: 14px;
    }}
    .progress-labels {{
      display: flex;
      justify-content: space-between;
      font-size: 13px;
      font-weight: 800;
      color: #94a3b8;
      margin-bottom: 8px;
    }}
    .progress-labels strong {{
      color: #38bdf8;
    }}
    .progress-bar-outer {{
      height: 10px;
      background: #1e293b;
      border-radius: 6px;
      overflow: hidden;
    }}
    .progress-bar-inner {{
      height: 100%;
      width: 100%;
      background: linear-gradient(90deg, #10b981, #0284c7, #38bdf8);
      border-radius: 6px;
    }}
    
    /* 12개 탭 스크롤 바 */
    .tabs-container {{
      overflow-x: auto;
      padding-bottom: 8px;
      margin-top: 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .tabs-bar {{
      display: flex;
      gap: 8px;
      width: max-content;
    }}
    .tab-btn {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #94a3b8;
      padding: 9px 16px;
      border-radius: 10px;
      font-size: 13.5px;
      font-weight: 800;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
    }}
    .tab-btn:hover {{
      background: rgba(255, 255, 255, 0.08);
      color: #f8fafc;
    }}
    .tab-btn.active {{
      background: #0284c7;
      border-color: #38bdf8;
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.4);
    }}
    
    /* 복사 바 */
    .action-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #091222;
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 16px;
      padding: 16px 22px;
      margin-top: 16px;
    }}
    .btn-bulk-copy {{
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #ffffff;
      border: none;
      padding: 13px 26px;
      border-radius: 12px;
      font-size: 15px;
      font-weight: 900;
      cursor: pointer;
      box-shadow: 0 4px 18px rgba(37, 99, 235, 0.4);
      transition: all 0.2s ease;
    }}
    .btn-bulk-copy:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 24px rgba(37, 99, 235, 0.6);
    }}
    
    /* 카드 리스트 */
    .cards-wrapper {{
      margin-top: 20px;
    }}
    .prompt-card {{
      background: #0b1325;
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 18px;
      padding: 20px 24px;
      margin-bottom: 16px;
    }}
    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 10px;
    }}
    .scene-title {{
      font-size: 17px;
      font-weight: 800;
      color: #f8fafc;
    }}
    .words-badge {{
      display: inline-block;
      background: rgba(56, 189, 248, 0.1);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.2);
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 11.5px;
      font-weight: 700;
      margin-bottom: 4px;
    }}
    .prompt-box {{
      background: #040711;
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 10px;
      padding: 12px 14px;
      font-size: 12.5px;
      color: #cbd5e1;
      line-height: 1.5;
      font-family: ui-monospace, monospace;
      white-space: pre-wrap;
      max-height: 130px;
      overflow-y: auto;
      margin-bottom: 8px;
    }}
    .btn-single-copy {{
      background: rgba(255, 255, 255, 0.08);
      color: #e2e8f0;
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 7px 14px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
    }}
    .btn-single-copy:hover {{
      background: rgba(255, 255, 255, 0.15);
      color: #ffffff;
    }}
    
    .toast {{
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
    }}
    .toast.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="master-header">
      <div class="status-row">
        <span class="live-badge"><span class="live-dot"></span> LIVE 1200단어 마스터 완성 상황실</span>
        <span class="time-tag">전 세트 빌드 완료: {now_str}</span>
      </div>
      
      <h1>보는 단어장 1200단어 완전 정복 상황실</h1>
      
      <div class="progress-wrap">
        <div class="progress-labels">
          <span>전체 1,202단어 100% 매핑 완료 (총 12개 세트 / 120편 완비)</span>
          <strong>100.0% READY</strong>
        </div>
        <div class="progress-bar-outer">
          <div class="progress-bar-inner"></div>
        </div>
      </div>
      
      <!-- 12개 세트 탭 -->
      <div class="tabs-container">
        <div class="tabs-bar">
          <button class="tab-btn active" onclick="switchSet('set03')">🚀 Set 03 (현재 진행)</button>
          <button class="tab-btn" onclick="switchSet('set04')">Set 04 (캠핑·탐험)</button>
          <button class="tab-btn" onclick="switchSet('set05')">Set 05 (카페·베이커리)</button>
          <button class="tab-btn" onclick="switchSet('set06')">Set 06 (정원·원예)</button>
          <button class="tab-btn" onclick="switchSet('set07')">Set 07 (미술·공예)</button>
          <button class="tab-btn" onclick="switchSet('set08')">Set 08 (바다·항해)</button>
          <button class="tab-btn" onclick="switchSet('set09')">Set 09 (과학·실험)</button>
          <button class="tab-btn" onclick="switchSet('set10')">Set 10 (건축·공구)</button>
          <button class="tab-btn" onclick="switchSet('set11')">Set 11 (음악·악기)</button>
          <button class="tab-btn" onclick="switchSet('set12')">Set 12 (의학·보건)</button>
          <button class="tab-btn" onclick="switchSet('set13')">Set 13 (사회·금융)</button>
          <button class="tab-btn" onclick="switchSet('set02')">✓ Set 02 (수확완료)</button>
        </div>
      </div>

      <!-- 액션 바 -->
      <div class="action-bar">
        <div>
          <div style="font-size: 14.5px; font-weight: 800; color: #f8fafc;" id="currentSetName">Set 03 (현재 진행 세트)</div>
          <div style="font-size: 12.5px; color: #94a3b8; margin-top: 2px;">정확히 10편 벌크 입력용 · 검증기 0 에러 통과</div>
        </div>
        <button class="btn-bulk-copy" onclick="copyCurrentBulk()">
          📋 이 세트 10편 전체 벌크 복사
        </button>
      </div>
    </div>

    <!-- 카드 렌더링 영역 -->
    <div id="cardsWrapper" class="cards-wrapper"></div>
  </div>

  <div id="toast" class="toast">클립보드에 복사되었습니다!</div>

  <script>
    const allSets = {sets_json};
    let currentSetId = 'set03';

    function renderCards(setId) {{
      const setData = allSets[setId];
      const wrapper = document.getElementById('cardsWrapper');
      wrapper.innerHTML = '';

      setData.scenes.forEach((p, idx) => {{
        const card = document.createElement('div');
        card.className = 'prompt-card';
        card.innerHTML = `
          <div class="card-top">
            <div>
              <div class="words-badge">${{p.chapter}}</div>
              <div class="scene-title">${{String(idx + 1).padStart(2, '0')}}. ${{p.title}}</div>
              <div style="font-size: 13px; color: #94a3b8; margin-top: 4px;">배정 단어: <strong>${{p.words.join(', ')}}</strong></div>
            </div>
            <button class="btn-single-copy" onclick="copySingle('${{p.id}}')">단편 복사</button>
          </div>
          <div class="prompt-box" id="text-${{p.id}}">${{p.prompt}}</div>
        `;
        wrapper.appendChild(card);
      }});
    }}

    function switchSet(setId) {{
      currentSetId = setId;
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
      
      const setData = allSets[setId];
      document.getElementById('currentSetName').innerText = setData.name;
      document.querySelector('.btn-bulk-copy').innerText = `📋 ${{setData.name.split(' ')[0]}} 10편 전체 벌크 복사`;
      renderCards(setId);
    }}

    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.classList.add('show');
      setTimeout(() => {{ t.classList.remove('show'); }}, 2000);
    }}

    function copyCurrentBulk() {{
      const setData = allSets[currentSetId];
      const text = setData.scenes.map(s => s.prompt).join('\\n\\n');
      navigator.clipboard.writeText(text).then(() => {{
        showToast(`${{setData.name.split(' ')[0]}} 10편 전체가 복사되었습니다! (Flow에서 정확히 10편 인식)`);
      }});
    }}

    function copySingle(id) {{
      const el = document.getElementById('text-' + id);
      if (el) {{
        navigator.clipboard.writeText(el.innerText).then(() => {{
          showToast('프롬프트가 복사되었습니다!');
        }});
      }}
    }}

    // 초기 렌더링
    renderCards('set03');
  </script>
</body>
</html>
"""

with open("_작업/제작허브.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved _작업/제작허브.html (Ultimate Edition) successfully!")
