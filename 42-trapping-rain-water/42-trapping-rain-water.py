class Solution:
    def trap(self, height: List[int]) -> int:
        minLeft = 0
        minRight = 0

        leftPointer = 0
        rightPointer = len(height) - 1
        liquidCount = 0
        while leftPointer <= rightPointer:
            if minLeft <= minRight:
                currWater = min(minLeft, minRight) - height[leftPointer]
                if currWater > 0:
                    liquidCount += currWater
                minLeft = max(minLeft,height[leftPointer])
                leftPointer += 1
            else:
                currWater = min(minLeft, minRight) - height[rightPointer]
                if currWater > 0:
                    liquidCount += currWater
                minRight = max(minRight,height[rightPointer])
                rightPointer -= 1


        return liquidCount