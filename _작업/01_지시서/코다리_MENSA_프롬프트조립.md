# 코다리 작업 — MENSA(부엌과 밥상) 6편 프롬프트 조립

발행 2026-08-12 · 로부장
**너는 단어를 창작하지 않는다. 아래 배정표 그대로 쓴다. 영어 문장(A~F)만 네가 쓴다.**

---

## 0. 골격

```
_작업/프롬프트/ch02_VITA/00_기준본.txt
```
없으면 아래 파일의 5편(램프 곁의 담요) 프롬프트를 쓴다.
```
/Users/mihyunlee/Desktop/코덱스/90_임시작업/DOMUS_1차6편_복사용.html
```

**골격 문장은 한 글자도 고치지 마라.** 특히 아래 셋은 절대 건드리지 않는다.
- `Style:` 문단 전체
- `Audio:` 문단 전체 (줄이지 마라. 이대로 두면 소리가 안 난다)
- `Never:` 블록 전체 (단어를 더하지도 빼지도 마라)

바꾸는 곳은 여섯 군데뿐이다.

| 슬롯 | 위치 | 무엇 |
|---|---|---|
| A | 2번째 문단 `The only visible subjects...` | 피사체 목록 |
| B | `0-4s:` 문단 끝 | 그리는 순서 |
| C | `4-7s:` 문단 중간 `Only the palest...` | 색 지정 |
| D | `7-8s:` 문단 | 마지막 미세 동작 |
| E | 마무리 `The finished image reads immediately as ...` | 한 줄 요약 |
| F | `Never:` 안의 `paint blooms behind the home corner` | 피사체 이름만 |

산출물은 `_작업/프롬프트/ch03_MENSA/` 아래 **한 편에 한 파일**, `mensa-01_아침상.txt` 형식.

---

## 1. 배정표 (이 단어만 쓴다. 하나도 더하지 마라)

### 1편 · 가지런한 아침상 — 8단어
```
1단계: rice · toast · tea · meal
2단계: lay · neat · total · pure
```
**그림 논리** — 넓은 쟁반 하나에 아침 한 상이 흐트러짐 없이 차려져 있다.
- rice 흰 밥 한 공기 / toast 접시 위 토스트 두 조각 / tea 찻잔과 작은 주전자 / meal 상 전체가 한 끼
- lay 수저 한 벌이 나란히 **놓여 있는 상태** / neat 그릇들이 줄 맞춰 가지런함
- total 쟁반 하나 안에 전부 들어와 있음 / pure 맑은 물 한 잔
**마지막 동작** — 작은 주전자 뚜껑이 제자리에서 아주 조금 내려앉고 멈춘다.

### 2편 · 과일 접시 — 9단어
```
1단계: pear · melon · lemon · plate
2단계: strawberry · sour · sort · amount · spare
```
**그림 논리** — 크기가 다른 접시 두 장에 과일이 종류별로 나뉘어 담겨 있다.
- pear 통배 하나 / melon 멜론 한 조각 / lemon 반으로 자른 레몬 / plate 접시 두 장
- strawberry 딸기 다섯 알 / sour 잘린 레몬 단면(신맛)
- sort 접시마다 **한 종류씩** 나뉘어 담김 / amount 한쪽은 수북, 한쪽은 두어 개뿐
- spare 옆에 **쓰지 않은 빈 접시**가 두 장 포개져 있음
**마지막 동작** — 포개진 빈 접시 맨 위 한 장이 제자리에서 아주 조금 기울었다 멈춘다.

### 3편 · 끓는 냄비와 주전자 — 8단어
```
1단계: boil · kettle · pour · sauce
2단계: pot · stir · crack · tin
```
**그림 논리** — 조리대 위, 불에 올린 냄비와 그 옆의 기구들.
- boil 냄비 표면의 작은 기포 / kettle 주전자 / pour 눕혀진 소스병에서 접시로 **흘러나온 자국**
- sauce 접시에 고인 소스 / pot 냄비 본체
- stir 냄비에 **꽂힌 채 서 있는 나무 주걱**과 국물의 소용돌이 자국
- crack 그릇 옆에 놓인 **반으로 갈라진 달걀 껍데기 두 쪽** / tin 뚜껑이 열린 깡통
**마지막 동작** — 냄비 뚜껑이 제자리에서 아주 조금 들썩였다 내려앉는다.

### 4편 · 도마 위에서 다듬기 — 9단어
```
1단계: bowl · mix · pepper · mushroom
2단계: chop · powder · press · rub · wipe
```
**그림 논리** — 도마와 그릇이 놓인 작업대. 다듬은 흔적이 남아 있다.
- bowl 사기 그릇 / mix 그릇 안에 여러 재료가 섞여 있음 / pepper 후추 갈이 / mushroom 버섯 세 개
- chop 도마 위 **썰린 조각들과 그 옆의 칼**
- powder 조리대에 흩어진 흰 가루 / press 납작하게 **눌린 자국이 남은 반죽 덩어리**
- rub 흙이 **반쯤 지워진 감자** 하나 / wipe 조리대 한쪽의 **닦인 자국과 접힌 행주**
**마지막 동작** — 도마 위 버섯 조각 하나가 제자리에서 아주 조금 굴렀다 멈춘다.

### 5편 · 프라이팬의 고기 — 8단어
```
1단계: fry · pan · dish · crisp
2단계: bacon · pork · chip · wrap
```
**그림 논리** — 프라이팬과 접시가 놓인 조리대.
- fry 팬 위에서 익고 있는 상태 / pan 프라이팬 / dish 넓은 접시 / crisp 가장자리가 바짝 말린 튀김옷
- bacon 베이컨 두 줄 / pork 도톰한 돼지고기 한 덩이
- chip 접시에 담긴 감자칩 / wrap 투명한 랩이 씌워진 그릇 하나
**마지막 동작** — 팬 위 베이컨 한 줄의 끝이 제자리에서 아주 조금 말렸다 멈춘다.

### 6편 · 다 먹은 저녁상 — 9단어
```
1단계: grocery · supper · honey · snack · sweet
2단계: pie · bitter · hunger · consume
```
**그림 논리** — 저녁을 마친 식탁. 장바구니는 아직 옆에 있다.
- grocery 옆에 놓인 장바구니와 그 안의 식료품 / supper 저녁상 차림
- honey 꿀단지 / snack 작은 접시의 과자 / sweet 각설탕 몇 개
- pie 한 조각 잘려나간 파이 / bitter 진한 갈색 초콜릿 조각
- hunger **아무것도 남지 않은 빈 접시** / consume **바닥이 드러난 그릇**
**마지막 동작** — 장바구니 손잡이 한쪽이 제자리에서 아주 조금 늘어졌다 멈춘다.

---

## 2. A~F를 쓸 때 지켜야 할 것

### ① 손을 부르는 동사를 쓰지 마라 — 가장 중요

`grip · hold · grab · press · rub · stir · chop · wipe · wrap · lay · pour · cut · place · carry · pull · push`

이 동사를 **`Never:` 앞 어디에도 쓰지 마라.** 한 번만 써도 화면에 사람 손과 펜이 나온다.
빨래 편에서 `clips gripping the string` 한 마디 때문에 손이 그려져 편 전체를 버렸다.

배정 단어 중 `stir · press · rub · wipe · chop · lay · wrap · pour`는 동작이지만,
**동작의 흔적을 명사로 묘사**해서 그린다.

| 쓰지 마라 | 이렇게 써라 |
|---|---|
| a spoon stirring the sauce | one wooden spoon standing upright in the pot, with one spiral mark in the surface of the sauce |
| a cloth wiping the counter | one folded cloth lying on the counter beside one clean streak across it |
| dough being pressed | one flat piece of dough with one shallow dent left in it |
| a knife chopping | one knife lying beside several already-cut slices |
| water pouring | one bottle lying on its side with one trail of sauce running from it onto the plate |

골격 5편(램프 편)에는 행위 동사가 **하나도** 없다. `resting` `beside` `beneath` 뿐이다. 그걸 그대로 따라라.

### ② 물·젖음을 뜻하는 말을 쓰지 마라

`pool · wet · watery · dries · drip · soak · damp · puddle · spreads across`

수채화 기법을 설명하려고 쓴 말인데 Veo가 **장면 묘사로 읽어서 물이 흐르는 그림**을 그린다.
장화에서 물이 새고 빨래가 젖은 사고가 이 단어들 때문이었다.
[C]는 **색 이름과 위치만** 말한다. 물 이야기는 골격이 이미 하고 있다.

### ③ [C]는 5편 문형을 그대로 따른다

```
Only the palest <색> on/along <물건>, one faint <색> on <물건>, the lightest <색> on <물건>, and a whisper of pale <색> at <물건>.
```
색 이름에는 **채도**를 넣어라 — `ochre tan` `olive green` `slate blue` `honey brown` `wheat gold`
`grey`만 나열하면 채색이 죽고 연필 소묘가 된다.

### ④ 마지막 동작은 제자리 미세 변형 하나뿐

물건이 A에서 B로 **이동**하면 Veo가 마지막에 화면을 다시 그리면서 피사체를 지운다.
배정표의 "마지막 동작"을 그대로 영어로 옮기고, 뒤에 이 문장을 붙인다.
```
No other subject moves, disappears, changes shape or is relocated.
```

### ⑤ 그 외 금지

- `densely` `pressed close together` 같은 밀도 지시 — 옅은 수채가 진한 연필 덩어리가 된다
- `narration` `voice` `music` `melody` — **골격 Audio 문단 안에 있는 건 그대로 두고**, 네가 새로 쓰지 마라
- `paper` `sheet` `board` `panel` — 종이가 깔린 그림이 된다
- 글자·숫자·라벨이 있어야 뜻이 통하는 물건은 넣지 마라. Never가 글자를 막고 있다
- 사람은 한 명도 넣지 마라. 이번 6편은 물건만이다

---

## 3. 제출 전 자기 검증

편마다 아래를 돌리고 **결과를 표로 보고**한다.

```bash
node -e "
const fs=require('fs');
const f=process.argv[1];
const t=fs.readFileSync(f,'utf8');
const head=t.split('Never:')[0];
const ACT=['grip','hold','grab','press','rub','stir','chop','wipe','wrap','lay ','pour','cut ','place','carry','pull','push'];
const WATER=['pool','wet','watery','dries','drip','soak','damp','puddle'];
const MISC=['densely','pressed close','paper','sheet','board','panel','children','hand'];
const hits=[...ACT,...WATER,...MISC].filter(w=>new RegExp('\\\\\\\\b'+w,'i').test(head));
console.log(f, hits.length?('!! '+hits.join(' ')):'OK');
" 파일경로
```

그리고 눈으로 확인할 것.

```
[ ] 골격과 다른 곳이 A~F 여섯 군데뿐인가 (Style · Audio · Never 문단이 글자 단위로 같은가)
[ ] 배정된 단어가 [A] 피사체 목록에 전부 눈에 보이는 물건으로 나오는가
[ ] 배정 안 한 단어를 새로 넣지 않았는가
[ ] 7-8s가 제자리 미세 동작 하나로 끝나는가 (이동 없음)
[ ] [C]의 색 이름에 채도가 들어갔는가
[ ] 사람이 한 명도 없는가
```

---

## 4. 보고 형식

```
1) 만든 파일 6개 경로
2) 편별 배정 단어 (파일에서 그대로 복사)
3) 편별 금지어 스캔 결과 (위 스크립트 출력)
4) 골격 대조 — 1편 골격과 다른 곳이 A~F 여섯 군데뿐인지
5) 판단이 안 서서 넘긴 것이 있으면 그 목록
```

---

## 5. 하지 말 것

- 단어 추가·변경·삭제
- 골격 문장 수정 (특히 Style · Audio · Never)
- 영상 생성 (대표님이 Flow에서 하신다)
- `git commit` / `push` / 배포 / 빌드 산출물 편집
- 파일을 `Desktop/코덱스/`에만 두는 것 → 반드시 저장소 `_작업/프롬프트/ch03_MENSA/`

**막히면 만들어내지 말고 멈춰서 보고해라.**

---

## 참고 — 이번에 뺀 단어 (보류 목록에 기록만)

`menu` `recipe` `label` `diet` — 글자가 있어야 뜻이 드러나는데 Never가 글자를 막는다
`spoil` — 곰팡이 그림이 되어 학습용으로 부적절
`alcohol` `beer` `cigarette` — 대표님 지시로 제외. alcohol은 나중에 실험실 편에서 재검토

이 7개는 `_작업/보류단어.md`를 만들어 사유와 함께 적어둔다.
