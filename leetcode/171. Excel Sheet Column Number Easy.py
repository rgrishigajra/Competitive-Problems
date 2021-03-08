class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)-1
        total = 0
        for itr in range(0, n+1):
            total *= 26
            total += (ord(columnTitle[itr]) - ord('A') + 1)
        return total
