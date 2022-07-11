class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        startPointer = 0
        endPointer = 0
        hashSet = set()
        longestLength = 0
        while endPointer < len(s):
        # if the current letter is already hashset, we need to pop from set
            while s[endPointer] in hashSet:
                hashSet.remove(s[startPointer])
                startPointer += 1
            hashSet.add(s[endPointer])

            longestLength = max(longestLength, endPointer - startPointer + 1)
            endPointer += 1
        
        return longestLength
                