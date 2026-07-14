# Last updated: 7/14/2026, 9:56:29 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)+1):
            if i not in nums:
                return i