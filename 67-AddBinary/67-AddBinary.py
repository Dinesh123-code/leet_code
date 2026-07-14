# Last updated: 7/14/2026, 10:17:53 AM
1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        x=int(a,2)
4        y=int(b,2)
5        return bin(x+y)[2:]