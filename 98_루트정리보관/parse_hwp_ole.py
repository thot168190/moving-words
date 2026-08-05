import struct
import zlib
import re

hwp_path = "/Users/mihyunlee/Desktop/철만이/디오라마/2화/동영상/국세청 국세외 체납관리단 기간제 근로자 채용 공고(공고2026-83호)_공고문.hwp"

with open(hwp_path, 'rb') as f:
    data = f.read()

# OLE Header check
if data[:8] != b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1':
    print("Not an OLE file")
    sys.exit(0)

sector_size = 1 << struct.unpack('<H', data[30:32])[0]
mini_sector_size = 1 << struct.unpack('<H', data[32:34])[0]
fat_count = struct.unpack('<I', data[44:48])[0]
dir_start = struct.unpack('<I', data[48:52])[0]
mini_fat_start = struct.unpack('<I', data[60:64])[0]
mini_stream_start = struct.unpack('<I', data[68:72])[0]

# Extract raw text from UTF-16LE strings found inside decompressed zlib streams
# We can scan for compressed Section streams inside the file.
sections_data = []
# Zlib streams in HWP 5.0 typically start with deflate format after stream header
# Let's search for deflate streams using zlib.decompressobj(-15)
for i in range(512, len(data) - 512, 64):
    try:
        d = zlib.decompress(data[i:], -15)
        # Check if contains Korean UTF-16LE text
        decoded = d.decode('utf-16le', errors='ignore')
        # Filter printable hangul / ascii / punctuation
        korean_chars = [c for c in decoded if '\uac00' <= c <= '\ud7a3' or c in '\n\r\t ']
        if len(korean_chars) > 50:
            # Clean up HWPTAG controls
            clean = ""
            for char in decoded:
                code = ord(char)
                if 0xac00 <= code <= 0xd7a3 or 0x3131 <= code <= 0x318e or 0x20 <= code <= 0x7e or char in '\n\r\t':
                    clean += char
            clean = re.sub(r'[ \t]+', ' ', clean)
            clean = re.sub(r'\n+', '\n', clean)
            sections_data.append(clean)
    except Exception:
        pass

# Deduplicate
unique_text = []
for block in sections_data:
    if len(block) > 50 and not any(block in u for u in unique_text):
        unique_text.append(block)

print(f"Found {len(unique_text)} unique text blocks.")
for idx, text in enumerate(unique_text[:5]):
    print(f"=== Block {idx+1} ===")
    print(text[:500])

