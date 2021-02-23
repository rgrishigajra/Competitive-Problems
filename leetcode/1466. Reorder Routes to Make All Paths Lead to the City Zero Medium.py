class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        connectedToCap = set()
        connectedToCap.add(0)
        visited = set()
        while len(visited) < n - 1:
            for index, edge in enumerate(connections):
                if index in visited:
                    continue
                if edge[0] in connectedToCap:
                    count += 1
                    connectedToCap.add(edge[1])
                    visited.add(index)
                elif edge[1] in connectedToCap:
                    connectedToCap.add(edge[0])
                    visited.add(index)
        return count
