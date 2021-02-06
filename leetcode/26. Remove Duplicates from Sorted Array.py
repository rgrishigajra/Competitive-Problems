class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        ptr = 1
        while ptr < len(nums):
            if nums[ptr] != nums[ptr-1]:
                nums[idx] = nums[ptr]
                idx += 1
            ptr += 1
        return idx
