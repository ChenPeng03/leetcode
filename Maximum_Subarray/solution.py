class solution(object):
    def maxSubarray:
        res, pre = float('-inf'), 0
        for num in nums:
            if pre > 0:
                pre += num
            else:
                pre = num
            res = max(pre, res)
        return res
