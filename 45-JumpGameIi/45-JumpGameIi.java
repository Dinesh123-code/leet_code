// Last updated: 7/14/2026, 9:57:29 AM
class Solution {
    public int jump(int[] nums) {
        int j=0;
        int e=0;
        int m_r=0;
        for(int i=0;i<nums.length-1;i++){
            m_r=Math.max(m_r,i+nums[i]);
            if(i==e){
                j++;
                e=m_r;
            }

        }
        return j;
    }
}