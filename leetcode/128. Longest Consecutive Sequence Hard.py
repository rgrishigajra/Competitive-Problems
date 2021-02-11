class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        freq = collections.defaultdict(int)
        for i in nums:
            freq[i] = 1
        curr_len = 0
        for idx, num in enumerate(nums):
            if freq[num] == 1:
                left, right = num, num
                while freq[left-1] == 1:
                    left -= 1
                    freq[left] = 0
                while freq[right+1] == 1:
                    right += 1
                    freq[right] = 0
                curr_len = right - left + 1
                if max_len < curr_len:
                    max_len = curr_len
        return max_len
