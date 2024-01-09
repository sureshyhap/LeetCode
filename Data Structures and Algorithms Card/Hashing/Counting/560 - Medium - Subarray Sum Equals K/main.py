class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sums = [0] * n
        prefix_sums[0] = nums[0]
        for i in range(1, n):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i]
        result = 0
        curr = 0
        counts = {0 : 1}
        for i in range(n):
            curr = prefix_sums[i]
            if curr - k in counts:
                result += counts[curr - k]
            if curr not in counts:
                counts[curr] = 1
            else:
                counts[curr] += 1
        return result
