# Last updated: 7/14/2026, 9:55:35 AM
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0,len(nums),2):
            nums[i],nums[i+1]=nums[i+1],nums[i]
        return nums