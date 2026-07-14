# Last updated: 7/14/2026, 9:56:37 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False