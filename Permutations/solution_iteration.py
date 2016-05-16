class Solution(object):
    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            temp = []
            for item in ans:
                for i in range(len(item) + 1):
                    temp.append(item[:i] + [n] + item[i:])
                    if i < len(item) and item[i] == n:
                        break
            ans = temp
        return ans if ans else []
