# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array has some duplicates, find all the duplicate numbers without using any extra space.


def find_all_duplicates(nums):
    duplicateNumbers = []
    itr = 0
    while itr < len(nums):
        if nums[itr] != itr+1:
            if nums[itr] == nums[nums[itr]-1]:
                duplicateNumbers.append(nums[itr])
                itr += 1
            else:
                nums[nums[itr]-1], nums[itr] = nums[itr], nums[nums[itr]-1]
        else:
            itr += 1
    return duplicateNumbers


def main():
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()
