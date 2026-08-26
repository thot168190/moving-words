# -*- coding: utf-8 -*-
"""
오직 단 하나의 정본 상황실 [_작업/제작허브.html]만 남기고 나머지 모든 과거/임시 허브 파일 100% 삭제 정리!
"""

import os, glob

# 삭제할 과거/임시 허브 파일 목록
junk_hubs = [
    "_작업/제작허브_3차신규10편.html",
    "_작업/제작허브_남은16편.html",
    "_작업/MENSA_부엌과밥상_전체통합허브.html",
    "_작업/DOMUS_우리집_전체통합허브.html"
]

for f in junk_hubs:
    if os.path.exists(f):
        os.remove(f)
        print(f"[삭제 완료] {f}")

print("\n오직 단 하나의 정본 [_작업/제작허브.html]만 남겼습니다!")
