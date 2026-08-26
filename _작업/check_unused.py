# -*- coding: utf-8 -*-
import json, re, csv

with open('public/learning/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines_list = text.split('\n')
start = 309
end = 7619
for idx in range(start, len(lines_list)):
    if lines_list[idx].strip().startswith('function ') and idx > 315:
        end = idx
        break

code = '\n'.join(lines_list[start:end]).strip()
while code and not code.endswith('}'): code = code[:-1].strip()
code = code.replace('const chapterData =', '').strip()
data = json.loads(code)

used_words = set()
existing_scenes = []
for ch_id, ch in data.items():
    for s in ch.get('works', []):
        existing_scenes.append(s.get('title', ''))
        for w in s.get('words', []):
            used_words.add(w[0].strip().lower())

# CSV 읽기
all_csv_words = {}
with open('_작업/1200_레벨태그_v3.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        w = row['단어'].strip().lower()
        all_csv_words[w] = row['갈래']

unused_by_cat = {}
unused_words = []
for w, cat in all_csv_words.items():
    if w not in used_words:
        unused_words.append(w)
        unused_by_cat.setdefault(cat, []).append(w)

print(f"정본 전체 단어: {len(all_csv_words)}개")
print(f"기존 66편 탑재 단어: {len(used_words)}개")
print(f"실제 남은 미사용 단어: {len(unused_words)}개 (소화율: {len(used_words)/len(all_csv_words)*100:.1f}%)")

print("\n=== 남은 단어 갈래별 개수 및 대표 단어 ===")
for cat, w_list in sorted(unused_by_cat.items(), key=lambda x: len(x[1]), reverse=True):
    sample_str = ", ".join(w_list[:6])
    print(f"- {cat} ({len(w_list)}개): {sample_str}...")

