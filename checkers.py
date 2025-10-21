# checkers.py
# Console Checkers with visible board

def create_board():
    board = []
    for row in range(8):
        row_list = []
        for col in range(8):
            if (row + col) % 2 == 0:
                row_list.append("⬜")  # white square
            else:
                if row < 3:
                    row_list.append("⚫")  # black piece
                elif row > 4:
                    row_list.append("🔴")  # red piece
                else:
                    row_list.append("⬛")  # empty black square
        board.append(row_list)
    return board

def print_board(board):
    print("  0 1 2 3 4 5 6 7")
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))
    print()

def get_moves(board, row, col):
    piece = board[row][col]
    moves = []
    directions = []
    if piece in ["🔴", "🔴K"]:
        directions = [(-1, -1), (-1, 1)]
    elif piece in ["⚫", "⚫K"]:
        directions = [(1, -1), (1, 1)]
    if "K" in piece:  # King can move both ways
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == "⬛":
            moves.append((r, c))
        # Jumping
        r2, c2 = row + 2*dr, col + 2*dc
        if 0 <= r2 < 8 and 0 <= c2 < 8 and board[r2][c2] == "⬛":
            if board[r + dr][c + dc] in ["🔴", "⚫"] and board[r + dr][c + dc] != piece:
                moves.append((r2, c2))
    return moves

def make_move(board, start, end):
    sr, sc = start
    er, ec = end
    piece = board[sr][sc]
    board[er][ec] = piece
    board[sr][sc] = "⬛"
    # Remove jumped piece
    if abs(er - sr) == 2:
        board[(er+sr)//2][(ec+sc)//2] = "⬛"
    # Promote to king
    if piece == "🔴" and er == 0:
        board[er][ec] = "🔴K"
    if piece == "⚫" and er == 7:
        board[er][ec] = "⚫K"

def has_moves(board, player):
    for r in range(8):
        for c in range(8):
            if (player == "r" and board[r][c] in ["🔴", "🔴K"]) or \
               (player == "b" and board[r][c] in ["⚫", "⚫K"]):
                if get_moves(board, r, c):
                    return True
    return False

def main():
    board = create_board()
    current_player = "r"
    while True:
        print_board(board)
        if not has_moves(board, current_player):
            print(f"{'Red' if current_player=='r' else 'Black'} has no moves. Game Over!")
            break
        print(f"{'Red' if current_player=='r' else 'Black'}'s turn")
        try:
            sr = int(input("Row of piece to move (0-7): "))
            sc = int(input("Col of piece to move (0-7): "))
            moves = get_moves(board, sr, sc)
            if not moves:
                print("No moves available for this piece.")
                continue
            print(f"Possible moves: {moves}")
            er = int(input("Row to move to (0-7): "))
            ec = int(input("Col to move to (0-7): "))
            if (er, ec) in moves:
                make_move(board, (sr, sc), (er, ec))
                current_player = "b" if current_player == "r" else "r"
            else:
                print("Invalid move.")
        except:
            print("Invalid input. Use numbers 0-7.")

if __name__ == "__main__":
    main()
