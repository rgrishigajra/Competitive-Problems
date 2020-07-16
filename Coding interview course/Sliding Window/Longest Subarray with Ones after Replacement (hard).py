#Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
def length_of_longest_substring(arr, k):
  num_of_zeroes=0
  window_start=0
  max_len=0
  for window_end in range(len(arr)):
    print(window_start,window_end,max_len)
    if arr[window_end] == 0:
      num_of_zeroes +=1
      if num_of_zeroes > k :
        while arr[window_start] != 0:
          window_start+=1
        window_start+=1
        num_of_zeroes-=1
    max_len=max(max_len,window_end-window_start+1)
  return max_len

def main():
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))