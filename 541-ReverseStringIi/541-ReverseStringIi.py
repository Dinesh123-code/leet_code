# Last updated: 7/14/2026, 9:56:08 AM
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans=list(s)
        for i in range(0,len(ans),2*k):
            ans[i:i+k]=reversed(ans[i:i+k])
        return "".join(ans)