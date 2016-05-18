class Solution(object):
    def isStrobogrammatic(self, num):
        i, j = 0, len(num) - 1
        F = {('1','1'), ('6','9'), ('9','6'), ('0','0'), ('8','8')}
        while i <= j:
            if (num[i],num[j]) in F:
                i += 1
                j -= 1
            else:
                return False
        return True
