# Last updated: 7/14/2026, 11:42:53 AM
1class Solution:
2    def mySqrt(self, n: int) -> int:
3        i=1
4        while i*i<=n:
5            i+=1
6        return i-1