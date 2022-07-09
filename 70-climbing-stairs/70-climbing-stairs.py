class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = []
        self.memo.append(1)
        self.memo.append(2)
        
        for index in range(2, n):
            ans = self.memo[index - 1] + self.memo[index - 2] 
            self.memo.append(ans)
                
        return self.memo[n - 1]