class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        
        maxSum = 0
        minNum = None
        
        for i in prices:
            if minNum is None:
                minNum = prices[0]
            else:
                minNum = min(minNum, i)
            print(i - minNum)
            maxSum = max(maxSum, i - minNum)
        
        return maxSum
                