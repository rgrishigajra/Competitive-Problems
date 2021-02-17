from __future__ import print_function
from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

    def __repr__(self):
        return f'{self.start}-{self.end}'

    def __lt__(self, other):
        return self.start < other.start


def find_employee_free_time(schedule):
    result = []
    # TODO: Write your code here
    heap = []
    for idx, p in enumerate(schedule):
        # pushing first interval for every list, list number(index) and current index(inside list)
        heappush(heap, (p[0], idx, 0))
    previousInterval = heap[0][0]
    while heap:
        currentInterval, list_idx, idx = heappop(heap)
        if previousInterval.end < currentInterval.start:
            result.append(
                Interval(previousInterval.end, currentInterval.start))
            previousInterval = currentInterval
        else:
            if previousInterval.end < currentInterval.end:
                previousInterval = currentInterval
        if len(schedule[list_idx])-1 > idx:
            heappush(heap, (schedule[list_idx][idx+1], list_idx, idx+1))
    return result


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
