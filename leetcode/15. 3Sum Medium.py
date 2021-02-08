class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        d = {}
        nums.sort()
        for i in range(0, len(nums)-2):
            if nums[i] > 0:
                break
            if nums[i] == nums[i-1] and i > 0:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[l]+nums[r]+nums[i]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([nums[l], nums[r], nums[i]])
                    while (l < r) and nums[l] == nums[l+1]:
                        l += 1
                    while (l < r) and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans
class Solution:
    def threeSum_hash_no_sort(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res