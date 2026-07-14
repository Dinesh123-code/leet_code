# Last updated: 7/14/2026, 9:56:42 AM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]