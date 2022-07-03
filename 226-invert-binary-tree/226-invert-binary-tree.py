# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.recursion(root)
        
    def recursion(self, root: Optional[TreeNode]):
        if root is None:
            return None
        
        leftChild = self.recursion(root.left)
        rightChild = self.recursion(root.right)
        
        filler = leftChild
        root.right = leftChild
        root.left = rightChild
        return root