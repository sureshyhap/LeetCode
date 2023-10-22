class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        smallest_prefix_sum = prefix_sum[0]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            smallest_prefix_sum = min(smallest_prefix_sum, prefix_sum[i])

        start_value = 1 - smallest_prefix_sum
        start_value = max(start_value, 1)

        return start_value
        
