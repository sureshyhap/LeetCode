class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            nonlocal memo
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i == 2:
                return max(nums[0] + nums[2], nums[1])
            if i not in memo:
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i], dp(i - 3) + nums[i])
            return memo[i]
        return dp(len(nums) - 1)