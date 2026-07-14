# Last updated: 7/14/2026, 9:56:57 AM
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total = 0
        tank = 0
        st = 0

        for i in range(len(gas)):

            total += gas[i] - cost[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                st = i + 1
                tank = 0

        if total >= 0:
            return st
        else:
            return -1