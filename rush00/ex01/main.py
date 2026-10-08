import sys
import os
from checkmate import checkmate

def main():
    if len(sys.argv) < 2:
        return

    for file_path in sys.argv[1:]:
        # ตรวจสอบว่าไฟล์มีอยู่จริงหรือไม่
        if not os.path.isfile(file_path):
            print("Error")
            continue
            
        try:
            # ใช้ errors='ignore' เพื่อให้อ่านไฟล์ข้ามตัวอักษรพังๆ ไปได้เลย
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            result = checkmate(content)
            print(result)
        except Exception:
            print("Error")

if __name__ == "__main__":
    main()

# python main.py board1.chess board2.chess invalid.chess