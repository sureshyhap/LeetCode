class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        for j in range(1, len(s)):
            if stack and s[j].lower() == stack[-1].lower() and s[j] != stack[-1]:
                stack.pop()
            else:
                stack.append(s[j])
        return "".join(stack)
