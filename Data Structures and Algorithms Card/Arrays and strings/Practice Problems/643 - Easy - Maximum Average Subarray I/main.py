class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        i = 0
        j = k - 1
        present_sum = sum(nums[i:j+1])
        max_sum = present_sum

        while j < n - 1:
            present_sum -= nums[i]
            i += 1
            j += 1
            present_sum += nums[j]
            max_sum = max(max_sum, present_sum)

        return max_sum / k
