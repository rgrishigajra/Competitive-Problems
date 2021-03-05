class Solution:
    def myAtoi(self, s: str) -> int:
        itr = 0
        while itr < len(s) and s[itr] == ' ':
            itr += 1
        isNegative = False
        if itr < len(s) and s[itr] == '-':
            isNegative = True
            itr += 1
        if itr < len(s) and s[itr] == '+':
            if isNegative:
                return 0
            itr += 1
        while itr < len(s) and s[itr] == '0':
            itr += 1
        num = 0
        while itr < len(s) and s[itr].isnumeric():
            num = num*10
            num += int(s[itr])
            itr += 1
        if num > 2**31-1:
            num = 2**31
            return -num if isNegative else (num-1)
        return -num if isNegative else num
