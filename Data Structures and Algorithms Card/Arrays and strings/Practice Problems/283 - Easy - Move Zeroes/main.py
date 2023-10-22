class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        n = len(nums)
        i = n - 1
        j = i

        while j >= 0:
            if nums[j] == 0:
                while i + 1 < n and nums[i + 1] != 0:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    i += 1
            j -= 1
            i = j
        """
        zero_count = 0
        n = len(nums)
        i = 0
        while i < n:
            while i < n and nums[i] == 0:
                zero_count += 1
                del nums[i]
                n -= 1
            i += 1
        zeros = [0] * zero_count
        nums.extend(zeros)
