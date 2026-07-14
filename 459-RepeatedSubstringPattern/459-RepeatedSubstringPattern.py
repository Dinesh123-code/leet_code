# Last updated: 7/14/2026, 9:56:14 AM
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        a=s+s
        b=a[1:-1]
        return s in b