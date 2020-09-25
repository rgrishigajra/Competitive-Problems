import copy


def find_subsets(nums):
    subsets = [[]]
    for num in range(len(nums)):
        if num == 0:
            holder = copy.deepcopy(subsets)
            n = len(holder)
        elif nums[num] != nums[num-1]:
            holder = copy.deepcopy(subsets)
            n = len(holder)
        for subset in range(n):
            holder[subset].append(nums[num])
        subsets.extend(copy.deepcopy(holder))
    print(subsets)
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
