# Last updated: 7/14/2026, 9:56:19 AM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        for i in nums1:
            if i in nums2 and i not in r:
                r.append(i)
        return r