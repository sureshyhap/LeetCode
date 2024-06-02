class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = {}
        max_freq = 0
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        max_freq = max(freqs.values())
        num_at_max = 0
        for num, freq in freqs.items():
            if freq == max_freq:
                num_at_max += 1
        return num_at_max * max_freq
