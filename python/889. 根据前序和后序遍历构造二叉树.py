# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        self.val2index = {num: i for i, num in enumerate(postorder)}
        return self.build(
            preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1
        )

    def build(self, preorder, pre_start, pre_end, postorder, post_start, post_end):
        if pre_start > pre_end:
            return

        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])

        root_val = preorder[pre_start]
        root_left_val = preorder[pre_start + 1]

        root_index = self.val2index[root_left_val]
        left_size = root_index - post_start + 1

        root = TreeNode(root_val)
        root.left = self.build(
            preorder,
            pre_start + 1,
            pre_start + left_size,
            postorder,
            post_start,
            root_index,
        )
        root.right = self.build(
            preorder,
            pre_start + left_size + 1,
            pre_end,
            postorder,
            root_index + 1,
            post_end - 1,
        )

        return root
