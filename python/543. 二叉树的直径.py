# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diamter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_depth(root)
        return self.max_diamter

    def max_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_max_diamter = self.max_depth(root.left)
        right_max_diamter = self.max_depth(root.right)
        self.max_diamter = max(self.max_diamter, left_max_diamter + right_max_diamter)

        return 1 + max(left_max_diamter, right_max_diamter)