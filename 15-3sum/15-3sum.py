class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        posList, negList, zeroList = [], [], []
        res = set()
        
        for num in nums:
            if num > 0:
                posList.append(num)
            elif num < 0:
                negList.append(num)
            else:
                zeroList.append(num)
                
        posSet = set(posList)
        negSet = set(negList)
        
        # I need to check 0 0 0
        if (len(zeroList) >= 3):
            res.add((0,0,0))
        
        # bigNeg + smallPos + smallPos, 
        for i in range(len(posList)):
            for j in range(i + 1, len(posList)):
                sum = posList[i] + posList[j]
                if sum * -1 in negSet:
                    res.add(tuple(sorted([posList[i], posList[j], sum * -1])))
        
        # bigNeg + 0 + bigPos
        if len(zeroList) > 0:
            for num in posList:
                if num*-1 in negSet:
                    res.add(tuple([num*-1, 0, num]))
            
        # smallNeg + smallNeg + bigPos
        for i in range(len(negList)):
            for j in range(i + 1, len(negList)):
                sum = negList[i] + negList[j]
                if sum * -1 in posSet:
                    res.add(tuple(sorted([negList[i], negList[j], sum * -1])))
                            
        return res
        