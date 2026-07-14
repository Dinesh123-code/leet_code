// Last updated: 7/14/2026, 9:55:57 AM
class Solution{
    public int tribonacci(int n){
        if(n==1 || n==2) 
        return 1; 
        int t0 =0,t1=1,t2=1,tn=0;
        for(int i=3;i<=n;i++){
            tn=t0+t1+t2; 
            t0=t1;
            t1=t2; 
            t2=tn; 
        }
        return tn; 
    }
}
public class Main{
    public static void main(String[] args){
        Solution solution=new Solution();
        int n=4;
        System.out.println(solution.tribonacci(n)); 
    }
}