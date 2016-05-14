class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        current = self.root
        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.is_word = True
        return
class Solution(object):
    def findWords(self, board, words):
        letterlist = {}
        for i in board:
            for j in i:
                if j not in letterlist:
                    letterlist[j] = 1
                letterlist[j] += 1
        result = []
        trie = Trie()
        node = trie.root
        prune_words = []
        for word in words:
            if self.precheck(word, a):
                prune_words.append(word)
        for word in prune_words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, node, board, result, "")
        return result
    def precheck(self, word, letterlist):
        a = letterlist.copy()
        for i in word:
            if i not in a:
                return False
            else:
                a[i] -= 1
                if a[i] < 0:
                    return False
        return True
    def dfs(self, i, j, node, board, result, pre):
        if node.is_word == True:
            result.append(pre)
            node.is_word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        temp = board[i][j]
        node = node.children.get(temp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(i+1, j, node, board, result, pre+temp)
        self.dfs(i, j+1, node, board, result, pre+temp)
        self.dfs(i-1, j, node, board, result, pre+temp)
        self.dfs(i, j-1, node, board, result, pre+temp)
        board[i][j] = temp

