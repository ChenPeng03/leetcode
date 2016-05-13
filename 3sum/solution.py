class Solution(object):
		def threeSum(self, nums):
				nums.sort()
        		res = []
				for i in range(len(nums) - 2):
						if i > 0 and nums[i] == nums[i-1]:
								continue
						l = i + 1
						j = len(nums) - 1

						while l < j:
								if nums[l] + nums[j] > 0 - nums[i]:
										j -= 1
								elif nums[l] + nums[j] < 0 - nums[i]:
										l += 1
								else:
										res.append([nums[i]], nums[l], nums[j])
										while l < j and nums[l] == nums [l + 1]:
												l += 1
										while l < j and nums[j] == nums[j - 1]:
												j -= 1
										l += 1
										j -= 1
				return res
				
