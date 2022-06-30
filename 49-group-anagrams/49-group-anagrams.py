class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string, i'm gonna get every letter and put it into an array
        # of 26. after, i will construct a string of length 26 that consists
        # of these and then check if the dictionary contains this string
        # either I will create a new array or add the current string to current
        finalDict = {}
        for curr in strs:
            tempList = [0]*26
            for i in curr:
                tempList[ord(i) - ord('a')] += 1
            endStr = ''
            for i in tempList:
                endStr += chr(i)
            if endStr not in finalDict:
                finalDict[endStr] = [curr]
            else:
                finalDict[endStr].append(curr)
        return finalDict.values()