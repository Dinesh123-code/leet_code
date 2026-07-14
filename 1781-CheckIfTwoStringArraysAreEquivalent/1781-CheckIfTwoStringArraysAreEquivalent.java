// Last updated: 7/14/2026, 9:55:50 AM
class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        int m=word1.length;
        int n=word2.length;
        String ch1="";
        String ch2="";
        for(int i=0;i<m;i++){
            
            ch1+=word1[i];
        }
        
        for(int j=0;j<n;j++){
            
            ch2+=word2[j];
        }
        if(ch1.equals(ch2))
        return true;
        else
        return false;
    }
}