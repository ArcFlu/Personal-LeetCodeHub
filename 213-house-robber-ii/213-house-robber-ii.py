class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def helper(houseArray):
            sumArray = [0] * 2
            
            sumArray[0] = houseArray[0]
            sumArray[1] = max(houseArray[0], houseArray[1])
            
            for i in range(2, len(houseArray), 1):
                sumArray[i % 2] = houseArray[i] + sumArray[i % 2] if houseArray[i] + sumArray[i % 2] >= sumArray[(i + 1) % 2] else sumArray[(i + 1)% 2]
                
            return max(sumArray[0], sumArray[1])
        
        print(nums)
        print(nums[1:])
        print(nums[:-1])
            
        return max(helper(nums[1:]), helper(nums[:-1]))        
        
        