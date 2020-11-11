class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = collections.defaultdict(int)
        for char in s:
            s_freq[char] += 1
        for char in t:
            s_freq[char] -= 1
        total = 0
        for key in s_freq.keys():
            total += abs(s_freq[key])
        return total // 2
