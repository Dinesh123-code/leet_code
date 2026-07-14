# Last updated: 7/14/2026, 9:56:02 AM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        for ch in jewels:
            c+=stones.count(ch)
        return c