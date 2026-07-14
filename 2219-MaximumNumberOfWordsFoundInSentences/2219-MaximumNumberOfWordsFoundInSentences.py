# Last updated: 7/14/2026, 9:55:45 AM
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max=0
        for s in sentences:
            words=len(s.split())
            if words>max:
                max=words
        return max