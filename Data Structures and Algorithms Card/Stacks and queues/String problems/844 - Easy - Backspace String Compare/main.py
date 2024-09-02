class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(string, pointer):
            while True:
                count = 0
                while string[pointer] == "#":
                    count += 1
                    pointer -= 1
                for i in range(count):
                    if string[pointer] != "#":
                        pointer -= 1
                    else:
                        pointer = backspace(string, pointer) - 1
                    if pointer < 0:
                        return pointer
                if pointer < 0 or string[pointer] != "#":
                    return pointer

        s_pointer = len(s) - 1
        t_pointer = len(t) - 1
        while True:
            if s[s_pointer] != t[t_pointer]:
                if s[s_pointer] == "#":
                    s_pointer = backspace(s, s_pointer)
                    if s_pointer < 0:
                        return False
                elif t[t_pointer] == "#":
                    t_pointer = backspace(t, t_pointer)
                    if t_pointer < 0:
                        return False
                else:
                    return False
            elif s[s_pointer] != "#":
                s_pointer -= 1
                t_pointer -= 1
            else:
                s_pointer = backspace(s, s_pointer)
                t_pointer = backspace(t, t_pointer)
            if s_pointer < 0 or t_pointer < 0:
                if s_pointer < 0 and t_pointer < 0:
                    return True
                while t_pointer < 0:
                    before_backspace = s_pointer
                    s_pointer = backspace(s, s_pointer)
                    if s_pointer == before_backspace:
                        return False
                    if s_pointer < 0:
                        return True
                while s_pointer < 0:
                    before_backspace = t_pointer
                    t_pointer = backspace(t, t_pointer)
                    if t_pointer == before_backspace:
                        return False
                    if t_pointer < 0:
                        return True
        """
        def apply_backspaces(s):
            stack = []
            for c in s:
                if stack and c == "#":
                    stack.pop()
                elif c != "#":
                    stack.append(c)
            return "".join(stack)
        return apply_backspaces(s) == apply_backspaces(t)
        """
