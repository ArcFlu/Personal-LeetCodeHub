# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Null cases first
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        rootNode = ListNode()
        headNode = rootNode
        
        currNode1 = list1
        currNode2 = list2
        
        
        while currNode1 and currNode2:
            if currNode1.val <= currNode2.val:
                headNode.next = currNode1
                currNode1 = currNode1.next
                headNode = headNode.next
            else:
                headNode.next = currNode2
                currNode2 = currNode2.next
                headNode = headNode.next
                
        if not currNode1:
                headNode.next = currNode2
                currNode2 = currNode2.next
                headNode = headNode.next
        elif not currNode2:
                headNode.next = currNode1
                currNode1 = currNode1.next
                headNode = headNode.next
                
        return rootNode.next