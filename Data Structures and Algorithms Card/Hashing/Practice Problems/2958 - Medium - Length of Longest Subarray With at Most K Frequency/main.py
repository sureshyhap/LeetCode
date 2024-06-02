class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = {}
        max_length = 1
        left = 0
        for right, num in enumerate(nums):
            if num in counts:
                counts[num] += 1
                while counts[num] > k:
                    counts[nums[left]] -= 1
                    left += 1
            else:
                counts[num] = 1
            max_length = max(max_length, right - left + 1)
        return max_length
