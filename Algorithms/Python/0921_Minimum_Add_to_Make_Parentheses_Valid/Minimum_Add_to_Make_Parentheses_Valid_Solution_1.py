
# Space: O(n)
# Time: O(n)


class Solution:
    def minAddToMakeValid(self, S):
        length = len(S)
        if length == 0: return 0

        stack = []

        # find invalid parentheses
        for i in range(length):
            if S[i] == '(':
                stack.append(i)
            elif S[i] == ')':
                if stack and S[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)

        return len(stack)




