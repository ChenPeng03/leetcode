class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) / 2
            if citations[mid] >= n - mid:
                end = mid - 1
            else:
                start = mid + 1
            return n - start
