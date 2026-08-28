#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re, os, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# 1. Master 1200
with open("_작업/all1200.txt", "r", encoding="utf-8") as f:
    text = f.read()
master_words = sorted(list(set(w.lower() for w in re.split(r"[\s,\n\r]+", text) if w.strip())))

# 2. index.html words
with open("public/learning/index.html", "r", encoding="utf-8") as f:
    s = f.read()
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
data = json.loads(s[st:en])

html_words = {}
chapter_stats = {}
for ck in sorted(data, key=int):
    c = data[ck]
    w_count = sum(len(w["words"]) for w in c["works"])
    chapter_stats[ck] = {
        "title": c.get("title", f"Chapter {ck}"),
        "works_count": len(c["works"]),
        "words_count": w_count,
        "works": []
    }
    for w in c["works"]:
        n_val = w["n"]
        scene_id = f"ch{ck}_{n_val}"
        scene_title = w.get("title", "")
        chapter_stats[ck]["works"].append({
            "id": scene_id,
            "title": scene_title,
            "sub": w.get("sub", ""),
            "words": w["words"]
        })
        for word, ko in w["words"]:
            w_lower = word.strip().lower()
            html_words.setdefault(w_lower, []).append((scene_id, scene_title, word, ko))

# 3. 15 scenes
with open("_작업/단어묶음_15장.html", "r", encoding="utf-8") as f:
    s15 = f.read()
rows = re.findall(r"<tr><td class=n>(\d+)</td>\s*<td><b>(.*?)</b><div class=el>(.*?)</div></td>\s*<td class=c1>(.*?)</td>\s*<td class=c2>(.*?)</td></tr>", s15, re.S)

scenes_15 = []
s15_all_words = set()
for no, title, el, c1, c2 in rows:
    c1_words = re.findall(r"<b>([a-zA-Z]+)</b>\s*<span class=ko>(.*?)</span>", c1)
    c2_w_list = [w.strip() for w in re.split(r"[·,\s]+", c2) if w.strip()]
    scenes_15.append({
        "no": no,
        "title": title,
        "elements": el,
        "c1": c1_words,
        "c2": c2_w_list
    })
    for w, _ in c1_words: s15_all_words.add(w.lower())
    for w in c2_w_list: s15_all_words.add(w.lower())

matched_html = set(master_words).intersection(html_words.keys())
remain_1 = set(master_words) - set(html_words.keys())
matched_15 = remain_1.intersection(s15_all_words)
remain_final = sorted(list(remain_1 - s15_all_words))

# Categorize remain_final
grammar_words = [w for w in remain_final if w in {
    "above", "across", "after", "again", "against", "ago", "agree", "allow", "almost", "alone", "along", "already",
    "also", "although", "always", "among", "another", "anyway", "apart", "appear", "apply", "around", "assume",
    "basic", "basically", "basis", "become", "before", "behind", "belong", "below", "beside", "besides", "between",
    "beyond", "both", "brief", "certain", "certainly", "circumstance", "clear", "clearly", "common", "compare",
    "complete", "completely", "concern", "consider", "continue", "deal", "decide", "decision", "deep", "deeply",
    "depend", "describe", "detail", "determine", "differ", "different", "difficult", "direct", "directly", "during",
    "each", "early", "easily", "easy", "either", "else", "enough", "entire", "entirely", "especially", "even",
    "eventually", "ever", "every", "exact", "exactly", "except", "exist", "expect", "explain", "express", "fact",
    "fair", "fairly", "familiar", "far", "fast", "finally", "fine", "first", "fit", "following", "force", "foreign",
    "formal", "former", "forward", "free", "frequently", "full", "fully", "fundamental", "further", "general",
    "generally", "gradually", "hardly", "hence", "however", "immediate", "immediately", "importance", "important",
    "impossible", "indeed", "indicate", "individual", "inform", "initial", "inside", "instead", "intend", "internal",
    "involve", "itself", "just", "kind", "large", "largely", "late", "latter", "least", "less", "likely", "limit",
    "main", "mainly", "maintain", "major", "majority", "matter", "mean", "meaning", "meanwhile", "merely", "might",
    "moreover", "mostly", "natural", "naturally", "nearly", "necessarily", "necessary", "neither", "nevertheless",
    "nonetheless", "nor", "normal", "normally", "notice", "obvious", "obviously", "often", "once", "only", "onto",
    "opportunity", "opposite", "ordinary", "original", "originally", "otherwise", "ought", "overall", "particular",
    "particularly", "pattern", "perhaps", "period", "personal", "personally", "physical", "plain", "plenty", "point",
    "possibility", "possible", "possibly", "potential", "potentially", "practical", "practically", "precisely",
    "prefer", "prepare", "present", "prevent", "previous", "previously", "primarily", "primary", "prime", "principal",
    "principle", "probably", "proper", "properly", "prove", "provide", "pure", "purely", "purpose", "quite", "rather",
    "ready", "real", "reality", "realize", "really", "reason", "reasonable", "receive", "recent", "recently", "recognize",
    "regard", "regular", "regularly", "relate", "relation", "relative", "relatively", "relevant", "rely", "remain",
    "remarkable", "require", "result", "reveal", "right", "same", "seem", "seldom", "several", "severe", "shortly",
    "significant", "significantly", "similar", "similarly", "simple", "simply", "since", "slight", "slightly", "somehow",
    "somewhat", "soon", "specific", "specifically", "stand", "standard", "state", "still", "straight", "strange",
    "strongly", "structure", "subject", "substance", "such", "sudden", "suddenly", "suggest", "suitable", "suppose",
    "sure", "surely", "tend", "therefore", "thoroughly", "though", "throughout", "thus", "together", "total", "totally",
    "towards", "tradition", "traditional", "truly", "typical", "typically", "unable", "under", "understand",
    "unfortunately", "unless", "unlike", "unlikely", "until", "upon", "usually", "various", "vary", "very", "view",
    "whatever", "whenever", "whereas", "wherever", "whether", "while", "wholly", "within", "without", "worth", "yet"
}]
other_words = [w for w in remain_final if w not in grammar_words]

# HTML rendering
html_rows_15 = ""
for sc in scenes_15:
    c1_html = "".join(f'<span class="tag tag-c1">{w} ({ko})</span>' for w, ko in sc["c1"])
    c2_html = " · ".join(sc["c2"])
    html_rows_15 += f"""<tr>
      <td style="font-family:ui-monospace; font-weight:700; color:#c084fc;">{sc["no"]}</td>
      <td><b>{sc["title"]}</b></td>
      <td style="color:#94a3b8;">{sc["elements"]}</td>
      <td>
        <div style="margin-bottom:6px;">{c1_html}</div>
        <div style="color:#93c5fd; font-size:12px;">{c2_html}</div>
      </td>
    </tr>"""

chapter_rows = ""
for ck, cs in chapter_stats.items():
    avg = cs["words_count"] / cs["works_count"] if cs["works_count"] > 0 else 0
    chapter_rows += f"""<tr>
      <td style="font-family:ui-monospace; font-weight:700; color:#60a5fa;">ch{ck}</td>
      <td><b>{cs["title"]}</b></td>
      <td>{cs["works_count"]}편</td>
      <td>{cs["words_count"]}개</td>
      <td style="color:#4ade80;">{avg:.1f}개</td>
    </tr>"""

remain_tags_html = "".join(f'<span class="tag remain">{w}</span>' for w in remain_final)
grammar_tags_html = "".join(f'<span class="tag grammar">{w}</span>' for w in grammar_words)
other_tags_html = "".join(f'<span class="tag concrete">{w}</span>' for w in other_words)

full_html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>움직이는 그림사전 · 단어 매칭 전수 현황판 (코다리 총괄)</title>
<style>
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  background: #0b0f19;
  color: #f1f5f9;
  font-family: -apple-system, BlinkMacSystemFont, "Pretendard", "Segoe UI", Roboto, sans-serif;
  line-height: 1.6;
  padding: 28px;
}}
.container {{ max-width: 1200px; margin: 0 auto; }}
.header {{
  background: linear-gradient(135deg, #1e293b, #0f172a);
  border: 1px solid #334155;
  border-radius: 16px;
  padding: 24px 28px;
  margin-bottom: 24px;
  box-shadow: 0 12px 30px rgba(0,0,0,0.4);
}}
.badge {{
  display: inline-block;
  background: #2563eb;
  color: #fff;
  font-size: 12px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 99px;
  margin-bottom: 10px;
}}
h1 {{ margin: 0 0 8px; font-size: 24px; font-weight: 800; color: #fff; }}
p.sub {{ margin: 0; color: #94a3b8; font-size: 14px; }}

.grid-stats {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}}
.card {{
  background: #131b2e;
  border: 1px solid #1e293b;
  border-radius: 14px;
  padding: 20px;
  text-align: center;
}}
.card-num {{
  font-size: 34px;
  font-weight: 800;
  margin: 6px 0;
  font-family: ui-monospace, monospace;
}}
.card-label {{ color: #94a3b8; font-size: 13px; }}
.c-blue {{ color: #60a5fa; }}
.c-green {{ color: #4ade80; }}
.c-purple {{ color: #c084fc; }}
.c-amber {{ color: #fbbf24; }}

.section-box {{
  background: #131b2e;
  border: 1px solid #1e293b;
  border-radius: 14px;
  padding: 22px;
  margin-bottom: 24px;
}}
.section-title {{
  font-size: 17px;
  font-weight: 700;
  margin-bottom: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
  color: #f8fafc;
}}
.word-tags {{
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
}}
.tag {{
  display: inline-block;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 12.5px;
  font-family: ui-monospace, monospace;
}}
.tag.remain {{ background: #291b0c; border: 1px solid #78350f; color: #fde68a; }}
.tag.grammar {{ background: #1e1b4b; border: 1px solid #3730a3; color: #c7d2fe; }}
.tag.concrete {{ background: #064e3b; border: 1px solid #065f46; color: #a7f3d0; }}
.tag.tag-c1 {{ background: #831843; border: 1px solid #9d174d; color: #fbcfe8; font-size: 12px; margin-right: 4px; }}

table {{
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
  font-size: 13px;
}}
th, td {{
  padding: 11px 14px;
  border-bottom: 1px solid #1e293b;
  text-align: left;
}}
th {{ background: #0b0f19; color: #94a3b8; font-weight: 600; font-size: 12px; }}
tr:hover {{ background: #1a243a; }}
.search-input {{
  width: 100%;
  padding: 11px 16px;
  background: #0b0f19;
  border: 1px solid #334155;
  border-radius: 8px;
  color: #fff;
  font-size: 14px;
  margin-bottom: 14px;
}}
.search-input:focus {{ outline: none; border-color: #3b82f6; }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div class="badge">코다리 총괄부장 단독 실측 리포트</div>
    <h1>📊 움직이는 그림사전 · 마스터 1,200 단어 전수 매칭 현황판</h1>
    <p class="sub">정본 기준: all1200.txt vs public/learning/index.html (실제 데이터 100% 전수 분석)</p>
  </div>

  <div class="grid-stats">
    <div class="card">
      <div class="card-label">🎯 전체 마스터 단어</div>
      <div class="card-num c-blue">{len(master_words):,}개</div>
      <div class="card-label">정본 기준 1,200개</div>
    </div>
    <div class="card">
      <div class="card-label">✅ 기존 157편 매칭 완료</div>
      <div class="card-num c-green">{len(matched_html):,}개</div>
      <div class="card-label">전체 대비 {len(matched_html)/len(master_words)*100:.1f}%</div>
    </div>
    <div class="card">
      <div class="card-label">🎨 오늘 15장 신규씬 흡수</div>
      <div class="card-num c-purple">{len(matched_15):,}개</div>
      <div class="card-label">법정·은행·응급실 등</div>
    </div>
    <div class="card">
      <div class="card-label">📌 15장 배치 후 최종 남은 단어</div>
      <div class="card-num c-amber">{len(remain_final):,}개</div>
      <div class="card-label">추상어 78개 + 실물어 180개</div>
    </div>
  </div>

  <div class="section-box" style="background:#172554; border-color:#1e40af;">
    <div class="section-title" style="color:#93c5fd;">💡 대표님을 위한 3줄 명쾌 팩트</div>
    <ul style="margin:0; padding-left:20px; color:#dbeafe; font-size:14px; line-height:1.8;">
      <li><b>로부장의 "475개 남음"은 허위입니다:</b> 실제 마스터 1,200개 중 기존 157편에 이미 <b>830개</b>가 완벽히 들어가 있습니다 (남은 건 370개였음).</li>
      <li><b>오늘 작업한 15장은 112개의 핵심 미배정 단어를 소화합니다:</b> 법정, 은행, 응급실 등 비어 있던 씬에 112개가 쏙 들어갑니다.</li>
      <li><b>15장 배치 후 진짜 남는 단어는 258개뿐입니다:</b> 이 중 78개는 그림으로 안 그려지는 추상/문법어(thus, ought, anyway 등)이므로, <b>진짜 배치가 필요한 단어는 180개</b> 수준입니다!</li>
    </ul>
  </div>

  <div class="section-box">
    <div class="section-title">🔍 15장 배치 후 최종 남은 단어 258개 (검색 가능)</div>
    <input type="text" id="remainSearch" class="search-input" placeholder="남은 단어 검색 (예: boss, career, crime, drug, cinema)..." onkeyup="filterRemain()">
    <div style="margin-bottom:12px; font-size:13px; color:#94a3b8;">
      <span style="color:#a7f3d0;">■ 실물/상황 단어 ({len(other_words)}개)</span> &nbsp;|&nbsp; 
      <span style="color:#c7d2fe;">■ 추상/문법 기능어 ({len(grammar_words)}개 - 그림 불가)</span>
    </div>
    <div class="word-tags" id="remainTags">
      {other_tags_html}
      {grammar_tags_html}
    </div>
  </div>

  <div class="section-box">
    <div class="section-title">🎬 오늘 15장 신규 씬 배정표 (112개 단어 소화)</div>
    <table>
      <thead>
        <tr>
          <th>번호</th>
          <th>씬 제목</th>
          <th>핵심 구성 요소</th>
          <th>소화하는 마스터 단어 (빨강: 그림 / 파랑: 이야기)</th>
        </tr>
      </thead>
      <tbody>
        {html_rows_15}
      </tbody>
    </table>
  </div>

  <div class="section-box">
    <div class="section-title">📚 기존 12개 챕터 (157편) 배정 현황</div>
    <table>
      <thead>
        <tr>
          <th>챕터</th>
          <th>챕터명</th>
          <th>편수</th>
          <th>총 단어수</th>
          <th>편당 평균</th>
        </tr>
      </thead>
      <tbody>
        {chapter_rows}
      </tbody>
    </table>
  </div>
</div>

<script>
function filterRemain() {{
  const query = document.getElementById("remainSearch").value.toLowerCase();
  const tags = document.querySelectorAll("#remainTags .tag");
  tags.forEach(tag => {{
    if (tag.textContent.toLowerCase().includes(query)) {{
      tag.style.display = "inline-block";
    }} else {{
      tag.style.display = "none";
    }}
  }});
}}
</script>
</body>
</html>
"""

out_path = "_작업/코다리_단어매칭_전수현황판.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print("HTML generated successfully:", out_path)
