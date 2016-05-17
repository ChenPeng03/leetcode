class Solution(object):
    def canPermutePalindrome(self, s):
        n = collections.Counter(s).values()
        count = 0
        for i in n:
            if i % 2 == 1:
                count += 1
                if count > 1:
                    return False
        return True
