
class Solution(objectt):
    def hIndex(self,citations):
        if not citations:
            return 0
        i = 0
        j = len(citations) - 1
        while i + 1 < j:
            mid = (i + j) / 2
            if citation[mid] < len(citations) - mid:
                i = mid
            else:
                j = mid
        if citation[i] >= len(citations) - i:
            return len(citations) - i
        if j == len(citations) - j:
            return min(citation[j],1)
        if citation[j] >= len(citations) - j:
            return len(citations) - j
