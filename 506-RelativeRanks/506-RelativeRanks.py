# Last updated: 7/14/2026, 9:56:09 AM
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr=sorted(score,reverse=True)
        d={}
        for i in range(len(arr)):
            if i==0:
                d[arr[i]]="Gold Medal"
            elif i==1:
                d[arr[i]]="Silver Medal"
            elif i==2:
                d[arr[i]]="Bronze Medal"
            else:
                d[arr[i]]=str(i+1)
        ans=[]
        for i in score:
            ans.append(d[i])
        return ans