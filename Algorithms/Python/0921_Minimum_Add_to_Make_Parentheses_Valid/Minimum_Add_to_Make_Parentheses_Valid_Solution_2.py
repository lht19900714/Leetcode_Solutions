
# Space: O(1)
# Time: O(n)


class Solution:
    def minAddToMakeValid(self, S):
        length = len(S)
        if length == 0: return 0

        left_parentheses_count, right_parentheses_count = 0, 0

        # find invalid parentheses
        for i in range(length):
            if S[i] == '(':
                left_parentheses_count += 1
            elif S[i] == ')':
                if left_parentheses_count > 0:
                    left_parentheses_count -= 1
                else:
                    right_parentheses_count += 1

        return left_parentheses_count + right_parentheses_count




