// Last updated: 7/14/2026, 9:56:43 AM
class Solution {
    public int rob(int[] nums) {
        int p1=0;
        int p2=0;
        for(int n:nums){
            int temp=p2; 
            if(p1+n > p2){
                p2=p1+n; 
            }
            p1=temp; 
        }
        return p2; 
    }
}