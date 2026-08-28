#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

P = json.load(open("_작업/_proms25.json", "r", encoding="utf-8"))

cards_html = ""
for i, item in enumerate(P, 1):
    title, el, l1, l2, ch, prompt = item
    l1_tags = " ".join([f"<span class=\"tag l1\">{w}</span>" for w in l1])
    l2_tags = " ".join([f"<span class=\"tag l2\">{w}</span>" for w in l2])
    
    cards_html += f"""
    <div class="card" id="card_{i:02d}">
      <div class="card-header">
        <div class="card-title-group">
          <span class="num-badge">{i:02d}</span>
          <h2 class="card-title">{title}</h2>
          <span class="ch-badge">기본 ch{ch}</span>
        </div>
        <button class="copy-btn" onclick="copyPrompt({i}, event)">📋 프롬프트 1초 복사</button>
      </div>
      <div class="card-meta">
        <div class="meta-row"><b>구성 사물:</b> {el}</div>
        <div class="meta-row"><b>L1 (그림 단어):</b> {l1_tags}</div>
        <div class="meta-row"><b>L2 (이야기 단어):</b> {l2_tags}</div>
      </div>
      <div class="prompt-box">
        <pre id="prompt_{i}">{prompt}</pre>
      </div>
    </div>
    """

full_html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>🎬 신규 영상 생성 프롬프트 작업대 (코다리 총괄)</title>
<style>
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  background: #090d16;
  color: #f1f5f9;
  font-family: -apple-system, BlinkMacSystemFont, "Pretendard", "Segoe UI", Roboto, sans-serif;
  line-height: 1.6;
  padding: 24px;
}}
.container {{ max-width: 1080px; margin: 0 auto; }}
.header {{
  background: linear-gradient(135deg, #1e1b4b, #0f172a);
  border: 1px solid #312e81;
  border-radius: 16px;
  padding: 24px 28px;
  margin-bottom: 24px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.4);
}}
.badge {{
  display: inline-block;
  background: #6366f1;
  color: #fff;
  font-size: 12px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 99px;
  margin-bottom: 8px;
}}
h1 {{ margin: 0 0 8px; font-size: 24px; font-weight: 800; color: #fff; }}
p.sub {{ margin: 0; color: #94a3b8; font-size: 14px; }}

.card {{
  background: #111827;
  border: 1px solid #1f2937;
  border-radius: 14px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}}
.card:hover {{ border-color: #374151; }}
.card-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 14px;
  flex-wrap: wrap;
  gap: 10px;
}}
.card-title-group {{
  display: flex;
  align-items: center;
  gap: 10px;
}}
.num-badge {{
  background: #374151;
  color: #fbbf24;
  font-weight: 800;
  font-family: ui-monospace, monospace;
  font-size: 15px;
  padding: 3px 9px;
  border-radius: 6px;
}}
.card-title {{
  margin: 0;
  font-size: 18px;
  font-weight: 700;
  color: #f8fafc;
}}
.ch-badge {{
  background: #1e293b;
  color: #94a3b8;
  font-size: 12px;
  padding: 2px 8px;
  border-radius: 4px;
}}
.copy-btn {{
  background: #2563eb;
  color: #fff;
  border: none;
  padding: 8px 18px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.15s, transform 0.1s;
}}
.copy-btn:hover {{ background: #1d4ed8; }}
.copy-btn:active {{ transform: scale(0.96); }}
.copy-btn.copied {{
  background: #059669 !important;
}}

.card-meta {{
  background: #0b0f19;
  border: 1px solid #1f2937;
  border-radius: 10px;
  padding: 12px 16px;
  font-size: 13px;
  margin-bottom: 14px;
}}
.meta-row {{ margin-bottom: 6px; }}
.meta-row:last-child {{ margin-bottom: 0; }}
.meta-row b {{ color: #94a3b8; margin-right: 6px; }}

.tag {{
  display: inline-block;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-family: ui-monospace, monospace;
}}
.tag.l1 {{ background: #831843; color: #fbcfe8; font-weight: 700; }}
.tag.l2 {{ background: #1e3a8a; color: #bfdbfe; }}

.prompt-box {{
  background: #030712;
  border: 1px solid #1f2937;
  border-radius: 10px;
  padding: 14px 16px;
  max-height: 180px;
  overflow-y: auto;
}}
pre {{
  margin: 0;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 12px;
  color: #cbd5e1;
  white-space: pre-wrap;
  word-break: break-word;
}}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div class="badge">검증 100% 통과 line-reveal 골격</div>
    <h1>🎬 신규 25편 영상 생성 프롬프트 작업대</h1>
    <p class="sub">버튼 한 번만 누르면 프롬프트가 즉시 복사됩니다. 영상 생성 툴에 붙여넣고 만드신 뒤, <code>01_...mp4</code>, <code>02_...mp4</code>로 저장하시면 됩니다!</p>
  </div>

  {cards_html}
</div>

<script>
function copyPrompt(id, evt) {{
  const pre = document.getElementById("prompt_" + id);
  const text = pre.innerText;
  navigator.clipboard.writeText(text).then(() => {{
    const btn = evt.target;
    const oldText = btn.innerText;
    btn.innerText = "✅ 복사 완료!";
    btn.classList.add("copied");
    setTimeout(() => {{
      btn.innerText = oldText;
      btn.classList.remove("copied");
    }}, 1500);
  }});
}}
</script>
</body>
</html>
"""

out_file = "_작업/프롬프트_생성작업대.html"
open(out_file, "w", encoding="utf-8").write(full_html)
subprocess.run(["open", out_file], check=False)
print(f"🚀 작업대 실행 완료: {out_file}")
