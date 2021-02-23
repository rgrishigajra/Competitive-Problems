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
            return None
        leftmost = root
        while leftmost:
            node = leftmost
            prev = None
            while node:
                if node.left:
                    if prev:
                        prev.next = node.left
                    prev = node.left
                if node.right:
                    if prev:
                        prev.next = node.right
                    prev = node.right
                node = node.next
            while leftmost and not leftmost.left and not leftmost.right:
                leftmost = leftmost.next
            if leftmost:
                if leftmost.left:
                    leftmost = leftmost.left
                else:
                    leftmost = leftmost.right
        return root
