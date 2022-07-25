class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        retVal = []
        leftPointer = 0
        rightPointer = k
        
        q = deque()
        for n in range(k):
            if not q:
                q.append(nums[n])
                continue
            
            while q and q[-1] < nums[n]:
                q.pop()

            q.append(nums[n])  
        
        retVal.append(q[0])
        
        while rightPointer < len(nums):
            while q and q[-1] < nums[rightPointer]:
                q.pop()
            
            q.append(nums[rightPointer])            
            rightPointer += 1
            if nums[leftPointer] == q[0]:
                q.popleft()
            leftPointer += 1
            
            retVal.append(q[0])
            
            
        return retVal