from heapq import *

from collections import deque


def find_closest_elements(arr, K, X):
    result = deque()
    index = binary_search(arr, X)
    leftPointer, rightPointer = index, index + 1
    n = len(arr)
    for i in range(K):
        if leftPointer >= 0 and rightPointer < n:
            diff1 = abs(X - arr[leftPointer])
            diff2 = abs(X - arr[rightPointer])
            if diff1 <= diff2:
                result.appendleft(arr[leftPointer])
                leftPointer -= 1
            else:
                result.append(arr[rightPointer])
                rightPointer += 1
        elif leftPointer >= 0:
            result.appendleft(arr[leftPointer])
            leftPointer -= 1
        elif rightPointer < n:
            result.append(arr[rightPointer])
            rightPointer += 1

    return result


def find_closest_elements(arr, K, X):
    result = []
    max_heap = []
    close_index = binary_search(arr, X)
    l, h = max(0, close_index-K), min(close_index+K+1, len(arr)-1)
    print(close_index, l, h)
    for itr in range(l, h):
        heappush(max_heap, (-abs(X - arr[itr]), arr[itr]))
    while len(result) < K:
        result.append(heappop(max_heap)[1])
    result.sort()
    return result


def binary_search(arr, key):
    l, h = 0, len(arr)-1
    while l <= h:
        mid = (l+h)//2
        if arr[mid] == key:
            return mid
        if arr[mid] <= key:
            l = mid + 1
        else:
            h = mid-1
    return l



def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
