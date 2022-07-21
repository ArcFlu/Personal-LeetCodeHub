class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minimumSubstring = ""
        
        if len(t) > len(s):
            return minimumSubstring
        
        requireMap = {}
        containsMap = {}
        requires = 0
        
        for letter in t:
            if letter not in requireMap:
                requireMap[letter] = 1
                requires += 1
            else:
                requireMap[letter] += 1

        
        leftPointer = 0
        rightPointer = 0
        matches = 0
        while rightPointer < len(s):
            currLetter = s[rightPointer]
            if currLetter not in requireMap:
                rightPointer += 1
                continue
            
            if currLetter not in containsMap:
                containsMap[currLetter] = 1
            else:
                containsMap[currLetter] += 1
            
            if containsMap[currLetter] == requireMap[currLetter]:
                matches += 1

            if matches == requires:
                while matches == requires:
                    leftLetter = s[leftPointer]
                    currString = s[leftPointer:rightPointer + 1]
                
                    if len(minimumSubstring) == 0:
                        minimumSubstring = currString
                    elif len(minimumSubstring) > len(currString):
                        minimumSubstring = currString
                        
                    if leftLetter in requireMap:
                        containsMap[leftLetter] -= 1
                        if containsMap[leftLetter] < requireMap[leftLetter]:
                            matches -= 1
                            
                    leftPointer += 1
                
                while leftPointer < rightPointer and s[leftPointer] not in requireMap:
                    leftPointer += 1
                    
            rightPointer += 1
        
        
        return minimumSubstring