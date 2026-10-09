import time

def print_board_table(grid):
    print()
    print("Current Board State:")
    n = len(grid)
    # พิมพ์เลขคอลัมน์ด้านบน (เป็น 2 เคาะ เพื่อให้ตรงกับตัวหมาก)
    col_header = "    " + "  ".join(str(c) for c in range(n))
    print(col_header)
    
    
    border = "  +" + "-" * (n * 3 + 1) + "+"
    print(border)

    # พิมพ์ข้อมูลแต่ละแถวพร้อมเลขแถวด้านข้าง
    for r in range(n):
        row_str = "  ".join(grid[r])
        print(f"{r} | {row_str}  |")
    print(border)
# ----------------------------------------------------------------------------
def checkmate(board_str):
    if not board_str or not isinstance(board_str, str):
        return "Error: ข้อมูลว่างเปล่า (ไฟล์อ่านไม่ได้(enc) หรืออาจจะยังไม่ได้กด Save)"

    lines = [line for line in board_str.replace('\r', '').split('\n') if line]
    if not lines:
        return "เช็คข้อความไม่สำเร็จ"

    n = len(lines)
    grid = [list(line) for line in lines]
    for i, row in enumerate(grid):
        if len(row) != n:
            return "ตารางไม่ถูกต้อง"
# ----------------------------------------------------------------------------
    king_pos = None
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break

    if not king_pos:
        return "ไม่พบตัว K บนกระดาน"
# ----------------------------------------------------------------------------
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
                    print_board_table(grid)
                    print(f"  King Position : ({kr}, {kc})")
                    print(f"  ATTACKED BY   : '{piece}' at ({r}, {c})")
                    return "Success"
                if step == 1 and dr == 1 and piece == 'P':
                    print_board_table(grid)
                    print(f"  King Position : ({kr}, {kc})")
                    print(f"  ATTACKED BY   : '{piece}' at ({r}, {c})")
                    return "Success"
                break
            r += dr
            c += dc
            step += 1
# ----------------------------------------------------------------------------
    ortho_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in ortho_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            piece = grid[r][c]
            time.sleep(0.5)  # เพิ่มการหน่วงเวลา 0.5 วินาที
            print(f"Checking position ({r}, {c}): {piece}")
            if piece in enemy_pieces:
                if piece in ('Q', 'R'):
                    print_board_table(grid)
                    print(f"  King Position : ({kr}, {kc})")
                    print(f"  ATTACKED BY   : '{piece}' at ({r}, {c})")
                    return "Success"
                break
            r += dr
            c += dc
    print_board_table(grid)
    print(f"  King Position : ({kr}, {kc})")
    print(f"  STATUS        : Safe (ไม่มีหมากโจมตี)")
    return "Fail"