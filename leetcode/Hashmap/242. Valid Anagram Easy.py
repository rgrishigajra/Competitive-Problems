class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            s, t = t, s
        dic = collections.defaultdict(int)
        for char in s:
            dic[char] += 1
        for char in t:
            if dic[char] > 0:
                dic[char] -= 1
            else:
                return False
        return True
