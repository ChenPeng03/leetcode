class Solution(object):
    def hIndex(self, citations):
        citations.sort(reverse = True)
        h = 0
        for c in citations:
            if c >= h + 1:
                h += 1
            else:
                return h
        return h
