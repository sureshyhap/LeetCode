class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        n = len(s)
        vowel_count = 0

        for i in range(k):
           if s[i] in vowels:
                vowel_count += 1
        max_vowel_count = vowel_count

        for i in range(k - 1, n - 1):
            if s[i + 1] in vowels:
                vowel_count += 1
            left_is_vowel = s[i - k + 1] in vowels
            if left_is_vowel:
                vowel_count -= 1
            max_vowel_count = max(max_vowel_count, vowel_count)

        return max_vowel_count

