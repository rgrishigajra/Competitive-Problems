import math


class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    l, h = 0, 1
    while reader.get(h) < key:
        new_l = h+1
        h += (h-l+1)*2
        l = new_l
    return binary_search(reader, key, l, h)


def binary_search(reader, key, l, h):
    while l <= h:
        mid = (l+h)//2
        mid_val = reader.get(mid)
        if mid_val == key:
            return mid
        if key < mid_val:
            h = mid-1
        else:
            l = mid+1
    return -1


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))


main()
