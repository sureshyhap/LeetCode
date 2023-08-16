class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(i):
            nonlocal memo
            if i <= 2:
                return i
            if i not in memo:
                memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        return dp(n)