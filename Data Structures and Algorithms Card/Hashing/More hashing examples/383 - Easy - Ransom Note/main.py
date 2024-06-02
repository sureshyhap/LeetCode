class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_counts = {chr(ord("a") + i) : 0 for i in range(26)}
        ransom_counts = {chr(ord("a") + i) : 0 for i in range(26)}
        for char in magazine:
            mag_counts[char] += 1
        for char in ransomNote:
            ransom_counts[char] += 1
        for letter in mag_counts:
            if ransom_counts[letter] > mag_counts[letter]:
                return False
        return True
