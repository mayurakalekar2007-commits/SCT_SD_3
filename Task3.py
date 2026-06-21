def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[r][col] for r in range(9)]:
        return False
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == num:
                return False
    return True

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None

def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        row_str = ""
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_str += " | "
            row_str += str(val) if val != 0 else "."
            if j % 3 != 2:
                row_str += " "
        print(row_str)

def take_input():
    board = []
    print("Enter 9 rows, 9 numbers each.")
    print("Use 0 for empty cells. Separate numbers with spaces.")
    print("Example row: 5 3 0 0 7 0 0 0 0\n")
    for i in range(9):
        while True:
            row_input = input(f"Row {i+1}: ").strip().split()
            if len(row_input) == 9 and all(x.isdigit() and 0 <= int(x) <= 9 for x in row_input):
                board.append([int(x) for x in row_input])
                break
            else:
                print("Invalid! Enter exactly 9 numbers (0-9).")
    return board

# --- Main ---
board = take_input()

print("\nYour Puzzle:")
print_board(board)

if solve_sudoku(board):
    print("\nSolved:")
    print_board(board)
else:
    print("\nNo solution exists for this puzzle.")