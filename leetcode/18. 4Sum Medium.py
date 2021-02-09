class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        ans = []
        for idx1 in range(len(nums)-3):
            if idx1 > 0 and nums[idx1] == nums[idx1-1]:
                continue
            for idx2 in range(idx1+1, len(nums)-2):
                if idx1+1 < idx2 and nums[idx2] == nums[idx2-1]:
                    continue
                low, high = idx2+1, len(nums)-1
                while low < high:
                    curr = nums[idx1] + nums[idx2] + nums[high] + nums[low]
                    if curr < target:
                        low += 1
                    elif curr > target:
                        high -= 1
                    else:
                        ans.append(
                            [nums[idx1], nums[idx2], nums[low], nums[high]])
                        high -= 1
                        low += 1
                        while low < high and nums[low] == nums[low-1]:
                            low += 1
        return ans
