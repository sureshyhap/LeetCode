class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = {}
        chars = list(s)
        for char in chars:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1
        lyst = freqs.items()
        return "".join([(entry[0] * entry[1]) for entry in sorted(lyst, reverse=True, key=lambda entry: entry[1])])
