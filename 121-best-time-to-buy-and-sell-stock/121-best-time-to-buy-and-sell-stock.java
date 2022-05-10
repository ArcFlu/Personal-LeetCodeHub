class Solution {
    public int maxProfit(int[] prices) {
        int maxDiff = 0;
        int high = 0;
        int low = 0;
        
        if (prices.length <= 1)
            return 0;
        
        high = prices[0];
        low = prices[0];
        
        for (int i = 1; i < prices.length; i++){
            // buy low sell high
            low = Math.min(low, prices[i]);
            int curDiff = prices[i] - low;
            maxDiff = Math.max(maxDiff, curDiff);
                
        }
        return maxDiff;
    }
}