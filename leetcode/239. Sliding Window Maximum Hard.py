class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        max_arr = []
        for idx, num in enumerate(nums):
            while d and nums[d[-1]] < num:
                d.pop()
            d.append(idx)
            if d[0] == idx-k:
                d.popleft()
            if idx >= k-1:
                max_arr.append(nums[d[0]])
        return max_arr
