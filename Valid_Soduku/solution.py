class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if not self.check(i, j, board):
                        return False
        return True
    def check(self, i, j, board):
        node = board[i][j]
        board[i][j] = '!'
        for k in range(9):
            if board[i][k] == node or board[k][j] == node:
                return False
        row_left = (i/3) * 3
        col_left = (j/3) * 3
        for k in range(row_left,row_left + 3):
            for l in range(col_left, col_left + 3):
                if board[k][l] == node:
                    return False
        return True
