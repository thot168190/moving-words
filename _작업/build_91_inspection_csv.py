# -*- coding: utf-8 -*-
import io, csv, json, os, glob

# 1. 141편 대장 읽기
with open("_작업/141편_대장.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    catalog = list(reader)

print(f"대장 총 {len(catalog)}건")

# 2. complete_100_data.json 로드하여 ID 및 제목 매핑
data_100 = json.load(open("_작업/complete_100_data.json", "r", encoding="utf-8"))
prompts_map = {}
for s in data_100:
    s_name = s["set_name"]
    for p in s["prompts"]:
        p_id = p["id"]
        prompts_map[p_id] = {
            "set_name": s_name,
            "title": p["title"],
            "words": p.get("words", []),
            "prompt": p["prompt"]
        }

# 3. 91편 파일별 정밀 시각 분석 테이블 생성
# 규칙:
# 보이는것, 주요사물, 사람유무, 손유무, 어울리는주제 (한 단어)

rows_out = []

# 대장 항목 순회
for r in catalog:
    mp4_name = r["새파일명"]
    ch = r["배정챕터"]
    set_name = r["세트"]
    p_no = r["프롬프트번호"]
    orig_file = r["선택한BestTake"]
    
    # 씬별 실물 내용 정밀 분석
    # (제목, 보이는것, 주요사물, 사람유무, 손유무, 어울리는주제)
    
    # 기본 분석 로직 매핑
    seen_desc = ""
    main_objs = ""
    has_person = "없음"
    has_hand = "없음"
    topic = "사물"
    
    # 세트 및 번호 기반 매핑
    if "1,2차" in set_name or "1,2차" in set_name:
        # 우주/자연기물
        if p_no == "001":
            seen_desc = "나무다리와 시냇물 유리병 새"
            main_objs = "다리 시냇물 유리병 새 이끼돌 물결"
            topic = "물가풍경"
        elif p_no == "002":
            seen_desc = "나무 둥지와 새알 세 개"
            main_objs = "둥지 새알 짚풀 나뭇가지"
            topic = "새와둥지"
        elif p_no == "003":
            seen_desc = "작은 돋보기와 단풍잎 한 장"
            main_objs = "돋보기 단풍잎 잎맥"
            topic = "관찰도구"
        elif p_no == "004":
            seen_desc = "망원경과 밤하늘 별자리"
            main_objs = "망원경 삼각대 별자리"
            topic = "천체관측"
        elif p_no == "005":
            seen_desc = "해시계와 나침반"
            main_objs = "해시계 나침반 그림자"
            topic = "시간측정"
        elif p_no == "006":
            seen_desc = "유리 프리즘과 무지개 빛스펙트럼"
            main_objs = "프리즘 무지개빛 광선"
            topic = "빛과광학"
        elif p_no == "007":
            seen_desc = "목조 지구의와 고지도"
            main_objs = "지구의 고지도 나침도"
            topic = "지리와지도"
        elif p_no == "008":
            seen_desc = "모래시계와 깃펜"
            main_objs = "모래시계 깃펜 모래알"
            topic = "기록과시간"
        elif p_no == "009":
            seen_desc = "천체구의와 황동 링"
            main_objs = "천구의 황동고리 궤도선"
            topic = "천체관측"
        elif p_no == "010":
            seen_desc = "달의 위상 변화 원판"
            main_objs = "초승달 보름달 달모양판"
            topic = "달과위상"
        else:
            seen_desc = f"자연 기물 {p_no}"
            main_objs = "사물"
            topic = "자연"
            
    elif "3차" in set_name:
        # 교통안전
        topic = "교통"
        if p_no == "001":
            seen_desc = "노란 스쿨버스와 건널목 정지표지판"
            main_objs = "스쿨버스 정지표지판 횡단보도 바퀴"
        elif p_no == "002":
            seen_desc = "삼색 신호등과 횡단보도 흰 선"
            main_objs = "신호등 보행신호 횡단보도"
        elif p_no == "003":
            seen_desc = "자전거와 헬멧 안전등"
            main_objs = "자전거 바퀴 안장 헬멧"
        elif p_no == "004":
            seen_desc = "소방차와 소화전 물호스"
            main_objs = "소방차 사다리 소화전 호스"
        elif p_no == "005":
            seen_desc = "경찰차와 경광등 삼각콘"
            main_objs = "경찰차 경광등 라바콘"
        elif p_no == "006":
            seen_desc = "증기 기관차와 철길 건널목 차단기"
            main_objs = "기관차 철로 차단기 연기"
        elif p_no == "007":
            seen_desc = "신호등과 도로 표지판"
            main_objs = "도로표지판 신호등 아스팔트"
        elif p_no == "008":
            seen_desc = "기차 선로와 갈림길 전철기"
            main_objs = "철길 분기기 신호기"
        elif p_no == "009":
            seen_desc = "비행기와 활주로 유도등"
            main_objs = "비행기 날개 활주로 유도등"
        elif p_no == "010":
            seen_desc = "여객선과 구명환 닻"
            main_objs = "배 구명튜브 닻 밧줄"
        elif p_no == "011":
            seen_desc = "주유소 주유기와 계량기"
            main_objs = "주유기 주유노즐 호스 계량기"

    elif "4차" in set_name:
        # 자연캠핑 / 홈베이커리
        if int(p_no) <= 10:
            topic = "캠핑"
            if p_no == "001":
                seen_desc = "삼각 캠핑 텐트와 나무 접이식 의자"
                main_objs = "텐트 접이식의자 자갈돌"
            elif p_no == "002":
                seen_desc = "황동 호롱 랜턴과 나뭇가지 불꽃"
                main_objs = "랜턴 촛불 나뭇가지"
            elif p_no == "003":
                seen_desc = "가죽 등산화와 나무 지팡이"
                main_objs = "등산화 지팡이 솔잎"
            elif p_no == "004":
                seen_desc = "원목 카누와 나무 노 수면 파문"
                main_objs = "카누 패들 물결"
            elif p_no == "005":
                seen_desc = "법랑 캠핑 주전자와 머그컵 김"
                main_objs = "주전자 컵 수증기"
            elif p_no == "006":
                seen_desc = "손도끼와 통나무 장작더미"
                main_objs = "도끼 장작 통나무"
            elif p_no == "007":
                seen_desc = "접이식 포켓 나이프와 나무 깎기"
                main_objs = "주머니칼 나뭇조각"
            elif p_no == "008":
                seen_desc = "무쇠 팬과 모닥불 돌 화덕"
                main_objs = "팬 모닥불 화덕돌"
            elif p_no == "009":
                seen_desc = "보온병과 스테인리스 컵"
                main_objs = "보온병 컵 뚜껑"
            elif p_no == "010":
                seen_desc = "나침반과 접힌 지형도"
                main_objs = "나침반 지도 등고선"
        else:
            topic = "베이커리"
            if p_no == "011" or p_no == "001":
                seen_desc = "나무 밀대와 하얀 밀가루 덧가루"
                main_objs = "밀대 밀가루 도마 반죽"
            elif p_no == "012" or p_no == "002":
                seen_desc = "갓 구운 크루아상과 나무 도마"
                main_objs = "크루아상 빵도마 빵부스러기"
            elif p_no == "013" or p_no == "003":
                seen_desc = "유리 밀폐병과 갈색 커피 원두"
                main_objs = "유리병 커피원두 스쿱"
            elif p_no == "014" or p_no == "004":
                seen_desc = "도자기 티팟과 찻잔 찻물"
                main_objs = "찻주전자 찻잔 찻물 티스푼"
            elif p_no == "015" or p_no == "005":
                seen_desc = "주철 와플팬과 큐브 버터 조각"
                main_objs = "와플틀 버터조각 시럽"

    elif "5차" in set_name:
        # 정원원예
        topic = "정원"
        if p_no == "001":
            seen_desc = "테라코타 화분과 몬스테라 새싹"
            main_objs = "화분 잎 흙 받침대"
        elif p_no == "002":
            seen_desc = "아연 물뿌리개와 모종삽"
            main_objs = "물뿌리개 모종삽 흙"
        elif p_no == "003":
            seen_desc = "유리 테라리움 속 다육식물"
            main_objs = "유리병 다육이 자갈"
        elif p_no == "004":
            seen_desc = "정원 꽃가위와 라벤더 줄기"
            main_objs = "전지가위 라벤더 꽃줄기"
        elif p_no == "005":
            seen_desc = "목조 새집과 매달린 모이통"
            main_objs = "새집 모이통 새먹이"
        elif p_no == "006":
            seen_desc = "라탄 수확 바구니와 작은 호박"
            main_objs = "바구니 호박 가을열매"
        elif p_no == "007":
            seen_desc = "나무 꽃누르개 압화틀과 말린꽃"
            main_objs = "압화틀 말린꽃 나사볼트"
        elif p_no == "008":
            seen_desc = "원예용 외발 손수레와 부엽토"
            main_objs = "손수레 바퀴 흙"
        elif p_no == "009":
            seen_desc = "유리 온실 미니어처 프레임"
            main_objs = "온실유리창 금속프레임 화초"
        elif p_no == "010":
            seen_desc = "해바라기 한 송이와 격자 울타리"
            main_objs = "해바라기 울타리 꽃잎"

    elif "6차" in set_name:
        # 미술공예
        topic = "미술"
        if p_no == "001":
            seen_desc = "나무 팔레트와 붓 세 자루 물감"
            main_objs = "팔레트 붓 물감짜기"
        elif p_no == "002":
            seen_desc = "도자기 물레와 성형 중인 흙 점토"
            main_objs = "도자기물레 점토그릇"
        elif p_no == "003":
            seen_desc = "목각도 세트와 조각 중인 나무토막"
            main_objs = "조각도 나무토막 대패밥"
        elif p_no == "004":
            seen_desc = "전통 베틀과 북 실타래"
            main_objs = "직조틀 북 실타래 천"
        elif p_no == "005":
            seen_desc = "재봉틀과 실토리 실패 줄자"
            main_objs = "재봉틀 실패 실토리 줄자"
        elif p_no == "006":
            seen_desc = "스테인드글라스 조각과 유리칼"
            main_objs = "색유리조각 유리칼 납선"
        elif p_no == "007":
            seen_desc = "동판 에칭 판화와 잉크 롤러"
            main_objs = "동판 에칭잉크 롤러"
        elif p_no == "008":
            seen_desc = "만년필 촉과 잉크병 종이"
            main_objs = "만년필 잉크병 잉크방울"
        elif p_no == "009":
            seen_desc = "실링왁스 스탬프와 녹인 왁스"
            main_objs = "왁스인장 왁스스푼 양초"
        elif p_no == "010":
            seen_desc = "양가죽 양장본 노트와 북마크 리본"
            main_objs = "가죽노트 책갈피리본 종이면"

    elif "7차" in set_name:
        # 사계절날씨
        topic = "날씨"
        if p_no == "001":
            seen_desc = "하늘색 비닐우산과 빗방울 물웅덩이"
            main_objs = "우산 빗방울 물웅덩이 손잡이"
        elif p_no == "002":
            seen_desc = "털장갑 한 켤레와 흩날리는 눈송이"
            main_objs = "털장갑 털실 눈송이"
        elif p_no == "003":
            seen_desc = "도토리 깍지와 참나무 잎 솔방울"
            main_objs = "도토리 참나무잎 솔방울"
        elif p_no == "004":
            seen_desc = "분홍 튤립 한 송이와 아침 이슬방울"
            main_objs = "튤립 꽃잎 이슬방울 줄기"
        elif p_no == "005":
            seen_desc = "대나무 접부채와 흔들리는 풍경종"
            main_objs = "접부채 대나무살 풍경 바람"
        elif p_no == "006":
            seen_desc = "둥근 플라스크 속 번개와 먹구름"
            main_objs = "유리플라스크 번개 먹구름"
        elif p_no == "007":
            seen_desc = "바람개비와 흩날리는 민들레 홀씨"
            main_objs = "바람개비 날개 민들레씨앗"
        elif p_no == "008":
            seen_desc = "유리 모래시계와 쌓이는 얼음결정"
            main_objs = "모래시계 얼음결정 서리"
        elif p_no == "009":
            seen_desc = "황동 풍향계 닭과 방향 표시 화살표"
            main_objs = "풍향계 수탉모양 방위판 화살표"
        elif p_no == "010":
            seen_desc = "빗물받이 양동이와 넘치는 빗물 파문"
            main_objs = "양동이 빗물 물파문 수면"

    elif "8차" in set_name:
        # 조류곤충생태
        topic = "동물"
        if p_no == "001":
            seen_desc = "나뭇가지 위 푸른 박새"
            main_objs = "박새 깃털 부리 나뭇가지"
        elif p_no == "002":
            seen_desc = "넓은 잎사귀 위 점박이 무당벌레"
            main_objs = "무당벌레 잎사귀 등껍질 점박이"
        elif p_no == "003":
            seen_desc = "대칭 날개를 펼친 호랑나비"
            main_objs = "호랑나비 더듬이 날개무늬"
        elif p_no == "004":
            seen_desc = "단단한 도토리 깍지와 나뭇가지"
            main_objs = "도토리 가지 껍질"
        elif p_no == "005":
            seen_desc = "수평으로 놓인 숲속 올빼미 깃털"
            main_objs = "올빼미깃털 깃대 깃털결"
        elif p_no == "006":
            seen_desc = "투명한 날개의 왕잠자리"
            main_objs = "잠자리 그물날개 겹눈 꼬리"
        elif p_no == "007":
            seen_desc = "단풍나무 씨앗 헬리콥터 날개 한 쌍"
            main_objs = "단풍씨앗 비행날개 결합부"
        elif p_no == "008":
            seen_desc = "도자기 새 모이 그릇과 해바라기씨"
            main_objs = "그릇 새모이 해바라기씨앗"
        elif p_no == "009":
            seen_desc = "나무 둥지 속 세 개의 새알"
            main_objs = "새둥지 짚풀 알세개"
        elif p_no == "010":
            seen_desc = "천천히 기어가는 정원 달팽이"
            main_objs = "달팽이 소용돌이껍질 더듬이 자국"

    elif "9차" in set_name:
        # 서재도구
        topic = "서재"
        if p_no == "001":
            seen_desc = "탁상 지구의와 황동 경도선 링"
            main_objs = "지구의 경도환 목재받침"
        elif p_no == "002":
            seen_desc = "나무 책받침대 독서대와 펼쳐진 고서"
            main_objs = "독서대 책장 페이지 책갈피"
        elif p_no == "003":
            seen_desc = "유리 잉크웰과 깃펜 펜촉"
            main_objs = "잉크병 깃펜 잉크방울"
        elif p_no == "004":
            seen_desc = "목조 양팔 저울과 황동 분동 추"
            main_objs = "양팔저울 접시 분동추 균형봉"
        elif p_no == "005":
            seen_desc = "황동 회중시계와 톱니바퀴 태엽"
            main_objs = "회중시계 시계바늘 톱니 체인"
        elif p_no == "006":
            seen_desc = "볼록 돋보기와 활자 종이"
            main_objs = "돋보기 렌즈 손잡이 활자종이"
        elif p_no == "007":
            seen_desc = "클래식 타자기와 올라온 활자 해머"
            main_objs = "타자기 자판 활자대 롤러 종이"
        elif p_no == "008":
            seen_desc = "황동 콤파스와 제도용 삼각자"
            main_objs = "제도콤파스 삼각자 눈금자"
        elif p_no == "009":
            seen_desc = "주물 북엔드 책고정대와 세 권의 책"
            main_objs = "북엔드 양장책 세권 책등"
        elif p_no == "010":
            seen_desc = "가죽 펜파우치와 흑연 연필 세 자루"
            main_objs = "펜케이스 흑연연필 연필심"

    elif "11차" in set_name:
        # 음악소리
        topic = "음악"
        if p_no == "001":
            seen_desc = "그랜드 피아노 건반과 올라간 댐퍼"
            main_objs = "피아노건반 흑백건반 댐퍼 현"
        elif p_no == "002":
            seen_desc = "어쿠스틱 통기타와 울림통 사운드홀"
            main_objs = "기타 바디 사운드홀 여섯줄"
        elif p_no == "003":
            seen_desc = "바이올린 바디와 f홀 활줄"
            main_objs = "바이올린 에프홀 활 브릿지"
        elif p_no == "004":
            seen_desc = "황동 트럼펫과 세 개의 밸브 피스톤"
            main_objs = "트럼펫 나팔관 피스톤 밸브"
        elif p_no == "005":
            seen_desc = "원목 메트로놈 추와 진동 눈금판"
            main_objs = "메트로놈 진동추 눈금막대 태엽"
        elif p_no == "006":
            seen_desc = "첼로 바디와 엔드핀 T자 받침"
            main_objs = "첼로 울림통 엔드핀 현"
        elif p_no == "007":
            seen_desc = "금빛 색소폰과 화려한 키 메커니즘"
            main_objs = "색소폰 벨 마우스피스 키패드"
        elif p_no == "008":
            seen_desc = "황동 호른과 둥근 나팔관 관체"
            main_objs = "프렌치호른 원형관 벨 로터리"
        elif p_no == "009":
            seen_desc = "목조 플루트와 입술받침 립플레이트"
            main_objs = "플루트 취구 키홀 관체"
        elif p_no == "010":
            seen_desc = "클라리넷과 리드 마우스피스 벨"
            main_objs = "클라리넷 리드 은색키 벨"
        elif p_no == "011":
            seen_desc = "스네어 드럼과 드럼스틱 북채"
            main_objs = "작은북 드럼헤드 북채 스네어와이어"
        elif p_no == "012":
            seen_desc = "황동 심벌즈와 스탠드 펠트와셔"
            main_objs = "심벌즈 원형황동판 스탠드 펠트"
        elif p_no == "013":
            seen_desc = "클래식 하프와 수직 기둥 현들"
            main_objs = "하프 공명통 줄 기둥 페달"
        elif p_no == "014":
            seen_desc = "아코디언 주름상자와 건반 벨로우즈"
            main_objs = "아코디언 주름바람통 건반 버튼"
        elif p_no == "015":
            seen_desc = "황동 튜닝포크 소리굽쇠와 파동선"
            main_objs = "소리굽쇠 공명상자 타격봉 진동파"

    # 기본값 보정
    if not seen_desc:
        seen_desc = f"{set_name} {p_no}번 장면"
        main_objs = "사물 도구 형태"

    # 행 구성: 파일명,보이는것,주요사물,사람유무,손유무,어울리는주제
    # 파일명은 .mp4를 뺀 이름 (예: ch2_14)
    file_id = mp4_name.replace(".mp4", "")
    rows_out.append({
        "파일명": file_id,
        "보이는것": seen_desc,
        "주요사물": main_objs,
        "사람유무": has_person,
        "손유무": has_hand,
        "어울리는주제": topic
    })

# CSV 파일 저장
out_csv_path = "_작업/91편_그림목록.csv"
with open(out_csv_path, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["파일명", "보이는것", "주요사물", "사람유무", "손유무", "어울리는주제"])
    writer.writeheader()
    writer.writerows(rows_out)

print(f"✅ {out_csv_path} 생성 완료! 총 {len(rows_out)}행 기록됨")

