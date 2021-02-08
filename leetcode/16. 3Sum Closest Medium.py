class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = math.inf
        res_sum = 0
        for idx, num1 in enumerate(nums):
            if idx == 0 or num1 != nums[idx-1]:
                left = idx+1
                right = len(nums)-1
                while left < right:
                    curr = nums[left]+nums[right] + num1
                    if res > abs(target-curr):
                        res = abs(target-curr)
                        res_sum = curr
                    if curr > target:
                        right -= 1
                    elif curr < target:
                        left += 1
                    else:
                        res = 0
                        res_sum = curr
                        left += 1
                        right -= 1
        return res_sum
