# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.


def dutch_flag_sort(arr):
    left = 0
    right = len(arr)-1
    i = 0
    while i <= right:
        if arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
            i += 1
        elif arr[i] == 2:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else:
            i += 1
    return arr


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)


main()
