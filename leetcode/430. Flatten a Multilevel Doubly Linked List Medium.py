"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        currentNode = head
        stack = [currentNode]
        prev=Node(0)
        while stack:    
            currentNode = stack.pop()
            currentNode.prev = prev
            if currentNode.next:
                stack.append(currentNode.next)
            if currentNode.child:
                stack.append(currentNode.child)
            currentNode.child=None
            prev.next = currentNode
            prev = currentNode
            currentNode = currentNode.next
        head.prev = None
        return head
            