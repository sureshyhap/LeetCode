class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters_seen = set()
        for char in s:
            if char in letters_seen:
                return char
            letters_seen.add(char)
