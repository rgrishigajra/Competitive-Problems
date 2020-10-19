from heapq import *


def find_Kth_smallest(lists, k):
    number = -1
    min_heap = []

    for list_root in range(len(lists)):
        heappush(min_heap, [lists[list_root][0], 0, list_root])
    heap_numbers, number = 0, 0
    while min_heap:
        [number, index, list_no] = heappop(min_heap)
        heap_numbers += 1
        if heap_numbers == k:
            break
        if index < len(lists[list_no])-1:
            heappush(min_heap, [lists[list_no][index+1], index+1, list_no])
    return number


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
