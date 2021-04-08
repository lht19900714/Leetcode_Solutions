
# Space: O(n)
# Time: O(n)

class Solution:
    def generateParenthesis(self, n):
        if n == 0: return ['']
        if n == 1: return ['()']
        self.res = []

        def backtracking(n, left_count, right_count, temp_res):
            if right_count > left_count: return
            if left_count == right_count == n:
                self.res.append(temp_res)
                return

            for each in '()':
                if each == '(' and left_count < n:
                    left_count += 1
                    temp_res += '('
                    backtracking(n, left_count, right_count, temp_res)
                    temp_res = temp_res[:-1]
                    left_count -= 1
                if each == ')' and right_count < n:
                    right_count += 1
                    temp_res += ')'
                    backtracking(n, left_count, right_count, temp_res)
                    temp_res = temp_res[:-1]
                    right_count -= 1

        backtracking(n, 0, 0, '')
        return self.res





