class Solution:
    def isHappy(self, n: int) -> bool:
        dic = set()
        su = n
        while su != 1 and su not in dic:
            s = str(su)
            dic.add(su)
            su = 0
            for digit in s:
                su += int(digit)*int(digit)
        if su == 1:
            return True
        return False
