// Last updated: 7/14/2026, 9:57:24 AM
class Solution {
    public int searchInsert(int[] nums, int target) {
        int n=nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] >= target) {
                return i;
            }
        }
        return nums.length;
    }
}