"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # 遍历 三叉树
        if not root:
            return
        self.traverse(root.left, root.right)
        return root

    def traverse(self, node_l, node_r):
        if (not node_l) or (not node_r):
            return
        # 连接node_l 和 node_r
        node_l.next = node_r

        # 同父节点的两个子节点
        self.traverse(node_l.left, node_l.right)
        self.traverse(node_r.left, node_r.right)

        # 跨父节点 的两个子节点
        self.traverse(node_l.right, node_r.left)
