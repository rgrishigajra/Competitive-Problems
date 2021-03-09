class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = 0
        dic = collections.defaultdict(int)
        for char in s:
            if dic[char] == 1:
                count -= 1
                dic[char] = 0
            else:
                dic[char] = 1
                count += 1
        if count == 1 and len(s) % 2 == 1:
            return True
        return True if count == 0 else False
