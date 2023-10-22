class Solution:
    def reverseWords(self, s: str) -> str:
        lyst = [list(word) for word in s.split()]
        for i, word in enumerate(lyst):
            word.reverse()
            lyst[i] = "".join(word)
        return " ".join(lyst)
