class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freqs1 = {}
        for c in word1:
            if c in freqs1:
                freqs1[c] += 1
            else:
                freqs1[c] = 1
        freqs2 = {}
        for c in word2:
            if c in freqs2:
                freqs2[c] += 1
            else:
                freqs2[c] = 1
        return (sorted(freqs1.values()) == sorted(freqs2.values())) and \
        (sorted(freqs1.keys()) == sorted(freqs2.keys()))
