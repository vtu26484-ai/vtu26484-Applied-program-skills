class Solution:
    def minRemoveToMakeValid(self, s):
        stack = []
        s = list(s)  # convert string to list

        # First pass: remove invalid ')'
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''

        # Second pass: remove remaining '('
        for i in stack:
            s[i] = ''

        return ''.join(s)
