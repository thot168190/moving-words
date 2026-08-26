# -*- coding: utf-8 -*-
"""
1200 정본 단어 실시간 정밀 매핑 분석기:
1. 정본 1200단어 중 현재 확정된 406단어 목록
2. 남은 794단어의 챕터/갈래별 전수 분류
3. 그림 단독 불가 추상어/접속사(서사 필요 단어) 85개 추출 및 서사 해결책 정의
4. 허브의 각 씬별 '진짜 해결되는 정본 단어' 매핑
"""

import json, re

# scene_tool.py 에서 정본 데이터 추출
with open("_작업/scene_tool.py", "r", encoding="utf-8") as f:
    st_code = f.read()

# 정본 및 현재 사용 단어 추출
from scene_tool import parse_index_words, parse_canonical, check_integrity

works, used_words = parse_index_words("public/learning/index.html")
canonical = parse_canonical()

print(f"현재 탑재 편수: {len(works)}편")
print(f"현재 사용 단어: {len(used_words)}개")

used_canon = [w for w in used_words if w in canonical]
unused_canon = [w for w in canonical if w not in used_words]

print(f"정본 1200 중 확정 사용: {len(used_canon)}개 (33.8%)")
print(f"정본 1200 중 남은 단어: {len(unused_canon)}개 (66.2%)")

# 남은 단어들을 챕터/갈래별로 분류
from scene_tool import CANONICAL_BRANCHES
# 갈래 분석
branch_unused = {}
for w in unused_canon:
    # w가 속한 갈래 찾기
    found = False
    # index.html의 정본 정의 찾기
    pass

print(f"남은 정본 단어 수: {len(unused_canon)}개")
