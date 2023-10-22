class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        left = 0
        right = n - 1
        string = list(s)
        a = ord('a')
        z = ord('z')
        A = ord('A')
        Z = ord('Z')

        while left < right:
            left_ascii = ord(string[left])
            right_ascii = ord(string[right])
            while not ((a <= left_ascii <= z) or (A <= left_ascii <= Z)):
                left += 1
                if left >= right:
                    break
                left_ascii = ord(string[left])
            while not ((a <= right_ascii <= z) or (A <= right_ascii <= Z)):
                right -= 1
                if left >= right:
                    break
                right_ascii = ord(string[right])
            if left >= right:
                break
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1
        
        return "".join(string)
