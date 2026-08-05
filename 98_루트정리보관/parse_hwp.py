import sys
import olefile
import zlib
import struct

def extract_text_from_hwp(hwp_path):
    try:
        f = olefile.OleFileIO(hwp_path)
        dirs = f.listdir()

        sections = []
        for d in dirs:
            if d[0] == 'BodyText':
                sections.append(d)

        sections.sort(key=lambda x: int(x[1].replace('Section', '')))
        
        full_text = []

        for sec in sections:
            stream = f.openstream(sec)
            data = stream.read()
            # Decompress using raw deflate (-15)
            try:
                unpacked_data = zlib.decompress(data, -15)
            except Exception:
                try:
                    unpacked_data = zlib.decompress(data)
                except Exception:
                    unpacked_data = data

            # Parse HWPTAG_PARA_TEXT (tag_id = 67 = 0x43) records
            i = 0
            while i < len(unpacked_data):
                if i + 4 > len(unpacked_data):
                    break
                header = struct.unpack('<I', unpacked_data[i:i+4])[0]
                tag_id = header & 0x3FF
                level = (header >> 10) & 0x3FF
                size = (header >> 20) & 0xFFF
                
                i += 4
                if size == 0xFFF:
                    if i + 4 > len(unpacked_data):
                        break
                    size = struct.unpack('<I', unpacked_data[i:i+4])[0]
                    i += 4

                if i + size > len(unpacked_data):
                    break

                record_data = unpacked_data[i:i+size]
                i += size

                # Tag 67 is HWPTAG_PARA_TEXT
                if tag_id == 67:
                    try:
                        text = record_data.decode('utf-16le', errors='ignore')
                        # filter control chars if needed
                        clean_text = "".join([c for c in text if ord(c) >= 32 or c in ('\n', '\r', '\t')])
                        if clean_text.strip():
                            full_text.append(clean_text.strip())
                    except Exception:
                        pass

        return "\n".join(full_text)
    except Exception as e:
        return f"Error reading HWP file: {e}"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(extract_text_from_hwp(sys.argv[1]))
