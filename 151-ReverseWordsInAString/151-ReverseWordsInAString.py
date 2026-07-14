# Last updated: 7/14/2026, 9:56:53 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        w=s.split()
        return " ".join(w[::-1])