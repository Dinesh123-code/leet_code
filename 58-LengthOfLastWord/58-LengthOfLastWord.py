# Last updated: 7/14/2026, 9:57:15 AM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w=s.split()
        return len(w[-1])