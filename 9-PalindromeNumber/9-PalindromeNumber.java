// Last updated: 7/14/2026, 9:57:41 AM
class Solution {
    public boolean isPalindrome(int x) {
        int temp=x,d,r=0;
        if(x<0 || (x!=0 && x%10==0))
        return false;
        while(x!=0){
            d=x%10;
            r=r*10+d;
            x=x/10;
        }
        if(r==temp)
        return true;
        else
        return false;
    }
}