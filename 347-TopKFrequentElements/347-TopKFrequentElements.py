# Last updated: 7/14/2026, 9:56:20 AM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=[]
        for i in range(k):
            maxi=max(d,key=d.get)
            ans.append(maxi)
            del d[maxi]
        return ans
        