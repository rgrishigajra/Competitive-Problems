# Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less than the target number.
def find_subarrays(arr, target):
  result = []
  product = 1
  left = 0
  for right in range(len(arr)):
    product *= arr[right]
    while (product >= target and left < len(arr)):
      product /= arr[left]
      left += 1  
    test=[]
    for i in range(right,left-1,-1):
      test.append(arr[i])
      result.append(test.copy())
  return result
