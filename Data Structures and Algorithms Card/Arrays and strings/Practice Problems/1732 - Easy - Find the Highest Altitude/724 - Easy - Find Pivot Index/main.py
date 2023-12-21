class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = 0
        right_sum = sum(nums[1:])
        for i in range(n - 1):
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
            right_sum -= nums[i + 1]
        if left_sum == right_sum:
            return n - 1
        return -1
