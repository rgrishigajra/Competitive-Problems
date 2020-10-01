
def count_rotations(arr):
    l, h = 0, len(arr)-1
    while l < h:
        mid = (l+h)//2
        if mid < h and arr[mid] > arr[mid+1]:  #mid is highest
            return mid +1                       
        # mid and mid +1 follow asc so check end points
        if arr[mid] > arr [l]:  # l to mid is ascending
            l = mid +1
        else:
            h = mid 
    return 0


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


main()
