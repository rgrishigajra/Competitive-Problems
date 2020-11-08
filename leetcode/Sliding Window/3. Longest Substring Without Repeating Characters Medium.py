class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0 
        start_ptr = 0
        characters = {}
        for end_ptr in range(len(s)):
            if s[end_ptr] in characters:
                    start_ptr = max(start_ptr,characters[s[end_ptr]]+1)
            characters[s[end_ptr]] = end_ptr
            max_len = max(max_len, end_ptr - start_ptr+1)
        return max_len
                