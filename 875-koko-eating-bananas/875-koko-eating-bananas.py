class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        leftRate = 1
        rightRate = max(piles)
        
        while leftRate < rightRate:
            midRate = leftRate + (rightRate - leftRate)/2
            midRate = floor(midRate)
            
            # Simulate
            curHours = 0
            
            for pile in piles:
                curHours += math.ceil(pile/midRate)
            
            if curHours > h:
                leftRate = midRate + 1
            else:
                rightRate = midRate
        
        return rightRate