class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashMap = {} 
        heap = []
        for point in points:
            distance = math.dist([0,0], point)
            heap.append(distance)
            if distance not in hashMap:
                hashMap[distance] = [point]
            else:
                hashMap[distance].append(point)
                
        heapq.heapify(heap)
        retList = []
        while len(retList) < k:
            retList += hashMap[heapq.heappop(heap)]
        return retList