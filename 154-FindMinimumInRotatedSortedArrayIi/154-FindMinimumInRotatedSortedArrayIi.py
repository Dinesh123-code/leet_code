# Last updated: 7/14/2026, 9:56:50 AM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        m=nums[0]
        for i in nums:
            if i<m:
                m=i
        return m