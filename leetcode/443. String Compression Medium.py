class Solution:
    def compress(self, chars: List[str]) -> int:
        res = 0
        prev = None
        prev_freq = 0
        for itr, char in enumerate(chars):
            if not prev:
                prev = char
                prev_freq += 1
            elif char == prev:
                prev_freq += 1
            else:
                chars[res] = prev
                res += 1
                if prev_freq > 1:
                    for digit in str(prev_freq):
                        chars[res] = digit
                        res += 1
                prev = char
                prev_freq = 1

        chars[res] = prev
        res += 1
        if prev_freq > 1:
            for digit in str(prev_freq):
                chars[res] = digit
                res += 1
        return res
