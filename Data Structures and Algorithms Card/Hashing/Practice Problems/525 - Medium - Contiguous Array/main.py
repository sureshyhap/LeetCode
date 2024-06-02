class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
 
        n = len(nums)
        surplus_ones = 0
        keep_track_of_indices = {0: -1}
        longest = 0
        for right in range(n):
            surplus_ones += (1 if nums[right] else -1)
            if surplus_ones in keep_track_of_indices:
                length = right - keep_track_of_indices[surplus_ones]
                longest = max(longest, length)
            else:
                keep_track_of_indices[surplus_ones] = right
        return longest
