class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        result = [0] * n
        i = n - 1
        
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result[i] = nums[right] ** 2
                right -= 1
            else:
                result[i] = nums[left] ** 2
                left += 1
            i -= 1
        
        return result
