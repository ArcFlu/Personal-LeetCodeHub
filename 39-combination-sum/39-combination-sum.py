class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Bottom-up approach
        # for target k, we computer the sets from 1 to k
        # as we go along, we reference previous ones and add their sets 
        # if there's a match
        
        # Create a set for easy lookups of digits
        # Dict mapping 1 to k storing all the subsets
        # We return all sets in the kth value of the dict
        
        self.hashSet = set(candidates)
        self.subsetDict = {n: [] for n in range(1, target + 1)}
        
        for n in range(1, target + 1):
            self.recursive(n)
            print(self.subsetDict[n])
        
        return self.subsetDict[target]
            
    def recursive(self, target):
        # Is there a number that matches k? 
        if target in self.hashSet:
            self.subsetDict[target].append([target])
        
        # Now we need to see if there are any numbers that add up to target
        for i in range(target - 1, target // 2 - 1, -1):
            if i < target // 2:
                break
            if i == 0:
                if i in self.hashSet:
                    self.subsetDict[target].append([i, i])
                continue
            for subSets in self.subsetDict[i]:
                for subsubSets in self.subsetDict[target - i]:
                    newCombo = []
                    newCombo += subSets + subsubSets
                    newCombo.sort()
                    if newCombo not in self.subsetDict[target]:
                        self.subsetDict[target].append(newCombo)
                
                    
        return
                    
                