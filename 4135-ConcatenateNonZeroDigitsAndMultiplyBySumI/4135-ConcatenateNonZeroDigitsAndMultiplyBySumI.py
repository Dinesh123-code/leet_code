# Last updated: 7/14/2026, 9:55:31 AM
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num=0
        s=0
        p=1
        while n>0:
            d=n%10
            if d!=0:
                num=d*p+num
                s+=d
                p*=10
            n//=10
        return num*s
