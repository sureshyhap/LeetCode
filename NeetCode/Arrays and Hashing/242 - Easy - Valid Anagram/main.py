class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#        return sorted(s) == sorted(t)
        freqs1 = {}
        freqs2 = {}
        for char in s:
            if char in freqs1:
                freqs1[char] += 1
            else:
                freqs1[char] = 0
        for char in t:
            if char in freqs2:
                freqs2[char] += 1
            else:
                freqs2[char] = 0
        return (freqs1 == freqs2)
