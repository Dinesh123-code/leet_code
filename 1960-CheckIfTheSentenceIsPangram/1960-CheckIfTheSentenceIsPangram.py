# Last updated: 7/14/2026, 9:55:46 AM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch not in sentence:
                return False
        return True