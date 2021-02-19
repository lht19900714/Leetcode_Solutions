
# Space: O(n)
# Time: O(n)


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        length = len(s)
        if length == 0: return s
        stack = []

        # find invalid parentheses
        for i in range(length):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)

        # remove invalid parentheses
        for index in reversed(stack):
            s = s[:index] + s[index + 1:]

        return s




