class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        n = len(s)
        counts = {}
        for i in range(n):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1
        amount_to_match = counts[s[0]]
        for count in counts.values():
            if count != amount_to_match:
                return False
        return True
