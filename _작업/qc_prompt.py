#!/usr/bin/env python3
"""성공문법 정본(line-reveal 2026-08-09) 구조 검사기.

이 검사는 영상의 미적 품질을 PASS로 판정하지 않는다.
프롬프트 구조만 확인하며 최종 판정은 Flow 결과를 직접 보고 내린다.
"""

from pathlib import Path
import re
import sys

REQUIRED = [
    "The very first frame is an entirely empty pure white field",
    "central three-quarters of the frame",
    "equal narrow breathing margins on the left and right",
    "Static locked-off camera",
    "The only visible subjects throughout the sequence are",
    "0-4s:",
    "4-8s:",
    "ultra-fine pale warm-grey graphite linework",
    "horizon and camera axis are perfectly level",
    "Every detail becomes visible sequentially, never all at once",
    "All color remains low-saturation and transparent",
    "Restraint means low saturation, not fewer colors or shared hues",
    "All other elements remain still",
    "master-level fine-line illustration",
]

FORBIDDEN = [
    "Never:",
    "0-3.5s:",
    "3.5-5.5s:",
    "5.5-8s:",
    "cropped by the edge",
    "gathers compactly toward the center",
    "hair-thin dark-charcoal linework",
]

TERRA2_FORBIDDEN = ["thermometer", "temperature gauge", "dial", "instrument"]
ICE_REQUIRED = [
    "steam begins exactly at the rim of the first stack",
    "Temperature is shown only by a slightly smaller ice block",
    "The ice never emits steam, smoke, mist, vapor, haze, fog or any airborne effect",
]

HUMAN_TERMS = ["person", "patient", "character", "athlete", "officer", "guard", "child", "friends", "student", "reporter"]
HUMAN_REQUIRED = [
    "every person is a clearly illustrated educational character",
    "not photorealistic",
    "fully and modestly clothed",
    "no bare torso",
    "No uncanny or disturbing expression",
    "extra fingers",
]


def validate(path: Path, assigned_words: list[str]) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    fails: list[str] = []
    warnings: list[str] = []

    for phrase in REQUIRED:
        if phrase.lower() not in text.lower():
            fails.append(f"성공문법 필수 구절 누락: {phrase}")
    for phrase in FORBIDDEN:
        if phrase.lower() in text.lower():
            fails.append(f"실패문법 잔존: {phrase}")

    if any(re.search(rf"\b{term}\b", text, re.I) for term in HUMAN_TERMS):
        for phrase in HUMAN_REQUIRED:
            if phrase.lower() not in text.lower():
                fails.append(f"사람 장면 안전문법 누락: {phrase}")

    if "coastal rock with a seal" in text.lower():
        # 부정문에 들어가는 금지어는 허용하되, 피사체/동작으로 재등장하는지 확인한다.
        positive = text.split("There is no thermometer")[0]
        for term in TERRA2_FORBIDDEN:
            if term in positive.lower():
                fails.append(f"물범 장면에 인공 온도계 요소 잔존: {term}")

    if "roadside block of winter ice" in text.lower():
        for phrase in ICE_REQUIRED:
            if phrase.lower() not in text.lower():
                fails.append(f"녹는 얼음 공간분리 문법 누락: {phrase}")

    length = len(text)
    if not 1500 <= length <= 2400:
        warnings.append(f"분량 {length}자 — 권장 1,500~2,400자")

    subject_block = re.search(
        r"The only visible subjects throughout the sequence are (.+?)\.\n\n",
        text,
        flags=re.I | re.S,
    )
    if subject_block:
        count = len(re.findall(r"\b(one|two|three|four|five|a single|one small)\b", subject_block.group(1), re.I))
        if count > 6:
            warnings.append(f"피사체 수 표현 {count}개 — 화면 과밀 여부를 눈으로 확인")

    for word in assigned_words:
        if not re.search(rf"\b{re.escape(word)}\b", text, re.I):
            warnings.append(f'배정 단어 "{word}"가 프롬프트에 직접 나오지 않음')

    return fails, warnings


def main() -> int:
    if len(sys.argv) < 2:
        print('사용법: python3 _작업/qc_prompt.py 프롬프트.txt "word1 word2"')
        return 2

    path = Path(sys.argv[1])
    words = sys.argv[2].split() if len(sys.argv) > 2 else []
    fails, warnings = validate(path, words)

    print(f"파일: {path}")
    if fails:
        print("[구조 FAIL] Flow에 넣지 마세요.")
        for item in fails:
            print("  ✗", item)
    else:
        print("[구조 OK] 성공문법 형식 충족 — 영상 품질은 아직 미판정")
    for item in warnings:
        print("  △", item)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
