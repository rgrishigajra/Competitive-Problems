from collections import deque


def print_orders(tasks, prerequisites):
  sortedOrder = []
  if tasks <= 0:
    return False

  # a. Initialize the graph
  inDegree = {i: 0 for i in range(tasks)}  # count of incoming edges
  graph = {i: [] for i in range(tasks)}  # adjacency list graph

  # b. Build the graph
  for prerequisite in prerequisites:
    parent, child = prerequisite[0], prerequisite[1]
    graph[parent].append(child)  # put the child into it's parent's list
    inDegree[child] += 1  # increment child's inDegree

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  print_all_topological_sorts(graph, inDegree, sources, sortedOrder)


def print_all_topological_sorts(graph, inDegree, sources, sortedOrder):
  if sources:
    for vertex in sources:
      sortedOrder.append(vertex)
      sourcesForNextCall = deque(sources)  # make a copy of sources
      # only remove the current source, all other sources should remain in the queue for the next call
      sourcesForNextCall.remove(vertex)
      # get the node's children to decrement their in-degrees
      for child in graph[vertex]:
        inDegree[child] -= 1
        if inDegree[child] == 0:
          sourcesForNextCall.append(child)

      # recursive call to print other orderings from the remaining (and new) sources
      print_all_topological_sorts(
        graph, inDegree, sourcesForNextCall, sortedOrder)

      # backtrack, remove the vertex from the sorted order and put all of its children back to consider
      # the next source instead of the current vertex
      sortedOrder.remove(vertex)
      for child in graph[vertex]:
        inDegree[child] += 1

  # if sortedOrder doesn't contain all tasks, either we've a cyclic dependency between tasks, or
  # we have not processed all the tasks in this recursive call
  if len(sortedOrder) == len(inDegree):
    print(sortedOrder)


def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
