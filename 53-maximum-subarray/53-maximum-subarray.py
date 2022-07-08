class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        self.max = nums[0]
        currSum = nums[0]
        for num in range(1, len(nums)):
            if currSum < 0:
                currSum = 0
            currSum += nums[num]
            self.max = max(self.max, currSum)

        return self.max