class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        startPointer = 0
        endPointer = len(numbers) - 1
        
        while startPointer < endPointer:
            if numbers[startPointer] + numbers[endPointer] == target:
                return [startPointer + 1, endPointer + 1]
            if numbers[startPointer] + numbers[endPointer] > target:
                endPointer -= 1
            else:
                startPointer += 1

        