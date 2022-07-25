class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        sumArray = [0] * amount
        coinSet = set(coins)
        
        for i in range(amount):
            currAmount = i + 1
            if currAmount in coinSet:
                sumArray[i] = 1
            else:
                minSum = None
                for coin in coins:
                    currSum = currAmount - coin - 1
                    if currSum < 0:
                        continue
                    elif sumArray[currSum] != 0:
                        if not minSum:
                            minSum = sumArray[currSum] + 1
                        else:
                            minSum = min(minSum, sumArray[currSum] + 1)   
                if not minSum:
                    sumArray[i] = 0
                else:
                    sumArray[i] = minSum
            
        return sumArray[amount - 1] if sumArray[amount - 1] > 0 else -1
                        