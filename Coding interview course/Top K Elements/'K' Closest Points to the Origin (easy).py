from heapq import *
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.dist() > other.dist()

    def dist(self):
        return self.x**2+self.y**2

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
    maxHeap = []
    for itr in range(k):
        heappush(maxHeap, points[itr])
    for i in range(k, len(points)):
        if points[i].dist() < maxHeap[0].dist():
            heappop(maxHeap)
            heappush(maxHeap, points[i])
    return list(maxHeap)


def main():

    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
from heapq import *
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.dist() > other.dist()

    def dist(self):
        return self.x**2+self.y**2 

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
    maxHeap = []
    for itr in range(k):
        heappush(maxHeap, points[itr])
    for i in range(k, len(points)):
      if points[i].dist() < maxHeap[0].dist():
        heappop(maxHeap)
        heappush(maxHeap, points[i])
    return list(maxHeap)


def main():

    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
