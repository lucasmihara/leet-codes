class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    s = s[:i] + s[i+1:]
                    n -= 1
                    i -= 1
            i += 1
        for i in reversed(stack):
            s = s[:i] + s[i+1:]
        
        return s
