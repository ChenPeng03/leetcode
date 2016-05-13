class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        if not citations:
            return 0
        for i in range(len(citations)):
            if i == len(citations) - 1:
                return min(citations[i],1)
            if citations[i] >= len(citations) - i:
                return len(citations) - i
