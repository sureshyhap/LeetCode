class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        unique_nums = set()
        unique_nums.add(nums[left])
        sub_sum = nums[left]
        max_sub_sum = sub_sum
        for right in range(1, len(nums)):
            while nums[right] in unique_nums:
                unique_nums.remove(nums[left])
                sub_sum -= nums[left]
                left += 1
            sub_sum += nums[right]
            unique_nums.add(nums[right])
            max_sub_sum = max(max_sub_sum, sub_sum)
        return max_sub_sum
