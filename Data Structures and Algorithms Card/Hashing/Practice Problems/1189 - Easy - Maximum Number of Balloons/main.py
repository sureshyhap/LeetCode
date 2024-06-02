class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = {
            "b" : 0,
            "a" : 0,
            "l" : 0,
            "o" : 0,
            "n" : 0
        }
        n = len(text)
        keyword = "balon"
        for letter in text:
            if letter in keyword:
                counts[letter] += 1
        instances = 0
        while counts["b"] >= 1 and counts["a"] >= 1 and \
            counts["l"] >= 2 and counts["o"] >= 2 and counts["n"] >= 1:
            counts["b"] -= 1
            counts["a"] -= 1
            counts["l"] -= 2
            counts["o"] -= 2
            counts["n"] -= 1
            instances += 1
        return instances
