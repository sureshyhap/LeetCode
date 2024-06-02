class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_total = -1
        digits = {}
        for i, val in enumerate(nums):
            digit_sum = 0
            while val > 0:
                digit_sum += val % 10
                val //= 10
            if digit_sum in digits:
                max_total = max(max_total, nums[i] + digits[digit_sum])
                digits[digit_sum] = max(digits[digit_sum], nums[i])
            else:
                digits[digit_sum] = nums[i]
        return max_total
