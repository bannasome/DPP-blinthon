def checkmate(board_str):
    if not isinstance(board_str, str) or not board_str:
        return "Error"

    # กรองเอาเฉพาะบรรทัดที่มีข้อความ และตัด \r ฝั่ง Windows ทิ้ง
    lines = []
    for line in board_str.split('\n'):
        clean_line = line.replace('\r', '').strip('\ufeff')
        if clean_line:
            lines.append(clean_line)

    if not lines:
        return "Error"

    n = len(lines)
    grid = [list(line) for line in lines]

    # ตรวจสอบว่าตารางเป็นจัตุรัสหรือไม่
    for row in grid:
        if len(row) != n:
            return "Error"

    # ค้นหาตำแหน่ง King
    king_pos = None
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break

    if not king_pos:
        return "Error"

    kr, kc = king_pos

    # 1. ตรวจแนวเฉียง (Queen, Bishop, Pawn)
    diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diag_dirs:
        r, c = kr + dr, kc + dc
        step = 1
        while 0 <= r < n and 0 <= c < n:
            piece = grid[r][c]
            if piece != '.':
                if piece in ('Q', 'B'):
                    return "Success"
                if step == 1 and dr == 1 and piece == 'P':
                    return "Success"
                break
            r += dr
            c += dc
            step += 1

    # 2. ตรวจแนวตรง (Queen, Rook)
    ortho_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in ortho_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            piece = grid[r][c]
            if piece != '.':
                if piece in ('Q', 'R'):
                    return "Success"
                break
            r += dr
            c += dc

    # 3. ตรวจม้า Knight 'N' (Creative Bonus)
    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2),  (1, 2),  (2, -1),  (2, 1)
    ]
    for dr, dc in knight_moves:
        r, c = kr + dr, kc + dc
        if 0 <= r < n and 0 <= c < n:
            if grid[r][c] == 'N':
                return "Success"

    return "Fail"