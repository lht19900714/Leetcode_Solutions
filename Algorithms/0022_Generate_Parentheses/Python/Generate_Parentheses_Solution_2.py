# Space: O(1)
# Time: O(n)

class Solution:
    def generateParenthesis(self, n):
        if n == 0: return ['']
        if n == 1: return ['()']
        self.res = []

        def recursive(n, left_count, right_count, temp_res):
            if right_count > left_count: return

            if left_count == right_count == n:
                self.res.append(temp_res)
                return

            if left_count < n: recursive(n, left_count + 1, right_count, temp_res + '(')
            if right_count < n: recursive(n, left_count, right_count + 1, temp_res + ')')

        recursive(n, 0, 0, '')

        return self.res



