# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.search(root)
    
    def search(self, root):
        if root is None:
            return 0

        return max(self.search(root.left), 
                   self.search(root.right)) + 1

            