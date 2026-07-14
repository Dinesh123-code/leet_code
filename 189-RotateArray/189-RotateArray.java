// Last updated: 7/14/2026, 9:56:45 AM
class Solution {
    public void rotate(int[] nums, int k) {
        int n=nums.length;
        k=k%n;
        int r[]=new int[n];
        int j=0;
        for(int i=n-k;i<n;i++){
            r[j]=nums[i];
            j++;
        }
        for(int i=0;i<n-k;i++){
            r[j]=nums[i];
            j++;
        }
        for(int i=0;i<n;i++){
            nums[i]=r[i];
        }
    }
}