# Last updated: 7/14/2026, 9:56:28 AM
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n=len(citations)
        for i in range(n):
            h=n-i
            if citations[i]>=h:
                return h
        return 0
        