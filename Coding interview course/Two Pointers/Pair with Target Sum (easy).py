# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.


def pair_with_targetsum(arr, target_sum):
    start_ptr = 0
    end_ptr = len(arr) - 1
#   if the array isnt sorted, we need to sort the thing
    while True:
        if arr[start_ptr] + arr[end_ptr] == target_sum:
            return [start_ptr, end_ptr]
        if arr[start_ptr] + arr[end_ptr] > target_sum:
            end_ptr -= 1
        if arr[start_ptr] + arr[end_ptr] < target_sum:
            start_ptr += 1


def pair_with_targetsum_hash(arr, target_sum):
    dic = {}
    for num in range(len(arr)):
        if arr[num] not in dic:
            dic[(target_sum-arr[num])] = num
        else:
            return [dic[arr[num]], num]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))
