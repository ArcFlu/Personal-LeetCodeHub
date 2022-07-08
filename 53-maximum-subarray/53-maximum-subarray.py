class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        self.max = None
        currSum = 0
        for num in nums:
            currSum += num
            if self.max is None:
                self.max = currSum
            self.max = max(self.max, currSum)
            if currSum < 0:
                currSum = 0

        return self.max