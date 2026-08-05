import zipfile
import xml.etree.ElementTree as ET
import sys

hwpx_path = "/Users/mihyunlee/Desktop/철만이/디오라마/2화/동영상/국세외수입체납관리단자기소개서양식.hwpx"

try:
    with zipfile.ZipFile(hwpx_path, 'r') as z:
        print("=== HWPX File Contents ===")
        for name in z.namelist():
            if 'section' in name and name.endswith('.xml'):
                xml_data = z.read(name)
                root = ET.fromstring(xml_data)
                # Extract text elements
                texts = []
                for elem in root.iter():
                    if elem.tag.endswith('t') and elem.text:
                        texts.append(elem.text)
                print("\n".join(texts))
except Exception as e:
    print(f"Error parsing HWPX: {e}")

