# Last updated: 7/14/2026, 9:56:31 AM
class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            s=0
            while num>0:
                d=num%10
                s+=d
                num//=10
            num=s
        return num    