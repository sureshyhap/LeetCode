class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)
        i = j = 0

        while j < n and word[j] != ch:
            j += 1
        
        if j == n:
            return word

        chars = list(word)
        
        while i < j:
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1

        return "".join(chars)
