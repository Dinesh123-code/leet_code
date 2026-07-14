# Last updated: 7/14/2026, 9:56:34 AM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
            if i >= k:
                s.remove(nums[i - k])
        return False