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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        left_most = root
        while left_most.left:
            node = left_most
            while node:
                if node.right:
                    node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                node = node.next
            left_most = left_most.left
        return root
