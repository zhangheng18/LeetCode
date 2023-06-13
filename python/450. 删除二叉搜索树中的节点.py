# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == key:
            # 没有左树 返回右树
            if root.left is None:
                return root.right
            # 没有右树 返回左数
            if root.right is None:
                return root.left

            # 找右树的最小节点
            min_node = self.get_min_node(root.right)
            # 删除右子树最小的节点
            root.right = self.deleteNode(root.right, min_node.val)
            # 最小节点替换 当前节点
            min_node.right = root.right
            min_node.left = root.left
            root = min_node
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

    def get_min_node(self, root: Optional[TreeNode]):
        # 最左边就是最小
        while root.left:
            root = root.left
        return root
