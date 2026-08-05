import sys
import os
# Add site-packages path if needed
for path in ['/Users/mihyunlee/.local/lib/python3.11/site-packages', '/Users/mihyunlee/Library/Python/3.11/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages']:
    if os.path.exists(path) and path not in sys.path:
        sys.path.append(path)

try:
    import olefile
    import zlib, struct
    hwp_path = "/Users/mihyunlee/Desktop/철만이/디오라마/2화/동영상/국세청 국세외 체납관리단 기간제 근로자 채용 공고(공고2026-83호)_공고문.hwp"
    f = olefile.OleFileIO(hwp_path)
    sections = [d for d in f.listdir() if d[0] == 'BodyText']
    sections.sort(key=lambda x: int(x[1].replace('Section', '')))

    full_text = []
    for sec in sections:
        stream = f.openstream(sec)
        data = stream.read()
        try:
            decomp = zlib.decompress(data, -15)
        except Exception:
            try:
                decomp = zlib.decompress(data)
            except Exception:
                decomp = data
        
        i = 0
        while i < len(decomp):
            if i + 4 > len(decomp): break
            header = struct.unpack('<I', decomp[i:i+4])[0]
            tag_id = header & 0x3FF
            size = (header >> 20) & 0xFFF
            i += 4
            if size == 0xFFF:
                if i + 4 > len(decomp): break
                size = struct.unpack('<I', decomp[i:i+4])[0]
                i += 4
            if i + size > len(decomp): break
            rec = decomp[i:i+size]
            i += size
            if tag_id == 67: # HWPTAG_PARA_TEXT
                txt = rec.decode('utf-16le', errors='ignore')
                clean = "".join([c for c in txt if ord(c) >= 32 or c in ('\n', '\r', '\t')])
                if clean.strip(): full_text.append(clean.strip())

    print("\n".join(full_text))
except Exception as e:
    print(f"Error: {e}")
