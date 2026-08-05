import sys
import zlib
import re

hwp_path = "/Users/mihyunlee/Desktop/철만이/디오라마/2화/동영상/국세청 국세외 체납관리단 기간제 근로자 채용 공고(공고2026-83호)_공고문.hwp"

with open(hwp_path, 'rb') as f:
    data = f.read()

# Scan for decompressed zlib blocks or strings
text_blocks = []
pos = 0
while pos < len(data):
    # zlib header check
    if data[pos:pos+2] in [b'\x78\x9c', b'\x78\x01', b'\x78\xda']:
        try:
            decomp = zlib.decompress(data[pos:], -15)
            decoded = decomp.decode('utf-16le', errors='ignore')
            clean = "".join([c for c in decoded if ord(c) >= 32 or c in ('\n', '\r', '\t')])
            clean = re.sub(r'\s+', ' ', clean).strip()
            if len(clean) > 20:
                text_blocks.append(clean)
        except Exception:
            pass
    pos += 64

print(f"Extracted {len(text_blocks)} blocks.")
for idx, b in enumerate(text_blocks[:10]):
    print(f"--- Block {idx+1} ---")
    print(b[:300])

