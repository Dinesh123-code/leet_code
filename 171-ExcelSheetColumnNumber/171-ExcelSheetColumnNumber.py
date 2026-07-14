# Last updated: 7/14/2026, 9:56:46 AM
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans=0
        for ch in columnTitle:
            ans=ans*26+ord(ch)-64
        return ans