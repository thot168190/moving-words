# -*- coding: utf-8 -*-
import io, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "public/learning/index.html")

s = io.open(SRC, encoding="utf-8").read()
i = s.index("const chapterData = {")
st = s.index("{", i)
d = 0
for j in range(st, len(s)):
    if s[j] == "{": d += 1
    elif s[j] == "}":
        d -= 1
        if d == 0: en = j + 1; break
data = json.loads(s[st:en])

report = []
report.append("=== 157편 전 장면 단어 매칭 전수조사 리포트 ===")

fake_count = 0
good_count = 0

for ch in range(1, 13):
    ch_k = str(ch)
    ch_obj = data[ch_k]
    report.append(f"\n[Chapter {ch}] ({len(ch_obj['works'])}편)")
    for idx, w in enumerate(ch_obj["works"]):
        l1 = ch_obj["levelOneWords"][idx]
        l2 = ch_obj["levelTwoWords"][idx]
        all_w = l1 + l2
        words_en = [pair[0] for pair in all_w]
        
        # 알파벳 몰림 검사 (예: 6개 단어가 전부 b로 시작하거나 c로 시작하는지)
        first_letters = [w_str[0].lower() for w_str in words_en]
        is_alpha_dump = len(set(first_letters)) <= 2 and len(first_letters) == 6
        
        status = "❌ 알파벳 억지 주입" if is_alpha_dump else "✅ 기존 매칭 / 확인 필요"
        if is_alpha_dump:
            fake_count += 1
        else:
            good_count += 1
            
        words_display = ", ".join([f"{a}({b})" for a, b in all_w])
        report.append(f"  {w['n']}. {w['title']} ({w['img']}) -> {status}\n     단어: {words_display}")

report.append(f"\n==========================================")
report.append(f"총계: 157편 중 억지 알파벳 주입 의심 {fake_count}편, 기존/기타 {good_count}편")

out_text = "\n".join(report)
print(out_text)

with open(os.path.join(ROOT, "_작업/전수조사_결과.txt"), "w", encoding="utf-8") as f:
    f.write(out_text)
