class Solution:
    def maxArea(self, height: List[int]) -> int:
        # you can't judge by the highest height or lowest
        # so maybe look at area between each line
        
        startLine = 0
        endLine = len(height) - 1
        maxWater = 0
        
        while startLine < endLine:
            maxWater = max(maxWater, (endLine - startLine) *                                            min(height[startLine], height[endLine]))
            if height[startLine] > height[endLine]:
                endLine -= 1
            else:
                startLine += 1
            
        return maxWater