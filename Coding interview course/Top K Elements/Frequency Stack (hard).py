from heapq import *
from collections import defaultdict


class element:
    def __init__(self, freq, seq, num):
        self.freq = freq
        self.seq = seq
        self.num = num

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.seq > other.seq
        return self.freq > other.freq


class FrequencyStack:
    freq_map = defaultdict(int)
    max_heap = []
    seq_no = 0

    def push(self, num):
        self.freq_map[num] += 1
        inst = element(self.freq_map[num], self.seq_no, num)
        heappush(self.max_heap, inst)
        self.seq_no += 1
        return 0

    def pop(self):
        inst = heappop(self.max_heap)
        fre = max(self.freq_map[inst.num]-1, -1)
        self.freq_map[inst.num] = fre
        if fre == -1:
            return -1
        return inst.num


def main():
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())


main()
