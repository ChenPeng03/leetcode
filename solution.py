class Solution(object):
    def canWin(self, s):
        dic ={}
        self.can(s,dic)
        return dic[s]
    def can(self, s, dic):
        if s not in dic:
            count = 0
            res = False
            for i in range(len(s) - 1):
                if s[i:i+1] == '++':
                    s = s[:i] + '--' + s[i+2:]
                    res = res or not self.can(s,dic)
                    s = s[:i] + '++' + s[i+2:]
            dic[s] = res
            return dic[s]
        else:
            return dic[s]
