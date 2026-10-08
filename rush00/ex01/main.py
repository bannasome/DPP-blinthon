import sys
import os
from checkmate import checkmate

def read_file_content(file_path):
    for enc in ['utf-8-sig', 'utf-8', 'utf-16', 'latin-1']:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                text = f.read()
                if text.strip(): #ตรวจสอบว่าข้อความไม่ได้มีแค่ช่องว่างหรือค่าว่าง ถ้ามีตัวอักษรอยู่จริง ให้ส่งคืนค่า text นั้นกลับไป
                    return text
        except Exception:
            continue
    return ""

def main():
    if len(sys.argv) < 2: # (sys.argv[0] = main.py, sys.argv[1] = board.chess)
        return

    for file_path in sys.argv[1:]: # วนลูปเอาชื่อไฟล์ที่รับมาตั้งแต่ตำแหน่งที่ 1 ไปจนจบ
        if not os.path.isfile(file_path):
            print("ไม่พบไฟล์:", file_path)
            continue

        content = read_file_content(file_path)
        result = checkmate(content)
        print(f"{result}\n")  # เพิ่ม \n เพื่อเว้นบรรทัดบน-ล่างให้ดูโปร่งขึ้น

if __name__ == "__main__":
    main()