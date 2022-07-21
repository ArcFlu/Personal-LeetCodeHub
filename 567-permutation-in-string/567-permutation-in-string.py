class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window and two arrays
        # Return true if 26 matches, else False
        
        s1Array = [0] * 26
        s2Array = [0] * 26
        matches = 0
        
        if len(s1) > len(s2):
            return False
                
        for n in range(len(s1)):
            s1Array[ord(s1[n]) - ord('a')] += 1
            s2Array[ord(s2[n]) - ord('a')] += 1
        
        for n in range(26):
            if s1Array[n] == s2Array[n]:
                matches += 1
        
        if matches == 26:
            return True
        
        rightPointer = len(s1)
        leftPointer = 0
        for n in range(len(s1), len(s2), 1):
            newLetter = s2[rightPointer]
            oldLetter = s2[leftPointer]
            

            if s2Array[ord(newLetter) - ord('a')] == s1Array[ord(newLetter) - ord('a')]:
                matches -= 1
                s2Array[ord(newLetter) - ord('a')] += 1
            else:
                s2Array[ord(newLetter) - ord('a')] += 1
                if s2Array[ord(newLetter) - ord('a')] == s1Array[ord(newLetter) - ord('a')]:
                    matches += 1
                
            if s2Array[ord(oldLetter) - ord('a')] == s1Array[ord(oldLetter) - ord('a')]:
                matches -= 1
                s2Array[ord(oldLetter) - ord('a')] -= 1
            else:
                s2Array[ord(oldLetter) - ord('a')] -= 1
                if s2Array[ord(oldLetter) - ord('a')] == s1Array[ord(oldLetter) - ord('a')]:
                    matches += 1

            if matches == 26:
                return True

            rightPointer += 1
            leftPointer += 1
            
        
        return False
        
    