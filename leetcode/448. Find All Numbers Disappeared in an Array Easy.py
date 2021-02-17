class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missingNumbers = []
        # TODO: Write your code here
        idx = 0
        while idx < len(nums):
            j = nums[idx]-1
            if nums[j] != nums[idx]:
                nums[idx], nums[j] = nums[j], nums[idx]
            else:
                idx += 1
        for idx, num in enumerate(nums):
            if num-1 != idx:
                missingNumbers.append(idx+1)
        return missingNumbers
