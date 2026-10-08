import time

def checkmate(board):
    if not board or not isinstance(board, str):
        print("error 1")
        return
    lines = [line for line in board.strip('\n').split('\n') if line]
    if not lines:
        print("เช็คข้อความไม่สำเร็จ")
        return
    n = len(lines)
    grid = [list(line) for line in lines] # แปลงจากสตริงเป็น ['R', '.', '.', '.']
    for row in grid: # รอบที่ 1: row จะได้ ['R', '.', '.', '.']
        if len(row) != n: 
            print("ตารางไม่ถูกต้อง")
            return
# ----------------------------------------------------------------------
                         #   ค้นหาตำแหน่ง king
    king_pos = None   #สร้างตัวแปรที่ว่างเปล่า
    for r in range(n): #range(n): ฟังก์ชันสร้างลำดับตัวเลขตั้งแต่งองค์ประกอบที่ 0 ถึง n-1 เช่น range(4) จะได้ตัวเลข 0, 1, 2, 3
        for c in range(n):
            if grid[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break

    if not king_pos:
        print("ไม่สามารถหาตำแหน่งของ King ได้")
        return
# --------------------------------------------------------------------------
    kr, kc = king_pos
    enemy_pieces = ('P', 'B', 'R', 'Q')
    diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diag_dirs:
        r, c = kr + dr, kc + dc
        step = 1
        while 0 <= r < n and 0 <= c < n:
            piece = grid[r][c]
            time.sleep(0.5)  # เพิ่มการหน่วงเวลา 0.5 วินาที  
            print(f"Checking position ({r}, {c}): {piece}")
            if piece in enemy_pieces:
                if piece in ('Q', 'B'):
                    print("Success")
                    return
                if step == 1 and dr == 1 and piece == 'P':
                    print("Success")
                    return
                break # เจอหมากศัตรูที่โจมตีไม่ได้ (เช่น Rook) บังสายตาอยู่
            r += dr
            c += dc
            step += 1

# ---------------------------------------------------------------------------

    ortho_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in ortho_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            piece = grid[r][c]
            time.sleep(0.5)  # เพิ่มการหน่วงเวลา 0.5 วินาที  
            print(f"Checking position ({r}, {c}): {piece}")
            if piece in enemy_pieces:
                if piece in ('Q', 'R'):
                    print("Success")
                    return
                break
            r += dr
            c += dc

    print("Fail")
#  ---------------------------------------------------------------------------