# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.depth(root)
        return self.ans
        
    def depth(self, root):
        if root is None:
            return 0
        leftTree = self.depth(root.left)
        rightTree = self.depth(root.right)
        
        self.ans = max(self.ans, leftTree + rightTree)

        return max(leftTree, rightTree) + 1