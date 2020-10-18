from collections import defaultdict
from heapq import *


def schedule_tasks(tasks, k):
    intervalCount = 0
    max_heap = []
    freq_map = defaultdict(int)
    for task in tasks:
        freq_map[task] += 1
    for key in freq_map.keys():
        heappush(max_heap, [-freq_map[key], key])
    while max_heap:
        q = []
        n = k + 1  # try to execute as many as 'k+1' tasks from the max-heap
        while n > 0 and max_heap:
            intervalCount += 1
            [task_freq, task] = heappop(max_heap)
            if task_freq < -1:
                q.append([task_freq+1, task])
            n -= 1
        for task in q:
            heappush(max_heap, task)
        if max_heap:
            intervalCount += n
    return intervalCount


def main():
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'b', 'a'], 3)))


main()
