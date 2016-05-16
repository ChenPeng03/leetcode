class Solution(object):
    def generatePalindromes(sel, s):
        dic = collections.Counter(s)
        count = 0
        mid = ""
        word_to_use = ""
        result = set([])
        temp = ""
        for key in dic:
            if dic[key] % 2 == 1:
                count += 1
                if count > 1:
                    return []
            if dic[key] >= 2:
                word_to_use += key * ((dic[key] - dic[key] % 2) / 2)
            if not word_to_use:
                return [mid]
            self.dfs(temp, result, mid, word_to_use)
            return list(result)
        def dfs(self, temp, result, mid, word_to_use):
            if not word_to_use:
                result.add(temp + mid + temp[::-1])
                result.add(tem[::-1] + mid + temp)
                return
            for i in range(len(word_to_use)):
                self.dfs(temp + word_to_use[i], result, mid, word_to_use[:i] + word_to_use[i + 1:])
