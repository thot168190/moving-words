import sys
import os
import zlib
import re

# Parse olefile streams cleanly
import subprocess

def get_hwp_text(filepath):
    # Try using python script with olefile
    cmd = '''
import olefile, zlib, struct, sys, re

f = olefile.OleFileIO(sys.argv[1])
sections = [d for d in f.listdir() if d[0] == 'BodyText']
sections.sort(key=lambda x: int(x[1].replace('Section', '')))

full_text = []
for sec in sections:
    stream = f.openstream(sec)
    data = stream.read()
    try:
        decomp = zlib.decompress(data, -15)
    except:
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
            clean = "".join([c for c in txt if ord(c) >= 32 or c in ('\\n', '\\r', '\\t')])
            if clean.strip(): full_text.append(clean.strip())

print("\\n".join(full_text))
'''
    res = subprocess.run(['python3', '-c', cmd, filepath], capture_output=True, text=True)
    return res.stdout

print(get_hwp_text("/Users/mihyunlee/Desktop/철만이/디오라마/2화/동영상/국세청 국세외 체납관리단 기간제 근로자 채용 공고(공고2026-83호)_공고문.hwp")[:1500])
