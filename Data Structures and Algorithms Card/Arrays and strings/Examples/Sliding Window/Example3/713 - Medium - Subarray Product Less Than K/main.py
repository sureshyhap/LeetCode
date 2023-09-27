class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        n = len(nums)
        left = right = 0
        product = 1
        num_subarrays = 0
        
        while right < n:
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            num_subarrays += (right - left + 1)
            right += 1
        
        return num_subarrays
