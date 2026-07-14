# Last updated: 7/14/2026, 9:56:06 AM
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(c**0.5)
        while a<=b:
            s=a*a+b*b
            if s==c:
                return True
            elif s<c:
                a+=1
            else:
                b-=1
        return False