class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_left, max_right = 0, 0
        max_left_idx, max_right_idx = -1, -1
        max_water = 0
        while left < right:
            if max_left < height[left]:
                max_left = height[left]
                max_left_idx = left
            if max_right < height[right]:
                max_right = height[right]
                max_right_idx = right
            if max_left > max_right:
                current_water = height[right]*abs(right-max_left_idx)
                right -= 1
            else:
                current_water = abs(max_right_idx-left)*height[left]
                left += 1
            if max_water < current_water:
                max_water = current_water
        return max_water
