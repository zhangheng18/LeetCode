# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)
        # 后续遍历

        # 拉平左右子树
        left = root.left
        right = root.right

        # 左子树作为右子树
        root.left = None
        root.right = left

        # 右子树 放到原左子树的末端
        p = root
        while p.right:
            p = p.right
        p.right = right
