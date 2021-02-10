import math as math
def shortest_window_sort(arr):
    low = 0
    print(arr)
    while low < len(arr)-1 and arr[low+1] > arr[low]:
        low += 1
    if low == len(arr)-1:
        return 0
    high = len(arr)-1
    while high > 0 and arr[high] > arr[high-1]:
        high -= 1
    mini = math.inf
    maxi = -math.inf
    for idx in range(low,high+1):
        mini = min(mini,arr[idx])
        maxi = max(maxi,arr[idx])
    while low > 0 and arr[low-1] > mini:
        low-=1
    while high < len(arr) and arr[high+1]<maxi:
        high+=1
    return high - low +1


def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))


main()
