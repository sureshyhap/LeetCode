class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(i):
            nonlocal memo
            if len(cost) == 3:
                return min(cost[1], cost[0] + cost[2])
            elif i <= 1:
                return cost[i]
            elif i not in memo:
                memo[i] = min(dp(i - 1), dp(i - 2)) + (0 if i == len(cost) else cost[i])
            return memo[i]
        return dp(len(cost))