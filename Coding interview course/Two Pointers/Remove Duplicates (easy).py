# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.
def remove_duplicates(arr):
    arr_ptr = 1
    forward_ptr = 1
    while True:
        print(arr, arr_ptr, forward_ptr)
        if arr[forward_ptr] != arr[arr_ptr]:
            arr[arr_ptr], arr[forward_ptr] = arr[forward_ptr], arr[arr_ptr]
            arr_ptr += 1
        forward_ptr += 1
        if forward_ptr == len(arr):
            break
    return arr_ptr


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
