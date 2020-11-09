class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        repeated = set()
        for char in range(len(s)):
            if s[char] in dic:
                del dic[s[char]]
                repeated.add(s[char])
            elif s[char] not in repeated:
                dic[s[char]] = char
        if dic:
            return min(dic.values())
        else:
            return -1
