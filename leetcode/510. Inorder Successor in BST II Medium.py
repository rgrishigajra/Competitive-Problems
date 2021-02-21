"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def inorderSuccessor(self, root: 'Node') -> 'Node':
        # TODO: Write your code here
        if not root:
            return root
        if root.right:
            root = root.right
            while root.left:
                root = root.left
            return root
        while root.parent and root.parent.right == root:
            root = root.parent
        return root.parent
