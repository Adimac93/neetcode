class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if (c == ")" and last == '(') or (c == ']' and last == '[') or (c == '}' and last == '{'):
                    pass
                else:
                    return False
        return len(stack) == 0