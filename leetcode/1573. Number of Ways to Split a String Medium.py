class Solution:
    def numWays(self, s: str) -> int:
        count = Counter()
        num = 1
        for i, char in enumerate(s):
            if char == '1':
                count[num] = i
                num += 1
        n = len(s)
        if len(count) == 0:
            return ((n-1)*(n-2)//2) % (10**9 + 7)
        target = (num-1)/3
        if (num-1) % 3 != 0:
            return 0
        return ((count[target+1]-count[target])*(count[target*2+1] - count[target*2])) % (10**9+7)
