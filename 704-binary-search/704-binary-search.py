class Solution:
    def search(self, nums: List[int], target: int) -> int:
        startPointer = 0
        endPointer = len(nums) - 1
        
        while startPointer <= endPointer:
            if nums[startPointer] == target:
                return startPointer
            if nums[endPointer] == target:
                return endPointer
            
            if nums[endPointer] + nums[startPointer] >= target:
                endPointer -= 1
            else:
                startPointer += 1
        
        return -1