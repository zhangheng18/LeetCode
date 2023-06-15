# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build(lo, hi):
            if lo > hi:
                # 不存在节点时 放入None
                return [None]
            res = []
            for mid in range(lo, hi + 1):
                # 左子树
                left_tree = build(lo, mid - 1)

                # 右子树
                right_tree = build(mid + 1, hi)

                # mid 为根节点的值 左右子树组合
                for left in left_tree:
                    for right in right_tree:
                        r = TreeNode(mid)
                        r.left = left
                        r.right = right
                        res.append(r)
            return res

        return build(1, n)
