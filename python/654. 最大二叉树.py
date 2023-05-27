# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def build(nums, left, right):
            if left >= right:
                return

            # 最大值 和索引
            index, max_val = left, nums[left]
            for i in range(left, right):
                if nums[i] > max_val:
                    index, max_val = i, nums[i]

            root = TreeNode(max_val)
            # 递归构建左右子树
            root.left = build(nums, left, index)
            root.right = build(nums, index + 1, right)

            return root

        return build(nums, 0, len(nums))
