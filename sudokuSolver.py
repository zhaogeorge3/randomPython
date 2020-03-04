class Solution:
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

    def possibleSub(self, board):
        for subbox in self.subboxes:
            for sub in subbox:
                if(board[sub[0]][sub[1]].startswith(".") and len(board[sub[0]][sub[1]]) == 2):
                    board[sub[0]][sub[1]] = board[sub[0]][sub[1]][1]
        for subbox in self.subboxes:
            temp = self.nums.copy()
            for sub in subbox:
                if(board[sub[0]][sub[1]] in temp):
                    temp.remove(board[sub[0]][sub[1]])
            for sub in subbox:
                if(board[sub[0]][sub[1]].startswith(".")):
                    tempSet = set(temp)
                    currentSet = set([l for l in board[sub[0]][sub[1]][1:]])
                    tempSetInter = tempSet.intersection(currentSet)
                    board[sub[0]][sub[1]] = "."+"".join(tempSetInter)


    def possibleRow(self, row):
        for i in range(len(row)):
            if(row[i].startswith(".") and len(row[i]) == 2):
                row[i] = row[i][1]
        temp = self.nums.copy()
        for i in row:
            if(i in temp):
                temp.remove(i)
        for i in range(len(row)):
            if(row[i].startswith(".")):
                tempSet = set(temp)
                currentSet = set([l for l in row[i][1:]])
                tempSetInter = tempSet.intersection(currentSet)
                row[i] = "."+"".join(tempSetInter)
    def loopCol(self, ind, board):
        temp = self.nums.copy()
        for row in range(len(board)):
            if(board[row][ind].startswith(".") and len(board[row][ind]) == 2):
                board[row][ind] = board[row][ind][1]
        for row in range(len(board)):
            if(board[row][ind] in temp):
                temp.remove(board[row][ind])
        for row in range(len(board)):
            if(board[row][ind].startswith(".")):
                tempSet = set(temp)
                currentSet = set([l for l in board[row][ind][1:]])
                tempSetInter = tempSet.intersection(currentSet)
                board[row][ind] = "."+"".join(tempSetInter)
    def initialPossibleRow(self, row):
        for i in range(len(row)):
            if(row[i].startswith(".") and len(row[i]) == 2):
                row[i] = row[i][1]
        temp = self.nums.copy()
        for i in row:
            if(i in temp):
                temp.remove(i)
        for i in range(len(row)):
            if(row[i].startswith(".")):
                for j in temp:
                    if(j not in row[i]):
                        row[i]+=j
    def checkWin(self, board):
        for row in range(len(board)):
            for col in range(len(board)):
                if(board[row][col].startswith(".") and len(board[row][ col]) == 2):
                    board[row][col] = board[row][col][1]
        for row in range(len(board)):
            for col in range(len(board)):
                if(board[row][col].startswith(".")):
                    return False
        return True



    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in board:
            self.initialPossibleRow(row)
        while not self.checkWin(board):
            for row in board:
                self.possibleRow(row)
            for col in range(len(board)):
                self.loopCol(col, board)
            self.possibleSub(board)
            print(board)
puzzle = [[".","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
s = Solution()
s.solveSudoku(puzzle)
print(puzzle)
