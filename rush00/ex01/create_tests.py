def make_file(name, text):
    with open(name, 'w', encoding='utf-8') as f:
        f.write(text)

# board1.chess = ควีน/เรือ ยิงไม่ถึง King (ต้องตอบ Fail)
make_file('board1.chess', "R...\n.K..\n....\n....\n")

# board2.chess = ควีนยิงแนวเฉียงถึง King (ต้องตอบ Success)
make_file('board2.chess', "R...\n.K..\n..Q.\n....\n")

# invalid.chess = ตารางไม่เป็นจัตุรัส 3x2 (ต้องตอบ Error)
make_file('invalid.chess', "...\n.K.\n")

print("สร้างไฟล์ทดสอบสำเร็จ 100%!")