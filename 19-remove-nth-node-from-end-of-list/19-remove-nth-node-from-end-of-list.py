# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        turtleNode = dummyNode
        bunnyNode = head
        
        for i in range(n):
            bunnyNode = bunnyNode.next
                
        while bunnyNode:
            turtleNode = turtleNode.next
            bunnyNode = bunnyNode.next

        turtleNode.next = turtleNode.next.next
        
        return dummyNode.next