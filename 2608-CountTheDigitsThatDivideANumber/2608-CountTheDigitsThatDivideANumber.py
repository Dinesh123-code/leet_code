# Last updated: 7/14/2026, 9:55:34 AM
class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        a=num
        while num>0:
            d=num%10
            if a%d==0:
                count+=1
            num//=10
        return count