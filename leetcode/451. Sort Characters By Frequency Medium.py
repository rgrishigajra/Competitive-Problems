class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s
        freq = collections.defaultdict(int)
        for char in s:
            freq[char] += 1
        li = []
        for char in freq.keys():
            li.append((freq[char], char))
        li.sort(key=lambda x: -x[0])
        return "".join([char*freq for freq, char in li])
