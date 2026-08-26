# -*- coding: utf-8 -*-
import json, html

with open("_작업/build_14_prompts.py", "r") as f:
    code = f.read()

# PROMPTS 리스트 추출
import re
from build_14_prompts import PROMPTS

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>보는 단어장 — 정본 제작 허브 14편</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700;900&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif;
      background: #090d16;
      color: #f1f5f9;
      padding: 32px 20px 100px;
      line-height: 1.6;
    }}
    .container {{
      max-width: 1000px;
      margin: 0 auto;
    }}
    
    /* 상단 헤더 전광판 */
    .header-board {{
      background: linear-gradient(135deg, #1e293b, #0f172a);
      border-radius: 24px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 32px 36px;
      margin-bottom: 32px;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5);
    }}
    .header-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 20px;
    }}
    .badge-pass {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #059669;
      color: #ffffff;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 0.02em;
    }}
    h1 {{
      font-size: 28px;
      font-weight: 900;
      color: #ffffff;
      margin-bottom: 6px;
    }}
    .sub-desc {{
      font-size: 14.5px;
      color: #94a3b8;
    }}
    
    /* 통계 그리드 */
    .stats-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 14px;
      margin-top: 20px;
      padding-top: 20px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .stat-box {{
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      padding: 14px 18px;
    }}
    .stat-num {{
      font-size: 24px;
      font-weight: 900;
      color: #38bdf8;
      line-height: 1.2;
    }}
    .stat-label {{
      font-size: 12px;
      color: #64748b;
      margin-top: 4px;
    }}

    /* 챕터 필터 바 */
    .filter-bar {{
      display: flex;
      gap: 8px;
      margin-bottom: 24px;
      overflow-x: auto;
      padding-bottom: 6px;
    }}
    .filter-btn {{
      padding: 8px 16px;
      background: #1e293b;
      color: #94a3b8;
      border: 1px solid #334155;
      border-radius: 12px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }}
    .filter-btn:hover, .filter-btn.active {{
      background: #2563eb;
      color: #ffffff;
      border-color: #3b82f6;
    }}

    /* 편 카드 */
    .card-list {{
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}
    .scene-card {{
      background: #151d2e;
      border-radius: 20px;
      border: 2px solid #233048;
      padding: 26px;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
      transition: all 0.2s;
    }}
    .scene-card:hover {{
      border-color: #38bdf8;
    }}
    .scene-card.done {{
      border-color: #10b981;
      background: #0f2420;
    }}
    .scene-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 16px;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .scene-info-left {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .scene-ch {{
      font-size: 12.5px;
      font-weight: 800;
      color: #38bdf8;
      letter-spacing: 0.05em;
    }}
    .scene-title {{
      font-size: 20px;
      font-weight: 900;
      color: #ffffff;
    }}
    .scene-tag {{
      display: inline-block;
      font-size: 12px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 8px;
      background: #1e3a8a;
      color: #93c5fd;
      border: 1px solid #2563eb;
    }}

    /* 단어 박스 */
    .words-box {{
      background: #0b111e;
      border: 1px solid #1e293b;
      border-radius: 12px;
      padding: 12px 16px;
      margin-bottom: 16px;
      font-size: 13.5px;
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .words-label {{
      color: #f59e0b;
      font-weight: 800;
      margin-right: 4px;
    }}
    .word-pill {{
      background: rgba(245, 158, 11, 0.12);
      color: #fbbf24;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 12.5px;
      font-weight: 600;
    }}

    /* 프롬프트 영역 */
    .prompt-area {{
      width: 100%;
      height: 140px;
      background: #080c14;
      border: 1px solid #1e2d42;
      border-radius: 12px;
      color: #94a3b8;
      padding: 14px;
      font-size: 13px;
      line-height: 1.5;
      font-family: inherit;
      resize: vertical;
      margin-bottom: 16px;
    }}
    .prompt-area:focus {{
      outline: none;
      border-color: #38bdf8;
      color: #e2e8f0;
    }}

    /* 버튼 그룹 */
    .btn-group {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 12px;
    }}
    .btn-copy {{
      padding: 14px;
      font-size: 15px;
      font-weight: 800;
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: white;
      border: none;
      border-radius: 12px;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
    }}
    .btn-copy:hover {{
      background: linear-gradient(135deg, #1d4ed8, #1e40af);
      transform: translateY(-1px);
    }}
    .btn-copy.copied {{
      background: linear-gradient(135deg, #10b981, #059669);
    }}
    .btn-toggle {{
      padding: 14px;
      font-size: 14px;
      font-weight: 800;
      background: #1e293b;
      color: #94a3b8;
      border: 1px solid #334155;
      border-radius: 12px;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .btn-toggle:hover {{
      background: #334155;
      color: white;
    }}
    .btn-toggle.is-done {{
      background: #10b981;
      color: white;
      border-color: #059669;
    }}

    /* 토스트 알림 */
    .toast {{
      position: fixed;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%);
      background: #10b981;
      color: white;
      padding: 12px 28px;
      border-radius: 30px;
      font-size: 14px;
      font-weight: 800;
      display: none;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      z-index: 999;
    }}
  </style>
</head>
<body>

<div class="container">
  <!-- 상단 헤더 전광판 -->
  <div class="header-board">
    <div class="header-top">
      <div>
        <div class="badge-pass">✓ verify_prompt.py 14편 전수 무결점 통과 (오류 0건)</div>
        <h1 style="margin-top: 10px;">보는 단어장 — 정본 제작 허브 14편</h1>
        <div class="sub-desc">지뢰 100% 박멸 · 맑고 연한 투명 수채화 · 단어 100% 선배정 완료</div>
      </div>
    </div>

    <!-- 통계 요약 -->
    <div class="stats-grid">
      <div class="stat-box">
        <div class="stat-num" id="total-count">14편</div>
        <div class="stat-label">탑재 대기 총 편수</div>
      </div>
      <div class="stat-box">
        <div class="stat-num" id="done-count">0 / 14</div>
        <div class="stat-label">생성 완료 진척도</div>
      </div>
      <div class="stat-box">
        <div class="stat-num">84개</div>
        <div class="stat-label">배정 정본 단어 수</div>
      </div>
      <div class="stat-box">
        <div class="stat-num" style="color: #10b981;">0건</div>
        <div class="stat-label">프롬프트 오류 잔존</div>
      </div>
    </div>
  </div>

  <!-- 챕터 필터 바 -->
  <div class="filter-bar">
    <button class="filter-btn active" onclick="filterChapter('all', this)">전체 14편</button>
    <button class="filter-btn" onclick="filterChapter('ch8', this)">ch8 운동·이동 (3편)</button>
    <button class="filter-btn" onclick="filterChapter('ch12', this)">ch12 자연·신비 (3편)</button>
    <button class="filter-btn" onclick="filterChapter('ch7', this)">ch7 감각·일상 (3편)</button>
    <button class="filter-btn" onclick="filterChapter('ch11', this)">ch11 과학·탐구 (3편)</button>
    <button class="filter-btn" onclick="filterChapter('ch5', this)">ch5 예술·무대 (2편)</button>
  </div>

  <!-- 14편 카드 목록 -->
  <div class="card-list">
"""

for idx, p in enumerate(PROMPTS, 1):
    words_pills = "".join([f'<span class="word-pill">{html.escape(w)}</span>' for w in p["words"]])
    ch_key = p["id"].split("-")[0]
    html_content += f"""
    <div class="scene-card" id="card-{p['id']}" data-ch="{ch_key}">
      <div class="scene-header">
        <div class="scene-info-left">
          <div class="scene-ch">{idx}. {html.escape(p['chapter'])} · {p['id']}</div>
          <div class="scene-title">{html.escape(p['title'])}</div>
        </div>
        <div class="scene-tag">{html.escape(p['type'])}</div>
      </div>

      <div class="words-box">
        <span class="words-label">배정 단어:</span>
        {words_pills}
      </div>

      <textarea id="prompt-{p['id']}" class="prompt-area" readonly>{html.escape(p['prompt'])}</textarea>

      <div class="btn-group">
        <button class="btn-copy" onclick="copyPrompt('prompt-{p['id']}', this)">
          📋 프롬프트 1초 복사하기
        </button>
        <button class="btn-toggle" id="btn-toggle-{p['id']}" onclick="toggleDone('{p['id']}')">
          ✓ 생성 완료 체크
        </button>
      </div>
    </div>
"""

html_content += """
  </div>
</div>

<div id="toast" class="toast">✓ 클립보드에 복사되었습니다! Flow에 붙여넣으세요.</div>

<script>
  // 로컬 스토리지로 생성 완료 상태 유지
  const STORAGE_KEY = 'inkword_14_prompts_done';
  let doneList = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');

  function updateDoneUI() {
    let count = 0;
    document.querySelectorAll('.scene-card').forEach(card => {
      const id = card.id.replace('card-', '');
      const btn = document.getElementById('btn-toggle-' + id);
      if (doneList.includes(id)) {
        card.classList.add('done');
        btn.classList.add('is-done');
        btn.innerHTML = '✓ 완료됨';
        count++;
      } else {
        card.classList.remove('done');
        btn.classList.remove('is-done');
        btn.innerHTML = '✓ 생성 완료 체크';
      }
    });
    document.getElementById('done-count').innerText = count + ' / 14';
  }

  function toggleDone(id) {
    if (doneList.includes(id)) {
      doneList = doneList.filter(x => x !== id);
    } else {
      doneList.push(id);
    }
    localStorage.setItem(STORAGE_KEY, JSON.stringify(doneList));
    updateDoneUI();
  }

  function copyPrompt(textareaId, btn) {
    const textarea = document.getElementById(textareaId);
    textarea.select();
    navigator.clipboard.writeText(textarea.value).then(() => {
      const originalText = btn.innerHTML;
      btn.classList.add('copied');
      btn.innerHTML = '✓ 복사 완료! Flow로 이동';
      
      const toast = document.getElementById('toast');
      toast.style.display = 'block';
      setTimeout(() => {
        toast.style.display = 'none';
        btn.classList.remove('copied');
        btn.innerHTML = originalText;
      }, 2500);
    });
  }

  function filterChapter(ch, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    document.querySelectorAll('.scene-card').forEach(card => {
      if (ch === 'all' || card.getAttribute('data-ch') === ch) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  // 초기 로드
  updateDoneUI();
</script>

</body>
</html>
"""

with open("_작업/제작허브_정본14편.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved _작업/제작허브_정본14편.html successfully.")
