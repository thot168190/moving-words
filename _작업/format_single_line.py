# -*- coding: utf-8 -*-
import json, re, html
from build_next_10_prompts import NEXT_10_PROMPTS

# 1. 2차 10편을 각각 한 줄로 압축
single_line_prompts = []
for p in NEXT_10_PROMPTS:
    clean_line = " ".join(p["prompt"].split())
    single_line_prompts.append({
        "id": p["id"],
        "chapter": p["chapter"],
        "title": p["title"],
        "words": p["words"],
        "prompt": clean_line
    })

# 2. 파일 저장 (각 편당 정확히 1줄)
with open("_작업/google_flow_bulk_set2_10.txt", "w", encoding="utf-8") as f:
    for item in single_line_prompts:
        f.write(item["prompt"] + "\n\n")

print(f"Set 2 10편 단일 라인 변환 완료 (총 {len(single_line_prompts)}편)")

# 3. HTML 허브 갱신
prompts_json = json.dumps([p["prompt"] for p in single_line_prompts])

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>보는 단어장 — 2차 완전 신규 10편 벌크 허브 (정확히 10편 인식)</title>
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
    
    .btn-bulk {{
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #ffffff;
      border: none;
      padding: 16px 28px;
      border-radius: 14px;
      font-size: 16px;
      font-weight: 800;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      transition: all 0.2s ease;
      box-shadow: 0 4px 15px rgba(37, 99, 235, 0.35);
      margin-top: 15px;
    }}
    .btn-bulk:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5);
    }}
    
    .prompt-card {{
      background: #131d2e;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 18px;
      padding: 24px;
      margin-bottom: 20px;
    }}
    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
    }}
    .scene-title {{
      font-size: 19px;
      font-weight: 800;
      color: #f8fafc;
    }}
    .words-badge {{
      display: inline-block;
      background: rgba(56, 189, 248, 0.12);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 4px 10px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      margin-bottom: 10px;
    }}
    .prompt-box {{
      background: #090e17;
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 12px;
      padding: 14px;
      font-size: 13.5px;
      color: #cbd5e1;
      line-height: 1.5;
      font-family: ui-monospace, monospace;
      white-space: pre-wrap;
      max-height: 160px;
      overflow-y: auto;
      margin-bottom: 12px;
    }}
    .btn-copy {{
      background: rgba(255, 255, 255, 0.08);
      color: #e2e8f0;
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
    }}
    .btn-copy:hover {{
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
      padding: 12px 24px;
      border-radius: 30px;
      font-weight: 800;
      font-size: 15px;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
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
    <div class="header-board">
      <div class="header-top">
        <div>
          <span class="badge-pass">✓ Flow 벌크 10편 정확 인식 보장 (단일 라인 포맷)</span>
          <h1 style="margin-top: 8px;">2차 완전 신규 10편 벌크 허브</h1>
          <p class="sub-desc">각 프롬프트가 한 줄로 압축되어 Flow에서 정확히 10편으로 인식됩니다.</p>
        </div>
      </div>
      
      <button class="btn-bulk" onclick="copyBulk()">
        📋 2차 10편 전체 벌크 복사 (정확히 10편 입력용)
      </button>
    </div>

    <div id="cardsList">
"""

for i, p in enumerate(single_line_prompts, 1):
    p_id = p["id"]
    p_title = p["title"]
    p_chapter = p["chapter"]
    p_words = ", ".join(p["words"])
    p_prompt = p["prompt"]
    
    html_content += f"""
      <div class="prompt-card">
        <div class="card-top">
          <div>
            <div class="words-badge">{p_chapter}</div>
            <div class="scene-title">{i:02d}. {p_title}</div>
            <div style="font-size: 13px; color: #94a3b8; margin-top: 4px;">배정 단어: <strong>{p_words}</strong></div>
          </div>
          <button class="btn-copy" onclick="copySingle('{p_id}')">단편 복사</button>
        </div>
        <div class="prompt-box" id="text-{p_id}">{html.escape(p_prompt)}</div>
      </div>
    """

html_content += f"""
    </div>
  </div>

  <div id="toast" class="toast">클립보드에 복사되었습니다!</div>

  <script>
    const promptsArray = {prompts_json};
    
    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.classList.add('show');
      setTimeout(() => {{
        t.classList.remove('show');
      }}, 2000);
    }}

    function copyBulk() {{
      const text = promptsArray.join('\\n\\n');
      navigator.clipboard.writeText(text).then(() => {{
        showToast('정확히 10편의 프롬프트가 복사되었습니다! (Flow에서 10편으로 인식)');
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
  </script>
</body>
</html>
"""

with open("_작업/제작허브_2차신규10편.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved _작업/제작허브_2차신규10편.html successfully.")
