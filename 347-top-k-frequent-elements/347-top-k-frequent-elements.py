class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countList = {}
        
        # first we count the occurence of each number via hashmap
        for num in nums:
            if num not in countList:
                countList[num] = 1
            else:
                countList[num] += 1
                
        bucketList = [[] for i in range(len(nums) + 1)]
        for num in countList:
            bucketList[countList[num]].append(num)
            
            
        retList = []
        for i in range(len(bucketList) - 1, -1, -1):
            if len(retList) >= k:
                return retList
            if len(bucketList[i]) > 0:
                retList += bucketList[i]
            
        return retList
        