# 코다리 작업 — 챕터3 보완 (2건)

발행 2026-08-12 · 로부장
`코다리_상시절차_영상탑재.md` STEP 6·7·8을 그대로 따른다. 아래는 넣을 데이터만.

---

## 작업 A — 뜻 4개 교정

`dist/learning/index.html`과 `public/learning/index.html` **양쪽 모두**에서
챕터3의 아래 네 개를 찾아 한국어 뜻만 바꾼다. 영어 단어는 건드리지 않는다.

```
"dump","더미"   →  "dump","버리다"
"mess","어지러움" →  "mess","엉망"
"bare","민둥한"  →  "bare","드러난"
"curl","말리다"  →  "curl","감기다"
```

---

## 작업 B — DOMUS 1차 6편 등록 (누락분)

`scene-ch3-06 ~ 11.mp4`가 폴더에 있는데 `chapterData[3]`에 없다.
아래 6편을 **works 배열의 5번 인덱스 뒤(=현재 12편 앞)** 에 끼워 넣는다.
즉 최종 순서는 `01 · 02 · 03 · 놀이공원2 · 06 · 07 · 08 · 09 · 10 · 11 · 12 · 13 · 14 · 15` = **15편**.

포스터는 `scene-ch3-NN-poster.jpg`. 없으면 아래 명령으로 만든다.

```bash
ffmpeg -y -loglevel error -ss 7.4 -i scene-ch3-NN.mp4 -frames:v 1 -q:v 3 scene-ch3-NN-poster.jpg
```

### 넣을 단어 (편당 5개)

| 파일 | 제목 | 단어 · 뜻 |
|---|---|---|
| `scene-ch3-06` | 벽돌집과 지붕 | cottage 시골집 · roof 지붕 · brick 벽돌 · villa 별장 · garage 차고 |
| `scene-ch3-07` | 계단 옆 거실 | stairs 계단 · ceiling 천장 · shelf 선반 · sheet 얇은 판 · livingroom 거실 |
| `scene-ch3-08` | 맑은 욕실 | shower 샤워기 · toilet 변기 · tap 수도꼭지 · towel 수건 · mirror 거울 |
| `scene-ch3-09` | 조용한 부엌 | microwave 전자레인지 · oven 오븐 · lid 뚜껑 · tray 쟁반 · bin 쓰레기통 |
| `scene-ch3-10` | 램프 곁의 담요 | furniture 가구 · bench 벤치 · carpet 카펫 · lamp 램프 · blanket 담요 |
| `scene-ch3-11` | 옷걸이의 옷 | sweater 스웨터 · jeans 청바지 · scarf 목도리 · glove 장갑 · pocket 주머니 |

### 규칙

- **레벨1/레벨2 구분은 `_작업/1200_레벨태그_v3.csv`를 조회해서 정한다.** 추측 금지
- **csv에 없는 단어가 하나라도 나오면 즉시 멈추고 그 단어를 보고**한다
- `words`는 레벨1 먼저, 레벨2 나중 순서
- 좌표는 **작업 C**에서 네가 직접 잡는다
- 뜻은 위 표 그대로 쓴다. **한 글자도 창작하지 마라**

---

## 작업 C — 좌표 잡기 (10편 · 신규 4편 + 06~11편)

지금 신규 4편의 `sceneSpots` · `levelOneSpots`가 빈 배열이라
**그림 위에 단어가 한 개도 안 뜬다.** 렌더링 코드가 이렇게 되어 있기 때문이다.

```js
const count = Math.min(allWords.length, (spots||[]).length);
```

좌표를 채워야 이 제품이 제품이 된다.

### 방법

편마다 포스터 `scene-ch3-NN-poster.jpg`를 **이미지로 직접 열어 보고**,
단어가 가리키는 물건이 화면 어디에 있는지 읽어서 좌표를 정한다.

```js
sceneSpots[k]    = [[x,y], [x,y], ...]   // levelTwoWords[k]와 같은 개수·같은 순서
levelOneSpots[k] = [[x,y], [x,y], ...]   // levelOneWords[k]와 같은 개수·같은 순서
```

- `x` = 그림 왼쪽 끝에서부터의 가로 위치, **0~100 사이 정수 (퍼센트)**
- `y` = 그림 위쪽 끝에서부터의 세로 위치, **0~100 사이 정수 (퍼센트)**
- 배열 순서는 단어 배열 순서와 **정확히 1:1 대응**해야 한다

### 좌표 규칙

```
[ ] 그 단어가 뜻하는 물건 위 또는 바로 옆에 찍는다
[ ] x 는 8 ~ 88 사이, y 는 12 ~ 82 사이 (화면 밖·자막 겹침 방지)
[ ] 좌표끼리 최소 14 이상 떨어뜨린다 (단어 버튼이 서로 안 겹치게)
[ ] 물건이 화면 왼쪽에 있으면 단어도 왼쪽에 둔다. 반대로 옮기지 마라
[ ] 추상어(mess · fit · bare · curl 등)는 그 뜻이 드러나는 자리에 찍는다
     예) mess → 물건이 흩어진 한가운데 / fit → 구두골이 부츠에 들어간 지점
```

### 판정 못 할 때

포스터를 봐도 그 물건이 어디 있는지 모르겠으면 **좌표를 지어내지 마라.**
그 편·그 단어를 목록으로 만들어 보고하고, 나머지 편만 먼저 넣는다.

### 자기 검증

좌표를 다 넣은 뒤 아래를 표로 보고한다.

```
[ ] 편별 sceneSpots[k].length == levelTwoWords[k].length
[ ] 편별 levelOneSpots[k].length == levelOneWords[k].length
[ ] 모든 x가 8~88, 모든 y가 12~82 범위 안
[ ] 같은 편 안에서 두 좌표 사이 거리가 14 미만인 쌍이 있는지 → 있으면 목록
```

마지막 항목은 스크립트로 세라.

```bash
node -e "
const fs=require('fs');
const s=fs.readFileSync('dist/learning/index.html','utf8');
const cd=eval('('+s.match(/const chapterData\s*=\s*(\{[\s\S]*?\n\};)/)[1].replace(/;\$/,'')+')');
const c=cd['3'];
c.works.forEach((w,i)=>{
  const all=[...(c.levelOneSpots[i]||[]),...(c.sceneSpots[i]||[])];
  const bad=[];
  all.forEach((a,x)=>all.forEach((b,y)=>{if(x<y&&Math.hypot(a[0]-b[0],a[1]-b[1])<14)bad.push([x,y])}));
  const out=all.filter(p=>p[0]<8||p[0]>88||p[1]<12||p[1]>82);
  console.log(i, (w.video||'').split('/').pop(), 'spots='+all.length, '근접쌍='+bad.length, '범위밖='+out.length);
});
"
```

---

## 검증 (배포 전)

```
[ ] works / levelOneWords / levelTwoWords / sceneSpots / levelOneSpots → 다섯 개 전부 15
[ ] 편별 levelOneWords[k].length + levelTwoWords[k].length == works[k].words.length
[ ] chapterData[3]의 모든 video / poster 경로가 dist/learning 아래에 실제로 존재
[ ] public 과 dist 두 index.html의 chapterData[3]이 동일
[ ] 작업 A의 네 단어가 양쪽 파일에서 다 바뀌었는지 grep으로 확인
[ ] 15편 전부 sceneSpots · levelOneSpots가 비어 있지 않은지 (작업 C 결과)
```

하나라도 어긋나면 배포하지 말고 보고.

---

## 배포

```bash
rsync -av --include='*/' --include='*.mp4' --include='*.jpg' --exclude='*' public/learning/ dist/learning/
npx gh-pages -d dist
```

`npm run build` / `npm run deploy` 금지. gh-pages 커밋 해시를 보고에 포함.

---

## 별건 보고만 (손대지 마라)

1. `scene-ch3-07`(계단 편)에 `sheet`가 실제로 그려져 있는지 포스터를 보고 **판정만** 보고.
   안 보이면 단어 교체가 필요하다 — 대표님 판단 대기.
2. 놀이공원 5편(`scene-ch3-01~03` + Flow 원본명 2개)은 URBS(도시) 소재라
   챕터5로 옮길지 미결정 상태다. **손대지 마라.**
