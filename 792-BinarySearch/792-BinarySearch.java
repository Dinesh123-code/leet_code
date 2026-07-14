// Last updated: 7/14/2026, 9:56:00 AM
class Solution {
    public int search(int[] nums, int target) {
        for(int i=0;i<nums.length;i++){
            if(nums[i]==target)
            return i;
        }
        return -1;
    }
}