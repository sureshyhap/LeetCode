class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_modified = ""
        for c in s:
            if c.isalnum():
                s_modified += c.lower()
        s_modified2 = list(s_modified)
        s_modified2.reverse()
        return s_modified2 == list(s_modified)
        """
        s_modified = ""
        for c in s:
            if c.isalnum():
                s_modified += c.lower()
        for i in range(len(s_modified)):
            if s_modified[i] != s_modified[-(i + 1)]:
                return False
        return True
        """
