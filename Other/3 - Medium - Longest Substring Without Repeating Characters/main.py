class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        seen_set = set()
        n = len(s)
        length = 0
        for i in range(n):
            length += 1
            if s[i] not in seen_set:
                seen_set.add(s[i])
            else:
                seen_set.clear()
                j = i
                while True:
                    seen_set.add(s[j])
                    if s[j - 1] != s[i]:
                        j -= 1
                    else:
                        break
                length = i - j + 1
            max_length = max(length, max_length)
        return max_length
