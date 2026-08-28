#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""스마트 영상 배치기 (코다리 총괄 업그레이드)
사용법: 
  1. Downloads 또는 바탕화면(현재작업다운로드 폴더 등)에 받은 mp4 이름 앞에 번호를 붙입니다 (01_..., 001_..., 1_...)
  2. python3 _작업/배치.py        → 어떤 파일이 발견되었고 어디로 옮겨질지 미리보기
  3. python3 _작업/배치.py --go   → 실제로 복사하고 포스터(jpg) 생성까지 원클릭 자동 실행
"""
import os, re, sys, glob, shutil, subprocess

HOME = os.path.expanduser("~")
SEARCH_DIRS = [
    os.path.join(HOME, "Downloads"),
    os.path.join(HOME, "Desktop", "현재작업다운로드"),
    os.path.join(HOME, "Desktop", "현재작업다운로드", "veo-folder-1"),
    os.path.join(HOME, "Desktop"),
]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LRN  = os.path.join(ROOT, "public", "learning")

# 번호 : (챕터, 새 파일번호, 제목, 부제)
MAP = {
 "01": ("9", "02", "그랜드 피아노와 건반", "올라간 댐퍼와 울림"),
 "02": ("9", "03", "어쿠스틱 기타와 울림통", "여섯 줄의 맑은 소리"),
 "03": ("9", "04", "바이올린과 활", "현을 켜는 소리"),
 "04": ("9", "05", "황동 트럼펫과 피스톤", "힘차게 뻗는 금관"),
 "05": ("9", "06", "피라미드 메트로놈", "박자를 세는 진자"),
 "06": ("9", "07", "중후한 첼로와 엔드핀", "낮고 깊은 울림"),
 "07": ("9", "08", "황동 색소폰과 키", "재즈의 풍부한 음색"),
 "08": ("9", "09", "프렌치 호른과 원형 관", "부드럽게 감싸는 관"),
 "09": ("9", "10", "은빛 플루트와 키", "가장 맑은 고음"),
 "10": ("9", "11", "흑단 클라리넷과 벨", "목관의 따뜻한 소리"),
}

def find(n):
    # n can be "01", look for patterns: 01_*, 001_*, 1_*
    int_n = int(n)
    patterns = [
        f"{n}_*.mp4", f"{n}.mp4", f"{n} *.mp4",
        f"{int_n:03d}_*.mp4", f"{int_n:03d}.mp4", f"{int_n:03d} *.mp4",
        f"{int_n}_*.mp4", f"{int_n}.mp4"
    ]
    all_found = []
    for d in SEARCH_DIRS:
        if not os.path.exists(d): continue
        for pat in patterns:
            matches = glob.glob(os.path.join(d, pat))
            all_found.extend(matches)
            submatches = glob.glob(os.path.join(d, "*", pat))
            all_found.extend(submatches)
    if all_found:
        all_found.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        return all_found[0]
    return None

def main():
    go = "--go" in sys.argv
    found, miss = [], []
    print("=" * 60)
    print("🔍 영상 파일 자동 검색 중... (Downloads / 바탕화면 / 현재작업다운로드)")
    print("=" * 60)
    for n in sorted(MAP):
        ch, no, title, sub = MAP[n]
        src = find(n)
        d   = os.path.join(LRN, "ch"+ch)
        dst = os.path.join(d, f"ch{ch}_{no}.mp4")
        pos = os.path.join(d, f"ch{ch}_{no}-poster.jpg")
        rel = f"ch{ch}/ch{ch}_{no}.mp4"
        if not src:
            miss.append((n, title, rel))
            continue
        found.append((n, ch, no, title, sub, rel, src, dst, pos))
        print(f"[{n}] {title:<12} 발견! → {os.path.basename(src)}")
        print(f"     목적지: public/learning/{rel}")

    print("\n" + "-" * 60)
    print(f"발견된 영상: {len(found)}개 / 아직 미발견: {len(miss)}개")
    if miss:
        print("  아직 없는 영상 번호:", ", ".join(f"{n}({t})" for n,t,r in miss))
    print("-" * 60)

    if go:
        done = []
        for n, ch, no, title, sub, rel, src, dst, pos in found:
            d = os.path.dirname(dst)
            os.makedirs(d, exist_ok=True)
            shutil.copy2(src, dst)
            subprocess.run(["ffmpeg","-y","-loglevel","error","-i",dst,
                            "-vf","select=eq(n\\,0)","-vframes","1","-q:v","3",pos],
                           check=False)
            done.append((n, ch, no, title, sub, rel))
            print(f"✅ 배치 완료: {rel} & 포스터 생성됨")

        print(f"\n🎉 총 {len(done)}개 영상 배치 및 포스터 추출 완료!")
    else:
        print("\n💡 실제로 복사 및 포스터를 생성하려면:")
        print("   python3 _작업/배치.py --go")

if __name__ == "__main__":
    main()
