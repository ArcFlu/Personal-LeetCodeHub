class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heapq._heapify_max(stones)
            stoneX = heapq._heappop_max(stones)
            stoneY = heapq._heappop_max(stones)
            newStone = stoneX - stoneY
            if newStone > 0:
                heapq.heappush(stones, newStone)
                
        if len(stones) == 1:
            return stones[0]
        else:
            return 0