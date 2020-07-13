# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
def smallest_subarray_with_given_sum(s, arr):
    result_len = len(arr)+1
    window_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            result_len = min(window_end - window_start, result_len)
            window_sum -= arr[window_start]
            window_start += 1
    if result_len == len(arr)+1:
        return 0
    return result_len + 1


def main():
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
