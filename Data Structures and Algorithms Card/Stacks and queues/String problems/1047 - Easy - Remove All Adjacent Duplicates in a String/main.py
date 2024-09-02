class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and c != stack[-1]:
                stack.append(c)
            elif not stack:
                stack.append(c)
                continue
            else:
                stack.pop()
        return "".join(stack)
