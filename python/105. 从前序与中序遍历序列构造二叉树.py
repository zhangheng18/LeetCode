# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 中序值-索引映射
        self.val_index = {num: i for i, num in enumerate(inorder)}
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preorder, pre_start, pre_end, inorder, inor_start, inor_end):
        # 前序
        if pre_start > pre_end:
            return

        # 前序 root节点值
        root_val = preorder[pre_start]

        # 中序 root 节点 索引
        index = self.val_index[root_val]

        # 左叶长度
        left_size = index - inor_start

        # 构造根节点
        root = TreeNode(root_val)

        # 左树： 前序： 开始位置+1 左叶长度   中序 开始 到 index -1
        root.left = self.build(
            preorder,
            pre_start + 1,
            pre_start + left_size,
            inorder,
            inor_start,
            index - 1,
        )
        # 右树： 前序： 开始位置+1+左叶长度 到 结束位置   中序 index + 1 到 结束位置
        root.right = self.build(
            preorder, pre_start + left_size + 1, pre_end, inorder, index + 1, inor_end
        )

        return root
