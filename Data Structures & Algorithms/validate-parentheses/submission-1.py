class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack:
                    return False
                f = stack.pop()

                if f == '{' and c != '}':
                    return False
                elif f =='(' and c != ')':
                    return False
                elif f == '[' and c != ']':
                    return False
        return True if not stack else False
