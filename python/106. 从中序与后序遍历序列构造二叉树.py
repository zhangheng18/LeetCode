# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 中序值-索引映射
        self.val2index = {num: i for i, num in enumerate(inorder)}
        return self.build(
            inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1
        )

    def build(self, inorder, inor_start, inor_end, postorder, post_start, post_end):
        if post_start > post_end:
            return
        # 后序 root节点值
        root_val = postorder[post_end]

        # 中序 root 节点 索引
        index = self.val2index[root_val]
        # 左叶长度
        left_size = index - inor_start

        root = TreeNode(root_val)
        # 左树： 中序 开始 到 index -1  后序： 开始位置   开始+左叶长度 -1
        root.left = self.build(
            inorder,
            inor_start,
            index - 1,
            postorder,
            post_start,
            post_start + left_size - 1,
        )

        # 右树： 中序 index + 1 到 结束位置   后序： 开始+左叶长度 结束-1
        root.right = self.build(
            inorder,
            index + 1,
            inor_end,
            postorder,
            post_start + left_size,
            post_end - 1,
        )

        return root
