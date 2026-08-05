import os
import zipfile
import xml.etree.ElementTree as ET

# 1. HWPX Conversion
hwpx_path = "/Users/mihyunlee/Desktop/철만이/디오라마/2화/동영상/국세외수입체납관리단자기소개서양식.hwpx"
output_md_1 = "/Users/mihyunlee/Desktop/철만이/디오라마/2화/동영상/01_자기소개서양식_보기.md"
output_html_1 = "/Users/mihyunlee/Desktop/철만이/디오라마/2화/동영상/01_자기소개서양식_보기.html"

texts = []
try:
    with zipfile.ZipFile(hwpx_path, 'r') as z:
        for name in z.namelist():
            if 'section' in name and name.endswith('.xml'):
                xml_data = z.read(name)
                root = ET.fromstring(xml_data)
                for elem in root.iter():
                    if elem.tag.endswith('t') and elem.text:
                        texts.append(elem.text.strip())
except Exception as e:
    texts = [f"Error: {e}"]

content_md = "# 📋 국세외수입체납관리단 자기소개서 양식\n\n"
content_html = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>국세외수입체납관리단 자기소개서 양식</title>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; line-height: 1.6; color: #333; background: #f9f9f9; }
.card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
h1 { color: #1e3a8a; border-bottom: 2px solid #3b82f6; padding-bottom: 10px; }
.q-box { background: #f0f9ff; border-left: 4px solid #0284c7; padding: 15px; margin: 20px 0; border-radius: 4px; }
.q-title { font-weight: bold; color: #0369a1; font-size: 1.1em; }
</style>
</head>
<body>
<div class="card">
<h1>📋 국세외수입체납관리단 자기소개서 양식</h1>
"""

for idx, t in enumerate(texts, 1):
    content_md += f"### {t}\n\n"
    content_html += f'<div class="q-box"><div class="q-title">{t}</div></div>\n'

content_html += "</div></body></html>"

with open(output_md_1, 'w', encoding='utf-8') as f:
    f.write(content_md)

with open(output_html_1, 'w', encoding='utf-8') as f:
    f.write(content_html)

print("Created converted files successfully!")
