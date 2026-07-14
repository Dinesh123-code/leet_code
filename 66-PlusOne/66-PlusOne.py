# Last updated: 7/14/2026, 10:12:17 AM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        s=""
4        for i in digits:
5            s=s+str(i)
6        a=int(s)+1
7        l=[]
8        for i in str(a):
9            l.append(int(i))
10        return l