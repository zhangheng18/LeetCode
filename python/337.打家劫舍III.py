# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.meom = {}

    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root in self.meom:
            return self.meom[root]

        left = 0 
        if root.left:
            left = self.rob(root.left.left) + self.rob(root.left.right)
        right = 0
        if root.right:
            right = self.rob(root.right.left) + self.rob(root.right.right)


        do_it = root.val + left + right
        do_no = self.rob( root.left) + self.rob(root.right)
        res = max(do_it, do_no)
        
        self.meom[root] = res
        return res
