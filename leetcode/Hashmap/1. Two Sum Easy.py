class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        targets = {}
        for index, value in enumerate(nums):
            if value in targets:
                return [index, targets[value]]
            else:
                targets[target - value] = index
