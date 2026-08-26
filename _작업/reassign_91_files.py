# -*- coding: utf-8 -*-
import io, csv, os, shutil, glob

# 91편 재배정 규칙 정의
# 1) 천체관측 10편: ch11_04 ~ ch11_13 (기존 그대로)
# 2) 서재도구 10편: ch11_14~23 -> ch4_14 ~ ch4_23
# 3) 교통 11편: ch5_06 ~ ch5_16 (기존 그대로)
# 4) 날씨 10편: ch10_05 ~ ch10_14 (기존 그대로)
# 5) 조류곤충 10편: ch2_24~33 -> ch2_14 ~ ch2_23 (ch2는 10편만!)
# 6) 정원원예 10편: ch2_14~23 -> ch3_11 ~ ch3_20 (ch3로 이동!)
# 7) 미술공예 10편: ch4_04 ~ ch4_13 (기존 그대로)
# 8) 캠핑 10편: ch12_05~09 & ch6_07~11 -> ch8_05 ~ ch8_14 (ch8로 이동!)
# 9) 음악 10편: ch5_17~21 & ch12_10~14 -> ch9_02 ~ ch9_11 (ch9로 이동!)

# 임시 작업 디렉토리
tmp_dir = "_작업/tmp_reassign"
os.makedirs(tmp_dir, exist_ok=True)

# 1. 141편 대장 로드
with open("_작업/141편_대장.csv", "r", encoding="utf-8-sig") as f:
    catalog = list(csv.DictReader(f))

# 기존 파일들을 일단 안전하게 tmp로 복사 및 목록 작성
mapping = []

# 대장 항목별 새 배정 결정
for r in catalog:
    s_name = r["세트"]
    p_no = str(r["프롬프트번호"]).zfill(3)
    curr_ch = r["배정챕터"]
    curr_file = r["새파일명"]
    
    new_ch = curr_ch
    new_file = curr_file
    
    if "1,2차" in s_name:
        # 천체관측 10편
        new_ch = "ch11"
        idx = int(p_no) + 3 # 001 -> 04
        new_file = f"ch11_{idx:02d}.mp4"
    elif "9차" in s_name:
        # 서재도구 10편 -> ch4
        new_ch = "ch4"
        idx = int(p_no) + 13 # 001 -> 14
        new_file = f"ch4_{idx:02d}.mp4"
    elif "3차" in s_name:
        # 교통 11편 -> ch5
        new_ch = "ch5"
        idx = int(p_no) + 5 # 001 -> 06
        new_file = f"ch5_{idx:02d}.mp4"
    elif "7차" in s_name:
        # 사계절날씨 10편 -> ch10
        new_ch = "ch10"
        idx = int(p_no) + 4 # 001 -> 05
        new_file = f"ch10_{idx:02d}.mp4"
    elif "8차" in s_name:
        # 조류곤충 10편 -> ch2
        new_ch = "ch2"
        idx = int(p_no) + 13 # 001 -> 14
        new_file = f"ch2_{idx:02d}.mp4"
    elif "5차" in s_name:
        # 정원원예 10편 -> ch3
        new_ch = "ch3"
        idx = int(p_no) + 10 # 001 -> 11 (ch3는 기존 10편 있음)
        new_file = f"ch3_{idx:02d}.mp4"
    elif "6차" in s_name:
        # 미술공예 10편 -> ch4
        new_ch = "ch4"
        idx = int(p_no) + 3 # 001 -> 04
        new_file = f"ch4_{idx:02d}.mp4"
    elif "4차" in s_name:
        # 캠핑 10편 -> ch8 (기존 ch8은 4편 있음 -> 05부터 시작)
        new_ch = "ch8"
        idx = int(p_no) + 4 # 001 -> 05
        new_file = f"ch8_{idx:02d}.mp4"
    elif "11차" in s_name:
        # 음악 10편 (1~10번 사용) -> ch9 (기존 ch9는 1편 있음 -> 02부터 시작)
        new_ch = "ch9"
        idx = int(p_no) + 1 # 001 -> 02
        new_file = f"ch9_{idx:02d}.mp4"

    # 이전 위치 파일 확인
    old_mp4_path = os.path.join("public/learning", curr_ch, curr_file)
    old_jpg_path = old_mp4_path.replace(".mp4", "-poster.jpg")
    
    new_mp4_path = os.path.join("public/learning", new_ch, new_file)
    new_jpg_path = new_mp4_path.replace(".mp4", "-poster.jpg")
    
    mapping.append({
        "row": r,
        "old_mp4": old_mp4_path,
        "old_jpg": old_jpg_path,
        "new_ch": new_ch,
        "new_file": new_file,
        "new_mp4": new_mp4_path,
        "new_jpg": new_jpg_path
    })

# 파일 이동 전 백업 복사 (tmp로)
for m in mapping:
    if os.path.exists(m["old_mp4"]):
        shutil.copy2(m["old_mp4"], tmp_dir)
    if os.path.exists(m["old_jpg"]):
        shutil.copy2(m["old_jpg"], tmp_dir)

# 불필요해진 이전 신규 파일들 정리 (기존 원본 66편은 절대 건드리지 않음!)
# 기존 원본 파일 보호 목록:
# ch1: scene-ch1-* (10편)
# ch2: scene-ch2-01~13 (13편)
# ch3: ch3_01~10 (10편)
# ch4: scene-ch4-01~03 (3편)
# ch5: scene-ch5-01~05 (5편)
# ch6: scene-ch6-01~06 (6편)
# ch7: scene-ch7-01~04 (4편)
# ch8: scene-ch8-01~04 (4편)
# ch9: scene-ch9-01 (1편)
# ch10: scene-ch10-01~03 (3편) + ch10_01~04 (기존)
# ch11: scene-ch11-01~03 (3편)
# ch12: scene-ch12-01~04 (4편) + ch12_01~04 (기존)

# tmp에서 new 경로로 복사 & 이전 위치 정리
for m in mapping:
    src_mp4 = os.path.join(tmp_dir, os.path.basename(m["old_mp4"]))
    src_jpg = os.path.join(tmp_dir, os.path.basename(m["old_jpg"]))
    
    os.makedirs(os.path.dirname(m["new_mp4"]), exist_ok=True)
    if os.path.exists(src_mp4):
        shutil.copy2(src_mp4, m["new_mp4"])
    if os.path.exists(src_jpg):
        shutil.copy2(src_jpg, m["new_jpg"])

    # 만약 old_mp4와 new_mp4가 다르면 old 파일 삭제 (단, 신규 배정 파일 패턴인 경우만)
    if m["old_mp4"] != m["new_mp4"]:
        if os.path.exists(m["old_mp4"]):
            os.remove(m["old_mp4"])
        if os.path.exists(m["old_jpg"]):
            os.remove(m["old_jpg"])

    # 대장 갱신
    m["row"]["배정챕터"] = m["new_ch"]
    m["row"]["새파일명"] = m["new_file"]

# 대장 CSV 저장
with open("_작업/141편_대장.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=catalog[0].keys())
    writer.writeheader()
    writer.writerows(catalog)

print("✅ STEP 1 파일 재배정 및 대장 갱신 완료!")

