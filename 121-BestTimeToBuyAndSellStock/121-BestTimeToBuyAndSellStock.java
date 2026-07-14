// Last updated: 7/14/2026, 9:57:11 AM
class Solution {
    public int maxProfit(int[] prices) {
        int minprice=prices[0];
        int maxprofit=0;
        for(int i=0;i<prices.length;i++){
            if(prices[i]<minprice){
                minprice=prices[i];
            }
            int profittoday=prices[i]-minprice;
            if(profittoday>maxprofit){
                maxprofit=profittoday;
            }
        }
        return maxprofit;
    }
}