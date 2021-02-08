class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        ans = collections.deque()
        left, right = 0, len(nums)-1
        left_sq = nums[left]*nums[left]
        right_sq = nums[right]*nums[right]
        while left <= right:
            if left_sq > right_sq:
                ans.appendleft(left_sq)
                left += 1
                left_sq = nums[left]*nums[left]
            else:
                ans.appendleft(right_sq)
                right -= 1
                right_sq = nums[right]*nums[right]
        return ans
