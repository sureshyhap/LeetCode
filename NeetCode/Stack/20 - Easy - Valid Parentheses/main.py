class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        left = ["{", "(", "["]
        right = ["}", ")", "]"]
        for delimiter in s:
            if delimiter in left:
                stack.append(delimiter)
            elif delimiter in right:
                if not stack:
                    print("Hi")
                    return False
                top = stack.pop()
                if (delimiter == "}" and top != "{") or \
                    delimiter == ")" and top != "(" or \
                    delimiter == "]" and top != "[":
                    return False
        if stack:
            return False
        return True
