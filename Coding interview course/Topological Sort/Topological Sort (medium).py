from collections import defaultdict, deque


def topological_sort(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    queue = deque()
    for source, child in edges:
        in_degree[child] += 1
        graph[source].append(child)
    for vertex in range(vertices):
        if in_degree[vertex] == 0:
            queue.append(vertex)
    while queue:
        parent = queue.popleft()
        for child in graph[parent]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)
        sortedOrder.append(parent)
    if len(sortedOrder) != vertices:
        return []
    return sortedOrder


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
