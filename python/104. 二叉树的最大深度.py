# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.depth = 0
        self.max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.max_depth

    def traverse(self, root):
        if root is None:
            return

        # 前序遍历 深度+1
        self.depth += 1
        # 更新最大深度
        self.max_depth = max(self.max_depth, self.depth)

        self.traverse(root.left)
        self.traverse(root.right)

        # 后序 深度-1
        self.depth -= 1