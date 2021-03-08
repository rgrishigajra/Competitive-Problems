class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC",
                    "L", "XL", "X", "IX", "V", "IV", "I"]
        res, i = "", 0
        while num:
            if num >= values[i]:
                res += numerals[i]*(num//values[i])
                num = num % values[i]
            i += 1
        return res
