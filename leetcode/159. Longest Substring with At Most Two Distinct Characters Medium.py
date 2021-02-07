class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if s == '':
            return 0
        freq = collections.defaultdict(int)
        start = 0
        max_len = 0
        for end, char in enumerate(s):
            if char not in freq:
                while len(freq) >= 2:
                    freq[s[start]] -= 1
                    if freq[s[start]] == 0:
                        del freq[s[start]]
                    start += 1
            freq[char] += 1
            if max_len < end-start + 1:
                max_len = end-start+1
        return max_len
