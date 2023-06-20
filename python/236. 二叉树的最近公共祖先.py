# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root, p.val, q.val)

    def find(self, root, p, q):
        if root is None:
            return root

        # 前序遍历
        if root.val == p or root.val == q:
            return root

        left = self.find(root.left, p, q)
        right = self.find(root.right, p, q)

        # 公共祖先 p
        if left and right:
            return root

        return left if left else right
