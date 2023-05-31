# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        # 记录重复的子树
        memo = defaultdict(int)
        res = []

        def traverse(root):
            if root is None:
                return "#"

            left = traverse(root.left)
            right = traverse(root.right)

            sub_tree = f"{left},{right},{root.val}"
            # 多次重复 只计一次
            if memo.get(sub_tree) == 1:
                res.append(root)
            # 出现次数+1
            memo[sub_tree] += 1
            return sub_tree

        traverse(root)
        return res
