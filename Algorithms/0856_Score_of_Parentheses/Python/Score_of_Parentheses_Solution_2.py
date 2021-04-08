
# Space: O(n)
# Time: O(n)

class Solution:
    def scoreOfParentheses(self, S):
        if len(S) == 2: return 1
        stack = []

        for char in S:
            if char == '(':
                stack.append(0)
            elif char == ')':
                last_number = stack.pop()
                if stack:
                    stack[-1] += max(1, 2 * last_number)
                else:
                    stack.append(max(1, 2 * last_number))

        return stack[0]




