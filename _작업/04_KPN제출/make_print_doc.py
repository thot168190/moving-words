import os
from PIL import Image, ImageOps, ImageDraw, ImageFont

# 300 DPI A4 size: 2480 x 3508
A4_W = 2480
A4_H = 3508

canvas = Image.new('RGB', (A4_W, A4_H), (255, 255, 255))
draw = ImageDraw.Draw(canvas)

# Font loading
font_path = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'
if not os.path.exists(font_path):
    font_path = '/System/Library/Fonts/AppleSDGothicNeo.ttc'

font_title = ImageFont.truetype(font_path, 54)
font_sub = ImageFont.truetype(font_path, 34)
font_section = ImageFont.truetype(font_path, 42)
font_footer = ImageFont.truetype(font_path, 32)

# Load images
id_img = ImageOps.exif_transpose(Image.open('주민등록증.jpeg')).convert('RGB')
raw_bank = Image.open('농협통장사본.jpeg').convert('RGB')
exif_bank = ImageOps.exif_transpose(raw_bank)

# For bankbook: check orientation.
# Raw is (4000, 3000) [Landscape], Exif transposed is (3000, 4000) [Portrait].
# A bankbook is naturally landscape. So let's use raw_bank if width > height, or rotate if needed.
if raw_bank.width > raw_bank.height:
    bank_img = raw_bank
else:
    bank_img = exif_bank

print(f"ID size: {id_img.size}")
print(f"Bank size: {bank_img.size}")

# 1. Header
draw.text((120, 100), "[KPN 제출용] 대표자 신분증 & 통장 사본", fill=(17, 24, 39), font=font_title)
draw.text((120, 180), "제출처: 한국결제네트웍스 유한회사 (eComm영업팀)", fill=(75, 85, 99), font=font_sub)
draw.line([(120, 240), (A4_W - 120, 240)], fill=(209, 213, 219), width=3)

# 2. Section 1: ID Card
draw.text((120, 280), "1. 대표자 신분증 사본 (주민등록증)", fill=(31, 41, 55), font=font_section)

# Resize ID card (Max width: 1800, Max height: 1100)
max_id_w, max_id_h = 1800, 1100
id_ratio = min(max_id_w / id_img.width, max_id_h / id_img.height)
new_id_w = int(id_img.width * id_ratio)
new_id_h = int(id_img.height * id_ratio)
id_resized = id_img.resize((new_id_w, new_id_h), Image.Resampling.LANCZOS)

id_x = (A4_W - new_id_w) // 2
id_y = 350

# Draw border around ID card
draw.rectangle([(id_x - 4, id_y - 4), (id_x + new_id_w + 4, id_y + new_id_h + 4)], outline=(229, 231, 235), width=3)
canvas.paste(id_resized, (id_x, id_y))

# 3. Section 2: Bankbook Copy
bank_y_start = id_y + new_id_h + 100
draw.line([(120, bank_y_start - 40), (A4_W - 120, bank_y_start - 40)], fill=(229, 231, 235), width=2)
draw.text((120, bank_y_start), "2. 대표자 통장 사본 (농협은행)", fill=(31, 41, 55), font=font_section)

# Resize Bankbook (Max width: 2000, Max height: 1400)
max_bank_w, max_bank_h = 2000, 1400
bank_ratio = min(max_bank_w / bank_img.width, max_bank_h / bank_img.height)
new_bank_w = int(bank_img.width * bank_ratio)
new_bank_h = int(bank_img.height * bank_ratio)
bank_resized = bank_img.resize((new_bank_w, new_bank_h), Image.Resampling.LANCZOS)

bank_x = (A4_W - new_bank_w) // 2
bank_y = bank_y_start + 70

# Draw border around Bankbook
draw.rectangle([(bank_x - 4, bank_y - 4), (bank_x + new_bank_w + 4, bank_y + new_bank_h + 4)], outline=(229, 231, 235), width=3)
canvas.paste(bank_resized, (bank_x, bank_y))

# 4. Footer
draw.line([(120, A4_H - 160), (A4_W - 120, A4_H - 160)], fill=(209, 213, 219), width=2)
footer_text = "※ 본 서류는 KPN 전자결제 서비스 계약 가입 제출 목적으로 작성되었습니다."
draw.text((A4_W // 2 - 450, A4_H - 120), footer_text, fill=(107, 114, 128), font=font_footer)

# Save PDF & Image
pdf_path = "신분증_통장사본_출력용.pdf"
jpg_path = "신분증_통장사본_출력용.jpg"

canvas.save(pdf_path, "PDF", resolution=300.0)
canvas.save(jpg_path, "JPEG", quality=95)

print("Saved PDF:", pdf_path)
print("Saved JPG:", jpg_path)
