// Last updated: 7/14/2026, 9:56:38 AM
class Solution {
    public int addDigits(int num) {
        if (num == 0)
            return 0;
        if (num % 9 == 0)
            return 9;
        return num % 9;
    }
}