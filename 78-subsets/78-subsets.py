class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        retList = [[]]
        
        for num in nums:
            retList += [curr + [num] for curr in retList]
            
        return retList