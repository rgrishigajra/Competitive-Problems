"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        seen = {}
        queue = [node]
        while queue:
            root = queue.pop()
            if root not in seen:
                seen[root]=Node(root.val,[])
            for n in root.neighbors:
                if n not in seen:
                    seen[n]=Node(n.val,[])
                    queue.append(n)
                seen[root].neighbors.append(seen[n])
        return seen[node]
            
            