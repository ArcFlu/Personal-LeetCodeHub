class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        magDict = {}
        
        for i in magazine:
            if i not in magDict:
                magDict[i] = 1
            else:
                magDict[i] += 1
                
        for i in ransomNote:
            if i not in magDict:
                return False
            else:
                magDict[i] -= 1
                if magDict[i] == 0:
                    del magDict[i]
            
        
        return True