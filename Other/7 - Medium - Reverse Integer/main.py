class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = -x
        result = 0
        while x > 0:
            result = (result * 10) + (x % 10)
            x //= 10
        if neg:
            result = -result
        min = -(2 ** 31)
        max = (2 ** 31) - 1
        if min <= result <= max: 
            return result
        else:
            return 0
