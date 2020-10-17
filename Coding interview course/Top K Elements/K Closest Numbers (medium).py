from heapq import *

from collections import deque


def find_closest_elements(arr, K, X):
    result = []
    q = []
    closest_index = binary_search(arr, X)
    left_ptr, right_ptr = max(
        closest_index, 0), min(len(arr)-1, closest_index+1)
    while len(result) < K and left_ptr >= 0 and right_ptr <= len(arr)-1:
        if abs(arr[left_ptr]-X) >= abs(arr[left_ptr]-X):
            result.insert(0, arr[left_ptr])
            left_ptr -= 1
        else:
            result.append(arr[right_ptr])
            right_ptr += 1
    if right_ptr == len(arr):
        while len(result) < K:
            result.insert(0, arr[left_ptr])
            left_ptr -= 1
    elif left_ptr == -1:
        while len(result) < K:
            result.append(arr[right_ptr])
            right_ptr += 1
    return result


def binary_search(arr, key):
    l, h = 0, len(arr)-1
    while l < h:
        mid = (l+h)//2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            l = mid+1
        else:
            h = mid-1
    return l


def main():
    print("'3' closest numbers to '7' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'3' closest numbers to '6' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'3' closest numbers to '10' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()


def find_closest_elementsnsbdfm(arr, K, X):
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
