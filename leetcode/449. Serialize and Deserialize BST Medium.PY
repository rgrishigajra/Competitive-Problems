# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class intWrapper:
    def __init__(self, i):
        self.val = i

    def incr(self):
        self.val += 1

    def value(self):
        return self.val


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        seq = []
        self._serial(root, seq)
        return ''.join(seq)

    def _serial(self, node, seq):
        if not node:
            seq.append('#')
        else:
            seq.append(chr(node.val+48))
            self._serial(node.left, seq)
            self._serial(node.right, seq)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        return self._deserial(data, intWrapper(0))

    def _deserial(self, data, i):
        idx = i.value()
        val = data[idx]
        i.incr()
        if val == '#':
            return None
        else:
            node = TreeNode(ord(val)-48)
            node.left = self._deserial(data, i)
            node.right = self._deserial(data, i)
            return node


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
