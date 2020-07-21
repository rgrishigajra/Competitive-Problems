# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
def search_triplets(arr):
    triplets = []
    arr.sort()
    for i in range(len(arr)):
        if arr[i] != arr[i-1]:
            search_pair(arr, i, triplets)
    return triplets


def search_pair(arr, target_ptr, triplets):
    target_sum = -arr[target_ptr]
    start_ptr = target_ptr+1
    end_ptr = len(arr)-1
    while start_ptr < end_ptr:
        if arr[start_ptr]+arr[end_ptr] == target_sum:
            triplets.append([arr[target_ptr], arr[start_ptr], arr[end_ptr]])
            start_ptr += 1
            end_ptr -= 1
        if arr[start_ptr]+arr[end_ptr] < target_sum:
            while True:
                start_ptr += 1
                if arr[start_ptr] != arr[start_ptr-1]:
                    break
        if arr[start_ptr]+arr[end_ptr] > target_sum:
            while True:
                end_ptr -= 1
                if arr[end_ptr] != arr[end_ptr-1]:
                    break


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()
