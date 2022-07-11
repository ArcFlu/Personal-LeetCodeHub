class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowList = [[0] * 9 for i in range(10)] 
        colList = [[0] * 9 for i in range(10)]
        cellList = [[[0] * 9 for i in range(10)] for i in range(10)]
        
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                currNum = int(board[i][j])
                if rowList[i][currNum - 1] is 1 or colList[j][currNum - 1] is 1 or cellList[int(i/3)][int(j/3)][currNum - 1] is 1:
                    print(rowList[i][currNum - 1])
                    print(colList[j][currNum - 1])
                    print(cellList[int(i/3)][int(j/3)][currNum - 1])
                    print(rowList)
                    print(colList)
                    print(cellList)
                    print(i)
                    print(j)
                    return False
                else:
                    rowList[i][currNum - 1] = 1
                    colList[j][currNum - 1] = 1
                    cellList[int(i/3)][int(j/3)][currNum - 1] = 1

    
        return True
                    
                    