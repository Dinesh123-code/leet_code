# Last updated: 7/14/2026, 9:56:51 AM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=nums[0]
        for i in range(n):
            p=1
            for j in range(i,n):
                p*=nums[j]
                if p>maxi:
                    maxi=p
        return maxi