def find_permutations(nums):
    if len(nums) == 0:
        return 0
    ans = []
    perms = []
    perms.append([])
    for i in range(0, len(nums)):
        print(perms)
        permlen=len(perms)
        for variations in range(permlen):
            oldperms = perms.pop()
            for k in range(len(oldperms)+1):
                newperms=list(oldperms)
                newperms.insert(k,nums[i])
                print(newperms)
                if len(newperms) == len(nums):
                    ans.append(newperms)
                else:
                    perms.append(newperms)
    return ans


def main():
    print("Here are all the permutations: " +
          str(find_permutations([1, 2, 3])))


main()
