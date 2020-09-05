# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.
def find_missing_number(nums):
    itr = 0
    while itr < len(nums):
        print(nums,itr)
        if nums[itr] == 0:
            itr += 1
            continue
        if nums[itr] != itr+1:
            nums[nums[itr]-1], nums[itr] = nums[itr], nums[nums[itr]-1]
        else:
            itr += 1
    for i in range(len(nums)):
        if nums[i] == 0:
            return i+1

def find_missing_number1(nums):
        return int((len(nums))*(len(nums)+1)/2-sum(nums))
def main():
    print(find_missing_number([4, 3, 1, 0]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 1, 0]))


main()
