class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        remainingCost = maxCost
        left = 0
        max_length = 0

        for right in range(n):
            diff = ord(t[right]) - ord(s[right])
            remainingCost -= abs(diff)
            while remainingCost < 0:
                remainingCost += abs(ord(t[left]) - ord(s[left]))
                left += 1
            max_length = max(max_length, right - left + 1)
        
        return max_length
