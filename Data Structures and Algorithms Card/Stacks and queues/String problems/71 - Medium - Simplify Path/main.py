class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        word = []
        for c in path + '/':
            if c != '/':
                word.append(c)
            else:
                if word and word[-1] == '/':
                    continue
                elif word:
                    if word == ['/', '.']:
                        pass
                    elif word == ['/', '.', '.']:
                        if stack:
                            stack.pop()
                    else:
                        stack.append("".join(word))
                    word = ['/']
                else:
                    word = ['/']
        if word != ['/'] or not stack:
            stack.append("".join(word))
        return "".join(stack)
