class Solution(object):
    def permute(self, nums):
        result = []
        temp = []
        self.helper(nums, result, temp)
        return result
    def helper(self, nums, result, temp):
        if not nums:
            result.append(temp)
            return
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i+1:], result, temp+[nums[i]])
