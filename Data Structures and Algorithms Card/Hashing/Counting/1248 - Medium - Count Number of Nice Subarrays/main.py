class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        curr = result = 0
        odd_counts = {0 : 1}
        for i in range(n):
            if nums[i] % 2 != 0:
                curr += 1
                if (curr >= k) and (curr - k in odd_counts):
                    result += odd_counts[curr - k]
                if curr in odd_counts:
                    odd_counts[curr] += 1
                else:
                    odd_counts[curr] = 1
            else:
                if (curr >= k) and (curr - k in odd_counts):
                    result += odd_counts[curr - k]
                odd_counts[curr] += 1
        return result
