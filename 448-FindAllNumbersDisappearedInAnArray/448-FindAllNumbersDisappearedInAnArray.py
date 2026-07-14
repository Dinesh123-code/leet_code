# Last updated: 7/14/2026, 9:56:16 AM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s=set(nums)
        ans=[]
        for i in range(1,len(nums)+1):
            if i not in s:
                ans.append(i)
        return ans