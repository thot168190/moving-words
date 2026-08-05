# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1920, 1080
BG      = (247, 245, 240)
INK     = (22, 24, 26)
BODY    = (70, 75, 80)
MUT     = (135, 139, 143)
ACCENT  = (7, 83, 63)
WARN    = (193, 85, 58)
CARD    = (255, 255, 255)
LINE    = (222, 218, 208)

FB = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
FR = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"

def font(path, size):
    for idx in (1, 0, 2):
        try:
            f = ImageFont.truetype(path, size, index=idx)
            if f.getbbox("가")[2] > 0:
                return f
        except Exception:
            pass
    return ImageFont.load_default()

F_NUM   = font(FB, 34)
F_TITLE = font(FB, 58)
F_SUB   = font(FR, 30)
F_META  = font(FR, 26)
F_METAB = font(FB, 28)
F_FOOT  = font(FR, 22)

SLIDES = [
 dict(n="1", title="가맹점 홈페이지 메인화면",
      sub="https://inkword.site",
      img="01_main.png", notes=[]),
 dict(n="2", title="홈페이지 하단 사업자 정보",
      sub="전자상거래법 제13조 필수 표기 사항",
      img="02_footer.png",
      notes=["상호 매또컴퍼니  |  대표 이미현  |  사업자등록번호 308-15-96097",
             "경기 양주시 고읍로 11-7, 105동 603호  |  대표전화 010-2058-9900",
             "통신판매업신고 : 면제 (부가가치세법상 간이과세자)  |  호스팅 제공 : GitHub, Inc."]),
 dict(n="3", title="로그인 페이지",
      sub="비회원 구매 불가 — 로그인 후 결제 가능",
      img="03_login.png",
      notes=["■ 심사용 테스트 계정",
             "     ID  :  thot168190+kakao@gmail.com",
             "     PW  :  Inkword2026!"]),
 dict(n="4", title="판매상품 페이지 (단건 결제)",
      sub="상품명 · 판매가격 · 서비스 제공 시기 표기",
      img="04_product.png",
      notes=["상품명 : 보는 단어장 출시 기념 이용권      판매가 : 9,900원 (1회 결제)",
             "서비스 제공 시기 : 결제 완료 즉시 이용 가능 (구매 후 기간 제한 없이 이용)",
             "청약철회 : 콘텐츠 미열람 상태에서 구매 후 7일 이내 전액 환불 (이용약관 제5조)"]),
 dict(n="5", title="일반 PG 결제창",
      sub="결제수단 선택 화면 — 간편결제 영역에 카카오페이 노출",
      img="05_pay.png",
      notes=["※ 현재 테스트 연동 상태로 화면 우측 하단에 「실제 결제가 안되는 테스트입니다」 표시가 나타납니다.",
             "     포트원(PortOne) 연동 키 수령 후 라이브 전환 예정이며, 전환 후에도 결제 경로와",
             "     결제수단 노출 위치는 동일합니다."]),
]

def draw_slide(s, out):
    im = Image.new("RGB", (W, H), BG)
    d  = ImageDraw.Draw(im)

    # 상단 먹 띠
    d.rectangle([0, 0, W, 8], fill=INK)

    # 번호
    d.text((72, 52), s["n"], font=F_NUM, fill=WARN)
    d.text((72, 96), s["title"], font=F_TITLE, fill=INK)
    d.text((76, 176), s["sub"], font=F_SUB, fill=BODY)

    # 본문 영역
    top = 236
    notes = s.get("notes") or []
    note_h = (len(notes) * 40 + 34) if notes else 0
    bottom = H - 56 - note_h

    # 이미지 카드
    src = Image.open(s["img"]).convert("RGB")
    box_w, box_h = W - 144, bottom - top
    r = min(box_w / src.width, box_h / src.height, 1.0)
    nw, nh = int(src.width * r), int(src.height * r)
    src = src.resize((nw, nh), Image.LANCZOS)
    x = (W - nw) // 2
    y = top + (box_h - nh) // 2
    d.rectangle([x - 2, y - 2, x + nw + 2, y + nh + 2], fill=CARD, outline=LINE, width=2)
    im.paste(src, (x, y))

    # 노트
    if notes:
        ny = bottom + 22
        d.line([72, ny - 14, W - 72, ny - 14], fill=LINE, width=2)
        for i, t in enumerate(notes):
            f = F_METAB if (t.startswith("■") or t.startswith("상품명")) else F_META
            c = INK if (t.startswith("■") or t.startswith("상품명")) else (WARN if t.startswith("※") else BODY)
            d.text((76, ny + i * 40), t, font=f, fill=c)

    # 푸터
    d.text((76, H - 34), "매또컴퍼니  |  보는 단어장  |  https://inkword.site", font=F_FOOT, fill=MUT)
    im.save(out, "PNG")
    print("만듦:", out, im.size)

for s in SLIDES:
    draw_slide(s, "slide_%s.png" % s["n"])
