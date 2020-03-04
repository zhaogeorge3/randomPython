puzzle = [[".","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

nums = [str(i) for i in range(1,10)]

subbox1 = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
subbox2 = [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)]
subbox3 = [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)]
subbox4 = [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)]
subbox5 = [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)]
subbox6 = [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)]
subbox7 = [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)]
subbox8 = [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)]
subbox9 = [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)]
subboxes = [subbox1, subbox2, subbox3, subbox4, subbox5, subbox6, subbox7, subbox8, subbox9,]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == ".":
                return (i, j)  # row, col
    return None


def valid(board, number, position):
    for rowItem in board[position[0]]:
        if(rowItem == number):
            return False
    for row in range(len(board)):
        if(board[row][position[1]] == number):
            return False
    for subbox in subboxes:
        if(position in subbox):
            for sub in subbox:
                if(board[sub[0]][sub[1]] == number):
                    return False
    return True

def solve(board):
    find = find_empty(board)
    if(not find):
        return True
    else:
        row, col = find
    for i in nums:
        if valid(board, i, (row, col)):
            board[row][col] = i
            if(solve(board)):
                return True
            else:
                board[row][col] = "."
    return False




print_board(puzzle)
solve(puzzle)
print_board(puzzle)
