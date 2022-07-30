# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        turtle = head
        bunny = head
        
        if bunny.next is None:
            return False
        bunny = bunny.next
        if bunny.next is None:
            return False    
        
        while turtle != bunny:
            if bunny is None:
                return False
            
            if bunny.next is None:
                return False
            bunny = bunny.next
            if bunny.next is None:
                return False    
            bunny = bunny.next
            
            turtle = turtle.next
        
        
        return True   
        