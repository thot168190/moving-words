# -*- coding: utf-8 -*-
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BULK_DIR = os.path.join(ROOT, "_작업/bulk_26")

files = [
    ("bulk_part1_01_07.txt", "1차 벌크 (01~07편)", "우체국 · 응급실 · 법정 · 기차역 · 박물관 · 호텔 · 영화관"),
    ("bulk_part2_08_14.txt", "2차 벌크 (08~14편)", "옛성 · 감옥창살 · 실험실 · 방직공장 · 헬리콥터 · 로켓 · 거리행진"),
    ("bulk_part3_15_20.txt", "3차 벌크 (15~20편)", "가게계산대 · 은행창구 · 식당차림표 · 머리목해부도 · 기계제어반 · 석탄광차"),
    ("bulk_part4_21_26.txt", "4차 벌크 (21~26편)", "가족사진틀 · 광장군중 · 군용장비 · 시인책상 · 골프그린 · 초원얼룩말"),
]

html_parts = []
html_parts.append("""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>새로 그릴 그림 26장 — 4분할 벌크 프롬프트 허브 (화이트 에디션)</title>
<style>
  * { box-sizing: border-box; }
  body { margin: 0; background: #f8fafc; color: #1e293b; font-family: Pretendard, -apple-system, sans-serif; line-height: 1.6; }
  header { position: sticky; top: 0; background: #ffffff; border-bottom: 1px solid #e2e8f0; padding: 16px 24px; display: flex; gap: 14px; align-items: center; justify-content: space-between; z-index: 99; box-shadow: 0 1px 3px rgba(0,0,0,0.03); }
  h1 { font-size: 18px; margin: 0; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 8px; }
  .badge { background: #059669; color: #ffffff; font-size: 12px; padding: 4px 10px; border-radius: 6px; font-weight: 700; }
  main { padding: 28px 24px; max-width: 1200px; margin: 0 auto; }
  .info-box { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px 20px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
  .info-box b { color: #0f172a; }
  .batch-card { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 22px; margin-bottom: 28px; box-shadow: 0 2px 5px rgba(0,0,0,0.03); }
  .batch-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; padding-bottom: 14px; border-bottom: 1px solid #f1f5f9; }
  .batch-title { font-size: 17px; font-weight: 800; color: #1d4ed8; }
  .batch-desc { font-size: 13px; color: #64748b; margin-top: 4px; }
  .copy-btn { background: #059669; color: #ffffff; border: 0; border-radius: 8px; padding: 10px 20px; font-size: 14px; font-weight: 700; cursor: pointer; transition: all 0.15s; }
  .copy-btn:hover { background: #047857; transform: translateY(-1px); }
  pre { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px; font-family: ui-monospace, monospace; font-size: 12px; color: #334155; white-space: pre-wrap; word-break: break-all; max-height: 480px; overflow-y: auto; line-height: 1.6; }
</style>
</head>
<body>
<header>
  <div>
    <h1>🔒 새로 그릴 그림 26장 — 4분할 벌크 프롬프트</h1>
    <div style="font-size: 13px; color: #64748b; margin-top: 2px;">영구잠금 세필수채 최종합격 공식 100% 적용</div>
  </div>
  <span class="badge">총 26편 · 4분할 복사 준비완료</span>
</header>
<main>
  <div class="info-box">
    <b>💡 원클릭 벌크 복사 안내</b><br>
    각 파트 우측의 <b>[전체 복사]</b> 버튼을 누르시면 해당 묶음의 프롬프트가 한 번에 클립보드에 복사되어 영상 생성기에 바로 붙여넣으실 수 있습니다.
  </div>
""")

for idx, (filename, title, desc) in enumerate(files):
    filepath = os.path.join(BULK_DIR, filename)
    content = open(filepath, encoding="utf-8").read()
    html_parts.append(f"""
  <div class="batch-card" id="part_{idx+1}">
    <div class="batch-head">
      <div>
        <div class="batch-title">📦 {title}</div>
        <div class="batch-desc">{desc}</div>
      </div>
      <button class="copy-btn" onclick="copyBatch('text_{idx+1}', this)">{title} 전체 복사</button>
    </div>
    <pre id="text_{idx+1}">{content}</pre>
  </div>
""")

html_parts.append("""
</main>
<script>
async function copyBatch(id, btn) {
  const text = document.getElementById(id).textContent;
  try {
    await navigator.clipboard.writeText(text);
    const orig = btn.textContent;
    btn.textContent = '복사 완료! ✓';
    btn.style.background = '#047857';
    setTimeout(() => {
      btn.textContent = orig;
      btn.style.background = '#059669';
    }, 1800);
  } catch(e) {
    alert('복사 실패');
  }
}
</script>
</body>
</html>
""")

out_html = os.path.join(ROOT, "_작업/bulk_26_복사허브.html")
with open(out_html, "w", encoding="utf-8") as f:
    f.write("".join(html_parts))

print("화이트 테마 허브 생성 완료:", out_html)
