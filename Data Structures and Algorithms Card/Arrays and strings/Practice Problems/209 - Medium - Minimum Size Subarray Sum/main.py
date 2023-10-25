class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        min_length = n + 1
        curr_sum = 0
        ran_while_loop = False

        for right in range(n):
            curr_sum += nums[right]
            while curr_sum >= target:
                ran_while_loop = True
                curr_sum -= nums[left]
                left += 1
            if ran_while_loop:
                left -= 1
                curr_sum += nums[left]
                ran_while_loop = False
            if curr_sum >= target:
                min_length = min(min_length, right - left + 1)

        return 0 if (min_length == n + 1) else min_length
