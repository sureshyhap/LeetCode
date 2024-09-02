class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        mappings = {
            "(" : ")",
            "{": "}",
            "[": "]"
        }
        for char in s:
            if char in mappings:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if mappings[top] != char:
                    return False
        if stack:
            return False
        return True
