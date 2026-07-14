# Last updated: 7/14/2026, 9:56:32 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return True
        else:
            return False