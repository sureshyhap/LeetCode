class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = {chr(ord("a") + i) for i in range(26)}
        for c in sentence:
            letters.discard(c)
        return len(letters) == 0
