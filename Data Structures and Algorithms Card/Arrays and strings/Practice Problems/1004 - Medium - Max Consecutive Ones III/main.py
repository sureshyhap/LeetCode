class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        j = 0
        zero_count = 0
        result = 0

        while j < n:
            if nums[j] == 1:
                j += 1
            else:
                zero_count += 1
                while zero_count > k:
                    if nums[i] == 0:
                        i += 1
                        zero_count -= 1
                    else:
                        i += 1
                j += 1
                
            result = max(result, j - i)

        return result
                
