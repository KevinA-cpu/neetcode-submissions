class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        i=1
        length = len(s)
        for i in range(1, length):
            if len(stack) != 0 and ((stack[-1] == '[' and s[i] == ']') or (stack[-1] == '{' and s[i] == '}') or (stack[-1] == '(' and s[i] == ')')):
               stack.pop()
            else:
               stack.append(s[i])

        return len(stack) == 0