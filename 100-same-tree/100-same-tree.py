# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.recursion(p, q)
    
    def recursion(self, p, q):
        try:
            if p.val != q.val:
                return False
            leftVal = self.recursion(p.left, q.left)
            rightVal = self.recursion(p.right, q.right)
            
            if leftVal and rightVal:
                return True
        except:
            if p is None and q is None:
                return True
            else:
                return False
        