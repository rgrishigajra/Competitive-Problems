class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        d = [0 for _ in range(n+1)]
        d[0] = 1
        d[1] = 0 if s[0] == "0" else 1
        for itr in range(2, n+1):
            count = 0
            if int(s[itr-1]) > 0:
                count += d[itr-1]
            if int(s[itr-2:itr]) < 27 and int(s[itr-2:itr]) > 9:
                count += d[itr-2]
            d[itr] = count
        return d[n]
