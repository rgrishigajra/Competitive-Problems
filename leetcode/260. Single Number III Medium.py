class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        num1, num2 = 0, 0
        x = 0
        for num in nums:
            x = x ^ num
        rightmost = 1
        while rightmost & x == 0:
            rightmost = rightmost << 1
        for num in nums:
            if num & rightmost != 0:
                num1 = num1 ^ num
            else:
                num2 = num2 ^ num
        return [num1, num2]
