"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.first, self.last = None, None

        def helper(node):
            if not node:
                return None
            helper(node.left)
            if self.last:
                self.last.right = node
                node.left = self.last
            else:
                self.first = node
            self.last = node
            helper(node.right)
        if not root:
            return None
        helper(root)
        self.last.right = self.first
        self.first.left = self.last
        return self.first


class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return
        first = Node(0, None, None)
        last = first
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            last.right = node
            node.left = last
            node = node.right
            last = last.right
        first.right.left = last
        last.right = first.right
        return first.right
