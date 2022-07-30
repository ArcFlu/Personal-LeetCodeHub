class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        originalColor = image[sr][sc]
        visited = set()
        
        def dfs(currRow, currCol):
            if (currRow, currCol) not in visited:
                visited.add((currRow, currCol))
            else:
                return
            
            if image[currRow][currCol] != originalColor:
                return
            else:
                image[currRow][currCol] = color
                directions = [(0, -1), (0, 1), (1, 0), (-1,0)]
                
                for direction in directions:
                    newRow = currRow + direction[0]
                    newCol = currCol + direction[1]
                    
                    if newRow > -1 and newRow < len(image) and newCol > -1 and newCol < len(image[0]):
                        dfs(newRow, newCol)
            
            return
        dfs(sr, sc)
        return image