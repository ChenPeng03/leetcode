class Solution(object):
    def nextPermutation(self, nums):
        for i in range(len(nums) - 1, -1, -1):
            if len(nums) <= 1:
                return None
            if i == 0:
                nums,reverse()
                return None
            if nums[i] > nums[i - 1]:
                for k in range(len(nums) - 1, -1, -1):
                    if nums[k] > nums[i - 1]:
                        nums[k], nums[i - 1] = nums[i - 1], nums[k]
                        nums[i:] = sorted(nums[i:])
                        return None

