# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.


def find_missing_numbers(nums):
    missingNumbers = []
    itr = 1
    while itr < len(nums):
        if nums[itr] != itr + 1 and nums[nums[itr] - 1] != nums[itr]:
            nums[nums[itr] - 1], nums[itr] = nums[itr], nums[nums[itr] - 1]
        else:
            itr += 1
    for itr, num in enumerate(nums):
        if num != itr + 1:
            missingNumbers.append(itr+1)
    return missingNumbers


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))


main()
