# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 不存在或找到root
        if root is None or root.val == val:
            return root
        if root.val > val:
            # root.val 大 ，去左树找
            return self.searchBST(root.left, val)
        else:
            # root.val 小 右树找
            return self.searchBST(root.right, val)
