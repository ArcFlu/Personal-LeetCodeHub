# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.traverse(root, subRoot)
    
    def traverse(self, root, subRoot):   
        if self.verify(root, subRoot):
            return True
        if not root:
            return False
        else:
            return (self.traverse(root.left, subRoot) or 
                    self.traverse(root.right, subRoot)
                   )
        
    def verify(self, root, subRoot):
        if not (root and subRoot):
            return root is subRoot

        if root.val == subRoot.val:
            return (self.verify(root.left, subRoot.left) and                                         self.verify(root.right, subRoot.right))
        else:
            return False
        