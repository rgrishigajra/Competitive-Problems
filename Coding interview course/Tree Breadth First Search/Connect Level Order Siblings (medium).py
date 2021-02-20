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
        dq = collections.deque([root])
        while dq:
            prev=None
            for _ in range(len(dq)):
                node = dq.popleft()
                if prev:
                    prev.next = node
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                prev = node
                
        return root