// Last updated: 7/14/2026, 9:56:56 AM
class Solution {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        for(int i=0;i<nums.length-1;i+=2){
            
                if(nums[i]!=nums[i+1])
                {
                   return nums[i];
                }
            
        }
            return nums[nums.length-1];
        
    }
}