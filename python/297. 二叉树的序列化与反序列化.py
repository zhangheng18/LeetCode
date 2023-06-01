# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    SEP = ","
    NULL = "#"

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        sb = []
        self._serialize(root, sb)
        return f"{self.SEP}".join(map(str, sb))

    def _serialize(self, root, sb):
        if not root:
            sb.append(self.NULL)
            return

        sb.append(root.val)
        self._serialize(root.left, sb)
        self._serialize(root.right, sb)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        node = data.split(self.SEP)
        return self._deserialize(node)

    def _deserialize(self, node):
        if not node:
            return None
        first = node.pop(0)
        if first == self.NULL:
            return None
        root = TreeNode(int(first))

        root.left = self._deserialize(node)
        root.right = self._deserialize(node)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
