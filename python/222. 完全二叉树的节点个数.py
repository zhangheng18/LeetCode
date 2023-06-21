# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l, r = root, root
        hl, hr = 0, 0

        while l:
            l = l.left
            hl += 1
        while r:
            r = r.right
            hr += 1
        if hl == hr:
            # 满二叉树 节点数
            return 2 ** (hr) - 1

        # 普通二叉树节点数
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
