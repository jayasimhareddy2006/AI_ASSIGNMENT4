def print_board(board):
    for r in board:
        print(r)

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def valid(board, num, pos):

    row, col = pos

    for i in range(9):
        if board[row][i] == num and col != i:
            return False

    for i in range(9):
        if board[i][col] == num and row != i:
            return False

    box_x = col // 3
    box_y = row // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):

        if valid(board, i, (row, col)):

            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


board = [
[0,0,3,0,2,0,6,0,0],
[9,0,0,3,0,5,0,0,1],
[0,0,1,8,0,6,4,0,0],
[0,0,8,1,0,2,9,0,0],
[7,0,0,0,0,0,0,0,8],
[0,0,6,7,0,8,2,0,0],
[0,0,2,6,0,9,5,0,0],
[8,0,0,2,0,3,0,0,9],
[0,0,5,0,1,0,3,0,0]
]

print("\nSudoku Puzzle:\n")
print_board(board)

solve(board)

print("\nSolved Sudoku:\n")
print_board(board)
