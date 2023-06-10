# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid_bst(root, -float('inf'), float('inf'))

    def is_valid_bst(self, root, min_, max_):
        if not root:
            return True
        # 当前节点的数 > 大于最小值  and 当前节点的数 < 小于最大值
        if root.val <= min_ or root.val >= max_:
            return False
        #左树最大值 root.val, 右树最小值 root.val
        return self.is_valid_bst(root.left, min_, root.val) and self.is_valid_bst(root.right, root.val, max_)