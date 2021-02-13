from heapq import *

import heapq


class Node(object):
    def __init__(self, key: str, val: int):
        self.val = val
        self.key = key

    def __repr__(self):
        return f'{self.key} {self.val}'

    def __lt__(self, other):
        return self.val > other.val if self.val != other.val else self.key < other.key


class MinStack:

    def __init__(self):
        self.hash = {}
        self.min_stack = []

    def Assign(self, s, a):
        if s in self.hash:
            self.Delete(s)
        node = Node(s, a)
        heappush(self.min_stack, node)
        self.hash[s] = node

    def Delete(self, s):
        if s in self.hash:
            node = self.hash[s]
            node.val = 0
            heapify(self.min_stack)
            del self.hash[s]

    def MaxScore(self) -> int:
        print(self.min_stack[0])

    def GetScore(self, s) -> int:
        if s in self.hash:
            print(self.hash[s].val)
        else:
            print(0)


a = MinStack()
a.Assign('abc', 10)
a.Assign('pqr', 5)
a.MaxScore()
a.Assign('aaa', 10)
a.GetScore('pqr')
a.MaxScore()
a.Assign('aaa', 5)
a.MaxScore()
a.Delete('abc')
a.MaxScore()
a.GetScore('abc')
a.GetScore('aaa')
