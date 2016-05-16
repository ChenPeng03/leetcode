class Solution(object):
    def convert(self, s, numRows):
        dir = 1
        index = 0
        ans = [""] * numRows
        if numRow == 1:
            return s
        for i in s:
            ans[index] += i
            index += dir
            if index == numRows:
                index = numRows - 2
                dir = -1
            if index == 0:
                dir = 1
        return "".join(ans)
