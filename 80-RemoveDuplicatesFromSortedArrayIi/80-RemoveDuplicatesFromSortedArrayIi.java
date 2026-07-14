// Last updated: 7/14/2026, 9:57:09 AM
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;  // Handle empty array
        int k=2;
        int n=nums.length;
        for(int i=2;i<n;i++){
            if(nums[i]!=nums[k-2]){
                nums[k]=nums[i];
            k++;}
        }
        return k;
    }
}