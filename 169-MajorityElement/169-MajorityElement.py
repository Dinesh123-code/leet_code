# Last updated: 7/14/2026, 9:56:48 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]