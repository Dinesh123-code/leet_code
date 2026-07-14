// Last updated: 7/14/2026, 9:55:59 AM
class Solution{
    public int fib(int n){
        if(n==0) 
        return 0; 
        if(n==1) 
        return 1; 
        int a=0; 
        int b=1; 
        int fib=0;
        for(int i=2;i<=n;i++){
            fib=a+b; 
            a=b; 
            b=fib; 
        }
        return fib; 
    }
}
public class Main{
    public static void main(String[] args){
        Solution solution=new Solution();
        int n=4; 
        System.out.println(solution.fib(n)); 
    }
}