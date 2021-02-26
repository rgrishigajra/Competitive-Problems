class UnionFind:

    # For efficiency, we aren't using makeset, but instead initialising
    # all the sets at the same time in the constructor.
    def __init__(self, n):
        self.parent = [node for node in range(n)]

    # The find method, without any optimizations. It traces up the parent
    # links until it finds the root node for A, and returns that root.
    def find(self, A):
        while A != self.parent[A]:
            A = self.parent[A]
        return A

    # The union method, without any optimizations. It returns True if a
    # merge happened, False if otherwise.
    def union(self, A, B):
        # Find the roots for A and B.
        root_A = self.find(A)
        root_B = self.find(B)
        # Check if A and B are already in the same set.
        if root_A == root_B:
            return False
        # Merge the sets containing A and B.
        self.parent[root_A] = root_B
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Condition 1: The graph must contain n - 1 edges.
        if len(edges) != n - 1:
            return False

        # Condition 2: The graph must contain a single connected component.
        # Create a new UnionFind object with n nodes.
        unionFind = UnionFind(n)
        # Add each edge. Check if a merge happened, because if it
        # didn't, there must be a cycle.
        for A, B in edges:
            if not unionFind.union(A, B):
                return False
        # If we got this far, there's no cycles!
        return True
