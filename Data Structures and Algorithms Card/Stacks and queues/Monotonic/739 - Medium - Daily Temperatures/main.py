class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decreasing_stack = []
        result = [None] * len(temperatures)
        i = 0
        while i < len(temperatures):
            if decreasing_stack:
                while temperatures[i] <= decreasing_stack[-1][0]:
                    decreasing_stack.append((temperatures[i], i))
                    i += 1
                    if i >= len(temperatures):
                        while decreasing_stack:
                            result[decreasing_stack[-1][1]] = 0
                            decreasing_stack.pop()
                        return result
                while decreasing_stack and temperatures[i] > decreasing_stack[-1][0]:
                    j = decreasing_stack[-1][1]
                    result[j] = i - j
                    decreasing_stack.pop()
                decreasing_stack.append((temperatures[i], i))
            else:
                decreasing_stack.append((temperatures[i], i))
            i += 1
        while decreasing_stack:
            result[decreasing_stack[-1][1]] = 0
            decreasing_stack.pop()
        return result
