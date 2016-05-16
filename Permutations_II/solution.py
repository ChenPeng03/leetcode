class Solution(object):
    def permuteUnique(self, nums):
        if not nums:
            return []
        res, lst = [], []
        visited = [False] * len(nums)
        self.helper(lst, res, nums, visited)
        return res
    def helper(self, lst, res, nums, visited):
        if len(lst) == len(nums):
            res.append(lst[:])
            return
        for i in range(len(nums)):
            if visited[i] == True or (visited[i - 1] == False and i != 0 and nums[i] == nums[i - 1]):
                continue
            visited[i] = True
            lst.append(nums[i])
            self.helper(lst, res, nums, visited)
            lst.pop()
            visited[i] = False
