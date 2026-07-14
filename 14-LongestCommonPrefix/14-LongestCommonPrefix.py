# Last updated: 7/14/2026, 9:57:36 AM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p=strs[0]
        for i in strs:
            while i.find(p)!=0:
                p=p[:-1]
        return p