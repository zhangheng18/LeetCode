# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0

        self.traverse(root)
        return root

    def traverse(self, root):
        if root is None:
            return
        # 二叉树 逆中序遍历 （降序)
        self.traverse(root.right)

        # 记录累加和
        self.sum += root.val
        root.val = self.sum

        self.traverse(root.left)
