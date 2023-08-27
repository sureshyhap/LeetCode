class Solution:
    def tribonacci(self, n: int) -> int:
        array = [0] * 38
        array[0] = 0
        array[1] = 1
        array[2] = 1
        for i in range(3, n + 1):
            array[i] = array[i - 1] + array[i - 2] + array[i - 3]
        return array[n]
