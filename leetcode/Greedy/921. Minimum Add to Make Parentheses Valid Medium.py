class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        count = 0
        ans = 0
        for para in S:
            if para == '(':
                count +=1
            else:
                count -=1
            if count < 0:
                ans += 1
                count +=1
        return abs(count) + ans