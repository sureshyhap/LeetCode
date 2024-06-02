class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqs = {}
        for num in arr:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        return len(set(freqs.values())) == len(freqs)
