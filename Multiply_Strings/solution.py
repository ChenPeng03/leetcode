class Solution(object):
    def multiply(self, num1, num2):
        res = [0] * (len(num1) + len(num2))
        index = len(res) - 1
        for i in reversed(num1):
            tmp_idx = index
            for j in reversed(num2):
                res[tmp_idx] += int(i) * int(j)
                res[tmp_idx - 1] += res[tmp_idx] / 10
                res[tmp_idx] %= 10
                tmp_idx -= 1
            index -= 1
        k = 0
        while k < len(res) - 1 and res[k] == 0:
            k += 1
        return ''.join(map(str,res[k:]))
