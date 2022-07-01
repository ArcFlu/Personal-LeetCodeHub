# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return False
        turtle = head
        rabbit = head.next
        while rabbit is not None and turtle is not None:
            if (turtle is rabbit):
                return True
            turtle = turtle.next
            rabbit = rabbit.next
            if rabbit is not None:
                rabbit = rabbit.next
            else:
                return False
            
        
        return False