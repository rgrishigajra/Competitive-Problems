class Solution:
    def trap(self, heights: List[int]) -> int:
        water = 0
        if len(heights) < 2:
            return 0
        left, right = 0, len(heights) - 1
        max_right, max_left = 0, 0
        while left < right:
            if max_right < heights[right]:
                max_right = heights[right]
            if max_left < heights[left]:
                max_left = heights[left]
            if max_right > max_left:
                water += max_left - heights[left]
                left += 1
            else:
                water += max_right - heights[right]
                right -= 1
        return water
