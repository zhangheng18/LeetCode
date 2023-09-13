# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """广度优先"""
        if not root:
            return 0

        q = Queue()
        q.put(root)

        depth = 1
        while not q.empty():
            for i in range(q.qsize()):
                cur = q.get()
                # 遍历到最后一层
                if not cur.left and not cur.right:
                    return depth

                # 添加 每一层的节点
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
            # 深度 +1
            depth += 1

        return depth
