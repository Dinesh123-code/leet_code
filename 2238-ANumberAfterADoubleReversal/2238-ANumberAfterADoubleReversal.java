// Last updated: 7/14/2026, 9:55:43 AM
class Solution {
    public boolean isSameAfterReversals(int num) {
        int temp = num;
        int reversed1 = 0, d, reversed2 = 0;
        while (num != 0) {
            d = num % 10;
            reversed1 = reversed1 * 10 + d;
            num /= 10;
        }
        while (reversed1 != 0) {
            d = reversed1 % 10;
            reversed2 = reversed2 * 10 + d;
            reversed1 /= 10;
        }
        return temp == reversed2;
    }
}
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] testNumbers = {123, 120, 0, 101, 10};
        for (int number : testNumbers) {
            boolean result = solution.isSameAfterReversals(number);
            System.out.println("Is the number " + number + " same after reversals? " + result);
        }
    }
}