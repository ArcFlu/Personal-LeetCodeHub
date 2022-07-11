class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window length - most frequent character counter <= k?
        hashMap = {}
        startPointer = 0
        endPointer = 0
        maxSubLength = 0
        while endPointer < len(s):
            curLetter = s[endPointer]
            if curLetter not in hashMap:
                hashMap[curLetter] = 1
            else:
                hashMap[curLetter] += 1
            
            mostFrequentLength = 0
            for letters in hashMap:
                mostFrequentLength = max(mostFrequentLength, hashMap[letters])                
            curWindowLength = endPointer - startPointer + 1
            
            # find valid startpointer for sliding window
            while curWindowLength - mostFrequentLength > k:
                hashMap[s[startPointer]] -= 1
                startPointer += 1
                curWindowLength -= 1
                for letters in hashMap:
                    mostFrequentLength = max(mostFrequentLength, hashMap[letters]) 
                curWindowLength = endPointer - startPointer + 1
            maxSubLength = max(maxSubLength, curWindowLength)
            endPointer += 1
            
        return maxSubLength