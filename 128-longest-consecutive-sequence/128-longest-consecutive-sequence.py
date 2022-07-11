class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxLength = 0
        
        for num in nums:
            if num - 1 not in hashSet:
                currLength = 0
                while num in hashSet:
                    currLength += 1
                    num += 1
                maxLength = max(maxLength, currLength)
            
        return maxLength