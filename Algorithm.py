board = [
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 3],
        [0, 7, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 2],
        [0, 8, 0, 0, 4, 0, 0, 1, 0],
        [6, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 7, 8, 0],
        [5, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0]
    ]

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r,c)
    return None       

def print_board(board):
    for r in range(9):
        if r%3 == 0 and r!=0:
                print("---------------------------------")
        for c in range(9):
            if c%3 == 0 and c != 0:
                print(" |  ", end = "")
            print(str(board[r][c]) + "  " , end = "")
        print()

def valid(board, num, pos):
#Here pos = position is (row, column) so p[0] is row value, p[1] is column value
#Checking number in the current row:
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
#Checking number in the current column:
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
#Checking number in the SMALL BOX (3x3)
    box_X = pos[1] // 3   #Column/3 ka floor
    box_Y = pos[0] // 3   #Row/3 ka floor

    for r in range(box_Y*3, box_Y*3 + 3):
        for c in range(box_X*3, box_X*3 + 3):
            if board[r][c] == num and pos != (r, c):
                return False
    return True

def Solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1, 10):        # 1 included but 10 is not included
        if valid(board, i, (row,column)):
            board[row][column] = i

            if Solve(board):
                return True
            
            board[row][column] = 0
    return False

#Main
print_board(board)
Solve(board)
print()
print()
print_board(board)