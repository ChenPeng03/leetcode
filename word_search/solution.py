class Solution(object):
    def exist(self,board,word):
        if not board:
            return False
        ##start precheck, check charactor numbers, optional
        precheck = {}
        for i in word:
            if i in precheck:
                precheck[i] += 1
            else:
                precheck[i] = 1
        for i in board:
            for j in i:
                if j in precheck:
                    precheck[j] -= 1
        for i in precheck.values():
            if i > 0:
                return False
        ##precheck end -------optional
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i,j,word,board):
                    return True
        return False
    def dfs(self,i,j,word,board):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        else:
            tmp = board[i][j]
            board[i][j] = "!"   # prevent visite again
            find = self.dfs(i+1,j,word[1:],board) or self.dfs(i,j+1,word[1:],board) or self.dfs(i-1,j,word[1:],board) or self.dfs(i,j-1,word[1:],board)
            board[i][j] = tmp
            return find
