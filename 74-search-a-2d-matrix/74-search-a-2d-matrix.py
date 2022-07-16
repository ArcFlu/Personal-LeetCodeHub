class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # to get the row, we do position of number / len(row)
        # to get column, we do position of number % len(row)
        numRows = len(matrix)
        numCols = len(matrix[0])
        leftPointer = 0
        rightPointer = numRows * numCols
        
        if matrix[0][0] == target or matrix[numRows - 1][numCols - 1] == target:
            return True
        
        
        while leftPointer != rightPointer:
            nextPos = leftPointer + (rightPointer - leftPointer)/2
            
            if leftPointer == nextPos or rightPointer == nextPos:
                return False
            
            nextPosRow = int(nextPos//numCols)
            nextPosCol = int(nextPos%numCols)
            
            num = matrix[nextPosRow][nextPosCol]
            
            if target < num:
                rightPointer = nextPos
            elif target > num:
                leftPointer = nextPos
            else:
                return True
            
        
        return False