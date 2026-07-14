# Last updated: 7/14/2026, 9:56:26 AM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in set(ransomNote):
            if ransomNote.count(ch) > magazine.count(ch):
                return False
        return True