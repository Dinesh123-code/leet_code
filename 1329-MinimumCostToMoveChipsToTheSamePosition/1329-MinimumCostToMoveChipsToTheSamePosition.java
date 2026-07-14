// Last updated: 7/14/2026, 9:55:56 AM
class Solution {
    public int minCostToMoveChips(int[] chips) {
        int evenCount = 0, oddCount = 0;
        
        for (int i = 0; i < chips.length; i++) {
            if (chips[i] % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }
        
        if (evenCount < oddCount) {
            return evenCount;
        } else {
            return oddCount;
        }
    }
}
