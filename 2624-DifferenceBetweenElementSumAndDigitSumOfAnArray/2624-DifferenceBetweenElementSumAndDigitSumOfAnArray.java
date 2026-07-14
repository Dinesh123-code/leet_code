// Last updated: 7/14/2026, 9:55:29 AM
class Solution {
    public int differenceOfSum(int[] nums) {
        int n=nums.length;
        int esum=0,dsum=0;
        for(int i=0;i<n;i++){
            esum+=nums[i];
        }
        for(int i=0;i<n;i++){
            int temp=nums[i];
            while(temp>0){
                int d=temp%10;
                dsum+=d;
                temp=temp/10;
            }
        }
        return esum - dsum;
    }
}